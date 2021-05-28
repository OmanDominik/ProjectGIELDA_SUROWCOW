from APIKey import *
import matplotlib.pyplot as plt
from datetime import datetime
import requests
import json
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import GUIActionFunctions

"""
Plik obsługujący kontakt kodu z API.
"""

"""
Wprowadzanie klucza oraz adresu hosta API. 
"""
headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': API_HOST
}


def get_current_value(material_symbol):
    """
    Funkcja pobierająca z API aktualną wartość danego surowca.

    :param material_symbol: symbol opisujący wybrany surowiec, którego wartość chcemy probać
    :return: krotka zawierająca obecną wartość danego surowca oraz walutę, w której ta wartość jest wyrażana.
            Ewentualnie zwraca komunikat błędu jeśli taki wystąpi.
    """

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"region": "GB", "symbols": {material_symbol}}
    response = requests.request("GET", url, headers=headers, params=querystring)
    parameters = json.loads(response.text)
    if parameters.get("error") is None:
        value = parameters.get("quoteResponse").get("result")[0].get("regularMarketPrice")
        currency = parameters.get("quoteResponse").get("result")[0].get("currency")
        formatted_value = "{:.2f}".format(value)
        return formatted_value, currency
    else:
        err = "Błąd połączenia, spróbuj ponownie"
        return err, 1


def get_chart(material_symbol, chart_range, chart_frame):
    """
    Funkcja tworząca oraz wyświetlająca w graficznym interfejsie wykres wybranego surowca dla podanego okresu.

    :param material_symbol: symbol opisujący wybrany surowiec, którego wykres chcemy wyświetlić
    :param chart_range: okres z jakiego chcemy wygenerować wykres (5 dni, miesiąc lub rok)
    :param chart_frame: ramka, w której wyświetlony zostanie wykres
    :return: funkcja zwraca wartość None w przypadku, w którym wystąpi błąd pobierania danych z API.
    """

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts"

    querystring = {"symbol": {material_symbol}, "interval": "1d", "range": {chart_range}, "region": "GB"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    chart_data = json.loads(response.text)

    if chart_data.get("error") is None:
        timestamp_list = []

        timestamp_list.extend(chart_data.get("chart").get("result")[0].get("timestamp"))

        days = []

        for ts in timestamp_list:
            dt = datetime.fromtimestamp(ts)
            days.append(dt.strftime("%d/%m/%Y"))

        values = []

        values.extend(chart_data.get("chart").get("result")[0].get("indicators").get("quote")[0].get("close"))

        formatted_values = []

        previous_value = 0

        for value in values:
            if value is not None:
                if material_symbol == "HG=F":
                    value *= 2.20462262185
                formatted_value = "{:.2f}".format(value)
                formatted_values.append(float(formatted_value))
                previous_value = float(formatted_value)
            else:
                formatted_values.append(previous_value)

        chart_figure = plt.Figure(figsize=(7.91, 4.45), dpi=100)
        values_plot = chart_figure.add_subplot(111)
        values_plot.plot(days, formatted_values, color='#E7E7E7')

        GUIActionFunctions.config_plot(values_plot, chart_figure, material_symbol, chart_range, days)

        chart_canva = FigureCanvasTkAgg(chart_figure, chart_frame)
        chart_canva.get_tk_widget().grid(row=0, column=0, padx=4, pady=4)
        chart_canva.draw()
    else:
        GUIActionFunctions.clear_frame(chart_frame)
        messagebox.showerror("Błąd", "Błąd połączenia z API, spróbuj ponownie")
        return None
