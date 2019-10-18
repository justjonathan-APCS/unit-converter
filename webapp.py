from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
@app.route("/response")
def render_response():
    Miles = request.args['Miles']
    response = float(Miles) * 1.60934
    
    return render_template('response.html', responseFromServer = response)
    
@app.route("/response2")
def render_response2():
    Dollars = request.args['Dollars']
    response2 = float(Dollars) * 10
    
    return render_template('response2.html', responseFromServer2 = response2)
    
@app.route("/response3")
def render_response3():
    Dollars2 = request.args['Dollars2']
    response3 = float(Dollars2) * 0.9
    
    return render_template('response3.html', responseFromServer3 = response3)
    
if __name__=="__main__":
    app.run(debug=False)
    


