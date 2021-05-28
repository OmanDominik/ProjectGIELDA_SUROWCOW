from GUI import *
from APIFile import *
from PIL import ImageTk, Image

"""
Wczytywanie obrazków ukazujących poszczególne surowce.
"""

img_start = Image.open('images/Start.jpg')
img_gold = Image.open('images/Złoto.jpg')
img_silver = Image.open('images/Srebro.jpg')
img_crudeoil = Image.open('images/Ropa.jpg')
img_platinum = Image.open('images/Platyna.jpg')
img_copper = Image.open('images/Miedź.jpg')

"""
Symbole charakteryzujące poszczególne surowce.
"""

gold_symbol = "GC=F"
silver_symbol = "SI=F"
crudeoil_symbol = "CL=F"
platinum_symbol = "PL=F"
copper_symbol = "HG=F"

"""
Waluty, w których określana jest wartość poszczególnych surowców
"""
gold_unit = "uncja"
silver_unit = "uncja"
crudeoil_unit = "baryłka"
platinum_unit = "uncja"
copper_unit = "kilogram"


def select_material(image_label, name_label, variable, t_button, m_button, r_button, text_label, chart_frame):
    """
    Funkcja definiująca działanie przycisku aktywującego wypisywanie danych dla wybranego surowca.

    :param image_label: etykieta, w której wyświetlany jest obrazek ukazujący wybrany surowiec
    :param name_label: etykieta, w której wyświetlana jest nazwa wybranego surowca
    :param variable: wartość wybrana w menu opcji(nazwa jednego z pięciu surowców)
    :param t_button: przycisk do wyświetlania wykresu z ostatnich 5 dni (uruchamiany domyślnie)
    :param m_button: przycisk do wyświetlania wykresu z ostatniego miesiąca
    :param r_button: przycisk do wyświetlania wykresu z ostatniego roku
    :param text_label: etykieta, w której wyświetlana jest wartość wybranego surowca
    :param chart_frame: ramka, w której wyświetlany jest wykres wartości wybranego surowca
    """

    t_button['state'] = 'normal'
    m_button['state'] = 'normal'
    r_button['state'] = 'normal'
    m_button.configure(bg="#666666")
    r_button.configure(bg="#666666")
    m_button.configure(bg="#666666")

    if variable.get() == '':
        conf_gui_start(image_label, name_label, text_label, chart_frame)
        t_button['state'] = 'normal'
        t_button.configure(bg="#666666")

    if variable.get() == "Złoto":
        conf_gui_gold(image_label, name_label, text_label, chart_frame)
        t_button['state'] = 'disabled'
        t_button.configure(bg="#000000")

    if variable.get() == "Ropa":
        conf_gui_crudeoil(image_label, name_label, text_label, chart_frame)
        t_button['state'] = 'disabled'
        t_button.configure(bg="#000000")

    if variable.get() == "Platyna":
        conf_gui_platinum(image_label, name_label, text_label, chart_frame)
        t_button['state'] = 'disabled'
        t_button.configure(bg="#000000")

    if variable.get() == "Srebro":
        conf_gui_silver(image_label, name_label, text_label, chart_frame)
        t_button['state'] = 'disabled'
        t_button.configure(bg="#000000")

    if variable.get() == "Miedź":
        conf_gui_copper(image_label, name_label, text_label, chart_frame)
        t_button['state'] = 'disabled'
        t_button.configure(bg="#000000")


def t_button_action(name_label, t_button, m_button, r_button, chart_frame):
    """
    Funkcja definiująca działanie przycisku wyświetlającego wykres wartości z ostatnich 5 dni.

    :param name_label: etykieta, w której wyświetlana jest nazwa wybranego surowca
    :param t_button: przycisk do wyświetlania wykresu z ostatnich 5 dni (uruchamiany domyślnie)
    :param m_button: przycisk do wyświetlania wykresu z ostatniego miesiąca
    :param r_button: przycisk do wyświetlania wykresu z ostatniego roku
    :param chart_frame: ramka, w której wyświetlany jest wykres wartości wybranego surowca
    """

    if (name_label.cget('text')) == 'Złoto':
        get_chart(gold_symbol, "5d", chart_frame)
    if (name_label.cget('text')) == 'Srebro':
        get_chart(silver_symbol, "5d", chart_frame)
    if (name_label.cget('text')) == 'Ropa':
        get_chart(crudeoil_symbol, "5d", chart_frame)
    if (name_label.cget('text')) == 'Platyna':
        get_chart(platinum_symbol, "5d", chart_frame)
    if (name_label.cget('text')) == 'Miedź':
        get_chart(copper_symbol, "5d", chart_frame)
    if (name_label.cget('text')) != '':
        t_button['state'] = 'disabled'
        m_button['state'] = 'normal'
        r_button['state'] = 'normal'
        t_button.configure(bg="#000000")
        m_button.configure(bg="#666666")
        r_button.configure(bg="#666666")


def m_button_action(name_label, t_button, m_button, r_button, chart_frame):
    """
    Funkcja definiująca działanie przycisku wyświetlającego wykres wartości z ostatniego miesiąca.

    :param name_label: etykieta, w której wyświetlana jest nazwa wybranego surowca
    :param t_button: przycisk do wyświetlania wykresu z ostatnich 5 dni (uruchamiany domyślnie)
    :param m_button: przycisk do wyświetlania wykresu z ostatniego miesiąca
    :param r_button: przycisk do wyświetlania wykresu z ostatniego roku
    :param chart_frame: ramka, w której wyświetlany jest wykres wartości wybranego surowca
    """

    if (name_label.cget('text')) == 'Złoto':
        get_chart(gold_symbol, "1mo", chart_frame)
    if (name_label.cget('text')) == 'Srebro':
        get_chart(silver_symbol, "1mo", chart_frame)
    if (name_label.cget('text')) == 'Ropa':
        get_chart(crudeoil_symbol, "1mo", chart_frame)
    if (name_label.cget('text')) == 'Platyna':
        get_chart(platinum_symbol, "1mo", chart_frame)
    if (name_label.cget('text')) == 'Miedź':
        get_chart(copper_symbol, "1mo", chart_frame)
    if(name_label.cget('text')) != '':
        t_button['state'] = 'normal'
        m_button['state'] = 'disabled'
        r_button['state'] = 'normal'
        m_button.configure(bg="#000000")
        t_button.configure(bg="#666666")
        r_button.configure(bg="#666666")


def r_button_action(name_label, t_button, m_button, r_button, chart_frame):
    """
    Funkcja definiująca działanie przycisku wyświetlającego wykres wartości z ostatniego roku.

    :param name_label: etykieta, w której wyświetlana jest nazwa wybranego surowca
    :param t_button: przycisk do wyświetlania wykresu z ostatnich 5 dni (uruchamiany domyślnie)
    :param m_button: przycisk do wyświetlania wykresu z ostatniego miesiąca
    :param r_button: przycisk do wyświetlania wykresu z ostatniego roku
    :param chart_frame: ramka, w której wyświetlany jest wykres wartości wybranego surowca
    """

    if (name_label.cget('text')) == 'Złoto':
        get_chart(gold_symbol, "1y", chart_frame)
    if (name_label.cget('text')) == 'Srebro':
        get_chart(silver_symbol, "1y", chart_frame)
    if (name_label.cget('text')) == 'Ropa':
        get_chart(crudeoil_symbol, "1y", chart_frame)
    if (name_label.cget('text')) == 'Platyna':
        get_chart(platinum_symbol, "1y", chart_frame)
    if (name_label.cget('text')) == 'Miedź':
        get_chart(copper_symbol, "1y", chart_frame)
    if (name_label.cget('text')) != '':
        t_button['state'] = 'normal'
        m_button['state'] = 'normal'
        r_button['state'] = 'disabled'
        r_button.configure(bg="#000000")
        t_button.configure(bg="#666666")
        m_button.configure(bg="#666666")


def conf_gui_start(image_label, name_label, text_label, chart_frame):
    """
    Funkcja definiująca działanie przycisku aktywującego wypisywanie danych dla wybranego surowca jeśli wybrane
    zostanie puste pole.

    :param image_label: etykieta, w której wyświetlany jest obrazek ukazujący wybrany surowiec
    :param name_label: etykieta, w której wyświetlana jest nazwa wybranego surowca
    :param text_label: etykieta, w której wyświetlana jest wartość wybranego surowca
    :param chart_frame: ramka, w której wyświetlany jest wykres wartości wybranego surowca
    """

    image_label.img = ImageTk.PhotoImage(img_start)
    image_label['image'] = image_label.img
    name_label.config(text='')
    text_label.config(text="")
    clear_frame(chart_frame)


def conf_gui_gold(image_label, name_label, text_label, chart_frame):
    """
    Funkcja definiująca działanie przycisku aktywującego wypisywanie danych dla wybranego surowca jeśli wybrane
    zostanie pole z napisem "Złoto".

    :param image_label: etykieta, w której wyświetlany jest obrazek ukazujący wybrany surowiec
    :param name_label: etykieta, w której wyświetlana jest nazwa wybranego surowca
    :param text_label: etykieta, w której wyświetlana jest wartość wybranego surowca
    :param chart_frame: ramka, w której wyświetlany jest wykres wartości wybranego surowca
    """

    image_label.img = ImageTk.PhotoImage(img_gold)
    image_label['image'] = image_label.img
    name_label.config(text='Złoto')

    value, currency = get_current_value(gold_symbol)
    if currency == 1:
        result = str(value)
        text_label.config(text=result)
        return
    else:
        result = str(value) + " " + str(currency) + "/" + gold_unit
        text_label.config(text=result)

    get_chart(gold_symbol, "5d", chart_frame)


def conf_gui_silver(image_label, name_label, text_label, chart_frame):
    """
    Funkcja definiująca działanie przycisku aktywującego wypisywanie danych dla wybranego surowca jeśli wybrane
    zostanie pole z napisem "Srebro".

    :param image_label: etykieta, w której wyświetlany jest obrazek ukazujący wybrany surowiec
    :param name_label: etykieta, w której wyświetlana jest nazwa wybranego surowca
    :param text_label: etykieta, w której wyświetlana jest wartość wybranego surowca
    :param chart_frame: ramka, w której wyświetlany jest wykres wartości wybranego surowca
    """

    image_label.img = ImageTk.PhotoImage(img_silver)
    image_label['image'] = image_label.img
    name_label.config(text='Srebro')

    value, currency = get_current_value(silver_symbol)
    if currency == 1:
        result = str(value)
        text_label.config(text=result)
        return
    else:
        result = str(value) + " " + str(currency) + "/" + silver_unit
        text_label.config(text=result)

    get_chart(silver_symbol, "5d", chart_frame)


def conf_gui_crudeoil(image_label, name_label, text_label, chart_frame):
    """
    Funkcja definiująca działanie przycisku aktywującego wypisywanie danych dla wybranego surowca jeśli wybrane
    zostanie pole z napisem "Ropa".

    :param image_label: etykieta, w której wyświetlany jest obrazek ukazujący wybrany surowiec
    :param name_label: etykieta, w której wyświetlana jest nazwa wybranego surowca
    :param text_label: etykieta, w której wyświetlana jest wartość wybranego surowca
    :param chart_frame: ramka, w której wyświetlany jest wykres wartości wybranego surowca
    """

    image_label.img = ImageTk.PhotoImage(img_crudeoil)
    image_label['image'] = image_label.img
    name_label.config(text='Ropa')

    value, currency = get_current_value(crudeoil_symbol)
    if currency == 1:
        result = str(value)
        text_label.config(text=result)
        return
    else:
        result = str(value) + " " + str(currency) + "/" + crudeoil_unit
        text_label.config(text=result)

    get_chart(crudeoil_symbol, "5d", chart_frame)


def conf_gui_platinum(image_label, name_label, text_label, chart_frame):
    """
    Funkcja definiująca działanie przycisku aktywującego wypisywanie danych dla wybranego surowca jeśli wybrane
    zostanie pole z napisem "Platyna".

    :param image_label: etykieta, w której wyświetlany jest obrazek ukazujący wybrany surowiec
    :param name_label: etykieta, w której wyświetlana jest nazwa wybranego surowca
    :param text_label: etykieta, w której wyświetlana jest wartość wybranego surowca
    :param chart_frame: ramka, w której wyświetlany jest wykres wartości wybranego surowca
    """

    image_label.img = ImageTk.PhotoImage(img_platinum)
    image_label['image'] = image_label.img
    name_label.config(text='Platyna')

    value, currency = get_current_value(platinum_symbol)
    if currency == 1:
        result = str(value)
        text_label.config(text=result)
        return
    else:
        result = str(value) + " " + str(currency) + "/" + platinum_unit
        text_label.config(text=result)

    get_chart(platinum_symbol, "5d", chart_frame)


def conf_gui_copper(image_label, name_label, text_label, chart_frame):
    """
    Funkcja definiująca działanie przycisku aktywującego wypisywanie danych dla wybranego surowca jeśli wybrane
    zostanie pole z napisem "Miedź".

    :param image_label: etykieta, w której wyświetlany jest obrazek ukazujący wybrany surowiec
    :param name_label: etykieta, w której wyświetlana jest nazwa wybranego surowca
    :param text_label: etykieta, w której wyświetlana jest wartość wybranego surowca
    :param chart_frame: ramka, w której wyświetlany jest wykres wartości wybranego surowca
    """

    image_label.img = ImageTk.PhotoImage(img_copper)
    image_label['image'] = image_label.img
    name_label.config(text='Miedź')

    value, currency = get_current_value(copper_symbol)
    if currency == 1:
        result = str(value)
        text_label.config(text=result)
        return
    else:
        value = float(value)
        value *= 2.20462262185
        value = "{:.2f}".format(value)
        result = str(value) + " " + str(currency) + "/" + copper_unit
        text_label.config(text=result)

    get_chart(copper_symbol, "5d", chart_frame)


def clear_frame(frame):
    """
    Funkcja usuwające wszystkie komponenty znajdujące się w ramce.

    :param frame: ramka do "oczyszczenia"
    """
    for widgets in frame.winfo_children():
        widgets.destroy()


def config_plot(values_plot, chart_figure, material_symbol, chart_range, days):
    """
    Funkcja stylizująca wykres.

    :param values_plot: wykres, który będzie stylizowany
    :param chart_figure: figura, w której tworzony jest wykres
    :param material_symbol: symbol materiału dla którego generowany jest wykres
    :param chart_range: okres, z któego wygenerowany został wykres (5 dni, miesiąc lub rok)
    :param days: lista dni dla których wygenerowany został wykres
    """

    font = {'fontname': 'Courier New', 'fontweight': 'bold'}

    values_plot.set_title('WYKRES WARTOŚCI SUROWCA', **font)
    chart_figure.patch.set_facecolor('#666666')
    values_plot.set_facecolor('#000000')
    values_plot.tick_params(axis='x', labelrotation=25, labelsize=7)

    values_plot.spines['bottom'].set_color('#E7E7E7')
    values_plot.spines['top'].set_color('#E7E7E7')
    values_plot.spines['right'].set_color('#E7E7E7')
    values_plot.spines['left'].set_color('#E7E7E7')
    values_plot.tick_params(axis='both', colors='#E7E7E7')

    if material_symbol == gold_symbol:
        values_plot.set_ylabel('WARTOŚĆ [USD/UNCJA]', **font)
    if material_symbol == silver_symbol:
        values_plot.set_ylabel('WARTOŚĆ [USD/UNCJA]', **font)
    if material_symbol == platinum_symbol:
        values_plot.set_ylabel('WARTOŚĆ [USD/UNCJA]', **font)
    if material_symbol == copper_symbol:
        values_plot.set_ylabel('WARTOŚĆ [USD/KILOGRAM]', **font)
    if material_symbol == crudeoil_symbol:
        values_plot.set_ylabel('WARTOŚĆ [USD/BARYŁKA]', **font)

    if chart_range == "1mo":
        days_for_month = []
        for i in range(len(days)):
            if i % 2 == 0:
                days_for_month.append(i)

        values_plot.set_xticks(days_for_month)

    if chart_range == "1y":
        days_for_year = []
        for i in range(len(days)):
            if i % 36 == 0:
                days_for_year.append(i)

        values_plot.set_xticks(days_for_year)
