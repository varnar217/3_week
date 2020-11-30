with open('referat.txt', 'r', encoding='utf-8') as f:

    content = f.read()
    print(len(content))

    content = content.replace("\n", " ")
    content = content.replace(",", "").replace(".", "").replace("?", "").replace("!", "")

    content = content.lower()
    #content = content.split()

    words = content.split()
    print(len(words))

    #f.close()
    f.seek(0)
    content_2 = f.read()

    content_2 = content_2.replace(".", "!")
    with open('referat2.txt', 'w', encoding='utf-8') as f1:
        f1.write(content_2)
        f1.close()

    #print(content_2)

    f.close()





    #words.sort()
