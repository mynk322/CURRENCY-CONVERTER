from tkinter import*
from tkinter.ttk import*
import requests
import time
import re
import smtplib
from string import ascii_uppercase
import pandas as pd
from bs4 import BeautifulSoup

#Function that converts some amount of a currency to another ( using live exchange rate )
def currency():
        
        root=Tk()
        root.title("Currency Converter")
        root.configure(background='moccasin')
        root.geometry("550x250")
        
        #Labels
        Label1=Label(root,text="WELCOME TO THE BEST CURRENCY CONVERTER!",font=("Times","16","bold italic"),foreground='darkred',background='moccasin')
        Label1.grid(row=1,columnspan=2,padx=5,pady=5)
        ans=Label(root,background='moccasin',font=("Comic Sans","14"),foreground='indigo')
        ans.grid(row=6,columnspan=2,padx=5,pady=5)
        From=Label(root,text="Convert from: ",background='moccasin',font=("Comic Sans","14"),foreground='indigo')
        From.grid(row=2,column=0, sticky = "E",padx=5,pady=5)
        To=Label(root,text="Convert to: ",background='moccasin',font=("Comic Sans","14"),foreground='indigo')
        To.grid(row=3,column=0, sticky = "E",padx=5,pady=5)
        Amt=Label(root,text="Enter the Amount: ",background='moccasin',font=("Comic Sans","14"),foreground='indigo')
        Amt.grid(row=4,column=0, sticky = "E",padx=5,pady=5)

        #declaring String type variables in root....to be used with combobox
        tkvar1=StringVar(root)
        tkvar2=StringVar(root)
        choices=['Argentine Peso','Australian Dollar','Bahraini Dinar','Botswana Pula',
         'Brazilian Real','British Pound','Bruneian Dollar','Bulgarian Lev','Canandian Dollar',
         'Chilean Peso','Chinese Yuan Renminbi','Colombian Peso','Croatian Kuna',
         'Czech Koruna','Danish Krone','Emirati Dirham','Euro','Hong Kong Dollar','Hungarian Forint',
         'Icelandic Krona','Indian Rupee','Indonesian Rupiah','Iranian Rial','Israeli Shekel',
         'Japanese Yen', 'Kazakhstani Tenge','South Korean Won','Kuwaiti Dinar','Libyan Dinar',
         'Malaysian Ringgit','Mauritian Rupee','Mexican Peso','Nepalese Rupee',
         'New Zealand Dollar','Norwegian Krone','Omani Rial','Pakistani Rupee',
         'Philippine Peso','Polish Zloty','Qatari Riyal','Romanian New Leu','Russian Ruble',
         'Saudi Arabian Riyal','Singapore Dollar', 'South African Rand','Sri Lankan Rupee',
         'Swedish Krona','Swiss Franc','Taiwan New Dollar','Thai Baht','Trinidadian Dollar',
         'Turkish Lira','US Dollar','Venezuelan Bolivar']
        tkvar1.set('SELECT')
        tkvar2.set('SELECT')
        
        #DropDown Menu
        ppm1=Combobox(root,textvariable=tkvar1,values=choices,state="readonly")
        ppm2=Combobox(root,textvariable=tkvar2,values=choices,state="readonly")
        ppm1.grid(row=2,column=1, sticky = "W",padx=5,pady=5)
        ppm2.grid(row=3,column=1, sticky = "W",padx=5,pady=5)
        
        #Function that webscrapes and calculates the required amount 
        def evaluate1(event=None):
                Curr1=tkvar1.get()
                Curr2=tkvar2.get()
                amt=entry.get()
                if(Curr1=='SELECT' or Curr2=='SELECT'):
                        ans.configure(text="Please Select a Currency",background='moccasin')
                else:
                        try:
                                amt = float (amt)
                                if Curr1==Curr2:
                                        CA=amt
                                else:
                                        data = requests.get('https://www.x-rates.com/table/?from=USD&amount=1')
                                        soup = BeautifulSoup(data.text,'html.parser')
                                        array = soup.find_all('td')
                                        n=len(array)
                                        if Curr1=="US Dollar":
                                                val1=1.0
                                        else:
                                                for i in range(0,n):
                                                        if array[i].string ==Curr1:
                                                                val1=array[i+2].string
        
                                        for i in range(0,n):
                                                if array[i].string==Curr2:
                                                        val2=array[i+1].string
        
                                        if Curr2=="US Dollar":
                                                val2=1.0
                
                                        val1=float(val1)
                                        val2=float(val2)
                                        CA=amt*val1*val2
                                ans.configure(text="Converted Amount: " + str("%.2f" % CA),background='moccasin')
                        except:
                              ans.configure(text="Please Enter Valid Amount",background='moccasin')  


        #Entry
        entry=Entry(root)
        entry.grid(row=4,column=1,sticky="W",padx=5,pady=5)
        entry.bind('<Return>',evaluate1)

        #Buttons
        B1=Button(root,text="Convert!",command=evaluate1)
        B1.grid(row=5,columnspan=2,padx=5,pady=5)
        B2=Button(root,text="Go to Stock Price Evaluator",command=stock)
        B2.grid(row=7,columnspan=2,padx=5,pady=5)

        #For Resizing the app window
        root.grid_rowconfigure(1,weight=1)
        root.grid_rowconfigure(2,weight=1)
        root.grid_columnconfigure(1,weight=1)
        root.grid_rowconfigure(3,weight=1)
        root.grid_columnconfigure(0,weight=1)
        root.grid_rowconfigure(4,weight=1)
        root.grid_rowconfigure(5,weight=1)
        root.grid_rowconfigure(6,weight=1)
        root.grid_rowconfigure(7,weight=1)
        root.mainloop()


#Function that shows the live price of any Indian Stock listed on NSE
def stock():
        
        root=Tk()
        root.title("Stock Price Evaluator")
        root.configure(background='moccasin')
        root.geometry("550x300")
        
        #Labels
        Label2=Label(root,text="STOCK PRICE EVALUATOR",font=("Times","16","bold italic"),foreground='darkred',background='moccasin')
        Label2.grid(row=1,columnspan=2,padx=5,pady=5)
        Label3=Label(root,text="Choose from over 1600 Indian Stocks!",font=("Times","16","bold italic"),foreground='darkred',background='moccasin')
        Label3.grid(row=2,columnspan=2,padx=5,pady=5)
        From=Label(root,text="Stock Name: ",background='moccasin',font=("Comic Sans","14"),foreground='indigo')
        From.grid(row=3,column=0, sticky = "E",padx=5,pady=5)
        ans=Label(root,background='moccasin',font=("Comic Sans","14"),foreground='indigo')
        ans.grid(row=6,columnspan=2,padx=5,pady=5)
        ans2=Label(root,background='moccasin',font=("Comic Sans","14"),foreground='indigo')
        ans2.grid(row=7,columnspan=2,padx=5,pady=5)
        ans3=Label(root,background='moccasin',font=("Comic Sans","14"),foreground='indigo')
        ans3.grid(row=8,columnspan=2,padx=5,pady=5)

        #Reading CSV file (using pandas) that contains list of 1612 Indian stocks listed in NSE 
        choice=pd.read_csv('LDE_EQUITIES_MORE_THAN_5_YEARS.csv',usecols=[0,2])
        choices=[]
        ch=[]
        symbols=[]
        for i in choice['Company']:
                if i=='kwality limited':
                        choices.append('Kwality Limited')
                        ch.append('Kwality Limited')
                elif i=='eClerx Services Limited':
                        choices.append('EClerx Services Limited')
                        ch.append('EClerx Services Limited')
                else:
                        choices.append(i)
                        ch.append(i)
        for i in choice['Symbol']:
                symbols.append(i)       
        n=len(choices)
        ch.sort()
        tkvar3=StringVar(root)
        tkvar3.set('SELECT')

        #Function to update the Combobox depending upon the user's input
        def get_values(event):
                x=tkvar3.get()
                x=x.upper()
                if (x=='SELECT' or x==''):
                        tkvar3.set('')
                        ppm1.config(values=ch)
                else:
                        new_choices=[]
                        for i in range(0,n):
                                if(re.search('^'+x,ch[i].upper())):
                                        new_choices.append(ch[i])
                        ppm1.config(values=new_choices)
                                
        
        #Function that webscrapes the price of the Stock selected
        def evaluate2():
                url='https://finance.yahoo.com/quote/'
                StockName=tkvar3.get()
                ticker=""
                for i in range(0,n):
                        if(StockName==choices[i]):
                                ticker=symbols[i]
                    
                data = requests.get(url+ticker+".NS?p=")
                soup = BeautifulSoup(data.text,'html.parser')
                price = soup.find_all('span',{'data-reactid':'21'})
                price[1]=price[1].string
                ans.configure(text='Live Price = ' + price[1])
                temp=time.asctime()
                temp1=temp[11:13]
                temp2=temp[14:16]
                temp1=int(temp1)
                temp2=int(temp2)
                if (temp1>15 or (temp2>=30 and temp1==15)) or (temp1<9 or (temp1==9 and temp2<15)):
                        ans2.configure(text='Market Closed' ,background='moccasin')


        #Function that emails the target user the live price of the selected stock
        def emailme():
                url='https://finance.yahoo.com/quote/'
                StockName=tkvar3.get()
                ticker=""
                for i in range(0,n):
                        if(StockName==choices[i]):
                                ticker=symbols[i]
                    
                data = requests.get(url+ticker+".NS?p=")
                soup = BeautifulSoup(data.text,'html.parser')
                price = soup.find_all('span',{'data-reactid':'21'})
                price[1]=price[1].string
                email_id=entry.get()
                match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_id)
                if(email_id==""):
                        ans3.configure(text="Please Enter a Valid Email Id")
                elif(match==None):
                        ans3.configure(text="Please Enter a Valid Email Id")
                else:
                        server=smtplib.SMTP('smtp.gmail.com',587)
                        server.starttls()
                        server.login("livestockandcurrency@gmail.com","mayank123")
                        msg="Hi! The Live Price of "+StockName+" is "+price[1]
                        server.sendmail("livestockandcurrency@gmail.com",email_id,msg)
                        server.quit()
                        ans3.configure(text="Email Sent!")
                

        #DropDown menu using Combobox
        ppm1=Combobox(root,textvariable=tkvar3,values=ch,state='normal')
        ppm1.grid(row=3,column=1, sticky = "W",padx=5,pady=5)
        ppm1.bind("<Button-1>",get_values)

        #Buttons
        B3=Button(root,text="Get Price!",command=evaluate2)
        B3.grid(row=4,columnspan=2,padx=5,pady=5)
        B4=Button(root,text="Email me the Price",command=emailme)
        B4.grid(row=5,column=0,padx=5,pady=5,sticky="E")

        #Entry
        entry=Entry(root)
        entry.grid(row=5,column=1,sticky="W",padx=5,pady=5)
        
        #For resizing the app window
        root.grid_rowconfigure(1,weight=1)
        root.grid_rowconfigure(2,weight=1)
        root.grid_columnconfigure(1,weight=1)
        root.grid_columnconfigure(0,weight=1)
        root.grid_rowconfigure(3,weight=1)
        root.grid_rowconfigure(4,weight=1)
        root.grid_rowconfigure(5,weight=1)
        root.grid_rowconfigure(6,weight=1)
        root.grid_rowconfigure(7,weight=1)
        root.grid_rowconfigure(8,weight=1)
        root.mainloop()

#Calling currency function
currency()

        
        
