from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_rectangle_area(length, width):
    return length * width

def calculate_square_area(side):
    return side * side

def calculate_circle_area(radius):
    return math.pi * radius**2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    shape = request.form['shape']

    if shape == 'triangle':
        base = float(request.form['base'])
        height = float(request.form['height'])
        result = calculate_triangle_area(base, height)
    elif shape == 'rectangle':
        length = float(request.form['length'])
        width = float(request.form['width'])
        result = calculate_rectangle_area(length, width)
    elif shape == 'square':
        side = float(request.form['side'])
        result = calculate_square_area(side)
    elif shape == 'circle':
        radius = float(request.form['radius'])
        result = calculate_circle_area(radius)
    else:
        result = 'Invalid shape'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)