from tkinter import *
from tkinter import ttk

root= Tk(className="NatoAlphabetic Translator",)
root.minsize(640,400)
def labelchange():
    phrase_to_translate = phrase_entry_variable.get()
    phrase_to_translate_lowercase = phrase_to_translate.lower()
    dic = {"a": "ALPHA", "b": "BRAVO", "c": "CHARLIE", "d": "DELTA", "e": "ECHO", "f": "FOXTROT", "g": "GOLF",
           "h": "HOTEL",
           "i": "INDIA", "j": "JULIET", "k": "KILO", "l": "LIMA", "m": "MIKE", "n": "NOVEMBER", "o": "OSCAR",
           "p": "PAPA",
           "q": "QUEBEC", "r": "ROMEO", "s": "SIERRA", "t": "TANGO", "u": "UNIFORM", "v": "VICTOR", "w": "WHISKEY",
           "x": "XRAY", "y": "YANKEE", "z": "ZULU"}
    word_list = []
    for w in phrase_to_translate_lowercase:
        if w not in dic:
            word_list.append(w)
        else:
            word_list.append((dic[w]))
    translated_phrase = word_list
    phrase_translated_label.configure(text=translated_phrase)


phrase_entry_variable = StringVar()
phrase_entry= Entry(root, textvariable = phrase_entry_variable, width=30,bd=8,font="Arial",justify=CENTER)
phrase_entry.grid(row=5, column=15)
phrase_entry_variable.set("write a phrase")


message_translation=Label(root, text="The NATO AlphaBetic translation is:",font="Arial")
message_translation.grid(row=10,column=15,padx=10,pady=10)
phrase_translated_label=Label(root,text="waiting for your phrase", bg="yellow",fg="blue",font="Arial")
phrase_translated_label.grid(row=15,column=15,padx=10,pady=10,sticky="WE")
tranlating_button=ttk.Button(root,text="Click me to Tranlate",command=labelchange)
tranlating_button.grid(row=20, column=15,padx=10,pady=10)


root.mainloop()