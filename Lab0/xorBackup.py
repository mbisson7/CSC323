import encoding
def string_xor(string, key):
    # Repeat key if it is shorter, loop is avoided if key >= str
    newKey = key
    while(len(newKey) < len(string)):
        newKey = newKey + key
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(string,newKey))

def msg_decrypt(hex_string):
    val = 0
    for val in range(256):
        res = string_xor(encoding.hex_to_ascii(hex_string), chr(val))
        print res
        # figure out frequency of characters        

def freq_analysis(line):
    line = line.replace(" ", "")
    letter_freq = {}
    for c in line:
        if c not in letter_freq
            letter_freq[c] = 1
        else
            letter_freq[c] = letter_freq[c] + 1;
    return

# Test xor function
str1 = 'abc123'
str2 = 'go@!'
res = string_xor(str1, str2)

#print ("Ascii result is: " + str(res))
#hex = encoding.ascii_to_hex(res)
#print("Hex result is: " + str(hex))

f = open("Lab0.TaskII.B.txt")
for line in f.readlines():
    #print line[:-1]
    msg_decrypt(line[:-1])
    print '\n\n\n\n'
#msg_decrypt(readfile)
