import pandas as pd
import requests
from io import BytesIO


def field_mapping(some_class):
    """returns a dictionary mapping model field names to lookukp values
    :param some_class: Any django model class with extra field properties
    :return: A dict mapping model field names to lookukp values
    """
    field_mapping_dict = {}
    for x in some_class._meta.get_fields():
        try:
            field_mapping_dict[(x.extra["data_lookup"]).strip()] = x.name
        except:  # noqa: E722
            pass
    return field_mapping_dict


def gsheet_to_df(sheet_id):
    GDRIVE_BASE_URL = "https://docs.google.com/spreadsheet/ccc?key="
    url = f"{GDRIVE_BASE_URL}{sheet_id}&output=csv"
    r = requests.get(url)
    print(r.status_code)
    data = r.content
    df = pd.read_csv(BytesIO(data))
    return df
