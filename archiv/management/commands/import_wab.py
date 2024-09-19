import glob
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from dateutil.parser import parse
from tqdm import tqdm

from archiv.models import Wab


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.
    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False


files = sorted(
    [
        x
        for x in glob.glob("../xml/bruckner-wab-data/data/wab-*.xml")
        if "exclude" not in x
    ]
)


class Command(BaseCommand):
    help = "imports WAB-XMLs"

    def handle(self, *args, **kwargs):
        for x in tqdm(files, total=len(files)):
            with open(x) as fp:
                soup = BeautifulSoup(fp, "xml")
            wab_id = soup.find("identifier", {"label": "WAB"}).text
            proper_wab_id = x.split("/")[-1].replace("wab-", "").replace(".xml", "")
            proper_wab_id
            title = soup.find("title")
            if title:
                title = " ".join(title.text.split())
                title = f"{title} | WAB {wab_id}"
            date = soup.find("date")
            written_date = date.text
            try:
                iso_date = sorted([x for x in date.attrs.values() if is_date(x)])[0]
            except IndexError:
                iso_date = None
            try:
                if len(iso_date) == 4:
                    iso_date = f"{iso_date}-01-01"
                elif len(iso_date) == 7:
                    iso_date = f"{iso_date}-01"
            except TypeError:
                iso_date = None
            wab, _ = Wab.objects.get_or_create(wab_id=proper_wab_id)
            wab.title = title
            wab.wab_xml = soup.prettify()
            wab.date = iso_date
            wab.date_written = written_date
            wab.save()
