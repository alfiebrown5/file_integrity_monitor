# file_integrity_monitor
Monitors file hashes to ensure integrity of file contents.

For a detailed writeup, check out my GitBook: https://alfie-brown-cybersecurity-portfo.gitbook.io/alfie-brown-portfolio/ 

This project is a python3 script that is able to hash files into SHA256 format and monitor files hashed in the SHA256 format for changes. I chose to use SHA256 as it creates longer and more complex hashes than other hashing formats like MD5 and SHA-1, thus storing the data in the file more securely than those other hashes. 

The script is able to monitor the integrity of files by comparing the current hash of the file with the has that has been stored by the script before. This ensures integrity of the contents of the files hashed and stored in the directory as the hash of the file is based on the contents of the file, and so would be different if the contents of the file were altered. This is useful for if certain files need to be protected from changes. For example, if a file contained sensitive data, or data critical to a company, a file integrity monitor would detect if a threat actor has tampered with the data in the file and alert the user of the monitor.

It writes hashes to the hashes.csv file and the .txt files in the repository are examples of files that I've hashed and stored in the hashes.csv file. 
