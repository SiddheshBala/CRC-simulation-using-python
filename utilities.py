def BinaryCheck(value):
    try:
        if int(value,2):
            return True
    except ValueError:
        return False

def xor(a,b):
    result = ""
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result = result + "0"
        else:
            result = result + "1"
    return result

def modulo2div(divident, divisor):
    div = len(divisor)
    tmp = divident[0 : div]
    while div < len(divident):
        if tmp[0] == "1":
            tmp = xor(divisor, tmp) + divident[div]
        else:
            tmp = xor("0"*div, tmp) + divident[div]

        div +=1

    if tmp[0]=="1":
        tmp = xor(divisor, tmp)
    else:
        tmp = xor("0"*div, tmp)
    
    checksum = tmp
    return checksum
