def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

def celsius_to_kelvin(c: float) -> float:
    # BUG: Should be c + 273.15
    return c - 273.15

def process_sensor_data(temperatures_c: list[float], target_unit: str) -> list[float]:
    if not temperatures_c:
        raise ValueError("No sensor data provided")
        
    results = []
    for temp in temperatures_c:
        if target_unit.upper() == "F":
            results.append(celsius_to_fahrenheit(temp))
        elif target_unit.upper() == "K":
            results.append(celsius_to_kelvin(temp))
        else:
            raise ValueError(f"Unknown target unit: {target_unit}")
            
    return results