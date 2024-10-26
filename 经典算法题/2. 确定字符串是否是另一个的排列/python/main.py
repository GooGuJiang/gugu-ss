txt_1 = list(input())
txt_2 = list(input())

txt_1.sort()
txt_2.sort()

if txt_1 != txt_2:
  print("NO")
else:
  print("YES")