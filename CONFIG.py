# Checking sites interval
REFRESH_RATE = 5

"""
MANUAL

CONTENT_REQUIREMENTS = {
    #search using element#
    "SITE_URL": ("ELEMENT", "CLASS", "EXPECTED_VALUE"},
    
    #search by text#
    "SITE_URL": ("TEXT", "EMPTY_STRING", "EXPECTED_VALUE")
}
"""

CONTENT_REQUIREMENTS = {
    "https://b3ta.com/404": ("a", "class", "gb1"),
    "https://www.facebook.com/": ("div", "class", "Najlepsze ¿yczenia dla przedsiêbiorców z okazji Dnia Ma³ych i ¦rednich Firm"),
    "https://aryaboudaie.com/python/technical/educational/web/flask/2018/10/17/flask.html": ("text", "", "Terefere"),
    "https://dzone.com/articles/python-flask-generating-a-static-html-page": ("li", "class", "rss-icon"),
    "https://pl.simplesite.com/pages/service-login.aspx": ("a", "href", "//pl.simplesite.com/go/cms/features/features"),
    "https://www.onet.pl/": {"h1", "class", "onetLogo"}
}
