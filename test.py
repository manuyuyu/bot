import cat_api

try:
    url = cat_api.get_random_cat_image_url()
    print(url)
except:
    print("Поймали исключение")