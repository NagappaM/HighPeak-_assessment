#READING INPUT:

input_file = open ("sample_input.txt","r")

#GETTING OUTPUT:

output_file = open("output.txt","w+")
goodies={}
output_list=[]

#GETTING INPUT DETAILS

for  f in input_file:
     index_toRead_price = f.index(":")
     print(f[index_toRead_price+1:].strip())
     print(f[:index_toRead_price])
     goodies[f[:index_toRead_price]] = f[index_toRead_price+1:].strip()
    #PRINTING THE GOODIES FROM THE INPUT
    
print(goodies)

#LISTING THE PRICES:

prices_only = list(goodies.values())
prices_only = [int (i) for i in prices_only]

#SORTING THE LIST:

prices_only.sort(reverse=True)
print(prices_only)

#TAKING VALUE OF INPUT:

no_of_employee = int(input("Enter number of employees: "))
length_consideration = (len(prices_only)-no_of_employee)
print(length_consideration)

#FINDING THE MINIMUM DIFFERENCES BETWEEN HIGHEST AND LOWEST:
for i in range(length_consideration):
    maxPrice = prices_only[i]
    minPrice = prices_only[no_of_employee+i]
    if i==0:
        difference = maxPrice - minPrice
        choosen_index = i
    elif (maxPrice - minPrice)<difference:
        difference = maxPrice - minPrice
        choosen_index = i
choosen_prices = prices_only[choosen_index:no_of_employee+choosen_index]

#DIFF B/W HIGH AND LOW PRICE:

difference = max(choosen_prices)- min (choosen_prices)
print("And the difference between the choosen goodie with highest price and the lowest price is", difference)

count = 0
for key,value in goodies.items():
    prices_only[count]
    print(value)
    if int(value)in choosen_prices and count<no_of_employee:
       strl = key+": "+value

       #PREPARING TO OUTPUT FILE
       output_list.append(strl)
       count+=1
       print(strl)

#GETTING OUTPUT FILE INFO:

output_file.write("The goodies selected for distribution are: ")

output_file.write("\n")
for i in output_list:
    output_file.write(i)
    output_file.write("\n")
output_file.write("And the difference between the choosen goodie with highest price and the lowest price is "+str(difference))

input_file.close()
output_file.close()
                      
                 
    
