from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def header():
    return '<h1 draggable="true">Flask App Example</h1>' \
           '<h3 contenteditable="true">This text is editable. Write anything you want here.</h3>'

if __name__ == '__main__':
    app.run("port", PORT)
