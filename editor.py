from tkinter import*
from tkinter import filedialog,messagebox,END,Tk
root=Tk()
root.geometry("500x500")
text=Text(root,height="200",width="200",bd='2',padx='5',font=("Andila Mono",16))
root.title("A simple Text Editor using Python GUI ")
text.pack()

#.....Functions for File Menu..........

def new():
    if len(text.get("1.0",END))>0:
        dialog_title="please answer"
        dialog_text="Do you want to save?"
        answer=messagebox.askquestion(dialog_title,dialog_text)

        if answer=='yes':
            save()
            text.delete("1.0",END)
        else:
            text.delete("1.0",END)
            
def open():
         dialog_title="please answer"
         dialog_text="Do you want to save changes?"
         answer=messagebox.askquestion(dialog_title,dialog_text)
         if answer=='yes':
             save()
            
             file=filedialog.askopenfile(parent=root,filetype=(("Text file","*.txt"),("All files","*.*")))

             if file !=None:
                  text.delete("1.0",END)
                  contents=file.read()
                  text.insert("1.0",contents)
                  file.close()
         else:
              file=filedialog.askopenfile(parent=root,filetype=(("Text file","*.txt"),("All files","*.*")))

              if file !=None:
                   text.delete("1.0",END)
                   contents=file.read()
                   text.insert("1.0",contents)
                   file.close()
            
def save():
    file=filedialog.asksaveasfile(mode="w")
    if file!=None:
        data=text.get("1.0",END+'-1c')
        file.write(data)
        file.close()
    pass

def exit():
     dialog_title="please answer"
     dialog_text="Do you want exit?"
     answer=messagebox.askquestion(dialog_title,dialog_text)
     if answer=='yes':
         root.destroy()
        
#.....Functions for Edit Menu..........
         
def copy():
    text.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    
def cut():
    text.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    text.delete(index1=SEL_FIRST,index2=SEL_LAST)
    
def paste():
    text.insert(INSERT,text.clipboard_get())
    
def delete():
    text.delete(index1=SEL_FIRST,index2=SEL_LAST)
    
def select_all():
    text.tag_add(SEL,"1.0",END)
    
    
#.....Functions for About Menu..........
    
def about():
    dialog_title="Help"
    dialog_text="Text editor using Python"
    messagebox.showinfo(dialog_title,dialog_text)

    
    
#....For File Menu options..........
    
mnu=Menu(root)
root.config(menu=mnu)
filemnu=Menu(mnu)
mnu.add_cascade(label="File",menu=filemnu)
filemnu.add_command(label="New",command=new)
filemnu.add_command(label="Open",command=open)
filemnu.add_command(label="Save",command=save)
filemnu.add_separator()
filemnu.add_command(label="Exit",command=exit)

#....For Edit Menu options.........

editmnu=Menu(mnu)
mnu.add_cascade(label="Edit",menu=editmnu)
editmnu.add_command(label="Undo",command=text.edit_undo)
editmnu.add_command(label="Redo",command=text.edit_redo)
editmnu.add_separator()
editmnu.add_command(label="copy",command=copy)
editmnu.add_command(label="cut",command=cut)
editmnu.add_command(label="paste",command=paste)
editmnu.add_command(label="delete",command=delete)
editmnu.add_separator()
editmnu.add_command(label="Select all",command=select_all)

#....for About Menu option.......

mnu.add_cascade(label="About",command=about)


root.mainloop()
