from pm4py.objects.log.util import xes
from pm4pyws.handlers.distributed.process_schema import factory as process_schema_factory

class DistributedHandler(object):
    def __init__(self, wrapper, parameters=None):
        if parameters is None:
            parameters = {}
        self.wrapper = wrapper
        # sets the filter chain
        self.filters_chain = []
        # classifier
        self.activity_key = xes.DEFAULT_NAME_KEY

        self.first_ancestor = self

    def get_filters_chain_repr(self):
        """
        Gets the representation of the current filters chain

        Returns
        -----------
        stri
            Representation of the current filters chain
        """
        return str(self.filters_chain)

    def remove_filter(self, filter, all_filters):
        self.wrapper.set_filters(all_filters)
        return self

    def add_filter(self, filter, all_filters):
        self.wrapper.set_filters(all_filters)
        return self

    def get_variants_number(self):
        # the number is not implemented
        return -1

    def get_cases_number(self):
        summary = self.wrapper.get_log_summary()
        return summary["cases"]

    def get_events_number(self):
        summary = self.wrapper.get_log_summary()
        return summary["events"]

    def get_schema(self, variant=process_schema_factory.DFG_FREQ, parameters=None):
        return list(process_schema_factory.apply(self.wrapper, variant=variant, parameters=parameters)) + [self.get_log_summary_dictio()]

    def get_numeric_attribute_svg(self, attribute, parameters=None):
        pass

    def get_case_duration_svg(self, parameters=None):
        pass

    def get_events_per_time_svg(self, parameters=None):
        pass

    def get_variant_statistics(self, parameters=None):
        pass

    def get_sna(self, variant="handover", parameters=None):
        pass

    def get_transient(self, delay, parameters=None):
        pass

    def get_case_statistics(self, parameters=None):
        pass

    def get_events(self, caseid, parameters=None):
        pass

    def download_xes_log(self):
        pass

    def download_csv_log(self):
        pass

    def get_start_activities(self, parameters=None):
        return self.wrapper.get_start_activities()

    def get_end_activities(self, parameters=None):
        return self.wrapper.get_end_activities()

    def get_attributes_list(self, parameters=None):
        return self.wrapper.get_attribute_names()

    def get_attribute_values(self, attribute_key, parameters=None):
        return self.wrapper.get_attribute_values(attribute_key)

    def get_paths(self, attribute_key, parameters=None):
        pass

    def get_alignments(self, petri_string, parameters=None):
        pass

    def get_events_for_dotted(self, attributes):
        pass

    def get_spec_event_by_idx(self, ev_idx):
        pass

    def get_log_summary_dictio(self):
        summary = self.wrapper.get_log_summary()
        this_variants_number = -1
        this_cases_number = summary["cases"]
        this_events_number = summary["events"]
        ancestor_variants_number = -1
        ancestor_cases_number = summary["cases"]
        ancestor_events_number = summary["events"]

        dictio = {"this_variants_number": this_variants_number, "this_cases_number": this_cases_number,
                  "this_events_number": this_events_number, "ancestor_variants_number": ancestor_variants_number,
                  "ancestor_cases_number": ancestor_cases_number, "ancestor_events_number": ancestor_events_number}

        return dictio
