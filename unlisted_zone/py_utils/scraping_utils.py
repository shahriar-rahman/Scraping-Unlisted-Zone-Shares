import json
import scrapy


class ScrapingUtils:
    def __init__(self):
        pass

    @staticmethod
    def scrape_xpath(response, xpath):
        if not isinstance(xpath, str):
            raise ValueError("! Invalid xpath. !")

        try:
            selection = response.xpath(xpath).extract()

        except Exception as exc:
            print(f"! Exception encountered while scraping xpath: {xpath} !\n", exc)
            return None

        else:
            print("> xpath navigation successful.")

        return selection if response else None


if __name__ == "__main__":
    main = ScrapingUtils()

