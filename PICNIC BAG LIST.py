from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

label_list = Label(root)
label_item = Label(root)

list_items = ["Sandwiches", "Fruit", "Chips", "Drinks", "Blanket", "Sunscreen", "Sunglasses"]
label_list["text"] = "Listed Items : " + str(list_items)


def bag_items():
    random_item = random.sample(range(1,7),1)
    label_item["text"] = "Put Item No. " + str(random_item) + " In Bag"
     

btn=Button(root,text="Which items to put in bag?",command = bag_items, bg="lightblue")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label_list.place(relx=0.5,rely=0.4,anchor=CENTER) 
label_item.place(relx=0.5,rely=0.6,anchor=CENTER) 
 

    
root.mainloop()