#10.7
# def is_anagram(word1,word2):
# 	t=list(word1)
# 	s=list(word2)
# 	t.sort()
# 	s.sort()
# 	if t==s:
# 		return True
# 	else:
# 		return False
	


# print is_anagram("abcd","dcba")

#10.13
fin=open('words.txt')
t=[]
newlist=[]
for line in fin:
	word=line.strip()
	t.append(word)
for i in t:
	len(i)
	t.remove(i)
	for j in t:
		if len(j)==len(i):
			for char in i:
				for char1 in j:
					newword=char+char1
			print newlist.append(newword)
        





	
