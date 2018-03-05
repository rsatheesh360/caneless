def CamelCase(string_ip):
    import re
    return ''.join(x.capitalize() or '_' for x in string_ip.split('_'))
print(CamelCase('guvi_technologies'))
print(camelcase('guvi_technologies'))
