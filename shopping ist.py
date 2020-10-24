
shopping_list=[]

print("welcome to our store")
print("what shuold we pick ip at the store?")
# bring the number if items in the list
def help_me():
    print("enter DONE to stop adding items")
    print("enter show to see the items present")
    print("enter help to see the instructions")

def show_list():
      for x,item in enumerate(shopping_list,start=1):
          print(x,item)


    
        

    
while(True):
 new_item =input("enter the intem u want:")
 if(new_item=="DONE"):
     end=input("are sure to quit:")
     if (end=="no"):
         continue
     else:
         print("thank you for shopping with us")
         break
 
  
 if(new_item=="help_me"):
     help_me()
     continue

 
    
 if(new_item=="show"):
     print("your shopping list has")
     show_list()
     continue


 shopping_list.append(new_item)

print("your shopping bag has:")
show_list()


  



