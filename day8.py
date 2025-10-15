#defining a function  
def get_pass(name,age):
 if age <=17:
   return f"{name},you are not allowed to go in!!"
 else:
  return f"{name},you are allowed to go in!!"

#generate the actual name and age
user_name = input()









def get_acces():
    name =input("Enter your name:")
    age  = int(input ("Enter yuor age: "))

    if age <=17:
       print(f"{name},You are not allowed to go in!!")
    else:
      print(f"{name},You are allowed to go in!!") 

      get_acces()  