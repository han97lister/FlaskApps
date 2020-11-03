from flask import Flask, render_template

app = Flask(__name__)

@app.route( '/' )
def users():
    list_of_users = ['ben', 'harry', 'bob', 'jay', 'matt', 'bill']
    return render_template('list_of_users.html', users=list_of_users)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
