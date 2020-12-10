import requests
import argparse
import yaml
from bs4 import BeautifulSoup as bs

parser = argparse.ArgumentParser()
parser.add_argument('-lb', '--lbin',required = False, help = 'Linux Binary')
parsValue = parser.parse_args()

gtfobinsUrl = 'https://gtfobins.github.io/'
gtfoRaw_url = 'https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/{}.md'

def binary():
    if parsValue.lbin:
        req = requests.get(gtfobinsUrl)
        source = bs(req.content,"html.parser")
        rows = source.find_all('a', class_="bin-name")
        bins = [i.text for i in rows]
        if parsValue.lbin in bins:
            return parsValue.lbin
        else:
            print("[!] Wrong Format")

def getBinary(bin):
    req = requests.get(gtfoRaw_url.format(bin)).text
    parsedYaml = list(yaml.load_all(req, Loader=yaml.SafeLoader))[0]
    parse(parsedYaml)

def parse(parsedYaml: dict):
    sections = parsedYaml["functions"]
    for sec in sections:
        category = sections[sec]
        for cat in category:
            if "description" in cat:
                print("#" + cat['description'])
            print("Code:\t" + cat['code'])
            print("Type:\t" + sec)
            print("\n")

getBinary(binary())