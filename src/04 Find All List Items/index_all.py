def index_all(mylist, char):
   index_list=[]
   for index, value in enumerate(mylist):
       if value ==char:
           index_list.append([index])
       elif isinstance(mylist[index],list):
           for i in index_all(mylist[index],char):
               index_list.append([index]+i)
   return index_list


# commands used in solution video for reference
if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]
