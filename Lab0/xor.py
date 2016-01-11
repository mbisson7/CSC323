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
        #print res
        if ioc(res) == 0.7674065588930:
            print res
            print ioc(res)  
            return 1
        # figure out frequency of characters        
    return 0

def freq_analysis(line):
    line = line.replace(" ", "")
    letter_freq = {}
    for c in line:
        if c not in letter_freq:
            letter_freq[c] = 1
        else:
            letter_freq[c] = letter_freq[c] + 1;
    return letter_freq

def occurrence_sum(dict):
    sum = 0
    for key in dict:
        sum = sum + (dict[key] * (dict[key] - 1))
    return sum

# Index of Coincidence
def ioc(line):
    string = line.replace(" ", "")
    numer =  occurrence_sum(freq_analysis(line))
    denom = 0.0667 * len(string) * (len(string) - 1)
    return numer / denom

#print ioc("Out on bail, fresh out of jail, California dreaming Soon as I step on the scene, I'm hearing ladies screaming")

f = open("Lab0.TaskII.B.txt")
for line in f.readlines():
    ret = msg_decrypt(line[:-1])
    if ret == 1:
        break
    #print '\n\n\n\n'
#msg_decrypt(readfile)

