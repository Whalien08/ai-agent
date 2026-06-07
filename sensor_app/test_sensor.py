import sys
from pkg.thermal import process_sensor_data

def test_sensor_conversion():
    test_data = [0.0, 100.0, -40.0]
    
    # Test Fahrenheit
    f_results = process_sensor_data(test_data, "F")
    assert f_results == [32.0, 212.0, -40.0], f"Fahrenheit fail: {f_results}"
    
    # Test Kelvin
    k_results = process_sensor_data(test_data, "K")
    assert k_results == [273.15, 373.15, 233.15], f"Kelvin fail: {k_results}"
    
    print("All thermal sensor tests passed successfully! 🚀")

if __name__ == "__main__":
    try:
        test_sensor_conversion()
    except AssertionError as e:
        print(f"Test Failed: {e}")
        sys.exit(1)