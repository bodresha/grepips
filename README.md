# grepips
Making this tool to get the ips ( fresh dns servers ) aka resolvers then inserting it on ~/.config/subfinder/config.yaml

Twitter: @Bodresha

# two ways to run
(1) - recommended

# run below command:
./run.sh config.yaml https://raw.githubusercontent.com/BBerastegui/fresh-dns-servers/master/resolvers.txt

# syntax:
./run.sh <config-file-path> <url-to-fetch-data>


# (2)
1. install the required lib from requirements.txt file
pip3 install requests
pip3 install oyaml

2. run below command:
python3 run.py config.yaml https://raw.githubusercontent.com/BBerastegui/fresh-dns-servers/master/resolvers.txt

syntax:
python3 run.py <config-file-path> <url-to-fetch-data>
