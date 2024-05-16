def analyze_weather_data(temperature_readings):

    if not temperature_readings:
        return None, None, None
    
    average_temp = sum(temperature_readings) / len(temperature_readings)
    
    highest_temp = max(temperature_readings)
    lowest_temp = min(temperature_readings)
    
    return average_temp, highest_temp, lowest_temp

temperature_readings = [25, 28, 21, 24, 27]
average_temp, highest_temp, lowest_temp = analyze_weather_data(temperature_readings)

print(f"Average Temperature: {average_temp}")
print(f"Highest Temperature: {highest_temp}")
print(f"Lowest Temperature: {lowest_temp}")