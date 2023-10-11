import hashlib
import csv
import datetime

FIELDNAMES = ["key", "hash"]

#creates a sha256 hash of the file
def hash_file(file_name):
        return hashlib.sha256(open(file_name,'rb').read()).hexdigest()

#save filename and hash
def write_hash(file_name):
    file_hash = hash_file(file_name)

# first it checks if the hash is already saved
    with open ("hashes.csv","r", newline="") as f:
        h = []
        reader = csv.DictReader(f)
        for row in reader:
            h.append({"key": row["key"], "hash": row["hash"]})

        if any(
            dictionary.get("key") == file_name
            for dictionary in h
        ):
            print("file already hashed")
        
        else: 
#if it hasnt been saved, it saves the file name and its hash
            with open ("hashes.csv","a", newline="") as hashes:
                writer = csv.DictWriter(hashes, fieldnames = FIELDNAMES)
                writer.writerow({"key": file_name, "hash": file_hash})
                print("file has been hashed")

#monitor files
def monitor():
#finds saved hashes
    with open ("hashes.csv","r", newline="") as f:
        saved_hashes = []
        reader = csv.DictReader(f)
        for row in reader:
            saved_hashes.append({"key": row["key"], "hash": row["hash"]})

    bucket=[]
    print(f"{datetime.datetime.now()}: Start file monitoring...")
    while True:
#hashes the files again to create the current hashes to compare against saved hashes
        current_hash = []
        for dictionary in saved_hashes:
            new_key = dictionary.get("key")
            new_hash = hash_file(new_key)
            current_hash.append({"key": new_key, "hash": new_hash})

#compare file hashes
        for dic in saved_hashes:
            for c in current_hash:
                saved_file = dic.get("key")
                if dic.get("key") == c.get("key") and dic.get("hash") != c.get("hash") and c.get("hash") not in bucket:
                    print(f"{datetime.datetime.now()}: Warning! File {saved_file} has been altered!")
                    bucket.append(c.get("hash"))
def main():
    a = ""
    while a.lower() != "h" or a.lower() != "m":
        a  = input("Do you want to hash a file (h) or monitor files (m): ")
        if a.lower() == "h":
            f = input("File to hash: ")
            write_hash(f)
        elif a.lower() == "m":
            monitor()

if __name__ == "__main__":
    main()