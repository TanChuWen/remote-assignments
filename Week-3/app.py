from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/sum.html")
def index():
    return render_template("sum.html")

@app.route("/data")
def handle_data():
    number_param = request.args.get('number')

    if number_param is None:
        return "Lack of Parameter"
    try:
        number = int(number_param)
    except ValueError:
        return "Wrong Parameter"

    if number <= 0:
        return "N should be a positive integer"

    result = sum(range(1, number + 1))
    return f"{result}"

if __name__ == "__main__":
    app.run(debug=True, port=3000)
