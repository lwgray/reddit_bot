import os
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap


# Create flask application
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# Setup Bootstrap
Bootstrap(app)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    ''' View for Scoring for Suicide Risk '''
    rule = request.url_rule
    searches = ['apple', 'orange', 'grape', 'pear']
    return render_template('index.html', rule=rule, searches=searches)


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port=5001, debug=True)
