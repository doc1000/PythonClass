
my_str = input("List numbers separated by commas (ie '1,2,3,4'): ")
#my_list = [int(x) for x in list(my_str) if x != ',' and x !=' ']
#my_str = my_str.replace(' ','')  #get the white out
#my_list = my_str.split(",")    #cheap and easy way to split by comma
#my_list = list(my_str)
#my_list = [int(x) for x in list(my_str) if x != ',' and x !=' '] #splits by comma and stops whitespace but odesn't take multi-digit
my_list = [int(x) for x in my_str.split(",")]
print(tuple(zip(my_list[::2],my_list[1::2])))

#my_t = tuple()
#[my_t for i,j in zip(my_list[::2],my_list[1::2])]
