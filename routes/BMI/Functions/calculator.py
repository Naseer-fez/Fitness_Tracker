def BMICalulator(weight,w_type,height,h_type):
    weight = float(weight)
    height = float(height)
    if h_type=="Inc":
        height=height*2.54
    if w_type=="lbs":
        weight=weight*0.45359
    height=height/100
    BMI=(weight/height**2)
    return round(BMI,2)


if __name__=="__main__":
    a=BMICalulator(70,"kgs",160,"cms")
    print(a)