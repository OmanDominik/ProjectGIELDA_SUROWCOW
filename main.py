from GUI import *

if __name__ == '__main__':
    "Uruchamianie aplikacji"

    root = tk.Tk()
    root.resizable(False, False)
    exchange_app = Application(master=root)
    exchange_app.mainloop()
