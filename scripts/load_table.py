import os
import json
import uuid
from mysql.connector import Error

def load_tables(cur):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    filepath = os.path.join(parent_dir, "data", "fake_property_data_new.json")

    # Initialize counters
    counts = {
        'property': 0,
        'leads': 0,
        'HOA': 0,
        'rehab': 0,
        'taxes': 0,
        'valuation': 0
    }

    with open(filepath, 'r') as file:
        properties = json.load(file)

    print("Inserting data into tables...")
    for property in properties:
        id = str(uuid.uuid4())
        # Insert into property table
        property_query = """
        insert into property (id, Property_Title, Address, Market, Flood, Street_Address, City, State, Zip, Property_Type, Highway, Train, Tax_Rate, SQFT_Basement, HTW, Pool, Commercial, Water, Sewage, Year_Built, SQFT_MU, SQFT_Total, Parking, Bed, Bath, BasementYesNo, Layout, Rent_Restricted, Neighborhood_Rating, Latitude, Longitude, Subdivision, School_Average)
        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
            counts['property'] += 1
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
        

        # Load table HOA
        hoa_query = """
        insert into HOA (id, property_id, hoa, hoa_flag) values(%s, %s, %s, %s)
        """

        try:
            for hoa in property.get('HOA'):
                cur.execute(hoa_query, (
                    str(uuid.uuid4()),
                    id,  # Property ID
                    hoa.get('HOA'),
                    hoa.get('HOA_Flag')
                ))
                counts['HOA'] += 1
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
        

        # Load table leads
        leads_query = """
        insert into leads (id, property_id, Most_Recent_Status, Source, Occupancy, Net_Yield, IRR, Selling_Reason, Seller_Retained_Broker, Final_Reviewer) 
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        try:
            cur.execute(leads_query, (
                str(uuid.uuid4()),
                id,  # Property ID
                property.get('Most_Recent_Status'),
                property.get('Source'),
                property.get('Occupancy'),
                property.get('Net_Yield'),
                property.get('IRR'),
                property.get('Selling_Reason'),
                property.get('Seller_Retained_Broker'),
                property.get('Final_Reviewer')
            ))
            counts['leads'] += 1
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
        
        # Load table Rehab
        rehab_query = """
        insert into rehab (id, property_id, Underwriting_Rehab, Rehab_Calculation, Paint, Flooring_Flag, Foundation_Flag, Roof_Flag, HVAC_Flag, Kitchen_Flag, Bathroom_Flag, Appliances_Flag, Windows_Flag, Landscaping_Flag, Trashout_Flag) 
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        try:
            for rehab in property.get('Rehab'):
                cur.execute(rehab_query, (
                    str(uuid.uuid4()),
                    id,  # Property ID
                    rehab.get('Underwriting_Rehab'),
                    rehab.get('Rehab_Calculation'),
                    rehab.get('Paint'),
                    rehab.get('Flooring_Flag'),
                    rehab.get('Foundation_Flag'),
                    rehab.get('Roof_Flag'),
                    rehab.get('HVAC_Flag'),
                    rehab.get('Kitchen_Flag'),
                    rehab.get('Bathroom_Flag'),
                    rehab.get('Appliances_Flag'),
                    rehab.get('Windows_Flag'),
                    rehab.get('Landscaping_Flag'),
                    rehab.get('Trashout_Flag')
                ))
                counts['rehab'] += 1
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

        # Load table Valuation
        valuation_query = """
        insert into valuation (id, property_id, Previous_Rent, List_Price, Zestimate, ARV, Expected_Rent, Rent_Zestimate, Low_FMR, High_FMR, Redfin_Value) 
        values(%s, %s, COALESCE(%s, 0), COALESCE(%s, 0), COALESCE(%s, 0), COALESCE(%s, 0), COALESCE(%s, 0), COALESCE(%s, 0), COALESCE(%s, 0), COALESCE(%s, 0), COALESCE(%s, 0))
        """

        try:
            for valuation in property.get('Valuation'):
                cur.execute(valuation_query, (
                    str(uuid.uuid4()),
                    id,  # Property ID
                    valuation.get('Previous_Rent'),
                    valuation.get('List_Price'),
                    valuation.get('Zestimate'),
                    valuation.get('ARV'),
                    valuation.get('Expected_Rent'),
                    valuation.get('Rent_Zestimate'),
                    valuation.get('Low_FMR'),
                    valuation.get('High_FMR'),
                    valuation.get('Redfin_Value')
                ))
                counts['valuation'] += 1
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

        # Load table taxes
        taxes_query = """
        insert into taxes (id, property_id, taxes) 
        values(%s, %s, COALESCE(%s, 0))
        """

        try:
            cur.execute(taxes_query, (
                str(uuid.uuid4()),
                id,  # Property ID
                property.get('Taxes')
            ))
            counts['taxes'] += 1
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
    # Print Summary
    print(f"Insertion completed!!!")
    print("Insertion Summary: ")
    for table, count in counts.items():
        print(f"{count} records inserted in {table}")
    
    # Verify from database
    for table in counts.keys():
        cur.execute(f"select count(*) from {table}")
        rec_count = cur.fetchone()[0]
        print(f"{table} contains {rec_count} records")
