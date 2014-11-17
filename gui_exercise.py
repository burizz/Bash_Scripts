# from swampy.Gui import *
#
# g = Gui()
# g.title('')
#
# def callback1():
#     g.bu(text='Now press me.', command=callback2)
#     entry = g.en(text='Text field')
#     entry.get()
#
#     canvas = g.ca(width=500, height=500)
#     canvas.circle([0,0], 100, fill='red')
#
# def callback2():
#     g.la(text='Nice job.')
#
# g.bu(text='Press me.', command=callback1)
#
# g.mainloop()



from swampy.Gui import *
from Tkinter import PhotoImage

g = Gui()

canvas = g.ca(width=300)
photo = PhotoImage(file='danger.gif')
canvas.image([0,0], image=photo)

g.mainloop()

#