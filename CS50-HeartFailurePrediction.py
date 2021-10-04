import pickle
import pandas as pd

from kivymd.app import MDApp
from kivy.lang import Builder

screen_helper = """
Screen:
    MDLabel:
        text: "CS50 Heart Failure Prediction"
        halign: "center"
        size_hint: (0.5, 0.1)
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        pos_hint: {"center_x": .5, "center_y": .95}

    MDLabel:
        text: "enter patients data to predict the death event"
        halign: "center"
        size_hint: (0.5, 0.1)
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        pos_hint: {"center_x": .5, "center_y": .9}

    MDTextField:
        id : Age
        hint_text: "Age"
        helper_text: "Sample : 75"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .25, "center_y": .82}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1

    MDTextField:
        id : Anaemia
        hint_text: "Anaemia"
        helper_text: "0 or 1"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .75, "center_y": .82}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1

    MDTextField:
        id : Creatinine_Phosphokinase
        hint_text: "Creatinine_Phosphokinase"
        helper_text: "Sample : 582"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .25, "center_y": .74}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1

    MDTextField:
        id : Diabetes
        hint_text: "Diabetes"
        helper_text: "0 or 1"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .75, "center_y": .74}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1

    MDTextField:
        id : Ejection_Fraction
        hint_text: "Ejection_Fraction"
        helper_text: "Sample : 20"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .75, "center_y": .68}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        
    MDTextField:
        id : High_Blood_Pressure
        hint_text: "High_Blood_Pressure"
        helper_text: "0 or 1"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .25, "center_y": .68}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        
    MDTextField:
        id : Platelets
        hint_text: "Platelets"
        helper_text: "Sample : 265000"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .25, "center_y": .6}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        
    MDTextField:
        id : Serum_Creatinine
        hint_text: "Serum_Creatinine"
        helper_text: "Sample : 1.5"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .75, "center_y": .6}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        
    MDTextField:
        id : Serum_Sodium
        hint_text: "Serum_Sodium"
        helper_text: "Sample : 130"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .25, "center_y": .52}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        
    MDTextField:
        id : Sex
        hint_text: "Sex"
        helper_text: "1 : Men , 0 : Women"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .75, "center_y": .52}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        
    MDTextField:
        id : Smoking
        hint_text: "Smoking"
        helper_text: "1 : Yes , 0 : No"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .75, "center_y": .44}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        
    MDTextField:
        id : Cure_Period
        hint_text: "Cure_Period"
        helper_text: "Sample : 45"
        helper_text_mode: "on_focus"
        size_hint: (0.4, 0.1)
        pos_hint: {"center_x": .25, "center_y": .44}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1

    MDRectangleFlatButton:
        text: "Created By Omid Airom"
        size_hint: (0.4, 0.05)
        pos_hint: {"center_x": .25, "center_y": .30}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        
    MDRectangleFlatButton:
        id : predict
        text: "Predict"
        size_hint: (0.4, 0.15)
        pos_hint: {"center_x": .25, "center_y": .15}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        on_press : app.predict()
        
    MDRectangleFlatButton:
        id : Result
        text: "Result"
        size_hint: (0.4, 0.25)
        pos_hint: {"center_x": .75, "center_y": .2}
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
"""


class Cs50App(MDApp):

    Cure_Period = 0
    Smoking = 0
    Sex = 0
    Serum_Sodium = 0
    Serum_Creatinine = 0
    Platelets = 0
    High_Blood_Pressure = 0
    Ejection_Fraction = 0
    Diabetes = 0
    Creatinine_Phosphokinase = 0
    Anaemia = 0
    Age = 0
    patient = []
    last = []
    CS50_model = pickle.load(open("CS50-HeartFailurePrediction.pkl", "rb"))

    def predict(self):

        self.Cure_Period = float(self.root.ids.Cure_Period.text)
        self.Smoking = float(self.root.ids.Smoking.text)
        self.Sex = float(self.root.ids.Sex.text)
        self.Serum_Sodium = float(self.root.ids.Serum_Sodium.text)
        self.Serum_Creatinine = float(self.root.ids.Serum_Creatinine.text)
        self.Platelets = float(self.root.ids.Platelets.text)
        self.High_Blood_Pressure = float(self.root.ids.High_Blood_Pressure.text)
        self.Ejection_Fraction = float(self.root.ids.Ejection_Fraction.text)
        self.Diabetes = float(self.root.ids.Diabetes.text)
        self.Creatinine_Phosphokinase = float(self.root.ids.Creatinine_Phosphokinase.text)
        self.Anaemia = float(self.root.ids.Anaemia.text)
        self.Age = float(self.root.ids.Age.text)
        self.patient = [self.Age, self.Anaemia, self.Creatinine_Phosphokinase, self.Diabetes, self.Ejection_Fraction,
                  self.High_Blood_Pressure,
                  self.Platelets, self.Serum_Creatinine, self.Serum_Sodium, self.Sex, self.Smoking, self.Cure_Period]

        self.last = [self.patient]
        testdata = pd.DataFrame(self.last)
        prediction = str(self.CS50_model.predict(testdata))
        if prediction[1] == 1:
            self.root.ids.Result.text = "Death Event : Positive"
        else :
            self.root.ids.Result.text = "Death Event : Negative"
        self.patient = []
        self.last = []

    def build(self):

        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        self.title = 'CS50-HeartFailurePrediction'
        return screen


Cs50App().run()
