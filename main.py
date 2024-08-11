from datetime import datetime
import json
import uuid

# Load data from JSON file
def load_data(path):
    with open (path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# Generate iCal file from data
def generate_cal_file(data, filename="repetitiekalender-kvl"):
    with open(f"temp/{filename}.ics", "w", encoding="utf-8") as file:
        file.write("BEGIN:VCALENDAR\n")
        file.write("VERSION:2.0\n")
        file.write("PRODID:-//KVL//2024//NL\n")
        for entry in data:
            file.write(f"BEGIN:VEVENT\n")

            # Generate unique ID for the event
            uid = uuid.uuid4()
            file.write(f"UID:{uid}\n")

            # Parse title from entry
            file.write(f"SUMMARY:{entry['title']}\n")

            # Parse date from entry (format: d/m/yyyy)
            date_str = entry["date"]
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")
            date = date_obj.strftime("%Y%m%d")

            file.write(f"DTSTART:{date}T180000Z\n")
            file.write(f"DTEND:{date}T210000Z\n")

            # Parse description from entry
            description = ""
            if entry["context"].get("topic") is not None:
                description += f"Wat: {entry["context"]["topic"]}"
            if entry["context"].get("excluded") is not None:
                description += f"\\nMoet niet komen: {entry["context"]["excluded"]}"
            file.write(f"DESCRIPTION:{description}\n")

            file.write(f"END:VEVENT\n")

        file.write("END:VCALENDAR\n")


# Point to the JSON file
path = "sample-data/dates.json"
output_filename = "calendar"

# Load data from JSON file
json_data = load_data(path)

# Generate iCal file from data
generate_cal_file(json_data, output_filename)
