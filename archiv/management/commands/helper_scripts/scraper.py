import pandas as pd
import requests
from bs4 import BeautifulSoup
import traceback

page = 0
count = 0

while True:
    try:
        page += 1
        # Search result url
        URL = "https://abcd.acdh-dev.oeaw.ac.at/archiv/event/?main_text=Ecce+sacerdos&Filter=Suchen&page=" + str(page)
        r = requests.get(URL)

        html = r.text

        # WAB detail url
        WabURL = "https://abcd.acdh-dev.oeaw.ac.at/archiv/wab/detail/13"

        WabR = requests.get(WabURL)
        WabHtml = WabR.text

        WabSoup = BeautifulSoup(WabHtml, features="html.parser")

        soup = BeautifulSoup(html, features="html.parser")
        table = soup.find('table', {"class": "table"})
        rows = table.find_all('tr')
        data = []
        for row in rows[1:]:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

        result = pd.DataFrame(data, columns=["ID", "Datum", "Haupttext"])
        for column in result["Datum"]:
            if column is not None:
                matches = WabHtml.find('>' + str(column) + '<')
            else:
                print('HERE NON FOUND: ', column, page)
                matches = 0

            if matches == -1:
                index = result.index[result['Datum'] == column].tolist()[0]
                print(result["ID"][index])
                count = count + 1
    except Exception as ex:
        print(ex)
        print(traceback.format_exc())
        print('Probably last page', page)
        print('Missing links founds:', count)
        break  # exit while loop
