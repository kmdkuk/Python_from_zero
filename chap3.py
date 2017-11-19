import tkinter
sample_path="12saipython/"
root = tkinter.Tk()
root.title("リリーに質問")
root.minsize(640, 480)

canvas = tkinter.Canvas(bg="black", width=640, height=480)
canvas.place(x=0, y=0)
img = tkinter.PhotoImage(file=(sample_path+"img3/chap3-back.png"))
canvas.create_image(320, 240, image=img)

root.mainloop()
