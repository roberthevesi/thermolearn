import board
import adafruit_dht
import time

# Define the DHT sensor and GPIO pin
dht_device = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        print(f"Temperature: {temperature_c:.2f}°C")
        print(f"Humidity: {humidity:.2f}%")

    except RuntimeError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    time.sleep(2.0)
