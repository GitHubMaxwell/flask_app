from flask import Flask, render_template

app = Flask(__name__)

# put in debug mode you can either
# app.debug = True
# or put debug=True in the app.run below
# this acts makes it so you just have to refresh the page when changes are made instead of stopping and starting the server


# usually return a template
@app.route('/')
def index():
    # return 'INDEX'
    return render_template('index')


# this conditional means that this script is what will be executed
if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
