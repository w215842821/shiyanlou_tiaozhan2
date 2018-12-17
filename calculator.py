import sys

#shuchu shuihou gongzi
dict_data = {}
#ding'yi yi'ge han'shu jiang shu'ru d lie'biao zhuan'huang cheng zi'dian
def handle_data(arg):

   # dict_data = {}
   # for arg in sys.argv[1:]: 
    temp_list = arg.split(':')
    dict_data[temp_list[0]] = temp_list[1]  #xie'ru zi'dian
#jian'suan gong'zi shui'jin
def pay_last(pay):
    
    #print(pay)
    tax_pay = float(pay)*(1-0.165)-3500 #ying nashui e
    if tax_pay <= 0:
        tax = 0
    elif tax_pay<=1500:
        tax = tax_pay*0.03
    elif tax_pay<=4500:
        tax = tax_pay*0.1-105
    elif tax_pay<=9000:
        tax = tax_pay*0.2-555
    elif tax_pay<=35000:
        tax = tax_pay*0.25-1005
    elif tax_pay<=55000:
        tax = tax_pay*0.3-2755
    elif tax_pay<80000:
        tax = tax_pay*0.35-5505
    else:
        tax = tax_pay*0.45-13505
    return float(pay)*(1-0.165) -tax

for arg in sys.argv[1:]:
    handle_data(arg)
    
for key,value in dict_data.items():
    temp = pay_last(value)
    #print(pay)

    print("{}:{:.2f}".format(key,temp))
    
    #print("%d:%0.2f"%(k,l_pay))
    #print(k,l_pay)
