from pathlib import Path

# Translation Table
ext_dictionary = {
'.gif': 'image/gif',
'.jpg': 'image/jpeg',
'.jpeg': 'image/jpeg',
'.png': 'image/png',
'.pdf': 'application/pdf',
'.txt': 'text/plain',
'.zip': 'application/zip',
}

def main():
    # Takes User Input
    user_input = str(input("File name:"))
    # Normalizes user input to all lower cases and no spaces around it
    clean_input = (user_input).strip().lower()
    # extract suffix from file name (Object-Oriented approach)
    file_suffix = Path(clean_input).suffix
    if file_suffix in ext_dictionary:
        print (ext_dictionary[file_suffix])
    else:
        print ("application/octet-stream")

main()
