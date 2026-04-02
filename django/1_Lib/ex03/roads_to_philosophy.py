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
    roads = { url : input_raw }

    while not is_dead_end and not is_infinity_loop and not is_philosophy:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            # print(response.status_code) # DB
            print("Error fetching data")
            sys.exit(1)

        if not response.text:
            print("Error: what is this word {} which does not exist?".format(input_search))
            sys.exit(1)


        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"H1 ==> {soup.find('h1')}")

        soup = soup.find_all('p')
        for p in soup:
            # 1. ¿El párrafo está vacío? Saltamos al siguiente
            # if not p.get_text(strip=True) or p.find_parent("div", class_="hatnote") != None:
            if not p.get_text(strip=True) or not p.find('b'):
                continue

            # 2. Si llegamos aquí, este párrafo tiene texto.
            # Vamos a buscar los enlaces que hay DENTRO de este párrafo
            links_in_p = p.find_all('a')
            if not links_in_p:
                # roads["It leads to a dead end !"] = "dead_end"
                roads["dead_end"] = "It leads to a dead end !"
                # print("It leads to a dead end !")
                is_dead_end = True
                break
            
            for link in links_in_p:
                # Aquí es donde ocurre la magia:
                # 'link' es un objeto. Puedo sacar su texto y su destino (href)
                link_text = link.get_text()
                destiny = str(link.get('href'))

                if destiny.startswith("/wiki/") \
                and not (destiny.startswith("#") \
                or destiny.startswith("/Wikipedia:") \
                or destiny.startswith("/wiki/Help") \
                or destiny.startswith("/wiki/File") \
                or destiny.startswith("/wiki/Wikipedia:Citation_needed") \
                or destiny.startswith("//upload.wikimedia.org/")):
                    if (wikipedia_url + destiny) in roads:
                        # roads["It leads to an infinite loop !"] = "infinite_loop"
                        roads["infinite_loop"] = "It leads to an infinite loop !"
                        is_infinity_loop = True
                        break
                    # roads[link_text] = wikipedia_url + destiny
                    roads[wikipedia_url + destiny] = link_text
                    url = wikipedia_url + destiny
                else:
                    continue

                print(f"Link: {destiny}") # DB
                print(roads) # DB
                break
                
            # Detener tras encontrar el primer párrafo
            break

    for road in roads:
        print(roads[road])
    if is_philosophy:
        print(f"{len(roads)} roads from {input_raw} to philosophy")


def roads_to_philosophy():
    input_raw, input_search = check_args()
    find_in_wikipedia(input_raw, input_search)


if __name__ == "__main__":
    roads_to_philosophy()