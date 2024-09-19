import requests
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from acdh_tei_pyutils.tei import TeiReader
from lxml import etree as ET
from tqdm import tqdm

from archiv.models import Person


NS_LIST = {
    "tei": "http://www.tei-c.org/ns/1.0",
    "mei": "http://www.music-encoding.org/ns/mei",
    "xml": "http://www.w3.org/XML/1998/namespace",
}


class Command(BaseCommand):
    help = "Enriches Persons with bruckner_entities_xml data"

    def handle(self, *args, **kwargs):
        headers = {"PRIVATE-TOKEN": settings.GITLAB_TOKEN}
        r = requests.get(settings.BRUCKNER_PERSON_URL, headers=headers)
        content = r.content.decode("utf-8")
        content = content.replace(
            "http://www.music-encoding.org/ns/mei", "http://www.tei-c.org/ns/1.0"
        )
        doc = TeiReader(content)
        person_entries = doc.any_xpath(".//tei:persName[@xml:id]")
        for x in tqdm(person_entries, total=len(person_entries)):
            item = {}
            item["xml_id"] = x.attrib["{http://www.w3.org/XML/1998/namespace}id"]
            try:
                item["last_name"] = x.xpath(
                    ".//tei:famName/text()", namespaces=NS_LIST
                )[0]
            except IndexError:
                item["last_name"] = ""
            try:
                item["first_name"] = x.xpath(
                    ".//tei:foreName/text()", namespaces=NS_LIST
                )[0]
            except IndexError:
                item["first_name"] = ""
            item["label"] = f"{item['first_name'].strip()} {item['last_name'].strip()}"
            item["xml_node"] = ET.tostring(x)
            try:
                pers = Person.objects.get(title=item["label"])
            except ObjectDoesNotExist:
                pers, _ = Person.objects.get_or_create(
                    bruckner_entity_id=item["xml_id"]
                )
                pers.title = item["label"]
            pers.bruckner_entity = True
            pers.bruckner_entity_id = item["xml_id"]
            pers.bruckner_entity_xml = item["xml_node"].decode("utf-8")
            pers.save()
