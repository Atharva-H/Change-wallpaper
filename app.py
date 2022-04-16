import ctypes
import requests
from pathlib import Path
from pyunsplash import PyUnsplash
from config import ACCESS_KEY

class change_wallpaper():
   
    def set_wallpaper():
        path=Path().resolve()
        path= str(path)+"\wallpaper.jpg"
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
        print("Wallpaper Set")
        
    def get_wallpaper():
        pu = PyUnsplash(api_key=ACCESS_KEY)

        photos = pu.photos(type_='random', count=1, featured=True, query="quote")
        [photo] = photos.entries
        print(photo.id, photo.link_download)
        response = requests.get(photo.link_download, allow_redirects=True)
        open('wallpaper.jpg', 'wb').write(response.content) 
        
    def get_anime_wallpaper():
        url="https://pic.re/image"
        response=requests.get(url)
        print(response.json())
        
def main():
    change_wallpaper.get_wallpaper()
    print("Download Done")
    change_wallpaper.set_wallpaper()
    
# change_wallpaper.get_anime_wallpaper()
main()