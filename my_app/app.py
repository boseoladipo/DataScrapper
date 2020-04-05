import re

import requests
from bs4 import BeautifulSoup

SOURCE = "data/alexa1M.txt"
RESULT = "data/results.txt"
FAILED = "data/failed_urls.txt"

def get_image_link(website, result_file, failed_load_file):
    """
    Get link to image from url
    Args:
        website (string): website address.
        result_file (_io.TextIOWrapper): File stream to write image link to.
        failed_load_file (_io.TextIOWrapper): File stream to write errors to.
    """
    domain = f"http://{website}"
    try:
        source = requests.get(domain, timeout=10)
    except Exception as error:
        failed_load_file.write(f"{website} image link not loaded due to {error}\n")
    else:
        soup = BeautifulSoup(source.text, features="html.parser")
        try:
            img_link = soup.find("meta", {"property": "og:image"})["content"]
            if "http" not in img_link:
                img_link = f"{domain}{img_link}"
        except (TypeError, KeyError):
            img_link = f"{domain}/favicon.ico"
        result_file.write(f"{img_link.strip()}\n")


def main():
    # open source file for reading
    source_file = open(SOURCE, "r")

    # open destination files for writing
    result_file = open(RESULT, "w")
    failed_load_file = open(FAILED, "w")

    print('URL extraction started')

    while True:
        line = source_file.readline()

        if not line:
            break

        website = line.strip()
        get_image_link(website, result_file, failed_load_file)
    
    print('URL extraction done')


if __name__ == "__main__":
    main()
