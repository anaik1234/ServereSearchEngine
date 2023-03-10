from flask import Flask, request, url_for, redirect, render_template
import wikipedia

class SearchEngineWiki():
    def Search(self, query):
        try:
            q = wikipedia.summary(query, 10)
        except:
            q = f"Not Found {query} in database"

        return q

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        query = request.form.get('Text')
        query = str(query)

        return redirect(url_for('Search', q=query))

    return render_template('search.html')

@app.route('/<q>', methods=["POST", "GET"])
def Search(q):
    if request.method == "POST":
        query = request.form.get('Text')
        query = str(query)

        return redirect(url_for('Search', q=query))

    if q.lower() != 'google':
        data = SearchEngineWiki().Search(q)
        return render_template('results.html', d=data, q=q)
    
    else:
        g= '''Google LLC is an American multinational technology company focusing on search engine technology, online advertising, cloud computing, computer software, quantum computing, e-commerce, artificial intelligence,[9] and consumer electronics. It has been referred to as "the most powerful company in the world"[10] and one of the world's most valuable brands due to its market dominance, data collection, and technological advantages in the area of artificial intelligence.[11][12][13] Its parent company Alphabet is considered one of the Big Five American information technology companies, alongside Amazon, Apple, Meta, and Microsoft.'''
        return render_template('results.html', d=g, q=q)

if __name__ == "__main__":
    app.run(host="192.168.1.22", port=80
            )
