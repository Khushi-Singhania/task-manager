
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
"""
def calculate_crop_yield():
    # Prompt the user for input
    field_area = float(input("Enter field area in hectares: "))
    crop_yield_per_hectare = float(input("Enter crop yield per hectare in kg: "))

    # Perform calculations
    total_yield = field_area * crop_yield_per_hectare

    # Display the result
    print("Total yield:", total_yield, "kg")
"""
if __name__ == '__main__':
    app.run()
