for a in range(66):
    for b in range(10):
        s = "0" + "b" * a + "0"
        while  "00" not in s:
            s = s.replace("033", "21120", 1)
            s = s.replace("034", "22120", 1)
            s = s.replace("04", "220", 1)
            s = s.replace("030", "200", 1)

            c = (s.count('1') + s.count('2') * 2)
            if len(s) == 65 and (s.count('1') + s.count('2') * 2) % ((s.count('1') + s.count('2') * 2)/2) == 0 and "b" == 4:
                print(a)



