import click
import requests


# Read url from CSV fail
def read_url(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            name, url = line.strip()
            return name, url

# Make def main() into callable script
@click.command()
@click.option("-i", "--input-file", required=True, help="CSV file with URLs")
def main(input_file):
    pass

# Invoke main()
if __name__ == "__main__":
    main()