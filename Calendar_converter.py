gmon= ["January","February","March","April","May","June","July","August","September","October","November","December"]
emon_a=["መስከረም","ጥቅምት","ህዳር","ታህሳስ","ጥር","የካቲት","መጋቢት","ሚያዚያ","ግንቦት","ሰኔ","ሐምሌ","ነሐሴ","ጳጉሜ"]
emon_e=["Meskerem","Tikimt","Hidar","Tahisas","Tir","Yekatit","Megabit","Miazia","Ginbot","Sene","Hamle","Nehase","Pagume"]
bd= [31,28,31,30,31,30,31,31,30,31,30,31]

print("==================================================")
print("  GREGORIAN / JULIAN CALENDAR TO ETHIOPIAN CALENDAR CONVERTER")
print("    ከግሪጎርያን / ጁሊያን ቀን መቁጠሪያ ወደ የኢትዮጵያ ቀን መቁጠሪያ መቀየሪያ")
print("==================================================")
print("   Student : Henok Teshome  |  ID: UGR/1488/17")
print("   Section : 6              |  College: CTBE")
print("   Instructor: Kassahun T.")
print("==================================================")

while True:
    print()
    raw = input("Enter a year (Julian or Gregorian) or Quit(q): ")

    clean = ""
    for char in raw.strip():
        if char != " ":
            clean += char

    low = clean.lower()

    if low == "q" or low == "quit":
        print("\nThank you! Goodbye.\n")
        break

    ad = True
    for char in clean:
        if char not in "0123456789":
            ad = False
            break

    if not ad or clean == "":
        print("    Please enter a valid integer year or quit(q).")
        continue

    yr = int(clean)

    if yr < 1 or yr > 9999:
        print("    Year must be between 1 and 9999.")
        continue

    print("\n==================================================")
    if yr <= 1751:
        print("  JULIAN CALENDAR  -  Year " + str(yr))
    elif yr == 1752:
        print("  CALENDAR REFORM YEAR  -  " + str(yr))
    else:
        print("  GREGORIAN CALENDAR  -  Year " + str(yr))
    print("==================================================")

    lp = False
    if yr <= 1751:
        if yr % 4 == 0:
            lp = True
    else:
        if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
            lp = True

    mn = 1
    while mn <= 12:

        dm = bd[mn - 1]
        if mn == 2 and lp:
            dm = 29
        if yr == 1752 and mn == 9:
            dm = 19

        ac = []
        if yr == 1752 and mn == 9:
            for dy in range(1, 3):
                ac.append(dy)
            for dy in range(14, 31):
                ac.append(dy)
        else:
            for dy in range(1, dm + 1):
                ac.append(dy)

        mz = mn
        yz = yr
        if mz < 3:
            mz += 12
            yz -= 1
        kz = yz % 100
        jz = yz // 100

        if yr < 1752 or (yr == 1752 and mn <= 9):
            h = (1 + (13 * (mz + 1)) // 5 + kz + kz // 4 + 5 - jz) % 7
        else:
            h = (1 + (13 * (mz + 1)) // 5 + kz + kz // 4 + jz // 4 - 2 * jz) % 7
        swd = (h + 6) % 7

        fd = ac[0]
        a = (14 - mn) // 12
        yjd = yr + 4800 - a
        mjd = mn + 12 * a - 3
        if yr > 1752 or (yr == 1752 and mn > 9) or (yr == 1752 and mn == 9 and fd >= 14):
            jdn = fd + (153 * mjd + 2) // 5 + 365 * yjd + yjd // 4 - yjd // 100 + yjd // 400 - 32045
        else:
            jdn = fd + (153 * mjd + 2) // 5 + 365 * yjd + yjd // 4 - 32083

        ee = 1724221
        er = jdn - ee
        ey = 1
        bk = er // 1461
        er -= bk * 1461
        ey += bk * 4
        while True:
            yl = 366 if ey % 4 == 3 else 365
            if er < yl:
                break
            er -= yl
            ey += 1
        em = 1
        while True:
            ml = 30
            if em == 13:
                ml = 6 if ey % 4 == 3 else 5
            if er < ml:
                break
            er -= ml
            em += 1
        ed = er + 1

        ld = ac[-1]
        a2 = (14 - mn) // 12
        yjd2 = yr + 4800 - a2
        mjd2 = mn + 12 * a2 - 3
        if yr > 1752 or (yr == 1752 and mn > 9) or (yr == 1752 and mn == 9 and ld >= 14):
            jdn2 = ld + (153 * mjd2 + 2) // 5 + 365 * yjd2 + yjd2 // 4 - yjd2 // 100 + yjd2 // 400 - 32045
        else:
            jdn2 = ld + (153 * mjd2 + 2) // 5 + 365 * yjd2 + yjd2 // 4 - 32083

        er2 = jdn2 - ee
        ey2 = 1
        bk2 = er2 // 1461
        er2 -= bk2 * 1461
        ey2 += bk2 * 4
        while True:
            yl2 = 366 if ey2 % 4 == 3 else 365
            if er2 < yl2:
                break
            er2 -= yl2
            ey2 += 1
        em2 = 1
        while True:
            ml2 = 30
            if em2 == 13:
                ml2 = 6 if ey2 % 4 == 3 else 5
            if er2 < ml2:
                break
            er2 -= ml2
            em2 += 1

        if yr <= 1751:
            yrl = "Julian Year: " + str(yr)
        elif yr == 1752:
            yrl = "Reform Year: " + str(yr)
        else:
            yrl = "Gregorian Year: " + str(yr)

        if ey != ey2:
            eyl = "Ethiopian Years: " + str(ey) + " - " + str(ey2)
        else:
            eyl = "Ethiopian Year: " + str(ey)

        seen_eth_months = []
        t_cey = ey
        t_cem = em
        t_ced = ed
        for _ in ac:
            if t_cem not in seen_eth_months:
                seen_eth_months.append(t_cem)
            t_ced += 1
            t_cml = 30
            if t_cem == 13:
                t_cml = 6 if t_cey % 4 == 3 else 5
            if t_ced > t_cml:
                t_ced = 1
                t_cem += 1
                if t_cem > 13:
                    t_cem = 1
                    t_cey += 1

        ems_parts = []
        for m in seen_eth_months:
            ems_parts.append(emon_e[m - 1] + " (" + emon_a[m - 1] + ")")
        ems = " - ".join(ems_parts)

        lh = yrl
        while len(lh) < 26:
            lh += " "

        gl = gmon[mn - 1]
        while len(gl) < 26:
            gl += " "

        print("\n" + lh + eyl)
        print(gl + ems)
        print("|------------------------------------------------|")
        print("|Sun   |Mon   |Tue   |Wed   |Thu   |Fri   |Sat   |")
        print("|------------------------------------------------|")

        cs = []
        for _ in range(swd):
            cs.append((-1, -1))

        cey = ey
        cem = em
        ced = ed

        for ai_val in ac:
            cs.append((ai_val, ced))
            ced += 1
            cml = 30
            if cem == 13:
                cml = 6 if cey % 4 == 3 else 5
            if ced > cml:
                ced = 1
                cem += 1
                if cem > 13:
                    cem = 1
                    cey += 1

        while len(cs) % 7 != 0:
            cs.append((-1, -1))

        for wi in range(0, len(cs), 7):
            wk = cs[wi:wi + 7]
            rgc = "|"
            rec = "|"
            for cl in wk:
                if cl[0] == -1:
                    rgc += "      |"
                    rec += "      |"
                else:
                    gcs = str(cl[0])
                    ecs = str(cl[1])

                    while len(gcs) < 5:
                        gcs = " " + gcs
                    while len(ecs) < 5:
                        ecs += " "

                    rgc += gcs + " |"
                    rec += " " + ecs + "|"
            print(rgc)
            print(rec)
            print("|------------------------------------------------|")

        mn += 1

    print()
    ar = input("Would you like to enter another year? yes(y) / no(n): ")

    agc = ""
    for char in ar.strip():
        if char != " ":
            agc += char

    agl = agc.lower()

    if agl != "y" and agl != "yes":
        print("\nThank you! Goodbye.\n")
        break
