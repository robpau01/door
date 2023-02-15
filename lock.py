from flask import Flask,request
app = Flask(__name__)
AvailableLocks=[{\"Brand\":\"Assa\"},{\"Brand\":\"Other\"}]

@app.route(\"/locks\")
def locks():
    return AvailableLocks
@app.route('/lock/<int:lockid>')
def lock(lockid):   
    return AvailableLocks[lockid]"
