from customtkinter import *
from PIL import Image, ImageTk
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

model=KNeighborsClassifier(n_neighbors=3)
data=pd.read_csv("diabetes.csv")
data.dropna()
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.33, random_state=42)
model.fit(x_train,y_train)

background="#003161"
window=CTk()
window.resizable(False,False)
window.geometry("700x500+200+100")
window.title("Diabetes Detection")
set_appearance_mode("dark")
window.configure(fg_color=background)

CTkLabel(window,text="DIABETES DETECTION USING ML\t\t",width=1000,height=50,font=("Cooper Black",20,"bold"),text_color="#000B58",fg_color="#fff").place(x=0,y=26)
logo_image = CTkLabel(window, text="")
logo_img = Image.open("health_icon.png")
logo_img = logo_img.resize((100, 100), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
logo_image.configure(image=logo_photo)
logo_image.image = logo_photo
logo_image.place(x=60, y=0)

class Home:
    def __init__(self):
        def method(i):
            b1.destroy()
            b2.destroy()
            b3.destroy()
            l1.destroy()
            l2.destroy()
            l3.destroy()
            if i == "detection":
                d1 = Detection()
            if i == "bmi":
                d1 = BMI()
            if i == "pedigree":
                d1 = Pedigree()

        # Replace ImageTk.PhotoImage with CTkImage for buttons
        img1 = CTkImage(light_image=Image.open("detect.png"), size=(100, 100))
        b1 = CTkButton(window, text="", image=img1, command=lambda: method("detection"))
        b1.place(x=100, y=130)
        l1 = CTkLabel(window, text="Detection", font=("Times New Roman", 25, "bold"))
        l1.place(x=120, y=245)

        img2 = CTkImage(light_image=Image.open("BMI.png"), size=(100, 100))
        b2 = CTkButton(window, text="", image=img2, command=lambda: method("bmi"))
        b2.place(x=450, y=130)
        l2 = CTkLabel(window, text="BMI Calculator", font=("Times New Roman", 25, "bold"))
        l2.place(x=450, y=245)

        img3 = CTkImage(light_image=Image.open("Pedigree.png"), size=(100, 100))
        b3 = CTkButton(window, text="", image=img3, command=lambda: method("pedigree"))
        b3.place(x=270, y=300)
        l3 = CTkLabel(window, text="Diabetes Pedigree Calculator", font=("Times New Roman", 25, "bold"))
        l3.place(x=200, y=415)


class Detection:
     def __init__(self):
        window.geometry("800x500+200+100")
        frame=CTkFrame(window,width=800,height=500,fg_color=background)
        frame.place(x=0,y=100)
        CTkLabel(frame,text="Fill the below Details",font=("Times New Roman",20,"bold"),text_color="#fff").place(x=270,y=0)
        entries=[]
        fields = [
            ("Pregnancies", "Example: 2 (0-17)"),
            ("Glucose", "Example: 120 (70-200 mg/dL)"),
            ("BloodPressure", "Example: 80 (40-140 mmHg)"),
            ("SkinThickness", "Example: 20 (0-99 mm)"),
            ("Insulin", "Example: 100 (0-846 µU/mL)"),
            ("BMI", "Example: 30.5 (18.5-50.0)"),
            ("DiabetesPedigreeFunction", "Example: 0.5 (0.0-2.5)"),
            ("Age", "Example: 30 (21-81)")
        ]
        for i in fields:
            CTkLabel(frame,text=i[0],font=("Times New Roman",15,"bold"),text_color="#fff").place(x=100,y=fields.index(i)*40+50)
            entry=CTkEntry(frame,placeholder_text=i[1],text_color="#fff")
            entry.place(x=300,y=fields.index(i)*40+50)
            entries.append(entry)
            
        def click():
            try:
                entry_values=[float(i.get()) for i in entries]
                prediction=model.predict([entry_values])
                if prediction == 1:
                    result_text = "⚠️ High risk of Diabetes ⚠️"
                    result_color = "red"
                else:
                    result_text = "✅ Low risk of Diabetes ✅"
                    result_color = "green"
                CTkLabel(frame,text=result_text,text_color=result_color,font=("Times New Roman",20,"bold")).place(x=500,y=200)
            except:
                CTkLabel(frame,text="Enter Valid values",text_color="red",font=("Times New Roman",20,"bold")).place(x=500,y=200)
        def back():
            frame.destroy()
            window.geometry("700x500+200+100")
            s1=Home()
        
        def show_help():
            # Create a new top-level window for the help section
            help_window = CTkToplevel()
            help_window.resizable(0,0)
            help_window.title("Input Parameter Specifications")
            help_window.geometry("1100x600+200+10")
            b2.configure(state="disabled")
            
            # Add a label for the title in the help window
            help_title_label = CTkLabel(help_window, text="Input Parameter Specifications", font=("Arial", 18, "bold"), text_color="#fff")
            help_title_label.pack(pady=10)
    
            # Detailed help content for each parameter
            help_text = (
                "Pregnancies:\n"
                "This refers to the number of times the patient has been pregnant. A higher number of pregnancies \n"
                "is often associated with a greater risk of developing diabetes, as pregnancy can lead to changes in insulin sensitivity.\n"
                "If you're unsure of the number, check medical history or consult with your doctor.\n\n"
    
                "Glucose:\n"
                "Glucose levels reflect the amount of sugar in your blood. High blood glucose levels can indicate impaired insulin function.\n"
                "For accurate readings, a glucose test is typically done after fasting for 8-12 hours. Normal levels range between 70-100 mg/dL.\n\n"
    
                "Blood Pressure:\n"
                "This measures the pressure in your arteries during the resting and contracting phases of your heartbeat.\n"
                "Higher blood pressure can strain the cardiovascular system and may be associated with metabolic issues like diabetes.\n"
                "A normal reading is around 80 mmHg for diastolic pressure.\n\n"
    
                "Skin Thickness:\n"
                "The skinfold thickness measures subcutaneous fat and is linked to body fat percentage.\n"
                "Abnormal skin thickness values can indicate poor fat distribution or metabolic irregularities.\n This is typically measured by a healthcare provider using calipers.\n\n"
    
                "Insulin:\n"
                "Insulin levels indicate how much insulin your body is producing. \nIf your body isn't making enough insulin or isn't using it effectively, "
                "it could lead to diabetes. Normal levels after fasting are typically between 2.6-24.9 µU/mL.\n\n"
    
                "BMI (Body Mass Index):\n"
                "BMI is a ratio of your weight to height and is a measure of body fat. A BMI over 25 indicates overweight, \n"
                "and a BMI over 30 suggests obesity, both of which increase the risk of diabetes. \nYou can calculate it as weight (kg) / (height (m))^2.\n\n"
    
                "Diabetes Pedigree Function:\n"
                "This is a function that reflects the genetic contribution to diabetes. \nA higher value indicates a greater risk due to family history.\n\n"
    
                "Age:\n"
                "Older individuals are generally at higher risk for diabetes, especially in individuals with risk factors. "
                "Make sure to accurately represent your age to get precise predictions."
            )
    
            # Add help text to the help window
            help_label = CTkLabel(help_window, text=help_text, font=("Arial", 12), text_color="#fff", anchor="w", justify="left")
            help_label.pack(pady=20, padx=20)
            def close():
                b2.configure(state="normal")
                help_window.destroy()
            help_window.protocol("WM_DELETE_WINDOW",close)
        b1=CTkButton(frame, text="Predict",font=("Times New Roman",20,"bold"),command=click)
        b1.place(x=500,y=100)
        b2=CTkButton(frame, text="Parameters?",font=("Times New Roman",20,"bold"),command=show_help)
        b2.place(x=500,y=50)
        b3=CTkButton(frame, text="Home",font=("Times New Roman",20,"bold"),command=back)
        b3.place(x=500,y=0)



class BMI:
        window.geometry("800x500+200+100")
        frame=CTkFrame(window,width=800,height=500,fg_color=background)
        frame.place(x=0,y=100)
        CTkLabel(frame,text="Body Mass Index Calculator",font=("Times New Roman",20,"bold")).place(x=300,y=10)
        img1=CTkImage(light_image=Image.open("BMI2.png"),size=(250, 250))
        b1=CTkLabel(frame,text="",image=img1)
        b1.place(x=0,y=140)
        tabs=CTkTabview(frame,fg_color=background,segmented_button_fg_color=background,segmented_button_selected_hover_color="red",segmented_button_unselected_hover_color="red")
        tabs.place(x=400,y=50)
        tabs.add("Inches")
        tabs.add("centimeters")
        def calculate(a):
            if a=="inches":
                height=float(e1.get())
                weight=float(e2.get())
                BMI=(weight/(height**2))*703
                CTkLabel(tabs.tab("Inches"),text="BMI = {:.2f}".format(BMI),font=("Times New Roman",17,"bold")).place(x=70,y=150)
            elif a=="centimeters":
                height=float(e3.get())
                weight=float(e4.get())
                BMI=weight/((height/100)**2)
                CTkLabel(tabs.tab("centimeters"),text="BMI = {:.2f}".format(BMI),font=("Times New Roman",17,"bold")).place(x=70,y=150)
        CTkLabel(tabs.tab("Inches"),text="Height",font=("Times New Roman",17,"bold")).place(x=0,y=0)
        e1=CTkEntry(tabs.tab("Inches"),placeholder_text="Enter height in inches")
        e1.place(x=100,y=0)
        CTkLabel(tabs.tab("Inches"),text="Weight",font=("Times New Roman",17,"bold")).place(x=0,y=50)
        e2=CTkEntry(tabs.tab("Inches"),placeholder_text="Enter weight in lbs")
        e2.place(x=100,y=50)
        CTkButton(tabs.tab("Inches"),text="Calculate",font=("Times New Roman",17,"bold"),command=lambda:calculate("inches")).place(x=50,y=100)
        CTkLabel(tabs.tab("centimeters"),text="Height",font=("Times New Roman",17,"bold")).place(x=0,y=0)
        e3=CTkEntry(tabs.tab("centimeters"),placeholder_text="Enter height in centimeters")
        e3.place(x=100,y=0)
        CTkLabel(tabs.tab("centimeters"),text="Weight",font=("Times New Roman",17,"bold")).place(x=0,y=50)
        e4=CTkEntry(tabs.tab("centimeters"),placeholder_text="Enter weight in kgs")
        e4.place(x=100,y=50)
        CTkButton(tabs.tab("centimeters"),text="Calculate",font=("Times New Roman",17,"bold"),command=lambda:calculate("centimeters")).place(x=50,y=100)
        def home():
            frame.destroy()
            window.geometry("700x500+200+100")
            s1=Home()
        CTkButton(frame,text="Home",font=("Times New Roman",17,"bold"),command=home).place(x=50,y=10)


class Pedigree:
     def __init__(self):
        window.geometry("800x500+200+100")
        frame=CTkFrame(window,width=800,height=500,fg_color=background)
        frame.place(x=0,y=100)
        CTkLabel(frame,text="Pedigree Function Calculator",font=("Times New Roman",20,"bold")).place(x=300,y=10)
        img1=CTkImage(light_image=Image.open("Pedigree_hierarchy.png"),size=(250, 250))
        b1=CTkLabel(frame,text="",image=img1)
        b1.place(x=10,y=140)
        CTkLabel(frame,text="Does your parents have Diabetes: ",font=("Times New Roman",17,"bold")).place(x=300,y=100)
        optionmenu = CTkOptionMenu(frame, values=["None","Single parent", "Both"])
        optionmenu.place(x=600,y=100)
        CTkLabel(frame,text="How many Siblings have diabetes: \n(0 if none)",font=("Times New Roman",17,"bold")).place(x=300,y=150)
        e1=CTkEntry(frame,placeholder_text="Enter Here")
        e1.place(x=600,y=150)
        CTkLabel(frame,text="How many people other than above \nhave diabetes: (0 if none)",font=("Times New Roman",17,"bold")).place(x=300,y=200)
        e2=CTkEntry(frame,placeholder_text="Enter Here")
        e2.place(x=600,y=200)
        def back():
            frame.destroy()
            window.geometry("700x500+200+100")
            s1=Home()
        b3=CTkButton(frame, text="Home",font=("Times New Roman",20,"bold"),command=back)
        b3.place(x=100,y=0)
        def calculate():
            parent=float(0 if optionmenu.get()=="None" else 1 if optionmenu.get()=="Single parent" else 2)*0.5
            sibling=float(e1.get())*0.3
            others=float(e2.get())*0.2
            CTkLabel(frame,text="Diabetes Pedigree Function = {:.2f}".format(parent+sibling+others),font=("Times New Roman",17,"bold")).place(x=400,y=300)
        CTkButton(frame,text="Calculate",font=("Times New Roman",17,"bold"),command=calculate).place(x=500,y=250)
s1 = Home()
window.mainloop()

