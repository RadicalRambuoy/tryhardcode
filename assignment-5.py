import random
import nltk
from newspaper import Article
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
 
nltk.download('punkt_tab', quiet=True)
 
article = Article('https://www.theguardian.com/world/2026/sep/13/russian-drone-hits-kyiv-warsaw-passenger-train-polish-border')
article.download()
article.parse()
sentences = nltk.sent_tokenize(article.text)
 
GREETINGS = ['hi', 'hello', 'hey', 'greetings']
 
def bot_response(user_input):
    sentences.append(user_input)
    vectors = CountVectorizer(stop_words='english').fit_transform(sentences)
    scores = cosine_similarity(vectors[-1], vectors).flatten()[:-1]
    sentences.pop()
    best = scores.argmax()
    if scores[best] < 0.2:
        return "Sorry, I don't understand."
    return sentences[best]
 
print("Bot: Ask me about the article. Type 'bye' to exit.")
while True:
    text = input("You: ").lower()
    if text in ('bye', 'exit', 'quit'):
        print("Bot: Goodbye!")
        break
    if any(word in GREETINGS for word in text.split()):
        print("Bot:", random.choice(GREETINGS))
    else:
        print("Bot:", bot_response(text))