from tkinter import Tk
from ui import UI

def main():
    window = Tk()
    window.title("Pakkausharjoitus")
    window.geometry("300x200")
    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__ == "__main__":
    main()