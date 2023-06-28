#make a venv, install request
#import the tools for doing web requests
import requests
from pathlib import Path
# an image API http://shibe.online/api/shibes
img_url="http://shibe.online/api/shibes?count=1"
img = requests.get(img_url).json()[0]
quote_url="http://quotes.stormconsultancy.co.uk/random.json"  # can`t find this place on the internet`
quote=requests.get(quote_url).json()["quote"]
#a quotes API http://quotes.stormconsultancy.co.uk/random.json
#create html structure
html=f"<p>{quote}</p><img src='{img}>"
print(html)
#create a new file
f=Path().home().joinpath("Escritorio").joinpath("index.html")
f.write_text(html)
print(html)
# write to the file