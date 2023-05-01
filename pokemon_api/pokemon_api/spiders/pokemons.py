import scrapy


class PokemonSpider(scrapy.Spider):
    name = "pokemons"
    start_urls = ["https://pokeapi.co/api/v2/pokemon"]

    def parse(self, response):
        json = response.json()
        for pokemon in json["results"]:
            yield {"name": pokemon["name"], "url": pokemon["url"]}

        next_page = json["next"]
        if next_page is not None:
            yield response.follow(next_page, self.parse)
