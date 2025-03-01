s = "0" + "1"*10 + "2"*10 + "0"
for x in range(len(s)):
    print(s)
    s = s[2:] + s[0]
    while not "00" in s:
        s = s.replace("012", "30", 1)

        if "00" in s:
            s = s.replace("011", "20", 1)
            s = s.replace("022", "40", 1)

        else:
            s = s.replace("01", "10", 1)
            s = s.replace("02", "101", 1)

    if s.count("1") == 7 and s.count("2") == 5 and s.count("0") == 2:
        print(s.count("3"))






