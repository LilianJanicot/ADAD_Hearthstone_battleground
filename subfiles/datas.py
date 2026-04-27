import pandas as pd

compo = pd.read_csv("subfiles/comp.csv", encoding='ISO-8859-1',index_col=0)
card = pd.read_csv("subfiles/card.csv", encoding='ISO-8859-1',index_col=0)
compo_card = pd.read_csv("subfiles/comp_card.csv", encoding='ISO-8859-1',index_col=0)

merged = pd.merge(compo, compo_card, left_on='id', right_on='comp_id', how='inner')

final = pd.merge(merged, card, left_on='card_id', right_on='id', how='inner')

def available(race1,race2,race3,race4,race5):
    not_available = final[((final["race1"]!=race1) & (final["race2"]!=race1)) & ((final["race1"]!=race2) & (final["race2"]!=race2)) & ((final["race1"]!=race3) & (final["race2"]!=race3)) & ((final["race1"]!=race4) & (final["race2"]!=race4)) & ((final["race1"]!=race5) & (final["race2"]!=race5)) & (final["race1"].notnull())]
    not_available_core = not_available[not_available["type"]=="Core"]
    not_available_core_comp_name = not_available_core["comp_name"].unique()
    avaible = final[~final["comp_name"].isin(not_available_core_comp_name)]
    return avaible

def clean_avaible(race1,race2,race3,race4,race5):
    t=available(race1,race2,race3,race4,race5)
    return t[["comp_name","difficulty","Tier","description_short","description_long","card_name","type","rank","race1","race2","effet","enabler","commit"]]

def compo_avaible(data):
    return data[['comp_name',"Tier","difficulty","description_short"]].drop_duplicates(subset='comp_name')

def compo_name_avaible(data):
    return data["comp_name"].unique()

def enabler_commit(data):
    return data[["comp_name","enabler","commit"]].drop_duplicates(subset='comp_name')

def description_long(data,name):
    return data[data["comp_name"]==name][["description_long"]].drop_duplicates(subset='description_long').values[0][0]

def compo_card_avaible(data,name):
    return data[(data["comp_name"]==name)][["card_name","type","rank","race1","race2","effet"]].drop_duplicates(subset='card_name')

