s = set()
for i in nums:

	if i in s: 
		return i
	s.add(i)