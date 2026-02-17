# Binary Watch Program (Run in VS Code)

def readBinaryWatch(turnedOn):
    r = []

    for h in range(12):        # hours: 0–11
        for m in range(60):    # minutes: 0–59
            if bin(h).count("1") + bin(m).count("1") == turnedOn:
                r.append(f"{h}:{m:02d}")

    return r
turnedOn = int(input("Enter number of LEDs ON: "))
result = readBinaryWatch(turnedOn)
print("Possible times:")
for t in result:
    print(t)
