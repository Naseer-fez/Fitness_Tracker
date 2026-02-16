def BMICalulator(weight,w_type,height,h_type,required=None):
    weight = float(weight)
    height = float(height)
    if h_type=="Inc":
        height=height*2.54
    if w_type=="lbs":
        weight=weight*0.45359
    height=height/100
    BMI=(weight/height**2)
    data=get_bmi_code(BMI)
    if required==None:
        return [round(BMI,2),data]
    if required!=None:  
        return {"BMI":round(BMI,2),"Category":data,"weight":weight,"height":height}
def get_bmi_code(bmi):
    if bmi < 18.5:
        return "Underweight"  # Underweight
    if bmi < 25.0:
        return "Healthy Weight"  # Healthy Weight
    if bmi < 30.0:
        return "Overweight"  # Overweight
    if bmi < 35.0:
        return "Obese 1"  # Obese Class 1
    return "Obese 2"      # Obese Class 2+


# 1	Underweight	Below 18.5
# 2	Healthy Weight	18.5 – 24.9
# 3	Overweight	25.0 – 29.9
# 4	Obese (Class I)	30.0 – 34.9
# 5	Severely Obese (Class II/III)	35.0 or higher

if __name__=="__main__":
    a=BMICalulator(70,"kgs",160,"cms")
    print(a)