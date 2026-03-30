import sys
import antigravity

# input → string → md5 → dividir → convertir → normalizar → sumar

def colors():
    colors = {
        "cyan" : "\x1b[36m",
        "red" : "\x1b[31m",
        "green" : "\x1b[32m",
        "reset" : "\x1b[37m",
    }
    return colors

def check_date_format():
    date = sys.argv[1]
    date_format_error = "Invalid date format (YYYY-MM-DD)"

    # 1. Check len
    if len(date) != 10:
        raise Exception(date_format_error)

    # 2. Spit and check separators
    y, m, d = date[:4], date[5:7], date[8:10]
    if date[4] != "-" or date[7] != "-":
        raise Exception("Invalid date separators")

    # 3. Check numeric parts
    if y.isdigit() and m.isdigit() and d.isdigit() != True:
        raise Exception("All parts of the date must be a integer")
    else:
        y = int(y)
        m = int(m)
        d = int(d)
        if (y < 0 or y > 2026) or (m < 1 or m > 12) or (d < 1 or d > 31):
            raise Exception("Year (0 - 2026), month (1 - 12) or day (1 - 31) out of range")

    return str(y), str(m), str(d)

def check_coords():
    lat = sys.argv[2]
    lon = sys.argv[3]

    try:
        lat = float(lat)
        lon = float(lon)
    except Exception as e:
        if str(e):
            raise Exception("Latitude and Longitude must be a float")

    if (lat < -90 or lat > 90) or (lon < -180 or lon > 180):
        raise Exception("Latitude (-90 - 90) or Longitude (-180 - 180) out of range")
        
    return str(lat), str(lon)


def check_dow_jones():
    dow = sys.argv[4]

    try:
        dow = float(dow)
    except Exception as e:
        if str(e):
            raise Exception("Dow Jones Industrial Average must be a float")

    if dow < 10000 or dow > 50000:
        raise Exception("Dow jones out of ranges (10.000 - 50.000)")
    
    return str(dow)

def md5_hexdigest(s: str) -> str:
    h = __import__("hashlib").md5()
    h.update(s.encode() if isinstance(s, str) else s)
    return h.hexdigest()

def check_args():
    color = colors()

    # 1.Number of args
    if len(sys.argv) != 5:
        print(color["red"] +
              "ERROR: " +
              color["reset"] +
              "Usage: geohashing.py 'date(YYYY-MM-DD)' 'latitude(-90 - 90)' 'longitude(-180 - 180)' 'Dow Jones Industrial Average'")
        exit(1)

    # 2. Check args
    y, m, d = check_date_format()
    lat, lon = check_coords()
    dow = check_dow_jones()

def geohashing():
    check_args()
    print("HOOLA!") # DB
    print(md5_hexdigest("HOOLA!")) # DB
    """
    """

if __name__ == '__main__':
    try:
        geohashing()
    except Exception as e:
        if str(e):
            print(f"ERROR: {e}")
