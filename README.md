# Content-based Book Recommendation System
## Project Overview
This project is a Content-based Book Recommendation System that suggests books to users based on their preferences.  
If a user likes a particular book, the system recommends similar books using the book's category and description.
The system is simple, interactive, and perfect for small datasets, making it ideal for learning recommendation systems in Python.
Objective of this project is
- To build a content-based system that recommends books using category and description similarity.
- To apply TF-IDF vectorization and cosine similarity using Pandas and Scikit-learn.
- To offer a simple, interactive tool for exploring book recommendations from a custom dataset.
## Technologies Used
- Python
- Pandas: for handling data in tabular format
- Scikit-learn: for TF-IDF vectorization and similarity calculations
## How It Works
1. Dataset Creation: A custom dataset of books is created with `title`, `category`, and `description`.
2. Feature Combination: Category and description are combined into a single text field.
3. Text Vectorization: TF-IDF vectorizer converts text into numerical vectors.
4. Similarity Calculation: Cosine similarity measures how similar each book is to others.
5. Recommendation: Based on the similarity scores, the top 3 most similar books are suggested.
## Example Books in Dataset
- The Silent Storm (Thriller)
- Hearts in Bloom (Romance)
- Mind Hacker (Technology)
- Journey Beyond Earth (Science Fiction)
- Laughing Pages (Comedy)
## How to Run
1. Clone or download the project folder.
2. Install required libraries:pip install pandas scikit-learn
3. Run the program:python book_recommendation.py
4. Enter a book name from the available list to get recommendations.
## Output 
Available Books:
- The Silent Storm
- Hearts in Bloom
- Mind Hacker
- Journey Beyond Earth
- Laughing Pages
Enter a book name you like: Mind Hacker
Recommended Books:
['Journey Beyond Earth', 'The Silent Storm', 'Hearts in Bloom']
## Features
- Custom dataset 
- Interactive user input
- Simple and easy to understand code
- Content-based recommendation using book features
## Author 
Anisha
