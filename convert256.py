#!/support/bin/python3.11

import re, json, requests, sys, json, configparser, argparse, getpass

vt_api = "[REDACTED]"

# Setting the CLI like options
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
parent_parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-f', '--file', action='store',
                dest='file_name',
                help='File name containing bulk of SHA1/MD5 hashes, one per line.', nargs='?')

if len(sys.argv) < 2 or sys.argv[1] == "--help" or sys.argv[1] == "-h":
        parser.print_help()
        sys.exit(1)

args = parser.parse_args()

# Snippet to create API calls to VirusTotal and respond with JSON sha256 attribute
def hash_convert(lines,count,i):
                string_line = str.rstrip(re.sub(r"[\n\t\s]*","",lines)) # Removing tabs, space and line breaks
                char_len = len(string_line)
                if char_len == 32 or char_len == 40 and (char_len < 64):
                        url_vt = "https://www.virustotal.com/api/v3/files/"
                        url_vt_cat = url_vt+string_line
                        headers = {'x-apikey': vt_api}
                        response = requests.get(url_vt_cat, headers=headers)
                        json_response = response.json()
                        try:
                                vt_256 = json_response['data']['attributes']['sha256']
                                vt_256 = vt_256.replace('\n','')
                                print(f"\n{count}) {lines} ---> {vt_256}")

                                if char_len == (32 or 33):
                                        md5.append(vt_256)
                                elif char_len == (40 or 41):
                                        sha1.append(vt_256)
                                else:
                                        pass

                        except:
                                print(f"\n{count}) {string_line} ---> N/A")
                                no_cov.append(lines)

                elif (char_len == 64):
                        print(f"\n{count}) {string_line} is already SHA256.")
                        already.append(lines)

                else:
                        print(f"\n{count}) {string_line} - Invalid Hash.")
                        invalid.append(lines)

# Final summary
def fin_summary():
        print("\n")
        print("MD5 Converted:")
        print("-------------")
        print(*md5, sep="\n")
        print(f"\n")
        print("SHA1 Converted:")
        print("--------------")
        print(*sha1, sep="\n")
        print(f"\n")
        print("MD5/SHA1 with no coverage (N/A):")
        print("-------------------------------")
        print(*no_cov, sep="\n")
        print(f"\n")
        print("Already present in list:")
        print("------------------------")
        print(*already, sep="\n")
        print(f"\n")
        print("Invalid Hash(es):")
        print("------------------------")
        print(*invalid, sep="\n")
        print(f"\n")

# Initiating the lists for final summary
list = []
md5 = []
sha1 = []
no_cov = []
already = []
invalid = []
count = 1

# To read filename as a list
args = parser.parse_args()
f = open(parser.parse_args().file_name)
lines = f.readlines()

# Start of output to print corresponding sha256
print(f"\nAssociated SHA256 hash(es):")
print(f"--------------------------")

for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
        if (lines[i] != ''):
                hash_convert(lines[i],count,i)
                i+=1
                count+=1
        else:
                break

fin_summary()
