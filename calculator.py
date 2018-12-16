import sys

#shuchu shuihou gongzi
pay = 15000 #gongzi jine

tax_pay = pay*(1-0.165)-3500 #ying nashui e
tax = 0.00
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

print(pay-pay*0.165-tax)
