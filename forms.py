from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from dht11 import get_mesure

class Dashboard(FlaskForm):
    humidity = StringField('Number')
    temperature = StringField('Number')

class Gardener():
    #Klasa odpowiedzialna za dane logowania i pobieranie danych z serwera
    # Login
    # Token

class Garden():
    # Częstotliwość pomiarów
    # podklasa Garden: Pot/Doniczka
        #Name - nazwa zioła
        #Wilgotność  (w pomieszczeniu)
        #Temperatura   (w pomiesczeniu)
        #Rozmiar Doniczki
        
        # podklasa Pot: Plant
            #Nazwa: Nazwa 
            #Type: Warzywo/Owoc/Zioło/Kwiat
            #Data posadzenia 

    humidity_measurement = get_mesure()


