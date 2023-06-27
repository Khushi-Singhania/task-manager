# File: test_agriculture.py

def calculate_crop_yield(field_area, crop_yield_per_hectare):
    return field_area * crop_yield_per_hectare

def test_calculate_crop_yield():
    field_area = 10  # in hectares
    crop_yield_per_hectare = 500  # in kg

    expected_yield = 5000  # Expected crop yield in kg

    actual_yield = calculate_crop_yield(field_area, crop_yield_per_hectare)

    assert actual_yield == expected_yield, "Crop yield calculation is incorrect"
