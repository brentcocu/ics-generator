# iCalendar Generator

This project generates an iCalendar (.ics) file from a JSON data source. The generated calendar file contains events with details such as title, date, and description.

## Requirements

No external libraries are required to run this script. The script is written in
Python 3.12.4, but it should work with any version of Python 3 or above.

## Usage

1. **Run the Script:**
    * Update the `path` variable in [`main.py`](main.py) to point to your JSON file.
    * Optionally, update the `output_filename` variable to change the name of the generated iCalendar file.
    * Execute the script by running the following command from root:
  
        ```sh
        python main.py
        ```

2. **Output:**
   * The script will generate an iCalendar file in the `temp` directory with the specified filename `calendar.ics`.

## License

This project is licensed under the MIT License.
