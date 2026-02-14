
    #   fields = [ "Age", "gender", "weight", "kgs", "Height", 
    # "FT", "Gym", "Protein", "prot_unit", "veg", "noofdays"]
from routes.BMI.Functions import calculator as cal
from routes.Dashboard.Functions.Dataentry import dataEntry
def Entry(user_data,app):
    # cal.BMICalulator(weight,w_type,height,h_type)
    conversion(user_data=user_data)
    bmicalculation=cal.BMICalulator(weight=float(user_data['weight']),
                w_type=user_data['Weight_type'], 
                height=(user_data['height']),
                h_type=user_data['Height_type'], 
                required=True)
    enough_protien=protiencalculator(user_data['Protien'],user_data["Protien_type"],bmicalculation["weight"],user_data['Gym'])
    user_data["BMI"]=bmicalculation["BMI"]
    user_data[f"{enough_protien}"]=enough_protien[0]
    user_data[f"{enough_protien}"]=enough_protien[1]
    Actualdata=dataEntry(userdata=user_data,app=app)


    



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
            

def conversion(user_data):
    user_data['weight'] = float(user_data['weight'])
    user_data['height'] = float(user_data['height'])
    user_data['Protien'] = float(user_data['Protien'])
    user_data['Age'] = int(user_data['Age'])
    user_data['Daysofweek'] = int(user_data['Daysofweek'])

    return user_data


