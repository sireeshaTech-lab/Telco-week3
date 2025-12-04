import json

def main():
    # Load both files
    with open("data1.json") as f:
        data1 = json.load(f)
    with open("data2.json") as f:
        data2 = json.load(f)

    # Merge safely with nested structure (recommended)
    merged = {
        "location1": data1,
        "location2": data2
    }

    # Save merged file
    with open("merged.json", "w") as f:
        json.dump(merged, f, indent=4)

    print("Merged JSON Saved to merged.json")
    print(json.dumps(merged, indent=4))

if __name__ == "__main__":
    main()