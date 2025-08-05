def main():
    import random
    import string


    punctuation_file = string.punctuation
    string_file = string.ascii_letters

    passwords = ["123456", "password", "qwerty", "admin", "abc123", "iloveyou", "dragon", "monkey", "welcome", "secret"]

    percentages = [22, 18, 14, 12, 9, 7, 6, 5, 4, 3]

    add_option = [
        lambda: str(random.randint(0, 999)).zfill(3),
        lambda: str(random.choice(punctuation_file)),
        lambda: str(random.randint(1990, 2026)),
        lambda: str(random.randint(0,1000)),
        lambda: random.choice(string_file)

    ]

    weight_of_add_option = [54,2,5,26,13]

    add_amount = [1, 2]
    weight_amount = [80, 20]

    add_position = ["first", "mid", "last", "none"]
    weight_position = [5,10,24,61]

    passwords_final = []

    for _ in range(100000):
        final_amount = random.choices(add_amount, weights=weight_amount, k=1)[0]
        words = random.choices(passwords, weights=percentages, k=1)[0]

        ad_mnt = []
        for _ in range(int(final_amount)):
            func = random.choices(add_option, weights=weight_of_add_option, k=1)[0]
            results = func()
            ad_mnt.append(results)

        combine_ad_mnt = "".join(ad_mnt)
        final_position = random.choices(add_position, weights=weight_position, k=1)[0]

        if final_position == "first":
            password_temp = combine_ad_mnt + words

        elif final_position == "last":
            password_temp = words + combine_ad_mnt

        elif final_position == "mid":
            if len(words) > 1:
                split_pos = random.randint(1, len(words) - 1)

            if len(words) == 1:
                split_pos = 1

            password_temp = words[:split_pos] + combine_ad_mnt + words[split_pos:]

        else:
            password_temp = words

        passwords_final.append(password_temp)

    with open("wordlist.txt", "w") as ar:
        for i in passwords_final:
            ar.write(i + "\n")


if __name__ == "__main__":
    main()