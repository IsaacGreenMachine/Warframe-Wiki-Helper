from pathlib import Path
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

# example
# https://lovecraft.fandom.com/api.php?action=query&prop=images&titles=Cthulhu&format=json

# API homepage
# https://warframe.fandom.com/api.php

warframes = [
    "Ash",
    "Atlas",
    "Banshee",
    "Baruuk",
    "Caliban",
    "Chroma",
    "Citrine",
    "Dagath",
    "Ember",
    "Equinox",
    "Excalibur",
    "Frost",
    "Gara",
    "Garuda",
    "Gauss",
    "Grendel",
    "Gyre",
    "Harrow",
    "Hildryn",
    "Hydroid",
    "Inaros",
    "Ivara",
    "Khora",
    "Kullervo",
    "Lavos",
    "Limbo",
    "Loki",
    "Mag",
    "Mesa",
    "Mirage",
    "Nekros",
    "Nezha",
    "Nidus",
    "Nova",
    "Nyx",
    "Oberon",
    "Octavia",
    "Protea",
    "Qorvex",
    "Revenant",
    "Rhino",
    "Saryn",
    "Sevagoth",
    "Styanax",
    "Titania",
    "Trinity",
    "Valkyr",
    "Vauban",
    "Volt",
    "Voruna",
    "Wisp",
    "Wukong",
    "Xaku",
    "Yareli",
    "Zephyr"
    ]

def download_warframe_data(warframes, savedir): # scrapes data for each warframe from fandom wiki
    # get all warframe data
    sources = {}

    for warframe in tqdm(warframes):
        # base call:
        params = {
        "action": "parse",
        "prop": "text", # some examples: "links",
        # "titles": "Ash",
        "page": warframe,
        "format": "json",
        }

        query_link = f"https://warframe.fandom.com/api.php"


        r = requests.get(query_link, params=params)
        html_content = r.json()["parse"]["text"]["*"]
        source_link = f"https://warframe.fandom.com/wiki/{r.json()['parse']['title']}"
        file_name = savedir / f"{warframe}.txt"
        sources[str(file_name)] = source_link
        soup = BeautifulSoup(html_content)
        # print(soup.get_text())
        text_file = open(file_name, "w")
        text_file.write(soup.get_text())
        text_file.close()

    sources_file = open(savedir / "SOURCES.json", "w")
    sources_file.write(json.dumps(sources))
    sources_file.close()


def run_download_warframe_data(savedir): # function to activate download_warframe_data
    if not savedir.exists():
        savedir.mkdir(parents=True, exist_ok=True)
    download_warframe_data(warframes, savedir)

def fandom_wiki_parse(page_search_content:str): # parse action for fandom wiki
    params = {
    "action": "parse",
    "prop": "text", # some examples: "links",
    # "titles": "Ash",
    "page": page_search_content, # "Ash", "Upgrades", ...
    "format": "json",
    }
    query_link = f"https://warframe.fandom.com/api.php"

    r = requests.get(query_link, params=params)
    return r.json()

def fandom_wiki_query(page_search_content:str): # query action for fandom wiki
    # base call:
    params = {
    "action": "query",
    "prop": "links", # some examples: "links",
    "titles": page_search_content, #"Warframes", "Excalibur", etc...
    "format": "json",
    }
    query_link = f"https://warframe.fandom.com/api.php"
    r = requests.get(query_link, params=params)
    return r.json()
