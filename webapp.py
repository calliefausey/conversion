from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/dog-years")
def render_dog_years():
    return render_template('dogyears.html')

@app.route("/cat-years")
def render_cat_years():
    return render_template('catyears.html')

@app.route("/fish-years")
def render_fish_years():
    return render_template('fishyears.html')

@app.route("/response")
def render_response():
    if 'dogyears' in request.args:
    #The request object stores info about the request sent to the server
    #args is a multiplicit (like a dictionary but can have multiple values for the same key)
    #The info in args is visible in the url for the page being requested (ex. .../response)
        reply = float(request.args['DY'])*7
    elif 'catyears' in request.args:
        reply = float(request.args['CY'])*4
    else:
        reply = float(request.args['FY'])*18
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
