# TDS Data Repository

**WARNING: Use this data at your own risk. Ensure all the data is correct and how you want it. There is no guarantee on the completeness and correctness of the data.**

## Overview

This repository contains raw data sources scraped from two sources:
1. [TDS 2025-01](https://tds.s-anand.net/#/2025-01/)
2. [TDS Knowledge Base on Discourse](https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34)

The data includes:
- **Discourse Posts**: JSON files representing the topic post streams exported from the Discourse JSON API endpoint.
- **Website Pages**: Markdown files generated from the HTML pages of the TDS 2025-01 website.

## Data Structure

- **discourse_posts.json**: A single JSON file containing all the Discourse posts.
- **discourse_json/**: A directory containing individual JSON files for each topic post stream.
- **tds_pages_md/**: A directory containing Markdown files for each page scraped from the TDS 2025-01 website.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/23f3004008/TDS-Project1-Data.git
   cd TDS-Project1-Data
   ```

2. **Install Dependencies**

   Ensure you have Python installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Downloading Data

To download the data, you can use the provided Python scripts:

- **Discourse Posts**

  ```bash
  python discourse_downloader_full.py
  ```

- **Website Pages**

  ```bash
  python website_downloader_full.py
  ```

### Viewing Data

- **Discourse Posts**

  The `discourse_posts.json` file contains all the Discourse posts. You can view this file directly or use a JSON viewer.

- **Website Pages**

  The Markdown files in the `tds_pages_md/` directory can be opened in any text editor or Markdown viewer.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
