#!/usr/bin/python3

# ------------------------------ MODULOS -----------------------------------

import argparse
import sys
import ft_totp
import base64
import ft_crypt

# ----------------------------- CONFIGURACION --------------------------------

def is_hex(key_hex):
	"""Function to verify if string is hex of 64 characters"""
	if len(key_hex) >= 64:
		try:
			int(key_hex, 16)
		except ValueError:
			return False
		return True
	else:
		return False

def save_encrypted_key(key_hex):
	with open(".key", "rb") as key_file:
		key = key_file.read().decode(encoding = 'utf-8')
	with open("./ft_otp.key", "wb") as file:
		file.write(ft_crypt.encrypt(key_hex, key))
		print("Key was successfully saved in ft_otp.key")

def verify_otp(otp_key):
	with open(".key", "rb") as key_file:
		key = key_file.read().decode(encoding = 'utf-8')
	with open(otp_key, "rb") as file_otp:
		otp_key = file_otp.read()
	otp_key = ft_crypt.decrypt(otp_key, key)
	num_otp_key = len(otp_key) - 1
	otp_key = otp_key[2:num_otp_key]
	with open("key1.hex", "wb") as file:
		file.write(otp_key)
		print("Key was successfully saved in key1.hex")

def args_conf():
	parser = argparse.ArgumentParser(
		description = 'Time One-Time Password implementation.'
	)
	# Save ciphered ft_otp.key
	parser.add_argument('-g', '--new-key', help = 'Save hexadecimal key in ft_otp.key', default = None)
	# Generate new key
	parser.add_argument('-k', '--key-gen', help = 'Generate new totp autentication code', default = None)

	arguments = parser.parse_args()
	return arguments

"""Este programa recibe una clave hexadecimal de al menos 64 caracteres como argumento, 
guarda esa clave cifrada en un archivo ft_otp.key y genera una contraseña temporal"""

# -------------------------------- EJECUCION ----------------------------------

def main():
	args = args_conf()
	if args.new_key:
		try:
			with open(sys.argv[2], "rb") as file:
				key_hex = file.read()
		except:
			print("There is an error with the " + key_file + " file")
		if is_hex(key_hex) is False:
			print("Error, you must set an hexadecimal password of 64 characters or more")
		else: 
			key_hex = str(key_hex)
			save_encrypted_key(key_hex)
	elif args.key_gen:
		try:
			otp_key = sys.argv[2]
			verify_otp(otp_key)
		except:
			print("There is an error with the encrypted key")
		with open("key1.hex", "rb") as file:
			otp_key = file.read()
		totp = ft_totp.get_totp_token(otp_key)
		print(totp)
	else:
		print ("Please indicate what action you want when executing the program. Consult the help (-h or --help) if you want to know what options there are.")
 
if __name__ == "__main__":
   main()
