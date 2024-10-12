from tkinter import messagebox
import tkintertools as tkt
m = ""
def mrr():
    global m
    entry_text = entry.get()
    m = entry_text
    while True:
        messagebox.showinfo("哈哈哈", m + "是SB")
        messagebox.showwarning("哈哈哈", m + "是SB")
        messagebox.showerror("哈哈哈", m + "是SB")
window = tkt.Tk(title="SB")
window.alpha(0.975)
cv = tkt.Canvas(window, zoom_item=True, keep_ratio="min", free_anchor=True)
cv.place(width=1280, height=720, x=640, y=360, anchor="center")
tkt.Text(cv, (650,250), text="骂 人 工 具", fontsize=48, anchor="center")
entry = tkt.InputBox(cv,position=(550, 300))
tkt.Button(cv, text="骂他！",command=mrr,position=(600, 360))
window.mainloop()
