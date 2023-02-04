from flask import Flask, request, url_for, redirect, render_template
import wikipedia

class SearchEngineWiki():
    def Search(self, query):
        q = wikipedia.summary(query, 10)
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

        
    data = SearchEngineWiki().Search(q)
    return render_template('results.html', d=data, q=q)

if __name__ == "__main__":
    app.run(debug=True)
 
