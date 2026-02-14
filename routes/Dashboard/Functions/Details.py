
    #   fields = [ "Age", "gender", "weight", "kgs", "Height", 
    # "FT", "Gym", "Protein", "prot_unit", "veg", "noofdays"]
from routes.BMI.Functions import calculator as cal
def Entry(user_data,fields):
    # cal.BMICalulator(weight,w_type,height,h_type)
    bmicalculation=cal.BMICalulator(weight=user_data['weight'],w_type=user_data['Kgs'],
        height=user_data['Height'],h_type=user_data['FT'],required=True)
    enough_protien=protiencalculator(user_data['Protein'],user_data["prot_unit"],bmicalculation["weight"],user_data['Gym'])
    user_data["BMI"]=bmicalculation["BMI"]
    user_data[f"{enough_protien}"]=enough_protien[0]
    user_data[f"{enough_protien}"]=enough_protien[1]
    



def protiencalculator(Protein,prot_type,weight,gym):
            if (prot_type!='grms'):
                    Protein=453.59237*Protein
            if gym=="Yes":
                    grams_of_prot=weight*1.6
            else:
                   grams_of_prot=weight*0.8
            value=(Protein-grams_of_prot)
            if grams_of_prot>Protein:
                       return [False,-value]
            else:
                    return [True,(value)]

