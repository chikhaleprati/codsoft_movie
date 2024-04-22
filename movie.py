 class MovieRecommendationSystem:
    def _init_(self):
        # Movie database with genres
        self.movies = {
            "The Shawshank Redemption": ["drama"],
            "The Godfather": ["drama", "crime"],
            "The Dark Knight": ["action", "crime", "drama"],
            "Forrest Gump": ["drama", "romance"],
            "Inception": ["action", "adventure", "sci-fi"],
            "Pulp Fiction": ["crime", "drama"],
            "The Matrix": ["action", "sci-fi"],
            "The Lord of the Rings: The Fellowship of the Ring": ["adventure", "fantasy"],
            "Titanic": ["drama", "romance"],
            "Avatar": ["action", "adventure", "fantasy"],
            "Toy Story": ["animation", "adventure", "comedy"],
            "Finding Nemo": ["animation", "adventure", "comedy"],
            "The Hangover": ["comedy"],
            "Step Brothers": ["comedy"],
            "Interstellar": ["adventure", "drama", "sci-fi"],
            "The Avengers": ["action", "adventure", "sci-fi"],
            "Jurassic Park": ["adventure", "sci-fi", "thriller"],
            "Deadpool": ["action", "comedy"],
            "The Lion King": ["animation", "adventure", "drama"]
        }

    def recommend_movies(self, preferences):
        recommended_movies = []
        for movie, genres in self.movies.items():
            if any(genre.lower() in preferences for genre in genres):
                recommended_movies.append(movie)
        return recommended_movies

    def print_recommendations(self, recommended_movies):
        if recommended_movies:
            print("Recommended movies based on your preferences:")
            for movie in recommended_movies:
                print("-", movie)
        else:
            print("Sorry, no movies found based on your preferences.")

if _name_ == "_main_":
    recommendation_system = MovieRecommendationSystem()
    user_preferences = input("Enter your movie preferences (e.g., Adventure, Action, Crime, Comedy, Drama): ").split(',')
    recommended_movies = recommendation_system.recommend_movies(user_preferences)
    recommendation_system.print_recommendations(recommended_movies)
