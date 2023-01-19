# N = int(input())
# divisor = []

# for i in range(1, int((N/2)) + 1):
#   if N % i == 0:
#     divisor.append(i)
#     divisor.append(N/i)
#   else:
#     continue
  
# divisor = set(divisor)
# divisor = list(divisor)
# divisor.sort()
# print(divisor)

# def list_sum(x):
#   a = 0
#   for i in x:
#     a = a + i
#   return a

# list_sum([1, 2, 3, 4, 5])

# def dict_list_sum(dict_list):
#     age = 0
#     for dict in dict_list:
#         for a in dict.keys():
#             if a == 'age':
#                 age = dict[a] + age
              
#     return age

# print(dict_list_sum([{'name': 'kim', 'age': 12},
# {'name': 'lee', 'age': 4}]))

# def all_list_sum(li):
#     answer = 0
#     for i in li:
#         for j in range(len(i)):
#             answer = answer + i[j]
#     return answer
            
# print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))

# dict = {'A': 65, 'B' : 66, 'C' : 67, 'D' : 68, 'E' : 69, 'F' : 70, 'G': 71 , 'H': 72, 'I': 73 , 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
# print(type(dict))

dict = {'A': 65, 'B' : 66, 'C' : 67, 'D' : 68, 'E' : 69, 'F' : 70, 'G': 71 , 'H': 72, 'I': 73 , 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
print(type(dict))

# def get_secret_word(li):
#   answer = ""
#   for i in li:
#     for j in dict.values():
#       if i == j:
#         for key, value in dict.items():
#           if value == j:
#             answer += key
#           else:
#             continue
#       else:
#         continue

#   return(answer)         

# def get_secret_number(name):
#     answer = 0
#     for i in name:
#         for j in dict.keys():
#             if i == j:
#                 answer = answer + dict['j']
#             else:
#               continue
#     return answer

# def get_strong_word(a, b):
#     answer_1 = 0
#     answer_2 = 0
#     for i in a:
#         for j in dict.keys():
#             if i == j:
#                 answer_1 = answer_1 + dict['j']
#             else:
#                 continue
#     for i in b:
#         for j in dict.keys():
#             if i == j:
#                 answer_2 = answer_2 + dict['j']
#             else:
#                 continue
    
#     if answer_1 > answer_2:
#         print(a)
#     elif answer_1 < answer_2:
#         print(b)
#     else:
#         print(a, b)    
        
        
        
        
        
# def dict_list_sum(dict_list):
#     age = 0
#     for dict in dict_list:
#         for a in dict.keys():
#             if a == 'age':
#                 age = dict[a] + age