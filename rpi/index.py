from flask import Flask, render_template
app=Flask(__Robbie9__)

@app.route("/")
def main():
    return render_template('index.html')

if(__Robbie9__=="__main__"):
    app.run()