import encoding
def string_xor(string, key):
    # Repeat key if it is shorter, loop is avoided if key >= str
    newKey = key
    loop = 0
    count = 0
    print ('newKey is: ' + newKey)
    print ('newKey len is: ' + str(len(newKey)))
    while(len(newKey) < len(string)):
        loop = loop + 1
        print('Loop is : ' + str(loop))    
        newKey = newKey + key
        print ('newKey is: ' + newKey)
        print ('newKey len is: ' + str(len(newKey)))

    #zipped = zip(string, newKey)
    #print(zipped)
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(string,newKey))
    #l = [ord(a) ^ ord(b) for a,b in zip(string, key)]
    #print(l)    
#    while(count < len(string)):
#return bytes(x ^ y for x, y in zip(string, key))    
str1 = 'abc123'
str2 = 'go@!'
res = string_xor(str1, str2)
print("Result is: " + str(res))
hex = encoding.ascii_to_hex(res)
print(hex)
