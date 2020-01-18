

"""
link: https://www.codewars.com/kata/5839c48f0cf94640a20001d3
name: Land perimeter
"""
lst =[
	"OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO",
	"OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]


def walk_true(lst, item, n=0):
	i = item[0]
	k = item[1]

	try:
		if lst[i][k + 1] == 'X':
			n += 0
		else:
			n += 1
	except IndexError:
		n += 1

	try:
		if lst[i][k - 1] == 'X':
			n += 0
		else:
			n += 1
	except IndexError:
		n += 1

	try:
		if lst[i + 1][k] == 'X':
			n += 0
		else:
			n += 1
	except IndexError:
		n += 1

	try:
		if lst[i - 1][k] == 'X':
			n += 0
		else:
			n += 1
	except IndexError:
		n += 1

	return n


def select_x(lst):
	list_x = []
	for i in range(len(lst)):
		for k in range(len(lst[i])):
			if lst[i][k] == "X":
				list_x.append([i, k])
	return list_x


def land_perimeter(arr):
	l_per = 0
	lst = select_x(arr)
	for j in lst:

		l_per += walk_true(arr, j)
	return l_per




print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))




print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]), 60)
print(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]), 52)
print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]), 40)
print(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]), 54)
print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]), 40)



df = ["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]
for i in range(len(df)):
	print(end="\n")
	for k in range(len(df[i])):
		print(df[i][k], end=" ")