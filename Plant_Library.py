import json

with open("plantdata.json","r") as plant_data:
    plant_dictionary = json.load(plant_data)

print("\nWelcome to the Plant Dictionary" "\nType 'exit' to end this chat" "\nSearch for a Plant or ask for the Plant List")

plant_dictionary = {
    "Orchid": {
    "Light":"Bright, Indirect",
    "Potting Mix":"Special Orchid Mix",
    "Watering":"Every 7-10 Days",
    "Temperature":"65-85",
    "Humidity":"Moderate to High"
    },
    "Monstera": {
    "Light":"Bright, Indirect",
    "Potting Mix":"Well Draining",
    "Watering":"When Top 2 Inches are Dry",
    "Temperature":"65-85",
    "Humidity":"Moderate to High"
    },
    "Snake Plant": {
    "Light":"Low to Bright, Indirect",
    "Potting Mix":"Cactus or Succulent Mix",
    "Watering":"Every 2-3 Weeks",
    "Temperature":"60-85",
    "Humidity":"Low to Average"
    },
    "Peace Lily": {
    "Light":"Low to Medium",
    "Potting Mix":"Rich Well Draining",
    "Watering":"Keep Soil Consistently Moist",
    "Temperature":"65-80",
    "Humidity":"High",
    "Note":"Droops When Thirsty, Sensitive to Fluoride"
    },
    "Fiddle Leaf Fig": {
    "Light":"Bright, Indirect",
    "Potting Mix":"Light, Well Draining Mix",
    "Watering":"Weekly",
    "Temperature":"60-75",
    "Humidity":"Moderate to High"
    },
    "Pothos": {
    "Light":"Low to Bright, Indirect",
    "Potting Mix":"All Purpose Indoor Mix",
    "Watering":"Weekly",
    "Temperature":"60-85",
    "Humidity":"Average"
    },
}


plant_List = ["Fiddle Leaf Fig", "Monstera", "Orchid", "Peace Lily", "Pothos", "Snake PLant"]

while True:
    plant_name = input("\nPlant Name: ").title()
    if plant_name == "Exit":
        print("\nGoodbye! Thanks for Playing!\n")
        break  
    if plant_name == "Plant List":
        print(plant_List)
        continue   
    if plant_name in plant_dictionary:
        print("\nCare requirements for " + plant_name + ":")
        plant = plant_dictionary[plant_name]
        for key in plant:
            print(key + ": " + plant[key])
    else:
        print("\nSorry we do not have information on " + plant_name.title() + " at this time.\nPlease add details below.\n")
        new_light = input("Light:")
        new_mix = input("Potting Mix:")
        new_water = input("Watering Frequency:")
        new_temp = input("Temperature:")
        new_humid = input("Humidity:")
        plant_dictionary[plant_name] = {
            "Light":new_light,
            "Potting Mix":new_mix,
            "Watering":new_water,
            "Temperature":new_temp,
            "Humidity":new_humid
             }
        
        with open("plantdata.json", "w") as plant_data:
            json.dump(plant_dictionary, plant_data)
        plant_List.append(plant_name)
