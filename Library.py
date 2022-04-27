import requests
import ctypes
def desktop_bg(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
def download_img_url(url, path):
    print("Getting image from url...", end='')
    response = requests.get(url)


    if response.status_code == 200:
        print("Success!")
        img_data = response.content
        with open(path, 'wb') as file:
            file.write(img_data)


    else:
        print('Connection failed...', response.status_code)



