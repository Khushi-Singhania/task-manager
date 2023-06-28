
from flask import Flask, request, jsonify, render_template

app = Flask(__name__) 

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
def calculate_crop_yield():

    field_area = float(request.form.get('field_area'))
    crop_yield_per_hectare = float(request.form.get('crop_yield_per_hectare'))

    total_yield = field_area * crop_yield_per_hectare
        
    print('Total crop yield is: ', total_yield)
        
    return jsonify({'crop_yield': total_yield})

if __name__ == '__main__':
    app.run(host='localhost', port=8080)

