import sys

ex_str = "Hi I'm Bumsu, I'm forntend developer"

#find, index
find_idx = ex_str.find("Bumsu")
find_idx = ex_str.find("Bumsu")
print(find_idx)

try:
    index_result = ex_str.index("piro")
    print(index_result)
except Exception as e:
    index_result = -1
    print(e)

#split
splitted_list = ex_str.split(" ")
print(splitted_list)


#join
joined_str = "-".join(splitted_list)
print(joined_str)

#replace
replaced_str = ex_str.replace("Bumsu", "piro")
print(replaced_str)


#strip
text = "         data data        "
print(text.strip())
print(text.replace(" ",""))

#dic
ex_dic = {
    "name" : "bumsu",
    "age":25,
    "job":"developer",
}

ex_keys = list(ex_dic.keys())
print(ex_keys)

ex_value = list(ex_dic.values())
print(ex_value)

ex_items = list(ex_dic.items())
print(ex_items)

#lambda
print((lambda x, y : x+y)(1,2))

#해석
def sum(x, y):
    return x+y

numbers = [1,2,3,4,5]
ex_map_2 = list(map(lambda number: number+10, numbers))
print("map2", ex_map_2)

ex_map_3 = []


