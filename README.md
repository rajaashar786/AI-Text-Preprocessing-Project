
AI Text Preprocessing Project

Project Overview

This project demonstrates text preprocessing on IMDb movie reviews for natural language processing (NLP) tasks.
The goal is to clean raw text data, making it suitable for AI or machine learning models such as sentiment analysis.

Dataset

The dataset contains mixed movie reviews from IMDb.
For this project, a smaller cleaned dataset (cleaned_mixeddata_small.csv) is provided to keep the file size below 25 MB for GitHub.
Each row contains:

rating → original movie rating
review → original review text
clean_review → cleaned and preprocessed text

Preprocessing Steps

1. Lowercasing – All text is converted to lowercase.
2. URL removal – Any links are removed from the reviews.
3. Special characters removal – Only alphabets and spaces are kept.
4. Stopwords removal – Common words like "the", "is", and "and" are removed to reduce noise.
5. Output – The cleaned text is saved as a new column clean_review in the CSV file.

Files in the Repository

 cleaned_mixeddata_small.csv → Small cleaned dataset ready for use in AI models
 text_preprocessing.py → Python code used to clean the full dataset
 make_small_csv.py → Python code used to create the smaller dataset for GitHub
 README.md → Project explanation
 report.pdf → Project report (optional)

Usage

The cleaned dataset can be directly used for AI/ML tasks like sentiment analysis or text classification.
Python code files can be run to reproduce preprocessing or create a smaller dataset.

Notes

The project uses Python, pandas, and regular expressions for text preprocessing.
No internet connection is required to run the preprocessing code since stopwords are hardcoded.



If you want, I can **also write a short project report version** that matches this explanation and is ready to save as `report.pdf`.

Do you want me to do that next?
