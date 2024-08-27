 #To access the website on ttkbootstrap
#Search on ttkbootstrap.readocs.io on the web and click on started
#We first start with intsalling ttkbootsttrap in out pc
#pip install ttkbootstrap
from tkinter import *
from tkinter import messagebox
#It is to make the attribute value be in capital letter and not be in a  strinf
from ttkbootstrap.constants import *
#For messagebox
from ttkbootstrap.dialogs import Messagebox 


import ttkbootstrap as tb

import language

from googletrans import Translator

from tkinter import PhotoImage

from PIL import Image, ImageTk

import os

import sys

from pathlib import Path




def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0,END)

    #messagebox.showinfo('','TEXT CLEARED')
    Messagebox.show_info('TEXT CLEARED','Here is the title')
    
    
def tranlate_it():
    


    try:
        
        if original_text.get(1.0, END) ==" " :
            Messagebox.show_error("PLEASE INSERT A TEXT INSIDE THE TEXTAREA",'ERROR')

        else:
                
            #getting the language key to translate from combo
            for key, value in languages.items():
                if value == original_option.get():
                    from_language_key = key



            #getting the language key from translated combo widget
            for key, value in languages.items():
                if value == translated_option.get():
                    to_language_key = key


            #Getting the text from our widget
            text =original_text.get(1.0,END)

            #Initializing our Translator
            
            translator =Translator()


            #Lets translate it here using translate() mathod

            translated_word =translator.translate(text, src=from_language_key , dest =to_language_key).text

            #INserting the text into the translated widget for view
            translated_text.insert(END,translated_word)
            


    except Exception as e:
        
        messagebox.showerror("Translator",e)
        
       

languages =language.lan

languages_list =list(languages.values())


# Seeting a root in ttkbootstrap
#The themename is an attribute storing different colors,part of the names are
# superhero cyborg minty united darkly vapor flatly lumen pulse sandstone solar cosmo lumen simplex cerculean morph yeti
#literal
root =tb.Window(themename='solar')

root.title("TRANSLATOR APPLICATION")
root.geometry("1200x530")
root.resizable(False,False)

# # Load the PNG image
# icon_image = Image.open("trans.png")  # Replace with your actual icon file path
# icon_photo = ImageTk.PhotoImage(icon_image)

# # Set the window icon using the PNG image
# root.tk.call('wm', 'iconphoto', root._w, icon_photo)

original_text =Text(root,height=25, width=58,font=('Helvetica',10))
original_text.grid(row=0, column=0, pady=0 ,padx=0)


# Create the Scrollbar widget
scrollbar = tb.Scrollbar(root, orient='vertical')
scrollbar.grid(row=0, column=0, sticky='ns', pady=20, padx=(470, 40))  # Add padding to the right for symmetry




# Configure the Scrollbar to work with the Text widget
original_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=original_text.yview)



original_option =my_combo =tb .Combobox(root,bootstyle="sucess",width=60 ,values=languages_list) 
original_option.grid(row=1, column=0)
original_option.current(22)



trasnlate_button = tb.Button(root,text="Translate!",bootstyle="danger,outline",width=20,command=tranlate_it)

trasnlate_button.grid(row=0, column=1, padx=10)




translated_text =Text(root,height=25, width=58,font=('Helvetica',10))
translated_text.grid(row=0, column=2, pady=20 ,padx=0)

# Create the Scrollbar widget
scrollbar2 = tb.Scrollbar(root, orient='vertical')
scrollbar2.grid(row=0, column=2, sticky='ns', pady=20, padx=(480, 40))  # Add padding to the right for symmetry




# Configure the Scrollbar to work with the Text widget
translated_text.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=translated_text.yview)


translated_option =tb .Combobox(root,bootstyle="success",width=60 , values=languages_list) 
translated_option.grid(row=1, column=2)
translated_option.current(0)









#clear Button

clear_button = tb.Button(root, text="clear",bootstyle="dark",width=20, command=clear)
clear_button.grid(row=2, column=1)



root.mainloop()