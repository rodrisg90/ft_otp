PYTHON=python3
NAME=ft_otp
FILENAME=ft_otp.py

rename: 
	chmod u+x ${FILENAME}
	ln -s ${FILENAME} ${NAME}
	@echo :page_facing_up: "\033[92;3;4mft_otp created\033[0m"

g:
	${PYTHON} ${NAME} -g key.hex

k:
	${PYTHON} ${NAME} -k ft_otp.key

.PHONY: rename g k