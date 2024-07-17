from flask import Flask, render_template

app = Flask(__name__)

name = "Jordan Tan Qi Shen"
secret_text = "Jordan Tan Qi Shen Chupapi Munyanyo"
secret_nums = [1111,2222,3333,4444]
secret_info = ["watermelon", "fried chicken", "koolaid"]

@app.route("/")
def home():
    return "<h1>Hello dogcheeks!</h1>"

@app.route("/bomboclat")
def bomboclat():
    return "<h1>What does bomboclat mean?</h1>"

@app.route("/brawl_stars")
def brawl_stars():
    return "<h1>D1 5 star recruit el crashout</h1>"

@app.route("/about")
def about():
    return render_template("about.html", name=name)

@app.route("/secret")
def secret():
    lucky_num = random.choice(secret_nums)
    return render_template("secret.html", lucky_num=lucky_num)


if __name__ =="__main__":
    app.run(debug=True, port=1234)
    
