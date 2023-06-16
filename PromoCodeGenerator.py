# make lists
list1 = ["DEAL","HOLIDAY","NEWCUST",]
list2 = ["5","10","15","20","21","22","23","24","25","30","33","35",
        "40","50","60","70","75","100"]

combinations = []
for base_item in list1:
    for str_num in list2:
        combinations.append(f'{base_item}{str_num}')

promo_code_count = len(combinations)

# open the text file for writing
f = open("promocodes.txt", "a")

# Write the pomocodes to a text file
for promo_code in combinations:
    f.write(promo_code + "\n")

print(str(promo_code_count) + " promo codes written to file.")

# close the file
f.close()

# *(Feel free to add more buzzwords to list1 in the code. 
# Companies like to use local organizations, partners, businesses, 
# universities, etc as promocodes, so try any number of those.
