def dePrima(plaintext):
    key = ['1Z', '2D', '3F', '4C', '4B', '5D', '6G', '7J', '8L', '8W', '9W', '1Q', '4H',
           '5K', '3D', '2F', '1D', '1B', '1A', '2G', '3M', '4D', '6D', '6H', '7F', '7D', '12', '55', '34', '77', '65', '88', '87', '85', '90', '09', '07', '21', '23', '28', '29', '20', '39', '80', '84', '78', 'B1', 'D1', 'C1', 'F1', 'G1', 'R1', 'U1', 'A1', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'B3', 'C3', 'D3', 'F3', 'G3', 'B4', 'C4', 'D4', 'F4', 'G4', 'B5', 'C5']
    alphabet = "[]abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chipertext = ""
    n = len(plaintext)
    prima = 173
    result = ""
    if n % 2 == 0:
        n = n / 2
        for i in range(round(n)):
            ii = i * 2
            iii = i * 2 + 1
            idx = key.index(plaintext[ii] + plaintext[iii])
            chipertext = chipertext + str(idx)
        x = int(chipertext) - prima
        x = str(round(x))
        i = 0
        ary = []
        h = ""
        start = True
        while start:
            try:
                if x[i] == "1":
                    h = x[i+1] + x[i+2]
                    i = i + 3
                    ary.append(h)
                else:
                    h = x[i]
                    i += 1
                    ary.append(h)
            except:
                start = False
        for x in ary:
            result = result + alphabet[int(x)]
        return result
    else:
        error = "Incorrect encryption!"
        return error


if __name__ == '__main__':
    print(dePrima("6G2D2D5D4B2D2D8W2D3F6G2D2D7J2D3F2D2D3F2D8W2D2D1Z3F8W4C"))
