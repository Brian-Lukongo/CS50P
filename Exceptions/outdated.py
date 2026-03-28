def main():
    months = [    
    "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    while True:
        date_str = input("Date: ").strip().title()
        try:
            if "/" in date_str:
                m, d, y = date_str.split("/")
                m = int(m)
                d = int(d)
                y = int(y)

                if 1<= m <= 12 and 1 <= d <=31:
                    print(f"{y:04}-{m:02}-{d:02}")
                    break
            elif "," in date_str:
                month_word, day_str, year_str = date_str.split()
                if day_str.endswith(","):
                    d = int(day_str.replace(",", ""))
                    if month_word in months and 1 <= d <= 31:
                        m = months.index(month_word) + 1
                        y = int(year_str)
                        print(f"{y:04}-{m:02}-{d:02}")
                        break
        except (ValueError, IndexError):
            pass
if __name__ == "__main__":
    main()