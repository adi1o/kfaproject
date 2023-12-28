from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactus', methods=['GET'])
def contact():
    return render_template('contactus.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:

        # if length <= 0 or width <= 0:
        #     return "Please enter positive values for length and width."

        area='nan'
        opt=request.form['cal']
        if opt=='rectangle' : 
            length = float(request.form['length'])
            width = float(request.form['width'])
            area_r = length * width 
            area=area_r
        elif opt=='square' :
            lenhq = float(request.form['lenhq'])
            area_s=lenhq**2
            area=area_s
        elif opt=='circle' :
            radius = float(request.form['radius'])
            area_c= (22/7)*radius**2
            area=area_c
        elif opt=='triangle' :
            base = float(request.form['base'])
            height = float(request.form['height'])
            area_t= (1/2)*base*height
            area=area_t

        # return f"The area of the rectangle is: {area_r} \n area of square is: {area_s}" 
        return render_template('index.html',messages={'area': area, 'opt':opt})
    except ValueError as error:
        return'enter valid input'
        
if __name__ == '__main__':
    app.run(debug=True)

