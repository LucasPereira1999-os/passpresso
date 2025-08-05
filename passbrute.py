import generate as g
import pyzipper
import argparse

default_wordlist = g.main()
parser = argparse.ArgumentParser()
parser.add_argument("--input_zip", "-iz", help="input your zip file", required=True, type=str)
parser.add_argument("--wordlist", "-w", help="input your wordlist", type=str, default=default_wordlist)
args = parser.parse_args()

password_file = []

if args.wordlist == default_wordlist:
    with open("wordlist.txt", "r") as r:
        content = r.read()
        for i in content.splitlines():
            password_file.append(i.strip())
else:
    with open(args.wordlist, "r") as rb:
        content2 = rb.read()
        for i in content2.splitlines():
            password_file.append(i.strip())

input_user = args.input_zip
found = False

for i in password_file:
    try:
        with pyzipper.AESZipFile(input_user, "r", encryption=pyzipper.WZ_AES) as ar:
            ar.pwd = i.encode()
            all_file = ar.namelist()
            for name_file in all_file:
                with ar.open(name_file) as f:
                    cont = f.read().decode("utf-8", errors="ignore")
            print(f"\rPassword found: {i}")
            print(cont)
            found = True
            break
    except Exception as e:
        print(f"\rWrong password: {i}", end="")

if not found:
    print("\nPassword not found")
