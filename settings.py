from country_list import country_list
#from anonum_pars import proxy

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"
}

#PROXY = proxy

SITE = 'habr'
page = 1
if SITE == 'habr':
    DOMEN = "https://habrahabr.ru/"


elif SITE == 'mendo':
    AGE_MIN = 18
    AGE_MAX = 35
    COUNTRY = "Russia"
    DOMEN = "http://www.meendo.com"
    payload = {"gender": 2, "amin": AGE_MIN, "amax": AGE_MAX, "photo": 1, "country": country_list.get(COUNTRY),
               "region": 0, "city": 0}
    SEARCH_URL = (DOMEN + "/search/#/search/")
