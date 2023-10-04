from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['GET'])
def check_number():
    try:
        number = int(request.args.get('number'))
        if number % 2 == 0:
            result = 'even'
        else:
            result = 'odd'
        return render_template('result.html', number=number, result=result)
    except ValueError:
        return render_template('result.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
