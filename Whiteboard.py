from tkinter import *


class SikiBoard():

    def __init__(self):

        # Make Board Window
        self.board = Tk()
        self.board.geometry("800x600")
        self.board.title("Siki-Board")
        self.board.rowconfigure(0, weight=1)
        self.board.columnconfigure(0, weight=1)
        self.canvas = Canvas(self.board)
        self.canvas.grid(row=0, column=0, sticky="nsew")


        # Clear func to rubber the screen
        self.clear()

        # Get the draw from user
        self.get_pos()

        # Define color of line
        self.color = "black"
        self.color_line()




        self.board.mainloop()





    def coordinate(self, event):
        self.x = event.x
        self.y = event.y
        try:
            if(self.old):
                self.x1, self.y1 = self.old
                self.canvas.create_line(self.x, self.y, self.x1, self.y1, fill=self.color)
                self.canvas.create_line(self.x+1, self.y+1, self.x1+1, self.y1+1, self.color)
                self.canvas.create_line(self.x-1, self.y-1, self.x1-1, self.y1-1, self.color)
            self.old = self.x, self.y
        except:
            self.old = self.x, self.y



    def get_pos(self):
        self.canvas.bind("<B1-Motion>", self.coordinate)
        self.canvas.bind("<ButtonRelease-1>", self.release)


    def release(self, event):
        self.old = None



    def clear(self):

        self.option_creen = Tk()
        self.option_creen.title("Clear Screen")
        self.clear_button = Button(self.option_creen, text="Clear", bg="black", padx=60, pady=20, command=self.new_field)
        self.clear_button.pack()



    def new_field(self):

        self.board.rowconfigure(0, weight=1)
        self.board.columnconfigure(0, weight=1)

        self.canvas = Canvas(self.board)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.get_pos()


    def color_line(self):

        self.color_setting_label = Label()






if __name__ == "__main__":

    board = SikiBoard()