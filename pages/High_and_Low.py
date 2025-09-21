import streamlit as st
import random

st.title("High and Low Game!")
qp = st.query_params
round_num = int(qp.get("round", "1"))
current_card= random.randint(1, 13)
st.write(f"Current_Card: {current_card}")
st.write("High か Low かを当ててください。")

if st.button("High"):
    next_card= random.randint(1, 13)
    if next_card > current_card:
        st.success("You Win! ")
        st.write(f"Next_Card: {next_card}")
        current_card = next_card
    elif next_card < current_card:
        st.error("You Lose ")
        st.write(f"Next_Card: {next_card}")
        current_card = next_card
    else:
        st.info("Draw ")
        st.write(f"Next_Card: {next_card}")
        current_card = next_card
    
    if st.button("For next round !"):
        round_num += 1
        st.query_params["round"] = str(round_num)  # URLを更新

elif st.button("Low"):
    next_card= random.randint(1, 13)
    if next_card < current_card:
        st.success("You Win! ")
        st.write(f"Next_Card: {next_card}")
        current_card = next_card

    elif next_card > current_card:
        st.error("You Lose ")
        st.write(f"Next_Card: {next_card}")
        current_card = next_card
    else:
        st.info("Draw ")
        st.write(f"Next_Card: {next_card}")
        current_card = next_card
    
    if st.button("For next round !"):
        round_num += 1
        st.query_params["round"] = str(round_num)  # URLを更新