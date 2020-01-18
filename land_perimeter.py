

"""
link: https://www.codewars.com/kata/5839c48f0cf94640a20001d3
name: Land perimeter
"""
lst = [[1, 2], [3, 4], [4, 5], [6, 7]]

def walk_true(lst, ind_i, ind_k):
	try:
		lst[ind_i][ind_k]
	except IndexError:
		return False
	return True

print(walk_true(lst, 2, 5))


def land_perimeter(arr):



	def deep_search(lst, ind_i, ind_k):
		if walk_true(lst, ind_i, ind_k):
			pass



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