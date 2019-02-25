from roots import *
import hashlib
import sys
message = sys.argv[1]

# Your code to forge a signature goes here.
temp = 0x0001ff003031300d060960864801650304020105000420
temp <<= 201*8+32*8
temp += int(hashlib.sha256(message).hexdigest(), 16) << 201*8
pair = integer_nthroot(temp, 3)
forged_signature = pair[0]
if pair[1] == 0:
    forged_signature += 1

print integer_to_base64(forged_signature)
