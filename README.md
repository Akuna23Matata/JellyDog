# JellyDog
A Python web scraper to get stock data from JellyCat.com
To use JellyDog simply do this:  
```
import JellyDog
url = "https://www.jellycat.com/us/toastie-vivacious-aubergine-tov3au/" #Use Online stock page url
stock = JellyDog.check(url)
```
The Stock variable would be a dictionary variable with following schemetic:  
```
stock = {'model1' : ['name1', 'stock count'], 'model2' : ['name2', 'stock count']}
```
