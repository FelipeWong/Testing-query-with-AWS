from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/voting')
def voting():
    candidates = [ '薯片','林林','正氣' ]
    return render_template('voting.html', title='Vote', candidates=candidates)

if __name__ == "__main__":
    app.run()