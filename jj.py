from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
import json
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.core.window import Window


Window.size = (360, 700)



with open("mimi.json", "r") as jsonfile:
    num = json.load(jsonfile)

with open("sdd.json", "r") as jsonfile:
    my_ponts = json.load(jsonfile)


class MYMIMO(MDFloatLayout):
    '''Implements a material card.'''

    text = StringProperty()


class MY(MDFloatLayout):
    '''Implements a material card.'''

    text = StringProperty()

class MyCard(MDCard):
    '''Implements a material card.'''

    text = StringProperty()
    

class MYMDRelativeLayout(MDRelativeLayout):
    '''Implements a material card.'''

    text = StringProperty()

class Example(MDApp):

    def build(self):
        self.ty = False
        self.btn = len(num) 
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file("pont.kv")
    
    def save(self,root):    
        self.name_mm = root.ids.data.text
        self.date_time = root.ids.pont.text
        if self.ty == True:
            self.root.remove_widget(root)
            self.new_card()
        
    def cancel(self,root):
        self.root.remove_widget(root)

    def on_delet(self,root):

        with open("mimi.json", "r") as jsonfile:
            item = json.load(jsonfile)

        item_removing = item
        self.id = int(root.id) 
        
        self.root.ids.box.remove_widget(root)
        item_removing.remove(item[self.id])
        self.id -= 1
        self.btn -= 1
        self.i -= 1

        with open("mimi.json", "w") as jsonfile:
            json.dump(item_removing, jsonfile,indent=1)
        
    def GREEN(self):
        self.ty = True
        self.teyp = (0.2745098039215686, 0.6470588235294118, 0.5607843137254902, 1)

    def RED(self):
        self.ty = True
        self.teyp = (0.7743055555555556,0.1076388888888889,0.1076388888888889,1)

    def on_start(self):
        self.root.add_widget(MDLabel(text='',pos_hint= {"center_x": .5, "center_y": .87},adaptive_size= True, theme_text_color= "Custom",theme_bg_color= "Custom",md_bg_color=(0.07450980392156863, 0.7803921568627451, 0.5098039215686274, 1),
            text_color= (0, 0, 0,0.85),bold= True,size_hint_x=0.92,size_hint_y=0.15,radius=32))
        self.old = MDLabel(text=f'{my_ponts}',role='small',font_style='Display',pos_hint= {"center_x": .5, "center_y": .86}
            ,adaptive_size= True, theme_text_color= "Custom",
            text_color= (0, 0, 0,0.85),bold= True)
        self.root.add_widget(self.old)
        self.root.add_widget(MDLabel(text='The points',bold= True,role='medium',font_style='Title',pos_hint= {"center_x": .5, "center_y": .91},text_color= (0, 0, 0,0.85),adaptive_size= True, theme_text_color= "Custom"))
        with open("mimi.json", "r") as jsonfile:
            num = json.load(jsonfile)
            self.random_test = num[0]["cards"][0]["time"]
        for self.i in range(self.btn):
            self.root.ids.box.add_widget(MyCard(MYMDRelativeLayout(MDLabel(text=f'{num[self.i]["cards"][0]["time"]}',role='large',font_style='Body',pos_hint= {"center_x": .9, "center_y": .5}
            ,adaptive_size= True, theme_text_color= "Custom",
            text_color= (num[self.i]["cards"][0]["teyp"]),bold= True),MDLabel(text=f'{num[self.i]["cards"][0]["note"]}',role='large',font_style='Body',pos_hint= {"center_x": .5, "center_y": .5})),id=f'{self.i}'))

    def num(self):
        self.root.add_widget(MY())

    def sp(self):
        self.root.add_widget(MYMIMO())

    def spe(self,root):    
        spechel = root.ids.sp.text
        if spechel == '':
            self.root.remove_widget(root)
        else:

            with open("sdd.json", "r") as jsonfile:
                my_ponts = json.load(jsonfile)

            new_pont = int(my_ponts) + int(spechel)

            with open("sdd.json", "w") as jsonfile:
                json.dump(new_pont, jsonfile,indent=1)  
        
            self.old.text = str(new_pont)
            self.root.remove_widget(root)

    def new_card(self):
        with open("mimi.json", "r") as jsonfile:
            num = json.load(jsonfile)
            
        self.new_data= {
            "cards": [{
                "note": self.name_mm,
                "time": self.date_time,
                "teyp": self.teyp
                }]}

        num.append(self.new_data)


        with open("mimi.json", "w") as jsonfile:
            json.dump(num, jsonfile,indent=1)

        self.root.ids.box.add_widget(MyCard(MYMDRelativeLayout(MDLabel(text=f'{num[self.i + 1]["cards"][0]["time"]}',id='pont',role='small',font_style='Title',pos_hint= {"center_x": .9, "center_y": .5}
            ,adaptive_size= True, theme_text_color= "Custom",
            text_color= (num[self.i + 1]["cards"][0]["teyp"]),bold= True),MDLabel(text=f'{num[self.i + 1]["cards"][0]["note"]}',role='large',font_style='Body',pos_hint= {"center_x": .5, "center_y": .5})),id=f'{self.i + 1 }'))
 
    def update_pont(self,root):
        with open("mimi.json", "r") as jsonfile:
            num = json.load(jsonfile)

        with open("sdd.json", "r") as jsonfile:
            my_ponts = json.load(jsonfile)

        pon = root.id
        prix = num[int(pon)]["cards"][0]["time"]
        new_pont = int(my_ponts) + int(prix)

        with open("sdd.json", "w") as jsonfile:
            json.dump(new_pont, jsonfile,indent=1)  
       
        self.old.text = str(new_pont)

        

Example().run()
