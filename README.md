# ft_otp
**OTP**

### DEFINITION:

The ft_otp program allows you to introduce an hexadecimal key and generate a TOTP (Time-based One-Time Passwords) password every certain seconds. This works like a 2-Factor Authentication (2FA).

•With the -g option, the program must receive as an argument a hexadecimal key of at least 64 characters. The program safely stores this encrypted key in a file called ft_otp.key.

•With the -k option, the program decrypt the saved key and generates a new temporary password which is printed through the standard output.

### USAGE:

	$ ./ft_otp -g key.hex
	Key was successfully saved in ft_otp.key.
	$ ./ft_otp -k ft_otp.key
	836492
	$ sleep 60
	$ ./ft_otp -k ft_otp.key
	123518
	$ oathtool --totp $(cat key.hex)			<- With this command it is verified the authentication code is correct if the output is the same
	123518

### REQUIREMENTS:

Install a virtual environment like docker or venv. You can use next command with the path of your project to run docker.

	docker run -it -v /"PATH":/home debian

 Once you have your docker/venv running, you have to install the following programs to execute the ft_otp.

	apt -y update && apt -y upgrade && apt install python3 && apt install -y python3-pip && pip install pycryptodome && apt install -y oathtool

File "requirements.txt" contains modules to install. In this case we just need pycryptodome, but this option is useful when there are several modules.

	install -r requirements.txt
	
Since the program must be named ft_otp, we use the following command to rename the ft_otp.py program:
	
	make rename

