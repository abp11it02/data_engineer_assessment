create table if not exists HOA (
    property_id varchar(50),
    hoa integer,
    hoa_flag varchar(3)
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
    Final_Reviewer varchar(50)
);

create table if not exists property (
    id varchar(50),
    Property_Title varchar(50),
    Address varchar(50),
    Market varchar(50),
    Flood varchar(50),
    Street_Address varchar(50),
    City varchar(50),
    State varchar(50),
    Zip varchar(50),
    Property_Type varchar(50),
    Highway varchar(50),
    Train varchar(50),
    Tax_Rate float,
    SQFT_Basement integer,
    HTW varchar(3),
    Pool varchar(3),
    Commercial varchar(3),
    Water varchar(50),
    Sewage varchar(50),
    Year_Built integer,
    SQFT_MU integer,
    SQFT_Total integer,
    Parking varchar(50),
    Bed integer,
    Bath integer,
    BasementYesNo varchar(3),
    Layout varchar(50),
    Rent_Restricted varchar(50),
    Neighborhood_Rating integer,
    Latitude float,
    Longitude float,
    Subdivision varchar(50),
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
    Trashout_Flag varchar(3)
);


create table if not exists taxes (
    property_id varchar(50),
    taxes integer
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
)