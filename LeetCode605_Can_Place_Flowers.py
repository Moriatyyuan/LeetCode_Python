class Solution:
	def canPlaceFlowers(self, flowerbed, n):
		"""
		:type flowerbed: List[int]
		:type n: int
		:rtype: bool
		"""
		count =1
		result = 0
		for i in range(len(flowerbed)):
			if flowerbed[i] == 0: # Counting the number of consecutive open spaces
				count = count + 1
			else:# Count the number of flowers that can be planted on this continuous open space
				result = result + (count-1)//2 
				count = 0
		if count !=0:
			result = result + count//2
		return result >= n