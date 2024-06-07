var pop;
function setup() {
	chatbot.loadFiles(['bot.rive']);
	pop = new Audio('pop.mp3');
}

window.onload = setup;
var np = require('numpy');
var pd = require('pandas');

movies = pd.df = pd.read_csv('final_movies.csv');

from sklearn.feature_extraction.text var TfidfVectorizer = require('TfidfVectorizer');
vectorizer = TfidfVectorizer(ngram_range=(1,10));
tfidf = vectorizer.fit_transform(movies['genre']);
from sklearn.metrics.pairwise var cosine_similarity = require('cosine_similarity');
function search(input) {
    query_vec = vectorizer.transform([input]);
    similarity = cosine_similarity(query_vec,tfidf).flatten();
    indices = np.argpartition(similarity, -15)[-15:];
    results = movies.iloc[indices][::-1];
    return results;
}
input_genre = input('Enter the genre: ');
output_movies = search(input_genre);
console.log('The recommended movies are: ');
console.log(output_movies);