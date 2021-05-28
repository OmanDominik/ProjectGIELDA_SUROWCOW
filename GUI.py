from GUIActionFunctions import *
import tkinter as tk
from PIL import ImageTk, Image
from functools import partial
import datetime

OPTIONS = ['', 'Miedź', 'Ropa', 'Platyna', 'Srebro', 'Złoto']


class Application(tk.Frame):
    def __init__(self, master=None):
        """
        Konstruktor interfejsu graficznego użytkownika.
        Wprowadzanie obiektów tkinter.
        """

        super().__init__(master)
        "Konfiguracja wyglądu GUI"
        self.configure_gui()

        variable = tk.StringVar(self.master)
        variable.set(OPTIONS[0])
        raw_materials_menu = tk.OptionMenu(self.master, variable, *OPTIONS)
        self.conf_option_menu(raw_materials_menu)

        select_button_frame = tk.Frame(self.master, background="#000000")
        select_button = tk.Button(select_button_frame, text="⫸", width=4, height=2)
        self.conf_select_option_button(select_button, select_button_frame)

        self.add_date_label()

        graph_frame = tk.Frame(self.master, background="#000000")
        graph_label = tk.Label(graph_frame, text="WYKRES:", font=('Courier', 25, 'bold'), height=1)
        chart_frame = tk.Frame(self.master, bg="#000000", height=450, width=800)
        self.conf_graph_frame(graph_label, graph_frame, chart_frame)

        value_frame = tk.Frame(self.master, background="#000000")
        value_label = tk.Label(value_frame, text="WARTOŚĆ:", font=('Courier', 25, 'bold'), height=1)
        text_label = tk.Label(value_frame, height=1, width=20, font=('Courier', 25, 'bold'))
        self.conf_value_frame(value_frame, value_label, text_label)

        buttons_frame = tk.Frame(self.master, background="#000000")
        t_button = tk.Button(buttons_frame, text="5D", width=5, height=2, font=('Courier', 15, 'bold'))
        m_button = tk.Button(buttons_frame, text="M", width=5, height=2, font=('Courier', 15, 'bold'))
        r_button = tk.Button(buttons_frame, text="R", width=5, height=2, font=('Courier', 15, 'bold'))
        self.conf_graph_buttons(buttons_frame, t_button, m_button, r_button)

        image_frame = tk.Frame(self.master, background="#000000")
        image_label = tk.Label(image_frame, bg='#666666')
        name_label = tk.Label(image_frame, height=1, width=15, font=('Courier', 25, 'bold'), anchor='center')
        self.conf_image_frame(image_frame, image_label, name_label)

        "Konfiguracja akcji GUI"

        select_button.configure(command=partial(select_material, image_label, name_label, variable, t_button, m_button,
                                                r_button, text_label, chart_frame))

        t_button.configure(command=partial(t_button_action, name_label, t_button, m_button, r_button, chart_frame))
        m_button.configure(command=partial(m_button_action, name_label, t_button, m_button, r_button, chart_frame))
        r_button.configure(command=partial(r_button_action, name_label, t_button, m_button, r_button, chart_frame))

    def configure_gui(self):
        """
        Nadawanie odpowiednich parametrów okna GUI.
        """

        self.master.title('Giełda surowców')
        self.master.geometry("1200x650")
        self.master.tk.call('wm', 'iconphoto', self.master._w, tk.PhotoImage(file='images/gielda.png'))
        self.master.config(bg="#2D2B2B")

    def conf_option_menu(self, raw_materials_menu):
        """
        Stylizacja menu wyboru surowców.

        :param raw_materials_menu: obiekt typu OptionsMenu wykorzystywany do wyboru interesującego użytkownika surowca
        """

        variable = tk.StringVar(self.master)
        variable.set(OPTIONS[0])
        raw_materials_menu.config(width=10, font=('Courier', 25, 'bold'))
        raw_materials_menu.config(bg='#666666', fg='#E7E7E7', activebackground='#000000', activeforeground='#E7E7E7',
                                  highlightbackground="#000000", highlightcolor="#000000")
        raw_materials_menu.place(x=30, y=20)

    @staticmethod
    def conf_select_option_button(select_button, button_frame):
        """
        Stylizacja przycisku aktywującego.

        :param select_button: przycisk uruchamiający wyszukiwanie danych dla wybranego surowca
        :param button_frame: ramka w której znajduje się przycisk button_frame
        """

        select_button.config(bg='#666666', fg='#E7E7E7', activebackground='#000000', activeforeground='#E7E7E7')
        select_button.pack(padx=3, pady=3)
        button_frame.place(x=300, y=23)

    def add_date_label(self):
        """
        Dodawanie etykiety z zegarem znajdującej się w prawym górnym rogu ekranu.
        """

        def tick():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            date_label.config(text=today + " " + time)
            date_label.after(200, tick)

        date_frame = tk.Frame(self.master, background="#000000")
        today = datetime.datetime.now().strftime("%d.%m.%Y")
        date_label = tk.Label(date_frame, font=('Courier', 15, 'bold'))
        date_label.config(bg='#666666', fg='#E7E7E7', borderwidth=3)
        tick()
        date_label.grid(padx=3, pady=3)
        date_frame.place(x=950, y=5)

    @staticmethod
    def conf_value_frame(value_frame, value_label, text_label):
        """
        Stylizacja pola, w którym wypisywana będzie wartość wybranego surowca.

        :param value_frame: ramka w, której znajdować będą sie obie etykiety
        :param value_label: etykieta, opisująca co znajduję się w etykiecie text_label
        :param text_label: etykieta, w której wyświetlana jest wartość wybranego surowca
        """

        value_label.config(bg='#666666', fg='#E7E7E7')
        value_label.grid(row=0, column=0, padx=3, pady=3)
        text_label.config(bg='#666666', fg='#000000', anchor=tk.W)
        text_label.grid(row=0, column=1, padx=3, pady=3)
        value_frame.place(x=600, y=100)

    @staticmethod
    def conf_graph_frame(graph_label, graph_frame, chart_frame):
        """
        Stylizacja pola, w których znajduje się wykres oraz pola, który ten wykres opisuje.

        :param graph_label: etykieta z napisem "wykres:"
        :param graph_frame: ramka, w której znajduje się etykieta graph_label
        :param chart_frame: ramka, w której wyświetlany jest wykres
        """

        graph_label.config(bg='#666666', fg='#E7E7E7')
        graph_label.grid(padx=3, pady=3)
        graph_frame.place(x=20, y=120)
        chart_frame.place(x=20, y=180)

    @staticmethod
    def conf_graph_buttons(buttons_frame, t_button, m_button, r_button):
        """
        Stylizacja ramki, w której znajdują się przyciski używane do określenia jaki typ wykresu ma być wyświetlany.

        :param buttons_frame: ramka, w której znajdują się wszytskie poniższe przyciski
        :param t_button: przycisk do wyświetlania wykresu z ostatnich 4 dni (uruchamiany domyślnie)
        :param m_button: przycisk do wyświetlania wykresu z ostatniego miesiąca
        :param r_button: przycisk do wyświetlania wykresu z ostatniego roku
        """

        t_button.config(bg='#666666', fg='#E7E7E7', activebackground='#000000', activeforeground='#E7E7E7')
        t_button.grid(row=0, column=0, padx=3, pady=3)

        m_button.config(bg='#666666', fg='#E7E7E7', activebackground='#000000', activeforeground='#E7E7E7')
        m_button.grid(row=0, column=1, padx=3, pady=3)

        r_button.config(bg='#666666', fg='#E7E7E7', activebackground='#000000', activeforeground='#E7E7E7')
        r_button.grid(row=0, column=2, padx=3, pady=3)

        buttons_frame.place(x=900, y=550)

    @staticmethod
    def conf_image_frame(image_frame, image_label, name_label):
        """
        Stylizacja ramki, w której wyświetlać będzie się ramka, w której skłąd wchodzi nazwa wybranego surowca oraz
        obraz ten surowiec ukazujący

        :param image_frame: ramka, w której zawierać będą się poniższe etykiety
        :param image_label: etykieta, w której wyświetlany jest obrazek ukazujący wybrany surowiec
        :param name_label: etykieta, w której wyświetla się nazwa wybranego surowca
        """

        image_label.grid(row=0, column=0, padx=3, pady=3)
        img = Image.open('images/Start.jpg')
        image_label.img = ImageTk.PhotoImage(img)
        image_label['image'] = image_label.img

        name_label.config(bg='#666666', fg='#000000')
        name_label.grid(row=1, column=0, padx=3, pady=3)
        image_frame.place(x=860, y=225)
