

"""
link: https://www.codewars.com/kata/5839c48f0cf94640a20001d3
name: Land perimeter
"""


def land_perimeter(arr):
	n = 0
	for i in arr:
		for k in i:
			if k == "X":
				n += 1
	return n




print(land_perimeter([
	"OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO",
	"OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))


"""
Test.describe("Basic tests")

Test.assert_equals(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]), "Total land perimeter: 60")
Test.assert_equals(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]), "Total land perimeter: 52")
Test.assert_equals(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]), "Total land perimeter: 40")
Test.assert_equals(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]), "Total land perimeter: 54")
Test.assert_equals(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]), "Total land perimeter: 40")

"""