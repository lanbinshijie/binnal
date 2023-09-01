def convert_ipv4_to_address_code(ipv4_address):

    # 将IPv4地址拆分为四个部分
    parts = ipv4_address.split('.')

    # 检查IP地址是否符合局域网内的地址范围
    if parts[0] == '192' and parts[1] == '168':
        type_code = '2W'
    elif parts[0] == '10' and parts[1] == '10':
        type_code = '2F'
    else:
        return None
    
    # 将IP地址转换为对应的地址码
    address_code = type_code
    for part in parts[2:]:
        part_value = int(part)
        address_code += convert_code(part_value)
    
    return address_code

def convert_address_code_to_ipv4(address_code):
    # 检查地址码长度是否正确
    if len(address_code) != 6:
        return None
    
    type_code = address_code[:2]
    ip_digits = address_code[2:]

    # 获取IP地址的类型
    if type_code == '2W':
        ip_type = '192.168'
    elif type_code == '2F':
        ip_type = '10.10'
    else:
        return None
    
    # 将地址码转换为IP地址
    fdi = ip_digits[0:2]
    ldi = ip_digits[2:]
    fdi = convert_code(fdi, 2)
    ldi = convert_code(ldi, 2)

    return ip_type+'.'+str(fdi)+'.'+str(ldi)


def convert_code(input_value, typer=1):
    
    def get_key_by_value(dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
        # 如果没有找到对应值的键，可以选择返回None或者其他自定义的值
        return None
    
    code_dict = {
        0: '00', 1: '01', 2: '02', 3: '03', 4: '04', 5: '05', 6: '06', 7: '07', 8: '08', 9: '09',
        10: '0A', 11: '0B', 12: '0C', 13: '0D', 14: '0E', 15: '0F', 16: '0G', 17: '0H', 18: '0I',
        19: '0J', 20: '0K', 21: '0L', 22: '0M', 23: '0N', 24: '0P', 25: '0Q', 26: '0R', 27: '0S',
        28: '0T', 29: '0U', 30: '0V', 31: '0W', 32: '0X', 33: '0Y', 34: '0Z',
        35: 'A0', 36: 'A1', 37: 'A2', 38: 'A3', 39: 'A4', 40: 'A5', 41: 'A6', 42: 'A7', 43: 'A8', 44: 'A9',
        45: 'AA', 46: 'AB', 47: 'AC', 48: 'AD', 49: 'AE', 50: 'AF', 51: 'AG', 52: 'AH', 53: 'AI',
        54: 'AJ', 55: 'AK', 56: 'AL', 57: 'AM', 58: 'AN', 59: 'AP', 60: 'AQ', 61: 'AR', 62: 'AS',
        63: 'AT', 64: 'AU', 65: 'AV', 66: 'AW', 67: 'AX', 68: 'AY', 69: 'AZ',
        70: 'B0', 71: 'B1', 72: 'B2', 73: 'B3', 74: 'B4', 75: 'B5', 76: 'B6', 77: 'B7', 78: 'B8', 79: 'B9',
        80: 'BA', 81: 'BB', 82: 'BC', 83: 'BD', 84: 'BE', 85: 'BF', 86: 'BG', 87: 'BH', 88: 'BI',
        89: 'BJ', 90: 'BK', 91: 'BL', 92: 'BM', 93: 'BN', 94: 'BP', 95: 'BQ', 96: 'BR', 97: 'BS',
        98: 'BT', 99: 'BU', 100: 'BV', 101: 'BW', 102: 'BX', 103: 'BY', 104: 'BZ',
        105: 'C0', 106: 'C1', 107: 'C2', 108: 'C3', 109: 'C4', 110: 'C5', 111: 'C6', 112: 'C7', 113: 'C8', 114: 'C9',
        115: 'CA', 116: 'CB', 117: 'CC', 118: 'CD', 119: 'CE', 120: 'CF', 121: 'CG', 122: 'CH', 123: 'CI',
        124: 'CJ', 125: 'CK', 126: 'CL', 127: 'CM', 128: 'CN', 129: 'CP', 130: 'CQ', 131: 'CR', 132: 'CS',
        133: 'CT', 134: 'CU', 135: 'CV', 136: 'CW', 137: 'CX', 138: 'CY', 139: 'CZ',
        140: 'D0', 141: 'D1', 142: 'D2', 143: 'D3', 144: 'D4', 145: 'D5', 146: 'D6', 147: 'D7', 148: 'D8', 149: 'D9',
        150: 'DA', 151: 'DB', 152: 'DC', 153: 'DD', 154: 'DE', 155: 'DF', 156: 'DG', 157: 'DH', 158: 'DI',
        159: 'DJ', 160: 'DK', 161: 'DL', 162: 'DM', 163: 'DN', 164: 'DP', 165: 'DQ', 166: 'DR', 167: 'DS',
        168: 'DT', 169: 'DU', 170: 'DV', 171: 'DW', 172: 'DX', 173: 'DY', 174: 'DZ',
        175: 'E0', 176: 'E1', 177: 'E2', 178: 'E3', 179: 'E4', 180: 'E5', 181: 'E6', 182: 'E7', 183: 'E8', 184: 'E9',
        185: 'EA', 186: 'EB', 187: 'EC', 188: 'ED', 189: 'EE', 190: 'EF', 191: 'EG', 192: 'EH', 193: 'EI',
        194: 'EJ', 195: 'EK', 196: 'EL', 197: 'EM', 198: 'EN', 199: 'EP', 200: 'EQ', 201: 'ER', 202: 'ES',
        203: 'ET', 204: 'EU', 205: 'EV', 206: 'EW', 207: 'EX', 208: 'EY', 209: 'EZ',
        210: 'F0', 211: 'F1', 212: 'F2', 213: 'F3', 214: 'F4', 215: 'F5', 216: 'F6', 217: 'F7', 218: 'F8', 219: 'F9',
        220: 'FA', 221: 'FB', 222: 'FC', 223: 'FD', 224: 'FE', 225: 'FF', 226: 'FG', 227: 'FH', 228: 'FI',
        229: 'FJ', 230: 'FK', 231: 'FL', 232: 'FM', 233: 'FN', 234: 'FP', 235: 'FQ', 236: 'FR', 237: 'FS',
        238: 'FT', 239: 'FU', 240: 'FV', 241: 'FW', 242: 'FX', 243: 'FY', 244: 'FZ',
        245: 'G0', 246: 'G1', 247: 'G2', 248: 'G3', 249: 'G4', 250: 'G5', 251: 'G6', 252: 'G7', 253: 'G8', 254: 'G9',
        255: 'GA', 256: 'GB'
    }

    if typer == 1:
        return code_dict[input_value]
    else:
        return get_key_by_value(code_dict, input_value)
