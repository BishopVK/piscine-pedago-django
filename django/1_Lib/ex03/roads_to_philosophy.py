import sys, requests
from bs4 import BeautifulSoup

def check_args():
    if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
        print("Usage error. Correct Use: python3 roads_to_philosophy.py 'string'")
        sys.exit(1)

    input_raw = sys.argv[1]
    input_search = input_raw.strip().replace(" ", "_").casefold()

    if input_search == "philosophy":
        print(f"0 roads from {input_raw} to philosophy")
        sys.exit(0)

    return input_raw, input_search

def find_in_wikipedia(input_raw, input_search):
    is_dead_end = False
    is_infinity_loop = False
    is_philosophy = False

    wikipedia_url = "https://en.wikipedia.org"
    url = wikipedia_url + "/wiki/" + input_search
    headers = {
        "User-Agent": "42school-project/1.0 (student project)"
    }

    # roads = { input_raw : url }
    # roads = { url : input_raw }
    visited_titles = []
    visited_urls = []


    while not is_dead_end and not is_infinity_loop and not is_philosophy:
        try:
            response = requests.get(url, headers=headers)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

        if response.status_code != 200:
            # print(response.status_code) # DB
            print("It leads to a dead end !")
            sys.exit(1)

        if response.url in visited_urls:
            print("It leads to an infinite loop !")
            return # Salimos de la función
        visited_urls.append(response.url)

        soup = BeautifulSoup(response.content, 'html.parser')

        current_title = soup.find('h1', id="firstHeading").get_text()
        print(current_title) # DB
        visited_titles.append(current_title)

        if current_title == "Philosophy":
            is_philosophy = True
            break

        soup = soup.find_all('p')
        # print(f"soup => {soup}") # DB
        for p in soup:
            # 1. ¿El párrafo está vacío? Saltamos al siguiente
            # if not p.get_text(strip=True) or p.find_parent("div", class_="hatnote") != None:
            if not p.get_text(strip=True) or not p.find('b'):
                continue

            print(f"p => {p}") # DB
            
            # 2. Si llegamos aquí, este párrafo tiene texto.
            # Vamos a buscar los enlaces que hay DENTRO de este párrafo
            links_in_p = p.find_all('a')
            if not links_in_p:
                # print("It leads to a dead end !")
                visited_titles.append("It leads to a dead end !")
                is_dead_end = True
                break
            
            for link in links_in_p:
                destiny = str(link.get('href'))

                if destiny.startswith("/wiki/") \
                and not (destiny.startswith("#") \
                or destiny.startswith("/Wikipedia:") \
                or destiny.startswith("/wiki/Help") \
                or destiny.startswith("/wiki/File") \
                or destiny.startswith("/wiki/Wikipedia:Citation_needed") \
                or destiny.startswith("//upload.wikimedia.org/")):
                    if (wikipedia_url + destiny) in visited_urls:
                        # roads["It leads to an infinite loop !"] = "infinite_loop"
                        # roads["infinite_loop"] = "It leads to an infinite loop !"
                        is_infinity_loop = True
                        break
                    url = wikipedia_url + destiny
                else:
                    continue

                """ print(f"Link: {destiny}") # DB
                print(visited_titles) # DB
                print(visited_urls) # DB """
                break

            # Detener tras encontrar el primer párrafo
            break

    for titles in visited_titles:
        print(titles)
    if is_philosophy:
        print(f"{len(visited_titles)} roads from {input_raw} to philosophy")


def roads_to_philosophy():
    input_raw, input_search = check_args()
    find_in_wikipedia(input_raw, input_search)


if __name__ == "__main__":
    roads_to_philosophy()