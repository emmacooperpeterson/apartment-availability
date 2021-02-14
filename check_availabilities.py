from bs4 import BeautifulSoup as bs
import requests

def check_1000_south_clark(url, desired_floorplans):

    try:
        page = requests.get(url)
        soup = bs(page.content, 'html.parser')

        floorplans = soup.find_all('td', {"data-label":"Floor Plan"})
        floorplans = [f.get_text().replace("Floor Plan", "") for f in floorplans]

        availabilities = soup.find_all('td', {"data-label":"Availability"})
        availabilities = [a.get_text() for a in availabilities]

        info = dict(zip(floorplans, availabilities))

        is_any_available = any(["Available" in info[f] for f in desired_floorplans])

    except Exception as e:
        return e

    return is_any_available
