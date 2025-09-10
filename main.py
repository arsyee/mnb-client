import sys
from suds.client import Client
from pprint import pprint
import xml.etree.ElementTree as ET

from datetime import datetime, timedelta

def main():
    try:
        yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
        print(f"Yesterday's date: {yesterday}")
        today = datetime.now().strftime('%Y-%m-%d')
        print(f"Today's date: {today}")
        # Current day is not available until 12:00

        client = Client('https://www.mnb.hu/arfolyamok.asmx?singleWsdl')

        # info = client.service.GetInfo()
        # print(info)

        rates = client.service.GetExchangeRates(yesterday, today, "EUR,USD")
        print(rates)
        data = ET.fromstring(rates)
        for day in data:
            print(day.tag, day.attrib)
            for rate in day:
                pprint(rate.attrib)
                print(rate.text)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
