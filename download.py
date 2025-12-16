import click
import requests




# Make def main() into callable script
@click.command()
@click.option("-i", "--input-file", required=True, help="CSV file with URLs")
def main(input_file):
    pass

# Invoke main()
if __name__ == "__main__":
    main()