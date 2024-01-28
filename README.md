# **convert256** #
This is a simple python script that takes SHA1 and/or MD5 hashes then "converts" them to SHA256 by making API calls to VirusTotal.

_Note:_
- _Only a file must be provided as an input as shown in the example below._ 
- _This requires a sample file to be pre-emptively created. eg: hashes.txt._
- _All of the instructions provided below are in the assumption that you already have the VirusTotal API key._

EXAMPLE:
```
ashareefdeen@shorts (v3)-> cat hashes.txt
736a4cfad1ed83a6a0b75b0474d5e01a3a36f950
85851e09b368ebba90f5d922cd77f348
f6e755e2af0231a614975d64ea3c8116
56a504a34d2cfbfc7eaa2b68e34af8ad
ad602039c6f0237d4a997d5640e92ce5e2b3bba3
13037b749aa4b1eda538fda26d6ac41c8f7b1d02d83f47b0d187dd645154e033

ashareefdeen@shorts (v3)-> convert256 -f hashes.txt
```

## Instructions: ##
1. Execute the below command to download:
```
wget https://raw.githubusercontent.com/sshakoor98/Public-convert256/main/convert256.py
```
2. Move the convert256 to /bin directory and give it executable permissions:
```
mv convert256 ~/bin
chmod +x ~/bin/convert256
```
3. Congratulations! You can now be stress free from those annoying bulk MD5 and SHA1 hashes:
```
convert256 -f <hash_file_list>
```
4. Alternatively, you may directly invoke the python script:
```
python convert256.py -f <hash_file_list>
```
