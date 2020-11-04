from flask import Flask, render_template

app.config['SECRET_KEY'] = 's3cret$hh'

if __name__='__main__':
    app.run(debug=True, host='0.0.0.0')
