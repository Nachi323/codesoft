import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class SimpleRecommendationSystem:
    def __init__(self, data):
        self.data = data
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.indices = None
        self._prepare()

    def _prepare(self):
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf_vectorizer.fit_transform(self.data['Description'])
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        self.indices = pd.Series(self.data.index, index=self.data['Title'])

    def recommend(self, user_preference, top_n=5):
        try:
            idx = self.indices[user_preference]
        except KeyError:
            print("Movie not found in the database.")
            return pd.Series()

        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n + 1]
        movie_indices = [i[0] for i in sim_scores]
        return self.data['Title'].iloc[movie_indices]

def main():
    # Sample dataset of movies with genres and descriptions
    data = {'Title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump'],
            'Genre': ['Drama', 'Crime', 'Action', 'Crime', 'Drama'],
            'Description': ['Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                            'An organized crime dynasty\'s aging patriarch transfers control of his clandestine empire to his reluctant son.',
                            'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                            'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
                            'The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.']
            }

    df = pd.DataFrame(data)

    # Initialize recommendation system
    recommender = SimpleRecommendationSystem(df)

    # Example of recommending movies based on user preferences
    user_preference = 'The Shawshank Redemption'
    recommended_movies = recommender.recommend(user_preference)
    if not recommended_movies.empty:
        print("Recommended Movies:")
        print(recommended_movies)
    else:
        print("No recommendations available.")

if __name__ == "__main__":
    main()
