import click
import requests
import time


# Read url from CSV fail
def read_url(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            name, url = line.split("|")
            yield name.strip(), url.strip()


# Check status code and request time
def check_url(name, url):
    try:
        start = time.time()
        response = requests.get(url,timeout=(3, 3))
        elapsed = time.time() - start

        print(f"\"{name}\", HTTP {response.status_code}, time {elapsed:.2f} seconds")

    except requests.exceptions.RequestException:
        print(f'"Skipping {url}"')

# Make def main() into callable script
@click.command()
@click.option("-i", "--input-file", required=True, help="CSV file with URLs")
def main(input_file):
    for name, url in read_url(input_file):
        check_url(name, url)


# Invoke main()
if __name__ == "__main__":
    main()