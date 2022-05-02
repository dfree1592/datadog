import os
def my_function(s):
	s = s.upper()
	while True:
		if 'AWS' in s:
			s =s.replace('AWS', '')
		elif s == '':
			return -1
			break
		else:
			return s
			break
	return s

if __name__ == '__main__':
     fptr = open(os.environ['OUTPUT_PATH'], 'w')
     s = input('')
     result = my_function(s)
     fptr.write(str(result) + '\n')
     fptr.close()