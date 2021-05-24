# testo jednokrotnej odpowiedzi, nie obsługuje prawidłowo wielokrotnego wyboru
# akceptowalne pliki abc.txt, gdzie a, b, c cyfry: Przykładowo "001.txt"

def readtesto(path: str, name: str):
    if isinstance(path, str) and isinstance(name, str):
        file = open(path+name, "r")
        index = file.read().find("1", 0, 5)
        file.seek(0)
        lines = file.readlines()
        file.close()
        file = open(path+"000_combined.txt/", "a")
        print(lines[1] + lines[index + 1])
        file.write(lines[1] + lines[index + 1] + "\n")
    else:
        exit()


if __name__ == '__main__':
    baza_path = "F:/OneDrive - Politechnika Wroclawska/PWR/sem IV/EAKU/" \
                "Elektroakustyka-1-master/Elektroakustyka-1-master/baza/"
    fail_index = 0
    f = open(baza_path+"000_combined.txt/", "w")
    f.write("")
    f.close()
    for a in range(10):
        for b in range(10):
            if a == 0 and b == 0:
                continue
            number = "0"+str(a)+str(b)+".txt/"
            try:
                readtesto(baza_path, number)
            except IOError:
                fail_index += 1
                if fail_index == 3:
                    break
