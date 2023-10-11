while True:
    meme_dict = {
                "cringe": "Garip ya da utandırıcı bir şey",
                "lol": "Komik bir şeye verilen cevap",
                }
    word = input("Anlamadığınız bir kelime yazın: ")
    word = word.lower()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Kelime sözlükte değil.")
