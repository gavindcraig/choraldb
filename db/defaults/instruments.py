from flask_sqlalchemy import SQLAlchemy
from ..models import Instruments
import requests
from bs4 import BeautifulSoup


def def_instruments(db: SQLAlchemy):
    """Pull list of instruments from IMSLP"""
    url = 'https://imslp.org/wiki/IMSLP:Abbreviations_for_Instruments'
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')

    table = soup.find('table').find_all('tr')[1:]
    for r in table:
        if 'voice' in str(r).lower():
            continue
        td = r.find_all('td')

        abr = td[0].get_text(strip=True)
        name = td[1].get_text(strip=True)
        print(abr + ': ' + name)
        db.session.add(Instruments(abbreviation=abr,
                                   name_full=name))
    db.session.commit()
