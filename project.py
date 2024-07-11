import sys
import json
import xml.etree.ElementTree as ET

def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    return input_file, output_file

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print("JSON file loaded successfully")
            return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print("Data saved to JSON file successfully")
    except IOError as e:
        print(f"Error saving JSON: {e}")
        sys.exit(1)

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        print("XML file loaded successfully")
        return root
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

def save_xml(data, file_path):
    try:
        tree = ET.ElementTree(data)
        tree.write(file_path)
        print("Data saved to XML file successfully")
    except IOError as e:
        print(f"Error saving XML: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    input_extension = input_file.split('.')[-1]
    output_extension = output_file.split('.')[-1]

    if input_extension == 'json':
        data = load_json(input_file)
    elif input_extension == 'xml':
        data = load_xml(input_file)
    else:
        print("Unsupported input file format")
        sys.exit(1)
    
    if output_extension == 'json':
        save_json(data, output_file)
    elif output_extension == 'xml':
        save_xml(data, output_file)
    else:
        print("Unsupported output file format")
        sys.exit(1)
