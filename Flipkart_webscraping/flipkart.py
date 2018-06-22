#libraries to perform datascraping
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url='https://www.flipkart.com/search?q=iphone&marketplace=FLIPKART&otracker=start&as-show=on&as=off'   #getting the url of the web page
uClient=uReq(url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,'html.parser')                                                                #convert client data into a structured html parser
containers=page_soup.findAll("div",{"class":"_3O0U0u"})                                                #class common to the iphone products
print(len(containers))

#print(soup.prettify(containers[0]))
#container=containers[0];

'''
each_product=containers[22]

price=each_product.findAll("div",{"class":"_6BWGkk"})
#print(price[0].text)

product=each_product.findAll("div",{"class":"_3wU53n"})
#print(product[0].text)

ratings=each_product.findAll("div",{"class":"niH0FQ"})
#print(ratings[0].text)
'''

filename="iphone_products.csv"
f=open(filename,"w")

headers="produc_name,Pricing,Ratings"                                                               #headers in csv file
f.write(headers)
for i in range(0,len(containers)):
    each_product=containers[i]
    price=each_product.findAll("div",{"class":"_6BWGkk"})
    product=each_product.div.img["alt"]
    ratings=each_product.findAll("div",{"class":"niH0FQ"})

    #actual_price=(''.join((price[0].text).split(','))).split('E')                                  #to avoid EMI inclusion and other discount details seperated by ','
    trim_price=''.join((price[0].text).split(','))
    rm_rupee=trim_price.split("₹")
    add_rs_price="Rs."+rm_rupee[1]
    split_price=add_rs_price.split('E')
    actual_price=split_price[0]
    
    actual_rating=((ratings[0].text).split(" "))[0]
    

    #print(actual_price,product)
    print(product.replace(",","|")+","+actual_price+","+actual_rating+"\n")
    f.write(product.replace(",","|")+","+actual_price+","+actual_rating+"\n")                       #write into the csv file having '|' in place of ',' as it is considered
                                                                                                    #as new column
f.close()



