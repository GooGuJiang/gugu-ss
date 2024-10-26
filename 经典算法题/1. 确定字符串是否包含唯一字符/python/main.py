def is_cf(text: str) -> bool:
  text = text.lower()
  char_list = set()
  for char in text:
    if char in char_list:
      print("NO")
      return False
    char_list.add(char)
  
  print("YES")
  return True


is_cf(input())


# 简短写法
s = input().lower()
print('YES' if len(set(s))==len(s) else 'NO')