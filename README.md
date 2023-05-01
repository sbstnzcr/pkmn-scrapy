# Pkmn Scrapy

This is a Scrapy app that scrapes data from the PokéAPI (https://pokeapi.co/api/v2/pokemon) and saves it to a JSON file.

## Requirements

- Python 3.x
- Scrapy

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/sbstnzcr/pkmn-scrapy-app.git
   ```
2. Navigate to the project directory:
   ```
   cd pokemon-scrapy-app
   ```
3. Install the required dependencies:
   ```
   pip install scrapy
   ```

## Usage

To run the app, navigate to the project directory in your terminal or command prompt and run the following command:
```
scrapy crawl pokemons -o pokemons.json
```

This will run the `pokemons` Spider and save the output to a file named `pokemons.json` in the project directory.

## Customization

You can customize the behavior of the app by modifying the following files:

- `pokemon_api/spiders/pokemons.py`: This file defines the Spider that extracts data from the PokéAPI. You can modify the code to extract different data or follow different links.
- `scrapy.cfg`: This file contains configuration settings for Scrapy, such as the user agent string and download delay. You can modify these settings to control the behavior of the app.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).