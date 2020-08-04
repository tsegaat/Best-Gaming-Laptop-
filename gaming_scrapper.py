from bs4 import BeautifulSoup
from requests import get
from pandas import *


html = get("https://www.t3.com/features/best-gaming-laptop").content
bsObj = BeautifulSoup(html, "html.parser")

names = [name.text for name in bsObj.find_all(class_ = "product__title")]
prices = [price.text for price in bsObj.find_all(class_ = "hawk-affiliate-link-price-widget-deal")]
specs = [cpu_spec.text for cpu_spec in bsObj.find_all(class_ = "spec_value")]
cpu_specs = []
graphics_specs = []
ram_specs = []
screen_specs = []
storage_specs = []
first_prices = []

s = 0
for spec in specs:
    if s % 5 == 0:
        cpu_specs.append(spec)
    elif s % 5 == 1:
        graphics_specs.append(spec)
    elif s % 5 == 2:
        ram_specs.append(spec)
    elif s % 5 == 3:
        screen_specs.append(spec)
    elif s % 5 == 4:
        storage_specs.append(spec)
    s += 1


p = 0
for price in prices:
    if p % 2 == 0:
        first_prices.append(price)


laptops = DataFrame({   
    "Names": names,
    "CPU": cpu_specs,
    "Graphics": graphics_specs,
    "Ram": ram_specs,
    "Screen": screen_specs,
    "Storage": storage_specs,
    "Prices": first_prices,
})

laptops.to_csv("laptops.csv")