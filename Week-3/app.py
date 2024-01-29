from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.route('/sum.html')
def index():
    return render_template('sum.html')

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

@app.route('/myName')
def show_name():
   user_name = request.cookies.get('user_name') #設定user_name是從cookies中取出來
   if user_name: # 如果 user_name 已存在
       return f'Hello, {user_name}! Welcome to this website.'
   else: # 如果user_name不存在，也就是說cookies中沒有這個user_name
       return render_template('nameForm.html') #要讓寫在myName.html的輸入框出現在網站上

@app.route('/trackName', methods = ['POST', 'GET']) #要讓寫在nameForm.html的 action="/trackName"回到這來處理，這邊接受兩種方法
def track_name():
    if request.method == 'GET':  #試過POST，不會出現網址要帶的參數。題目要有參數就用GET
        user_name = request.args.get('name') #這邊是GET慣用的語法

        if user_name: #not null
            response = make_response(redirect('/myName')) #回到/myName這個路徑
            response.set_cookie('user_name', user_name) #塞cookie進去
            return response
    return "Please enter your name first." 

if __name__ == "__main__":
    app.run(debug=True, port=3000)
