# bulletproof-prayer
Brute force your way to salvation
generates a unique prayer for every possible combination of non-vowel characters up to a specified length in various languages. It simulates fetching language-specific alphabets, then iterates through combinations of their characters (excluding vowels and symbols) to print a personalized prayer for each generated name.

## Features

- Support for multiple languages including English, French, Spanish, Italian, Russian, Arabic, Hebrew, German, Greek, Japanese (Hiragana), and Korean (Hangul).
- Dynamic alphabet retrieval based on the specified language.
- Customizable maximum length for name generation.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/multilingual-prayer-generator.git
cd multilingual-prayer-generator
```

### Usage
Run the script from the command line, specifying the language for which you wish to generate prayers:

```bash
python pray.py --language english
```

Replace english with any of the supported languages to generate prayers in that language.

### Supported Languages
english
french
spanish
italian
russian
arabic
hebrew
german
greek
japanese_hiragana
korean_hangul
Note: The chinese option is included as a placeholder, given the logographic nature of the Chinese writing system, which does not adapt well to this script's concept.

### Contributing
Contributions to expand the language support or improve the project are welcome. Please follow these steps to contribute:

 - Fork the repository.
 - Create a new branch (git checkout -b feature/AmazingFeature).
 - Make your changes.
 - Commit your changes (git commit -m 'Add some AmazingFeature').
 - Push to the branch (git push origin feature/AmazingFeature).
 - Open a pull request.

### License
Distributed under the MIT License. See LICENSE for more information.

