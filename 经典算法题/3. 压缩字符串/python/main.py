text = input()
text_set = set(text)
text = list(text)
output_text = ""
start_num = 0
list_num = 0
def find_diff(start_num: int,text_list: list) -> int:
    for i in range(start_num,len(text_list)):
        #print(text_list[start_num],text_list[i])
        if text_list[start_num] != text_list[i]:
            return i
    
    return len(text_list)

for i in range(len(text_set)):
    list_char = text[start_num] # 取出字符
    start_num = find_diff(start_num,text)
    char_count = start_num - list_num
    list_num = start_num
    output_text += f"{list_char}{char_count}"

if len(text)>len(output_text):
    print(output_text)
else:
    print("NO")
