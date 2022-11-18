import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('Model/model.pkl', 'rb'))

def get_form_data(data):

    feature_values = {
                         'LotArea': 0,
                         'OverallQual': 0,
                         'OverallCond': 0,
                         'YearBuilt': 0,
                         'YearRemodAdd': 0,
                         'BsmtFinSF1': 0,
                         'TotalBsmtSF': 0,
                         '1stFlrSF': 0,
                         '2ndFlrSF': 0,
                         'GrLivArea': 0,
                         'BsmtFullBath': 0,
                         'Fireplaces': 0,
                         'GarageYrBlt': 0,
                         'GarageCars': 0,
                         'GarageArea': 0,
                         'OpenPorchSF': 0,
                         'MSZoning_RM': 0,
                         'LandCon': 0,
                         'tour_HLS': 0,
                         'LandContour_Lvl': 0,
                         'LotConfig_FR2': 0,
                         'Neighborhood_Crawfor': 0,
                         'Neighborhood_NWAmes': 0,
                         'Neighborhood_StoneBr': 0,
                         'Condition1_Norm': 0,
                         'Condition1_RRAe': 0,
                         'BldgType_2fmCon': 0,
                         'BldgType_Duplex': 0,
                         'Exterior1st_BrkComm': 0,
                         'Exterior1st_BrkFace': 0,
                         'Exterio': 0,
                         'r1st_HdBoard': 0,
                         'Exterior2nd_CmentBd': 0,
                         'MasVnrType_BrkFace': 0,
                         'MasVnrType_Stone': 0,
                         'ExterQual_TA': 0,
                         'ExterCond_Fa': 0,
                         'BsmtQual_Fa': 0,
                         'BsmtQual_Gd': 0,
                         'BsmtQual_TA': 0,
                         'BsmtExposure_Gd': 0,
                         'BsmtFinType1_GLQ': 0,
                         'CentralAir_Y': 0,
                         'KitchenQual_Gd': 0,
                         'KitchenQual_TA': 0,
                         'Functional_Mod': 0,
                         'Functional_Sev': 0,
                         'Functional_Typ': 0,
                         'SaleType_ConLD': 0,
                         'SaleType_New': 0,
                         'SaleCondition_Family': 0,
    }

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values

def predict(data):

    values = get_form_data(data)

    order = ['LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'BsmtFinSF1', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'BsmtFullBath', 'Fireplaces', 'GarageYrBlt', 'GarageCars', 'GarageArea', 'OpenPorchSF',
             'MSZoning_RM', 'LandContour_HLS', 'LandContour_Lvl', 'LotConfig_FR2', 'Neighborhood_Crawfor', 'Neighborhood_NWAmes', 'Neighborhood_StoneBr', 'Condition1_Norm', 'Condition1_RRAe', 'BldgType_2fmCon', 'BldgType_Duplex', 'Exterior1st_BrkComm',
             'Exterior1st_BrkFace', 'Exterior1st_HdBoard', 'Exterior2nd_CmentBd', 'MasVnrType_BrkFace', 'MasVnrType_Stone', 'ExterQual_TA', 'ExterCond_Fa', 'BsmtQual_Fa', 'BsmtQual_Gd', 'BsmtQual_TA', 'BsmtExposure_Gd', 'BsmtFinType1_GLQ', 'CentralAir_Y',
             'KitchenQual_Gd', 'KitchenQual_TA', 'Functional_Mod', 'Functional_Sev', 'Functional_Typ', 'SaleType_ConLD', 'SaleType_New', 'SaleCondition_Family']

    values = np.array([values[feature] for feature in order], dtype=object)
    values = pd.DataFrame(data.reshape(1,-1), columns=order)

    pred = model.predict(values)

    return pred
