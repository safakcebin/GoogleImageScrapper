# Google Image Scrapper
collects image resources such as ".jpg", ".png", ".gif" from each google images url. saves url addresses in csv format

You can save only the source of the first image from each google images link in csv format

## exemple:
-  ``` https://www.google.com/search?q=github&sxsrf=ALeKk02renO6Npze-6aTZWXupNjr5wEStg:1626102707135&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj8gujR6N3xAhXlhf0HHWl_DnkQ_AUoAXoECAEQAw&biw=1920&bih=937```
  
- by giving this link you will get this source output -->>

-  ``` https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Font_Awesome_5_brands_github.svg/1200px-Font_Awesome_5_brands_github.svg.png ```

## installation (python3)
- ```git clone git@github.com:safakcebin/GoogleImageScrapper.git```,
- ```pip3 install selenium```
- ```python3 getImgSrc.py```
