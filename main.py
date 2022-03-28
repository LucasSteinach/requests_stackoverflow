import requests


import datetime

from pprint import pprint


def time_calculator():
    days_from_start = str(datetime.date.today() - datetime.date(1970, 1, 1)).split(" ")
    date_in_seconds = (int(days_from_start[0]) - 2) * 86400
    return date_in_seconds


if __name__ == '__main__':
    response = requests.get('https://api.stackexchange.com/2.3/questions',
                            params={'site': 'stackoverflow',
                                    'sort': 'votes',
                                    'order': 'desc',
                                    'fromdate': f'{time_calculator()}',
                                    'tagged': 'Python'
                                    }
                            )
    pprint(response.json())
