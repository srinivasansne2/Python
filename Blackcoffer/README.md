
# Data Extraction and NLP

This project is developed in collaboration with BlackCoffer, is a data extraction and natural language processing (NLP) solution designed to streamline the extraction and analysis of unstructured data, providing valuable insights for businesses. The project combines the power of data extraction techniques with NLP algorithms to convert raw textual information into structured, actionable knowledge.

## Scraping

How It Works

Import Required Libraries: The code uses Python's BeautifulSoup for parsing HTML, requests for making HTTP requests, pandas for working with data, and os for creating folders and files.

Define the Scrap Function: The scrap function is the heart of this script. It takes a list of URLs and custom file names as input. For each URL, it fetches the web page content, parses it, and extracts data.

Make HTTP Request: The script sends an HTTP request to the specified URL, pretending to be a regular web browser by specifying user-agent and language headers.

Parse HTML: BeautifulSoup is used to parse the HTML content of the web page, making it easy to extract specific elements.

Extract Data: The code identifies and extracts data from the web page. It finds the main heading and the content paragraphs and stores them in variables.

Create Folders: It checks if a folder called "txt" exists. If not, it creates one. This is where the extracted text files will be stored.

Write to Text File: The extracted data (heading and content) is then written to a text file. Each URL's data is saved in a separate text file, and the file name is customized based on your input.






How to Use

Prepare an Excel file named "Input.xlsx" with two columns: "URL" and "URL_ID." The "URL" column should contain the URLs you want to scrape, and the "URL_ID" should be a unique identifier for each URL.

Run the script. It will read the Excel file, extract URLs and custom file names, and then proceed to scrape the web pages.

The scraped text files will be saved in a "txt" folder within your project directory.

This script can be useful for various web scraping and text extraction tasks. Customize it to suit your specific needs and data sources.
## Data Analysis

1.	POSITIVE SCORE
2.	NEGATIVE SCORE
3.	POLARITY SCORE
4.	SUBJECTIVITY SCORE
5.	AVG SENTENCE LENGTH
6.	PERCENTAGE OF COMPLEX WORDS
7.	FOG INDEX
8.	AVG NUMBER OF WORDS PER SENTENCE
9.	COMPLEX WORD COUNT
10.	WORD COUNT
11.	SYLLABLE PER WORD
12.	PERSONAL PRONOUNS
13.	AVG WORD LENGTH

All the variables are calculated using natural language processing(NLP) methods.Calculated values are stored in excel sheet.

