import hmac, base64, struct, hashlib, time

def get_hotp_token(secret, intervals_no):
	key = base64.b16decode(secret, True)
	#decodificar la key
	msg = struct.pack(">Q", intervals_no)
	#conversiones entre valores de Python y estructuras C representadas
	h = hmac.new(key, msg, hashlib.sha1).digest()
	o = h[19] & 15
	#genera un hash usando ambos. El algoritmo hash es HMAC
	h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
	#unpacking
	return h

def get_totp_token(secret):
	#asegurarse de dar el mismo otp
	x = str(get_hotp_token(secret, intervals_no=int(time.time())//30))
	while len(x)!=6:
		x = str(x).zfill(6)
	return x
