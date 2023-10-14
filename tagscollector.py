import nltk
import itertools
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import advertools as adv

sitemap = adv.sitemap_to_df("https://ticapsoriginal.com/static/sitemap.xml")
urls = sitemap["loc"].to_list()


def get_code(url) -> requests.Response:
    return requests.get(url)


wordlist = ''
for item in tqdm(urls):
    urlg = (get_code(item))
    soup = BeautifulSoup(urlg.text, 'html.parser')
    tagmanager = ['span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    for item in tagmanager:
        counter = (soup.find_all(item))
        for item in counter:
            strings = (item.string)
            if strings != (None):
                wordlist += str(item.string)
with open('textdatasitemaps1.txt', 'w') as f:
    f.write(wordlist)
nltk.download('stopwords')
notags = stopwords.words('english')
ticapsoriginalen = open("textdatasitemaps1.txt", "r")
ticapsoriginalen = ticapsoriginalen.read()
ticapsoriginalen = word_tokenize(ticapsoriginalen)
both = nltk.FreqDist(ticapsoriginalen)
both_most_common = both.most_common()
for item in (list(itertools.chain(*(sorted(ys) for k, ys in itertools.groupby(
             both_most_common, key=lambda t: t[1]))))):
    if item[1] > 10 and (item[0] not in notags and len(item[0]) > 2):
        print(item)
