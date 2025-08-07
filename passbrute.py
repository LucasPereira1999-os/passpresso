
import generate as g
import pyzipper
import argparse
import time
loop = True
question = True

def brute():
    global loop, question
    default_wordlist = g.main()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_zip", "-iz", help="input your zip file", required=True, type=str)
    parser.add_argument("--wordlist", "-w", help="input your wordlist", type=str, default=default_wordlist)
    parser.add_argument("--batch", "-b", help="automate brute-force until found", action="store_true")
    args = parser.parse_args()

    question = not args.batch
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
                print(f"\n[+] Password found: {i}")
                print(f"[+] File name   : {name_file}")
                print(f"[+] File content:\n{cont}")
                found = True
                loop = False
                break
        except Exception as e:
            print(f"\rWrong password: {i}", end="")

    if not found:
        print("\nPassword not found")


while loop:
    time.sleep(2)
    brute()
    if question:
        while True:
            user_input = input("Input your choice, Do you want to continue ? [Y] | [N] : ").upper()
            if user_input == "Y":
                break

            elif user_input == "N":
                loop = False
                break

            else:
                print("Input the right option")
                continue
    else:
        continue
