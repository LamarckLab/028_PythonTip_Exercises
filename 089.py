def remove_keys(dict_input, key_list):
    # 此处编写代码 
    target_dict = {}
    for element in dict_input:
        if element not in key_list:
            target_dict[element] = dict_input[element]
    return target_dict
# 获取输入 
user_dict = eval(input())
user_key_list = input().split()

# 调用函数 
print(remove_keys(user_dict, user_key_list))