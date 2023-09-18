import json
import os
from scraper_noticias.utils import clean_html

def save_to_json(data, filename, path):    
    # Check if the provided path exists, create if not
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Check if the file already exists
    file_path = os.path.join(path, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as existing_file:
            existing_data = json.load(existing_file)
            existing_data.extend(data)
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, indent=4, ensure_ascii=False)
            print(f"Data appended to {filename}")
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"JSON saved to {filename}")