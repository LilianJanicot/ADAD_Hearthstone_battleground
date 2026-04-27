import streamlit as st

st.set_page_config(page_title="Hearthstone Battlegrounds", layout="wide")

options = ["Bête","Démon","Dragon","Elémentaire","Huran","Méca","Mort-vivant","Murloc","Naga","Pirate"]
selected_options = st.multiselect("Choississez les 5 races disponibles dans votre partie", options)

if len(selected_options) != 5:
    st.write("Veuillez sélectionner exactement 5 races.")
else:
    from subfiles.datas import clean_avaible, compo_avaible, compo_card_avaible, enabler_commit, compo_name_avaible, description_long
    data = clean_avaible(*selected_options)
    st.write("Voici les compositions disponibles :")
    st.dataframe(compo_avaible(data).sort_values('comp_name').rename(columns={'comp_name': 'Nom de la composition', 'difficulty': 'Difficulté', 'description_short': 'Courte description'}), hide_index=True)
    st.write("Voici les conditions pour jouer une composition :")
    st.dataframe(enabler_commit(data).sort_values('comp_name').rename(columns={'comp_name': 'Nom de la composition', 'enabler': 'Condition pour jouer la composition', 'commit': 'Engagement de la composition'}), hide_index=True)
    st.write("Voici les cartes d'une composition :")
    name = st.selectbox("Choississez une composition", compo_name_avaible(data))
    st.dataframe(compo_card_avaible(data, name).rename(columns={'card_name': 'Nom de la carte', 'type': 'Type', 'rank': 'Rang', 'race1': 'Race 1', 'race2': 'Race 2', 'effet': 'Effet'}), hide_index=True)
    st.write(description_long(data,name))