def read():
    try:
        namefile = input("File name: ")
        with open(namefile, "rb") as r:
            byte = r.read(1)
            k = 0
            while byte:
                try:
                    byte = r.read(1).decode("utf-8")
                except:
                    continue
                print(byte, end="")
                k += 1
    except FileNotFoundError:
        print("\n[x] File: '" + str(namefile) + "' is not defined!")
        raise SystemExit
    else:
        print("\n[+] Number of bytes in the '" + str(namefile) + "': " + str(k))



def write():
    try:
        namefile = input("File name: ")
        with open(namefile, 'ab') as file:
            text = input("Write the text: ")
            file.write(text.encode("utf-8"))
    except FileNotFoundError:
        print("[x] File: '" + str(namefile) + "' is not defined!")
        raise SystemExit
    else:
        print("[+] File: " + str(namefile) + " successfully overwritten!")



def python_zip():
    try:
        namefile = input("File-Cover: ")
        with open(namefile, 'rb') as file1:
            read1 = file1.read()
    except FileNotFoundError:
        print("[x] File: '" + str(namefile) + "' is not defined!")
        raise SystemExit
    try:
        zipfile = input("Zip-File: ")
        with open(zipfile, 'rb') as file2:
            read2 = file2.read()
    except FileNotFoundError:
        print("[x] File: '" + str(zipfile) + "' is not defined!")
        raise SystemExit
    with open(namefile, 'wb') as file3:
        file3.write(read1)
        file3.write(read2)
        print("[+] File: " + str(namefile) + " successfully overwritten!")


def main():
    print("r - read, w - write, z - zip write")
    choise = input()
    if choise == "w":
        write()
    elif choise == "r":
        read()
    elif choise == "z":
        python_zip()

if __name__ == "__main__":
    main()
