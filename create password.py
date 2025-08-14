# این برنامه جهت ساختن پسوورد رندوم هستش
from random import choices
import string

symbols = "@#$%&*+-"
digits = "0123456789"
letters = string.ascii_letters

all_char = digits + letters + symbols

#آیتم های رمز رو باهم جمع کردم

while True: 

    menu = ("""
              1. Create password
              2. Exit
          """)
       
        # فقط نمایش گزینه ها
    print(menu)
    
    
    
      
    
          # اگه کاربر 2 رو انتخاب کنه ، برنامه بسته میشه.
    select_option = int(input("Select Option: "))
    if select_option == 2 :
        print("End.")
        break
        
            #انتخاب گزینه 1 و رفتن سیستم برای ساخت پسوورد.
            # برای دفعات خطا و شمارنده هم گذاشتم.
    elif select_option == 1:
        def create_password():
            count = 0
            
            
            
            while True:
                # کنترل با try , except
                try:
                    number = int(input("How many long! (5-30) :  "))
                    res = choices(all_char , k=number)
                    result = "".join(res)
                except ValueError:
                    print("Please enter numbers only!!!")
                    continue
                          # ارقام مجاز از 5 تا 30 و ساخت رمز کنارهم.
                
                
                
                    #وقتی عدد کمتر از 5  بیشتر از 30 بود ارور بده.
                if len(result) < 5 or len(result) > 30  :
                    print("The minimum password length should be 5 to 30 !!\n")
                    if len(result) < 5 :
                        print("⚠Password is weak!! Try again ↺ \n")
                    if len(result) > 30 :
                        print("⚠Max allowed length is 30 characters. Try again ↺ \n")
                    count += 1
                    continue
                
                
                
                    # این کد حداقل یک کاراکتر رو میخواد.
                if not any(i in symbols for i in result):
                    print("the system has chosen a password for you, but your password does not contain symbols.\n")
                    print("We will try again ↺ ")
                    count += 1
                    continue
                
                    # این کد حداقل یک عدد رو میخواد.
                if not any(i in digits for i in result):
                    print("the system has chosen a password for you, but your password does not contain numbers.\n")
                    print("We will try again ↺ ")
                    count += 1
                    continue
                
                
                
                    # این کد حداقل یک حروف کوچک و بزرگ رو میخواد.
                if  not any(i in letters for i in result):
                    print("the system has chosen a password for you, but your password does not contain letters.\n")
                    print("We will try again ↺ ")
                    count += 1
                    continue
                
                
                    # اگه همش درست بود، نتیجه رو میده.
                else:
                    print(f"Password length: {len(result)}\nYour password has been created: {result} ✔ \n")
                    print(f"Number of incorrect attempts: {count}")

                    break
                
    create_password()

            
        
