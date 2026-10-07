s1 = {2,3,5}
s2 = {'b','c','a'}
s3 = list(zip(s1,s2))
print(s3, "\n")

list1 = [100,200,300,400]
list2 = [300,600,900,1200]
for x,y in zip(list1, list2[::-1]):
    print(x,y)

stocks = ['reliance', 'marketing', 'tcs']
prices = [ 12909, 45000, 34589]
new_dict= {stocks:prices for stocks,prices in zip(stocks,prices)}
print(new_dict)
