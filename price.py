import requests

def get_gold_price():
    try:
        url = "https://www.tgju.org/profile/geram18"
        html = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        ).text

        return html

    except Exception:
        return None
