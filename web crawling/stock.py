import re
import urllib.request
url = "https://finance.google.com/finance?q="
stock = input("Enter name of the stock:")
url = url + stock
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m = re.search('<meta itemprop="price"',data1)
start = m.start()
end = m.end() + 50
newString = data1[start:end]
m = re.search('content="',newString)
start = m.end()
newString2 = newString[start:]
m = re.search("/",newString2)
end = m.end()-3
price = newString2[0:end]
print("The Latest Price of the " + stock + " is : " + price)

