import os
import json
import uuid
from mysql.connector import Error

def load_tables(cur):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    filepath = os.path.join(parent_dir, "data", "fake_property_data_new.json")

    with open(filepath, 'r') as file:
        properties = json.load(file)

    for property in properties:
        id = str(uuid.uuid4())
        # Insert into property table
        property_query = """
        INSERT INTO property (id, Property_Title, Address, Market, Flood, Street_Address, City, State, Zip, Property_Type, Highway, Train, Tax_Rate, SQFT_Basement, HTW, Pool, Commercial, Water, Sewage, Year_Built, SQFT_MU, SQFT_Total, Parking, Bed, Bath, BasementYesNo, Layout, Rent_Restricted, Neighborhood_Rating, Latitude, Longitude, Subdivision, School_Average)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cur.execute(property_query, (
                id,
                property.get('Property_Title'),
                property.get('Address'),
                property.get('Market'),
                property.get('Flood'),
                property.get('Street_Address'),
                property.get('City'),
                property.get('State'),
                property.get('Zip'),
                property.get('Property_Type'),
                property.get('Highway'),
                property.get('Train'),
                property.get('Tax_Rate'),
                property.get('SQFT_Basement'),
                property.get('HTW'),
                property.get('Pool'),
                property.get('Commercial'),
                property.get('Water'),
                property.get('Sewage'),
                property.get('Year_Built'),
                property.get('SQFT_MU'),
                property.get('SQFT_Total'),
                property.get('Parking'),
                property.get('Bed'),
                property.get('Bath'),
                property.get('BasementYesNo'),
                property.get('Layout'),
                property.get('Rent_Restricted'),
                property.get('Neighborhood_Rating'),
                property.get('Latitude'),
                property.get('Longitude'),
                property.get('Subdivision'),
                property.get('School_Average')
            ))
        except Error as e:
            print(f"Error connecting to MySQL: {e}")