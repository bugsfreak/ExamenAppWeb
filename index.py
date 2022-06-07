from flask import Flask, render_template,url_for,redirect

app = Flask(__name__,template_folder='templates')

@app.route('/')
def principal():
    
    return render_template ('principal.html')


if __name__ == '__main__':
    app.run(debug=True)

