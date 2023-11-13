from flask import Flask, render_template
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click')
def click():
    pyautogui.click(x=-1844, y=736)
    return "Clicked"

if __name__ == '__main__':
    app.run(debug=True)
