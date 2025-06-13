from flask import Flask, render_template, request
from database import Database
import random, string # for generating unique slug

app = Flask(__name__, template_folder="templates")
db = Database()

def generate_slug(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def add_content(content, title):
    slug = generate_slug() 
    db.insert(title="Untitled", content=content, slug=slug)

@app.route('/pasteit')
def paste():
    return render_template('index.html')

@app.route('/pasteit/viewpage', methods=['POST'])
def display():
    title = request.form.get('title')
    text = request.form.get('textbox')
    add_content(content=text, title=title)
    return render_template("view_page.html", paste_content = text)




app.run(debug=True)