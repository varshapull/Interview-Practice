#Zigzag string conversion

def convert(s,numRows):
	length = len(s)
	if length == 1:
		return s

	zigzag_str = ''

	for i in range(0,numRows):
		column_flag = True

		j = i
		while True:
			if j > length -1:
				break
			zigzag_str = zigzag_str + s[j]

			if i == 0 or i == numRows -1:
				step = 2*numRows - 2

			elif column_flag:
				step = 2*numRows - 2 - 2*i 
				column_flag = False
			else:
				step = 2*i
				column_flag = True

			j = j + step

	return zigzag_str


print convert("PAYPALISHIRING",3)

