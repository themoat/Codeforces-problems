#Pyaara sawaal ---->
t=int(input())
for i in range(0,t):
	n,k=list(map(int,input().split()))
	checker_odd = n-(k-1)
	checker_even = n-(2*(k-1))
	if checker_odd % 2 ==1 and checker_odd>0:
		print("YES")
		for i in range(1,k):
			print(1)
		print(checker_odd)

	elif checker_even % 2 == 0 and checker_even>0:
		print("YES")
		for i in range(1,k):
			print(2)
		print(checker_even)

	else:
		print("NO")





