from flask import Flask
from utils import BAD_RETURN_CODE

import score

app = Flask(__name__)


def return_score():
    try:
        html_content = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is:</h1>
            <div is="score"> {score.get_score()} </div>
        </body>
        </html>
        """
    except Exception as e:
        html_content = f"""
        <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>ERROR:</h1>
            <div is="score" style="color:red"> ERROR {BAD_RETURN_CODE} </div>
        </body>
        </html>
        """

    return html_content


@app.route('/score')
def score_route():
    return return_score()


if __name__ == '__main__':
    app.run(debug=True)
