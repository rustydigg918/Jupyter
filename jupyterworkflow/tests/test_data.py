from jupyterworkflow.data import get_melb_data
import pandas as pd

def test_melb_data():
    data = get_melb_data()
    assert all(data.columns == ['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',
       'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
       'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',
       'Longtitude', 'Regionname', 'Propertycount'])
    #assert isinstance(data.Regionname = pd.object)
    
