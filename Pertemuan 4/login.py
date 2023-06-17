login_chance = 3

while login_chance > 0:

    username = input("Masukan username: ")
    password = input("Masukan password: ")

    login_success = (username == "jungkook") and (password == "jeon1997")

    if login_success:
        print("Login berhasil!")
        break

    else:
        login_chance = login_chance - 1
        print(f"Login gagal! Kesempatan mencoba: {login_chance}")
