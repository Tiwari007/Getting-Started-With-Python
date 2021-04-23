# Write a Python script to merge two Python dictionaries



def dictionary_merge(dict1, dict2):
    return(dict2.update(dict1))
     

dict1 = {'Vivek': 22, 'bucky': 18}
dict2 = {'Alita': 26, 'kate': 19}
 
print(dictionary_merge(dict1, dict2))
print(dict2)




