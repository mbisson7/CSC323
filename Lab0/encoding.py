import binascii
import base64
import sys

# Converts an ASCII-encoded string to Hex-encoded string
def ascii_to_hex(ascii_string):
    return binascii.hexlify(ascii_string)

# Converts a Hex-encoded string to ASCII-encoded string
def hex_to_ascii(hex_string):
    return binascii.unhexlify(hex_string)

# Converts base64-encoded string to Hex-encoded string
def b64_to_hex(b64_string):
    return ascii_to_hex(base64.b64decode(b64_string))

# Converts Hex-encoded string to base64-encoded string
def hex_to_b64(hex_string):
    return base64.b64encode(hex_to_ascii(hex_string))

str1 = 'Hallelujah'
str2 = 'Crypto'

print ('String 1 length is: ' + str(len(str1)))
print ('String 2 length in bytes is: ' + str(sys.getsizeof(str1)))

print ('String 1 with ASCII encoding is: ' + str1)
print ('String 2 with ASCII encoding is: ' + str2)

str1_hex = ascii_to_hex(str1)
str2_hex = ascii_to_hex(str2)

print ('String 1 with ASCII->Hex encoding is: ' + str1_hex)
print ('String 2 with ASCII->Hex encoding is: ' + str2_hex)

print ('String 1 with Hex->ASCII encoding is: ' + hex_to_ascii(str1_hex))
print ('String 2 with Hex->ASCII encoding is: ' + hex_to_ascii(str2_hex))

str1_b64 = hex_to_b64(str1_hex)
str2_b64 = hex_to_b64(str2_hex)

print ('String 1 with Hex->b64 encoding is: ' + str1_b64)
print ('String 2 with Hex->b64 encoding is: ' + str2_b64)

print ('String 1 with b64->Hex encoding is: ' + b64_to_hex(str1_b64))
print ('String 2 with b64->Hex encoding is: ' + b64_to_hex(str2_b64))
