import requests
from pprint import pprint
from bs4 import BeautifulSoup
from collections import Counter


def extract_lyrics(url):
    r = requests.get(url)
    print(f"fetching lyrics {url}")
   

    if r.status_code != 200:
        print("Page impossible à recupérer")
        return []

    soup = BeautifulSoup(r.content, "html.parser")
    lyrics = soup.find("div", class_= "Lyrics__Container-sc-1ynbvzw-6 jYfhrf")
    if not lyrics:
        extract_lyrics (url)

    all_words=[] 
    for sentence in lyrics.stripped_strings :
        sentence_word = [word.strip(",").strip(".").lower() for word in sentence.split() if len(word) > 3 and "[" not in word and "]" not in word]

        all_words.extend(sentence_word)

    return all_words
    #pprint(all_words)







def get_all_urls():
    page_number = 1
    links = []
    while True:
        r = requests.get(f"https://genius.com/api/artists/29743/songs?page={page_number}&sort=popularity")
        if r.status_code == 200 :
            print(f"fetching page {page_number}")
            response = r.json().get("response", {})
            next_page = response.get("next_page")

            songs = response.get("songs")
            links.extend([song.get("url") for song in songs])
            page_number +=1

            
           

            if not next_page:
                print("No more page_number to fetch")
                break
    return links

    pprint(links)
    print(len(links))
    


def get_all_words() :
    urls = get_all_urls()
    words = []
    for url in urls:
        lyrics = extract_lyrics(url = url)
        words.extend(lyrics)


    counter = Counter(words)
    most_commun_words = counter.most_common(15)

    pprint(most_commun_words)


get_all_words()



extract_lyrics(url = "https://genius.com/Patrick-bruel-place-des-grands-hommes-lyrics")