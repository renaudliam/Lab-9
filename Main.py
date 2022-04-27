from pokeinfo_function import *
from Library import *
from tkinter import *
from tkinter import ttk
import os
import sys
import ctypes
def main():
    script_dir = sys.path[0]
    image_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)
    root = Tk()
    root.title('Pokemon Image Viewer')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.minsize(500, 600)
    myappid = 'Pokeimgviewer'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    root.iconbitmap(os.path.join(script_dir, 'Poke.ico'))

    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))
    frm.rowconfigure(0, weight=10)
    frm.columnconfigure(0,weight=1)

    img_poke = PhotoImage(file=os.path.join(script_dir, 'pokeball.png'))
    lbl_img = ttk.Label(frm, image=img_poke)
    lbl_img.grid(row=0, column=0, padx=10, pady=10)

    poke_list = get_poke_list()
    poke_list.sort()
    poke_list = [p.capitalize() for p in poke_list]

    cbo_pokemon = ttk.Combobox(frm, values=poke_list, state='readonly')
    cbo_pokemon.set('Select a Pokemon')
    cbo_pokemon.grid(row=1,column=0,padx=10,pady=10)

    def handle_poke_select(event):
        current_sel = cbo_pokemon.get()
        image_url = get_pokemon_image_url(current_sel)
        image_path = os.path.join(image_dir, current_sel + '.png')
        download_img_url(image_url, image_path)
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])

    cbo_pokemon.bind('<<ComboboxSelected>>', handle_poke_select)
    def set_desktop_handle():
        current_sel = cbo_pokemon.get()
        image_path = os.path.join(image_dir, current_sel + '.png')
        desktop_bg(image_path)
    btn_set_desktop = ttk.Button(frm, text='Set As Desktop Background', command= set_desktop_handle)
    btn_set_desktop.state(['disabled'])
    btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)
    root.mainloop()

main()













main()
