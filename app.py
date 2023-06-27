from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-crop-yield', methods=['POST'])
def calculate_crop_yield():
    field_area = float(request.form.get('field_area'))
    crop_yield_per_hectare = float(request.form.get('crop_yield_per_hectare'))

    total_yield = field_area * crop_yield_per_hectare

    return jsonify({'crop_yield': total_yield})

if __name__ == '__main__':
    app.run()
