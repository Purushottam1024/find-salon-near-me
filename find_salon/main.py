import argparse

from .scraper.driver import get_driver
from .scraper.excel import save_to_excel
from .scraper.extractor import extract_salon_data
from .scraper.search import search_salons
from .scraper.utils import extract_salon_name_from_url


def main():
    parser = argparse.ArgumentParser(
        description="Scrape salon details from Google Maps."
    )
    parser.add_argument(
        "--query",
        required=True,
        help="Search query for Google Maps, e.g., 'salons in Mumbai'",
    )
    parser.add_argument(
        "--scrolls",
        type=int,
        default=5,
        help="How many times to scroll the results list",
    )
    parser.add_argument("--output", default="salons.xlsx", help="Output Excel filename")

    args = parser.parse_args()
    driver = get_driver()

    try:
        print(f"Searching for: {args.query}")
        urls = search_salons(driver, args.query, args.scrolls)
        print(f"Found {len(urls)} salons. Extracting details...")

        all_data = []
        for idx, url in enumerate(urls, start=1):
            salon_name = extract_salon_name_from_url(url)
            print(f"[{idx}/{len(urls)}] Scraping: {salon_name}")
            data = extract_salon_data(driver, url)
            all_data.append(data)

        save_to_excel(all_data, args.output)
        print(f"Data saved to '{args.output}'")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
