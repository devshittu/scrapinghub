import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url):
    print(f"Downloading {url}")
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print(f"Download error: {e.reason}")
        html = None
    return html
 
download('https://github.com/richardpenman/whois')