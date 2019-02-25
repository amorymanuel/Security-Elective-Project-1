import httplib, urlparse, urllib, sys
import base64, copy

def valid_padding(sender, recipient, query):
    url = "https://eecs388.org/paddingoracle/verify?message=" + query + "&from=" + sender + "&to=" + recipient
    #url = "http://141.212.115.128/paddingoracle/verify?message=" + query + "&from=" + sender + "&to=" + recipient
    parsedUrl = urlparse.urlparse(url)

    try:
        conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
        #conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
        conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
        message = conn.getresponse().read()
    except KeyboardInterrupt:
        raise
    except:
        print "error"

    if message == "Error 400: Invalid Padding":
        # This is a padding error
        return False
    elif message == "Invalid Validation" or message == "Valid Validation":
        # Correct padding!
        return True
    else:
        print "Bad response:\n" + message
        exit()

def int_to_hex(n):
    hexstr = hex(n).split('0x')[1].upper()
    if len(hexstr) == 1:
        hexstr = '0' + hexstr
    return hexstr

def main():
    if len(sys.argv) != 4:
        print("Usage: python padding_oracle.py \"from\" \"to\" \"base16_ciphertext\"")
        exit()

    # Add code here
    blocksize = 16
    send = sys.argv[1]
    receive = sys.argv[2]
    cipherb16 = sys.argv[3]

    numblock = len(cipherb16)/(blocksize*2)

    plaintext = ""

    for i in range(numblock-1, 0, -1):
        dec = []
        padding = 0
        cipherlist = ['0' for j in range(2*blocksize)]
        for j in range((blocksize-1)*2, -2, -2):
            padding += 1
            for k in range(len(dec)):
                hexc = int_to_hex(dec[k]^padding)
                cipherlist[2*blocksize - 2*k - 2] = hexc[0]
                cipherlist[2*blocksize - 2*k - 1] = hexc[1]
            cipherbyte = int(cipherb16[(i-1)*2*blocksize+j : (i-1)*2*blocksize+j+2], 16)
            for k in range(0, 256):
                hexc = int_to_hex(k)
                cipherlist[j] = hexc[0]
                cipherlist[j + 1] = hexc[1]
                newcipher = ''.join(cipherlist)+cipherb16[i*2*blocksize : (i+1)*2*blocksize]
                if valid_padding(send, receive, newcipher):
                    dec.append(padding^k)
                    plainchar = int_to_hex(dec[len(dec)-1]^cipherbyte)
                    plaintext = plainchar + plaintext
                    break
    print plaintext

if __name__ == "__main__":
    main()
