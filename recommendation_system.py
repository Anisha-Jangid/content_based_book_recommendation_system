import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
book_data = {
    "title": [
        "The Silent Storm",
        "Hearts in Bloom",
        "Mind Hacker",
        "Journey Beyond Earth",
        "Laughing Pages"
    ],
    "category": [
        "Thriller",
        "Romance",
        "Technology",
        "Science Fiction",
        "Comedy"
    ],
    "description": [
        "a journalist uncovers hidden secrets behind a political conspiracy",
        "a beautiful love story filled with emotions and relationships",
        "understanding hacking mindset and cybersecurity techniques",
        "an astronaut explores unknown planets and space missions",
        "a collection of humorous stories and funny incidents"
    ]
}
df = pd.DataFrame(book_data)
df["combined_features"] = df["category"] + " " + df["description"]
vectorizer = TfidfVectorizer(stop_words="english")
feature_vectors = vectorizer.fit_transform(df["combined_features"])
similarity_matrix = cosine_similarity(feature_vectors)
def recommend_book(book_name):
    if book_name not in df["title"].values:
        return "Book not found in database"
    book_index = df[df["title"] == book_name].index[0]
    similarity_scores = list(enumerate(similarity_matrix[book_index]))
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )
    recommendations = []
    for i in similarity_scores[1:4]:
        recommendations.append(df.iloc[i[0]]["title"])
    return recommendations
if __name__ == "__main__":
    print("Available Books:")
    for book in df["title"]:
        print("-", book)
    user_book = input("\nEnter a book you like: ")
    result = recommend_book(user_book)
    print("\nRecommended Books:")
    print(result)
