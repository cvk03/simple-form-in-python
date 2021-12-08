# -*- coding: utf-8 -*-
import tkinter
import pickle
 

#wb = open('C:\\Users\\ADMIN\\Desktop\\python.txt')


class stu:
    #import tkinter
    def __init__(self):
    
        self.name2= name1.get()
        self.mis2= mis1.get()
        self.branch2 = branch1.get()
        self.email2 = email1.get()
        self.sem2 = sem1.get()
        self.result2 = result1.get()
        
        
  
def save():
    
    st=stu()
    wb = open('C:\\Users\\ADMIN\\Desktop\\python.txt','ab+')
    pickle.dump([st.name2,st.mis2,st.branch2,st.email2,st.sem2,st.result2],wb)
    wb.close()
    tkinter.messagebox.showinfo("info","saved")
def search():
    st=stu()
    tuple=[l_name,l_mis]
    wb = open('C:\\Users\\ADMIN\\Desktop\\python.txt','rb+')
    p=0
    while wb !=EOFError:
         info=pickle.load(wb)
         print(info[0],info[1])
         if(name1.get()==info[0]):
             print("got it!!",info[0])
             mis1.insert(0,info[1])
             branch1.insert(0,info[2])
             email1.insert(0,info[3])
             sem1.insert(0,info[4])
             result1.insert(0,info[5])
             print("done!!!")
             tkinter.messagebox.showinfo("info","search completed!!")
             
    wb.close()
    
def clear():
    st=stu()
    tuple=[l_name,l_mis]
    name1.delete(0,"end")
    mis1.delete(0,"end")
    branch1.delete(0,"end")
    sem1.delete(0,"end")
    result1.delete(0,"end")
    tkinter.messagebox.showinfo("info","cleared!!")
    
# Driver code

window = tkinter.Tk()
window.title("form")
window.geometry('500x500')
#window.configure(background = "grey");

name=tkinter.Label(window ,text="name").grid(row=0,column=0)
mis=tkinter.Label(window ,text="mis").grid(row=1,column=0)
branch=tkinter.Label(window ,text="branch").grid(row=2,column=0)
email=tkinter.Label(window ,text="email_id").grid(row=3,column=0)
sem=tkinter.Label(window ,text="sem").grid(row=4,column=0)
result=tkinter.Label(window ,text="result").grid(row=5,column=0)


name1= tkinter.Entry(window,width=20)
name1.place(x=50,y=5)
mis1 = tkinter.Entry(window)
mis1.place(x=50,y=25)
branch1 = tkinter.Entry(window)
branch1.place(x=50,y=45)
email1 = tkinter.Entry(window)
email1.place(x=50,y=65)
sem1 = tkinter.Entry(window)
sem1.place(x=50,y=85)
result1 = tkinter.Entry(window)
result1.place(x=50,y=105)

l_name=list(name1.get())
l_mis=list(mis1.get())

savebtn=tkinter.Button(window,text="save",command=save)
savebtn.place(x=50,y=150)
searchbtn=tkinter.Button(window,text="search",command=search)
searchbtn.place(x=100,y=150)
clearbtn=tkinter.Button(window,text="clear",command=clear)
clearbtn.place(x=150,y=150)


#st=stu(
window.mainloop()



     
        
        

    



        