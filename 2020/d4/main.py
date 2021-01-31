from utils import read_files
import re

raw = read_files("d4")  # , 'example.txt')

passports = []
temp_passport = ""
for line in raw:
    if line == "":
        passports.append(temp_passport.strip())
        temp_passport = ""
    temp_passport += " " + line
passports.append(temp_passport.strip())


def valid_byr(val):
    """Birth year"""
    val = int(val)
    return bool(val >= 1920 and val <= 2002)


def valid_iyr(val):
    """Issue year"""
    val = int(val)
    return bool(val >= 2010 and val <= 2020)


def valid_eyr(val):
    """Expiration year"""
    val = int(val)
    return bool(val >= 2020 and val <= 2030)


def valid_hgt(val):
    """Height"""
    if re.match(r"^\d+(cm|in)$", val):
        num = int(re.match(r"\d+", val).group())
        if "cm" in val:
            return bool(num >= 150 and num <= 193)
        elif "in" in val:
            return bool(num >= 59 and num <= 76)
        else:
            raise ValueError(f'Invalid hgt: {val}')
    return False


def valid_hcl(val):
    """Hair color"""
    return bool(re.match(r"^#([0-9a-f]{6})$", val))


def valid_ecl(val):
    """Eye color"""
    return bool(val in ("amb blu brn gry grn hzl oth".split()))


def valid_pid(val):
    """Passport ID"""
    return bool(re.match(r"^\d{0,9}$", val))


def valid_p(p):
    """Count passports that have each of the fields not including CID"""
    required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    id_dict = dict()
    key_vals = p.split()
    for item in key_vals:
        k, v = item.split(":")
        id_dict[k] = v.strip()
    return all(k in id_dict.keys() for k in required_keys)


print(sum(valid_p(p) for p in passports))


def valid_p_2(p):
    required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    id_dict = dict()
    key_vals = p.split()
    for item in key_vals:
        k, v = item.split(":")
        id_dict[k] = v
    all_fields = all(k in id_dict.keys() for k in required_keys)
    if not all_fields:
        return False
    if (
        valid_byr(id_dict["byr"])
        and valid_iyr(id_dict["iyr"])
        and valid_eyr(id_dict["eyr"])
        and valid_hgt(id_dict["hgt"])
        and valid_hcl(id_dict["hcl"])
        and valid_ecl(id_dict["ecl"])
        and valid_pid(id_dict["pid"])
    ):
        return True
    return False


# 199 too high!
print(sum(valid_p_2(p) for p in passports))
# It was 198 which I got by guessing...!
