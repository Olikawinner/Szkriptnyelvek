hex_str = "4D69 61 6E657665 616E6E616B 61 68656C7969 6B617063736F6C6F6B6F7A706F6E746E616B2C 61686F6C 6D616A646E656D 656C6B617074616B"
cleaned = hex_str.replace(" ", "")
bytes_obj = bytes.fromhex(cleaned)
print(bytes_obj.decode("utf-8"))

"""
Mi a neve annak a helyi kapcsolóközpontnak, ahol majdnem elkaptak?
"""