from bs4 import BeautifulSoup


def fix_hrefs(item):
    fields = []
    try:
        fields = item.search_field_names()
    except AttributeError:
        pass
    for x in fields:
        data = getattr(item, x)
        if data:
            soup = BeautifulSoup(data, "html.parser")
            for link in soup.find_all("a"):
                href = link.get("href")
                if href is not None:
                    if "abcd.acdh" in href:
                        pass
                    else:
                        link.attrs["target"] = "_blank"
            setattr(item, x, str(soup))
    return "done"
