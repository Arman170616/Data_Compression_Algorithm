input_str = 'AABABBBABAABABBBABBABB' 

keys_dict = {}

ind = 0
inc = 1
while True:
    if not (len(input_str) >= ind+inc):
        break
    sub_str = input_str[ind:ind + inc]
    #print(sub_str,ind,inc)
    if sub_str in keys_dict:
        inc += 1
    else:
        keys_dict[sub_str] = 0
        ind += inc
        inc = 1
        
a= list(keys_dict)
print(a)
