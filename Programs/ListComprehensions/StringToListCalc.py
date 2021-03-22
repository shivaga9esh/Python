#Requirement:
#
# [100,200,300,400,500,600] - calculate percent increment by 10 %
# output: [110,220,335,444,555,687]

# '100,200,300,400,500,600'
# output: [110,220,335,444,555,687]

def cost_increment(cost_input):
    if(type(cost_input) == str):  # decide the final result

        # Option 1
        # split_result_list = cost_input.split(",") #here we get list of strings but not list of integers -- List 1
        # split_result_list_converted = []  # create empty new list  -- List 2
        # for i in split_result_list:
        #     i = int(i) # converted string to integer
        #     result = i + (i * 10 / 100)  # 10% of cost_input - business logic: calculate percent increment by 10 %
        #     split_result_list_converted.append(result)
        # final_result = split_result_list_converted ####print(split_result_list) # write your code to case str to list

        #Option 2 : Benefits: no need to write for loop and append functions, business logic isolation
        split_result_list_converted = [int(x) for x in cost_input.split(",")] # here we get list of strings but not list of integers -- List 1
        business_logic = map(lambda mycost: mycost + (mycost * 10 / 100), split_result_list_converted) # here we get list of strings in terms of object
        final_result_list = list(business_logic)  # here we get list of strings but not list of integers -- List 2 - update
    else:
        final_result_list = []  # create empty new list - List 1
        for i in cost_input:
             result = i + (i * 10 / 100)  # 10% of cost_input
             final_result_list.append(result)

    return final_result_list

#print(cost_increment((110,220,335,444,555,687)))
#print(cost_increment([110,220,335,444,555,687]))
print(cost_increment('110,220,335,444,555,687'))





