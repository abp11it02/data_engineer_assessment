create table if not exists HOA (
    property_id varchar(50),
    hoa integer,
    hoa_flag varchar(3),
    FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE
);

create table if not exists leads (
    property_id varchar(50),
    Most_Recent_Status varchar(50),
    Source varchar(50),
    Occupancy varchar(50),
    Net_Yield float,
    IRR float,
    Selling_Reason varchar(50),
    Seller_Retained_Broker varchar(50),
    Final_Reviewer varchar(50),
    FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE
);

create table if not exists property (
    id varchar(50) primary key,
    Property_Title varchar(255),
    Address varchar(255),
    Market varchar(100),
    Flood varchar(100),
    Street_Address varchar(255),
    City varchar(100),
    State varchar(50),
    Zip varchar(20),
    Property_Type varchar(100),
    Highway varchar(100),
    Train varchar(100),
    Tax_Rate float,
    SQFT_Basement integer,
    HTW varchar(3),
    Pool varchar(3),
    Commercial varchar(3),
    Water varchar(100),
    Sewage varchar(100),
    Year_Built integer,
    SQFT_MU integer,
    SQFT_Total varchar(50),
    Parking varchar(100),
    Bed integer,
    Bath integer,
    BasementYesNo varchar(3),
    Layout varchar(100),
    Rent_Restricted varchar(100),
    Neighborhood_Rating integer,
    Latitude float,
    Longitude float,
    Subdivision varchar(100),
    School_Average float
);

create table if not exists rehab (
    property_id varchar(50),
    Underwriting_Rehab integer,
    Rehab_Calculation integer,
    Paint varchar(3),
    Flooring_Flag varchar(3),
    Foundation_Flag varchar(3),
    Roof_Flag varchar(3),
    HVAC_Flag varchar(3),
    Kitchen_Flag varchar(3),
    Bathroom_Flag varchar(3),
    Appliances_Flag varchar(3),
    Windows_Flag varchar(3),
    Landscaping_Flag varchar(3),
    Trashout_Flag varchar(3),
    FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE
);


create table if not exists taxes (
    property_id varchar(50),
    taxes integer,
    FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE
);

create table if not exists valuation (
    property_id varchar(50),
    Previous_Rent integer,
    List_Price integer,
    Zestimate integer,
    ARV integer,
    Expected_Rent integer,
    Rent_Zestimate integer,
    Low_FMR integer,
    High_FMR integer,
    Redfin_Value integer,
    FOREIGN KEY (property_id) REFERENCES property(id) ON DELETE CASCADE
);