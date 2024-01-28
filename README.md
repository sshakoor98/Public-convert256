# **convert256** #
This is a simple python script that takes SHA1 and/or MD5 hashes of malicious files in Bulk and then "converts" them to SHA256 by making API calls to VirusTotal.

_Note:_
- _Only a file must be provided as an input as shown in the example below._ 
- _This requires a sample file to be pre-emptively created. eg: hashes.txt._
- _All of the instructions provided below are in the assumption that you already have the VirusTotal API key._

EXAMPLE:
```
ashareefdeen@kali-> cat hashes.txt
736a4cfad1ed83a6a0b75b0474d5e01a3a36f950
85851e09b368ebba90f5d922cd77f348
f6e755e2af0231a614975d64ea3c8116
56a504a34d2cfbfc7eaa2b68e34af8ad
ad602039c6f0237d4a997d5640e92ce5e2b3bba3
13037b749aa4b1eda538fda26d6ac41c8f7b1d02d83f47b0d187dd645154e033

ashareefdeen@kali-> convert256 -f hashes.txt

Associated SHA256 hash(es):
--------------------------

1) 736a4cfad1ed83a6a0b75b0474d5e01a3a36f950 ---> 13037b749aa4b1eda538fda26d6ac41c8f7b1d02d83f47b0d187dd645154e033

2) 85851e09b368ebba90f5d922cd77f348 ---> N/A

3) f6e755e2af0231a614975d64ea3c8116 ---> N/A

4) 56a504a34d2cfbfc7eaa2b68e34af8ad ---> 9309fb2a3f326d0f2cc3f2ab837cfd02e4f8cb6b923b3b2be265591fd38f4961

5) ad602039c6f0237d4a997d5640e92ce5e2b3bba3 ---> N/A

6) 13037b749aa4b1eda538fda26d6ac41c8f7b1d02d83f47b0d187dd645154e033 is already SHA256.


MD5 Converted:
-------------
9309fb2a3f326d0f2cc3f2ab837cfd02e4f8cb6b923b3b2be265591fd38f4961


SHA1 Converted:
--------------
13037b749aa4b1eda538fda26d6ac41c8f7b1d02d83f47b0d187dd645154e033


MD5/SHA1 with no coverage (N/A):
-------------------------------
85851e09b368ebba90f5d922cd77f348
f6e755e2af0231a614975d64ea3c8116
ad602039c6f0237d4a997d5640e92ce5e2b3bba3


Already present in list:
------------------------
13037b749aa4b1eda538fda26d6ac41c8f7b1d02d83f47b0d187dd645154e033


Invalid Hash(es):
------------------------


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
