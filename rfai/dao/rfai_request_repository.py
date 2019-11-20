from rfai.dao.common_repository import CommonRepository
from datetime import datetime as dt


def generate_sub_query_for_filter_params(filter_parameter):
    if filter_parameter is not None and filter_parameter != {}:
        sub_query = "= %s AND ".join(filter_parameter.keys()) + "= %s "
        sub_query_values = list(filter_parameter.values())
    else:
        sub_query = ""
        sub_query_values = list()
    return sub_query, sub_query_values


def generate_sub_query_for_update_parameters(update_parameters):
    update_parameters.update({"row_updated": dt.utcnow()})
    if update_parameters is not None and update_parameters != {}:
        sub_query = "= %s , ".join(update_parameters.keys()) + "= %s "
        sub_query_values = list(update_parameters.values())
    else:
        sub_query = ""
        sub_query_values = list()
    return sub_query, sub_query_values


class RFAIRequestRepository(CommonRepository):

    def __init__(self, connection):
        super().__init__(connection)
