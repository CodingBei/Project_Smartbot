from tkinter import*
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import pyaudio

class Login:

    def __init__(self,root):
        pass
        self.root=root
        self.root.title("Smartbot")
        self.root.geometry("1920x1080")
        self.root.resizable(True,True)

        #=====BG Image======
        self.bg=PhotoImage(file="C:\\Users\Lakshya Narula\\Desktop\\Deliverables_Clevered\\Background for program(deliverables)\\loginbackground.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #====Login Frame====
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=520,y=240,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=140,y=30)
        desc=Label(Frame_login,text="Login Area for personal Chatbot",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=110,y=100)
        
        lbl_user=Label(Frame_login,text="Username",font=("Algerian",20,"bold"),fg="black",bg="white").place(x=30,y=137)
        
        self.txt_user=Entry(Frame_login,font=("times new roman",15),fg="black",bg="lightgray")
        self.txt_user.place(x=200,y=140,width=250,height=35)

        lbl_user=Label(Frame_login,text="Password",font=("Algerian",20,"bold"),fg="black",bg="white").place(x=30,y=200)
        
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),fg="black",bg="lightgray")
        self.txt_pass.place(x=200,y=200,width=250,height=35)
        self.txt_pass.config(show="*")


        Login_btn=Button(self.root,command=self.login_function,text="Login",font=("times new roman",30,"bold"),fg="white",bg="#d25d17").place(x=696,y=520)


    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_user.get()!="Lakshya" or self.txt_pass.get()!="123":
            messagebox.showerror("Error","Invalid Username or Password",parent=self.root)

        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}",parent=self.root)
            response = messagebox.askquestion("Proceed to next page")
            if response=="yes":
                #=======BK Image===========
                self.bk=PhotoImage(file="C:\\Users\\Lakshya Narula\\Desktop\\Deliverables_Clevered\\Background for program(deliverables)\\Screenshot (188).png")
                self.bk_image=Label(self.root,image=self.bk).place(x=0,y=0,relwidth=1,relheight=1)

                Notes_btn=Button(self.root,command=self.notes,text="Make Notes",font=("Old english text MT",30),fg="white",bg="black").place(x=450,y=678)
                Convo_btn=Button(self.root,command=self.chatscreen,text="Conversation",font=("Old english text MT",30),fg="white",bg="black").place(x=900,y=678)



    def notes(self):
        self.bw=PhotoImage(file="C:\\Users\\Lakshya Narula\\Desktop\\Deliverables_Clevered\\Background for program(deliverables)\\BackgroundNotes.png")
        self.bw_image=Label(self.root,image=self.bw).place(x=0,y=0,relwidth=1,relheight=1)
        #=======Notes Frame======
        Frame_notes=Frame(self.root,bg="white")
        Frame_notes.place(x=470,y=200,height=400,width=590)
        title=Label(self.root,text="Make Notes",font=("Impact",50,"bold"),fg="#d25d17",bg="black").place(x=620,y=30)
        desc_Btn=Button(self.root,command=self.setaudio,text="Click here",font=("Goudy old style",30,"bold"),fg="Darkblue",bg="white").place(x=676,y=650)


    def setaudio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            MyText =r.recognize_google(audio)

        notes=Label(self.root,text=MyText,font=("Times New Roman",20),fg="black",bg="white").place(x=500,y=220)

        
    def chatscreen(self):
        self.br=PhotoImage(file="C:\\Users\\Lakshya Narula\\Desktop\\Deliverables_Clevered\\Background for program(deliverables)\\Screenshot (190).png")
        self.br_image=Label(self.root,image=self.br).place(x=0,y=0,relwidth=1,relheight=1)
        title=Label(self.root,text="Chat with Sam",font=("Algerian",50,"bold"),fg="#d25d17",bg="black").place(x=565,y=43)
        desc_Btn=Button(self.root,command=self.assistant,text="Click here",font=("Times New Roman",30,"bold"),fg="Darkblue",bg="white").place(x=670,y=660)




    def speaktext(self,text):
        friend=pyttsx3.init()
        friend.say(text)
        friend.runAndWait()

    def getaudio(self):
        r = sr.Recognizer()
        with sr.Microphone()as source:
            print('...listening')
            audio = r.listen(source)
            MyText = r.recognize_google(audio)
            return(MyText)

    def assistant(self):
        while True:
            start=self.getaudio()
            if "hello" in start:
                self.speaktext("hiii")
                title=Label(self.root,text="You: Hi",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=500)
                title=Label(self.root,text="You: Hello",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=600)
            elif "how are you" in start:
                self.speaktext("I'm great, what about you?")
                title=Label(self.root,text="You: Hi",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=500)
                title=Label(self.root,text="You: Hello",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=600)
            elif "i am feeling very stressed out" in start:
                self.speaktext("What happened? Too many assignments?")
                title=Label(self.root,text="You: Hi",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=500)
                title=Label(self.root,text="You: Hello",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=600)
            elif "yes, and on top of that, exams" in start:
                self.speaktext("I have a great way for you to relax.")
                title=Label(self.root,text="You: Hi",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=500)
                title=Label(self.root,text="You: Hello",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=600)
            elif "sure" in start:
                self.speaktext("You can listen to music.")
                title=Label(self.root,text="You: Hi",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=500)
                title=Label(self.root,text="You: Hello",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=600)
            elif "yes! i love music. thank you." in start:
                self.speaktext("No problem, I'm always here for you.")
                title=Label(self.root,text="You: Hi",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=500)
                title=Label(self.root,text="You: Hello",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=600)
            elif "ok, i guess then i will relax a bit. bye." in start:
                self.speaktext("Bye")
                title=Label(self.root,text="You: Hi",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=500)
                title=Label(self.root,text="You: Hello",font=("Times New Roman",30),fg="black",bg="white").place(x=500,y=600)
            break


root=Tk()
obj=Login(root)
root.mainloop()

obj.assistant()






    

