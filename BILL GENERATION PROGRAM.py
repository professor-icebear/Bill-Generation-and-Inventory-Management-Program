import purchase
import csv
import read
import write

print('\n\n')
print('▄'*48)
print("█  WELCOME TO ELECTRONIC STORE SHOPPING OUTLET █")
print('▀'*48)
while True:
     print('\n\n')
     print('╔'+  86*('═')+ '╗')
     print('║ 1. PURCHASE ITEMS FROM THE STORE                                                     ║')
     print('║ 2. VIEW PREVIOUSLY GENERATED BILLS                                                   ║')
     print('║ 3. DELETE PREVIOUSLY GENERATED BILLS AND CORRESPONDING CUSTOMER RECORD FROM DATABASE ║')
     print('║ 4. CUSTOMER DETAILS DATABASE                                                         ║')
     print('║ 5. DISPLAY INDIVIDUAL CUSTOMER RECORDS                                               ║')
     print('║ 6. UPDATE CUSTOMER DETAILS IN THE DATABASE AND THE BILL                              ║')
     print('║ 7. EXIT                                                                              ║')
     print('╚'+  86*('═')+ '╝')
     print('\n\n')
     n=int(input('''ENTER THE SERIAL NUMBER CORRESPONDING TO YOUR DESIRED ACTION FROM THE ABOVE MENU -------> '''))
     print('\n\n')
     if n==1:
          again = "Y"
          buy = read.read_file()
          buy_act= purchase.purchase(buy)
          write.over_write(buy, buy_act)
          print("\nThank you for shopping from our store!!")
          print("Please check your invoice for your shopping details, \nWhich we have created in .txt file format.")
          print('\n\n')         
     if n==2:
          billView=input('ENTER THE INVOICE NUMBER OF THE BILL TO BE ACCESSED ------> ') + '.txt'
          fo=open(billView,'r')
          print(fo.read())
          print('\n\n')
          fo.close()
     if n==3:
          billDelete=input('ENTER THE INVOICE NUMBER OF THE BILL TO BE DELETED ------> ')
          fo=open(billDelete+ '.txt','r+')
          fo.truncate(0)
          
          undeletd=[]
          regenBill=open('customer details.csv','r',newline='')
          actBill=csv.reader(regenBill, delimiter=',')
          for rec in actBill:
                if rec[0]!=str(billDelete):
                     undeletd.append(rec)
          regenBill.close()
          custDetail=open('customer details.csv','w',newline='')
          newDetail=csv.writer(custDetail)
          newDetail.writerows(undeletd)
          print('RECORD AND BILL IS SUCCESSFULLY DELETED')
          print('\n\n')
          custDetail.close()

     if n>=7 or n<1:
          term=('PROGRAM HAS BEEN SUCCESSFULLY TERMINATED. THANK YOU FOR USING OUR SOFTWARE')
          print(term)
          print('**************************************************************************')
          break
        
     if n==4:
          custDatabase=open('customer details.csv','r',newline='')
          a=csv.reader(custDatabase, delimiter=',')
          print('═'*148)
          print('▐   CUSTOMER NUMBER   ▐','   CUSTOMER NAME   ▐','   CUSTOMER PHONE NUMBER   ▐','   CUSTOMER LOCATION   ▐','   TOTAL AMOUNT PAID   ▐','   METHOD OF PAYMENT   ▐')
          print('═'*148)
          for rec in a:
                print('▐        ',rec[0],'        ▐','     ',rec[1],(' ')*(11-(len(rec[1]))),'▐','        ',rec[2],(' ')*(16-(len(rec[2]))),'▐','       ',rec[3],(' ')*(13-(len(rec[3]))),'▐','     ',rec[4],(' ')*(15-(len(rec[4]))),'▐','        ',rec[5],'         ▐')
          print('═'*148)
          print('\n\n')
          custDatabase.close()
     if n==5:
          custRecord=open('customer details.csv','r',newline='')
          actCustRecord=csv.reader(custRecord, delimiter=',')
          next(actCustRecord)
          rcn=int(input('ENTER THE CUSTOMER NUMBER: '))
          print()
          for rec in actCustRecord:
               if rec[0]==str(rcn):
                    print('CUSTOMER NAME: ',rec[1])
                    print('CUSTOMER PHONE NUMBER: ',rec[2])
                    print('CUSTOMER LOCATION: ',rec[3])
                    print('TOTAL AMOUNT PAID: ',rec[4])
                    print('METHOD OF PAYMENT: ',rec[5])
                    print()
                    xy=input('WOULD YOU LIKE TO VIEW THE BILL TOO? ')
                    sos=xy.upper()
                    if sos=='YES' or sos=='Y':
                            Nbill=str(rcn)+'.txt' 
                            fo=open(Nbill,'r')
                            print(fo.read())
                            print('\n\n')
                            fo.close()
                    else:
                         print()
     
     if n==6:
          st=input('ENTER THE INVOICE NUMBER OF THE BILL TO BE UPATED: ')
          updateBill=open(st+'.txt','r')
          t=open('customer details.csv', 'r', newline='')
          l=[]
          c=csv.reader(t)
          for rec in c:
               l.append(rec)
          t.close()
          print('\n')
          print('1. CUSTOMER NAME')
          print('2. CUSTOMER PHONE NUMBER')
          print('3. CUSTOMER LOCATION')
          st2=int(input('WHICH OF THE FOLLOWING IS TO BE UPDATED (SERIAL NUMBER): '))
          if st2==1:
               for p in l:
                    if p[0]==st:
                         before=str(p[1])
               name=input('ENTER THE NEW NAME TO BE UPDATED: ')

               with open(st+'.txt','r') as file:
                    maus=file.read()
                    maus=maus.replace(before,name)
               with open(st+'.txt','w') as file:
                    file.write(maus)
                    print("NAME HAS BEEN REPLACED")
                    print('\n\n')

               for lst in l:
                    if lst[0]==st:
                         lst[1]=name
               
               updateBill.close()
               
          if st2==2:
               for p in l:
                    if p[0]==st:
                         bfrnum=(p[2])
               number=input('ENTER THE NEW NUMBER TO BE UPDATED: ')

               with open(st+'.txt','r') as file:
                    maus=file.read()
                    maus=maus.replace(bfrnum,number)
               with open(st+'.txt','w') as file:
                    file.write(maus)
                    print("PHONE NUMBER HAS BEEN REPLACED")
                    print('\n\n')

               for lst in l:
                    if lst[0]==st:
                         lst[2]=number
               updateBill.close()

          if st2==3:
               for p in l:
                    if p[0]==st:
                         bfrlocation=str(p[4])
               location=input('ENTER THE NEW LOCATION TO BE UPDATED: ')

               with open(st+'.txt','r') as file:
                    maus=file.read()
                    maus=maus.replace(bfrlocation,location)
               with open(st+'.txt','w') as file:
                    file.write(maus)
                    print("LOCATION HAS BEEN REPLACED")
                    print('\n\n')

               for lst in l:
                    if lst[0]==st:
                         lst[3]=location
               updateBill.close()
          wr=open('customer details.csv','w',newline='')
          u=csv.writer(wr)
          u.writerows(l)
          wr.close()

          
          
               
               

     
          
           
           
           
          
          
 
