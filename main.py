try:
    import pm4pycvxopt
except:
    pass


import shutil
import os

if not os.path.exists("files"):
    print("sii")
    os.mkdir("files")
if not os.path.exists("files/databases"):
    files = os.listdir("files2/")
    for f in files:
        shutil.move("files2/" + f, "files/")

from pm4pyws.entrypoint import PM4PyServices
from pm4pywsconfiguration import configuration as Configuration

app = PM4PyServices.app

import sqlite3
conn_event_logs = sqlite3.connect(Configuration.event_log_db_path)
cursor_event_logs = conn_event_logs.cursor()
S = PM4PyServices()
cursor_event_logs.execute("SELECT LOG_NAME, LOG_PATH FROM EVENT_LOGS WHERE LOADED_BOOT = 1")
for result in cursor_event_logs.fetchall():
    S.load_log(str(result[0]), str(result[1]))
conn_event_logs.close()

there_is_ssl_context = False
CERT_FILE = "this.crt"
PRIVATE_KEY_FILE = "this.key"

try:
    content = os.listdir(Configuration.ssl_context_directory)
    if CERT_FILE in content and PRIVATE_KEY_FILE in content:
        there_is_ssl_context = True
except:
    pass

print("there_is_ssl_context", there_is_ssl_context)

# offers the service to the outside
if __name__ == "__main__":
    if not there_is_ssl_context:
        LISTENING_HOST = "0.0.0.0"
        LISTENING_PORT = 5000
        S.serve(host=LISTENING_HOST, port=LISTENING_PORT)
    else:
        LISTENING_HOST = "0.0.0.0"
        LISTENING_PORT = 5443
        CERT_FILE = os.path.join(Configuration.ssl_context_directory, CERT_FILE)
        PRIVATE_KEY_FILE = os.path.join(Configuration.ssl_context_directory, PRIVATE_KEY_FILE)
        S.serve(host=LISTENING_HOST, port=LISTENING_PORT, ssl_context=(CERT_FILE, PRIVATE_KEY_FILE))
