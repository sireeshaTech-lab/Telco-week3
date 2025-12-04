import requests
import json

url1 = "https://api.open-meteo.com/v1/forecast?latitude=14.4499&longitude=79.987&hourly=temperature_2m"

def main():
    response = requests.get(url1)
    response.raise_for_status()
    data = response.json()

    # Save to file
    with open("data1.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Location 1 Data Saved to data1.json")
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()