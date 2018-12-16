import sys

#shuchu shuihou gongzi
dict_data = {}
#ding'yi yi'ge han'shu jiang shu'ru d lie'biao zhuan'huang cheng zi'dian
def handle_data(arg):

   # dict_data = {}
   # for arg in sys.argv[1:]: 
    temp_list = arg.split(':')
    dict_data[temp_list[0]] = temp_list[1]  #xie'ru zi'dian

for arg in sys.argv[1:]:
    handle_data(arg)
#print(dict_data)

    
for k in dict_data:
    pay =float( dict_data[k]) #gong'zi jin'e
    #print(pay)
    tax_pay = float(pay*(1-0.165)-3500) #ying nashui e
    tax = 0.00
    l_pay = 0.00
    if 0<tax_pay<=1500:
        tax = tax_pay*0.03
    elif 1500<tax_pay<=4500:
        tax = tax_pay*0.1-105
    elif 4500<tax_pay<=9000:
        tax = tax_pay*0.2-555
    elif 9000<tax_pay<=35000:
        tax = tax_pay*0.25-1005
    elif 35000<tax_pay<=55000:
        tax = tax_pay*0.3-2755
    elif 55000<tax_pay<80000:
        tax = tax_pay*0.35-5505
    else:
        tax = tax_pay*0.45-13505
    
    l_pay = pay*(1-0.165) -tax
    print("{}:{}".format(k,l_pay))
    #print("%d:%0.2f"%(k,l_pay))
    #print(k,l_pay)
