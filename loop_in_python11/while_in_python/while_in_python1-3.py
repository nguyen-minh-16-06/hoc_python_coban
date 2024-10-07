# Vòng lặp while-else và cách hoạt động:
k = 0 
while k < 3:
	print('value of k is', k)
	k += 1
	if k == 1:
		break
else:
	print('k is not less than 3 anymore')
# Trường hợp đặc biệt:

# Khi ta sài câu lệnh break trong while thì else sẽ không được thực hiện.
