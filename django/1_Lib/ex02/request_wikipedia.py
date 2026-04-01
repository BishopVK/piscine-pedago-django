import sys
import json
import dewiki
import requests

def request_wikipedia():
    if len(sys.argv) != 2:
        print("Usage error. Correct Use: python3 request_wikipedia.py 'string'")
        sys.exit(1)

    input_search = sys.argv[1]
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": input_search,
        "format": "json"
    }
    headers = {
        "User-Agent": "42school-project/1.0 (student project)"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print("Error fetching data")
        sys.exit(1)

    try:
        data = response.json()
    except:
        print("Invalid response")
        sys.exit(1)
    # print(data) # -> step_1

    results = data["query"]["search"]
    if not results:
        print("No results found")
        sys.exit(1)

    page_title = results[0]["title"]

    # Second search
    params2 = {
        "action": "query",
        "prop": "extracts",
        "explaintext": True,
        "titles": page_title,
        "format": "json"
    }

    response2 = requests.get(url, params=params2, headers=headers)
    if response2.status_code != 200:
        print("Error fetching data")
        sys.exit(1)

    data2 = response2.json()
    # print(data2) # -> step_2

    pages = data2["query"]["pages"]
    if not pages:
        print("No results found")
        sys.exit(1)

    page = next(iter(pages.values()))
    if "extract" not in page:
        print("No content found")
        sys.exit(1)

    content = page["extract"]

    clean = dewiki.from_string(content)

    # Create output file
    output_filename = input_search.replace(" ", "_") + ".wiki"

    with open(output_filename, "w", encoding="utf-8") as output:
        output.write(clean)

if __name__ == "__main__":
    request_wikipedia()