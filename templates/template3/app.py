from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initial global dictionary to store registered users
users = {}

# List of allowed organizations
allowed_organizations = ["org1", "org2", "org3", "org4", "org5"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    organization = request.form.get('organization')

    # Frontend validation
    if not name or not organization:
        error_message = "Both name and organization are required."
        return render_template('error.html', error_message=error_message)

    if organization not in allowed_organizations:
        error_message = "Invalid organization selected."
        return render_template('error.html', error_message=error_message)

    # Add user to the global dictionary
    users[name] = organization

    return redirect(url_for('registered'))

@app.route('/registered')
def registered():
    return render_template('registered.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
