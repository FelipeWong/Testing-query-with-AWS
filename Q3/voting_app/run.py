from flask import Flask, render_template, request
from datetime import datetime
import logging, boto3, random, string, os

if os.path.exists(os.path.abspath("demo.log")):
    os.remove(os.path.abspath("demo.log"))

app = Flask(__name__)

logging.basicConfig(filename="demo.log")

def s3_upload(key):
    s3 = boto3.client('s3', region_name='us-east-1')
    date = str(datetime.now())
    random_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    BUCKET_NAME='abc882021'
    s3.upload_file(
        Bucket = BUCKET_NAME,
        Filename="demo.log",
        Key = "%s/" % (key) + date + "-" + random_text + ".txt")
        

@app.route("/")
@app.route("/vote", methods=["GET", "POST"])
def voting():
    candidates = [ "薯片", "林林", "正氣" ]
    
    if request.method == "POST":
        print(request.form["vote"])
        s3_upload(key=request.form["vote"])
        return render_template("voting.html", title="Vote", candidates=candidates)
        
    
    return render_template("voting.html", title="Vote", candidates=candidates)

if __name__ == "__main__":
    app.run()