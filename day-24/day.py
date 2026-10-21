import hashlib
from pathlib import Path

file = input(f"\nEnter file path: ").strip()

path = Path(file)

if path.exists():
    try: 

        if path.is_file():
            file_content = path.read_bytes()
            current_hash = hashlib.sha256(file_content).hexdigest()

            hash_file = path.with_name(path.name + ".sha256")

            if hash_file.exists():
                original_hash = hash_file.read_text().strip()

                if current_hash == original_hash:

                    print("File is unchanged")

                else:
                    print("File is different!")
                    print("Current_hash: ", current_hash)

            else:
                hash_file.write_text(current_hash)
                print("Original hash saved")
                print("Hash: ", current_hash)

        else:
            print("Path exists but is not a file!")
            
    except OSError as error:
        print("File error: ", error)

else:
    print("Path doesn't exist!")



