import requests

def get_random_cat_image_url():
    r = requests.get('https://cataas.com/cat?json=true')
    r.raise_for_status()

    url = "https://cataas.com" + r.json()["url"]
    return url

