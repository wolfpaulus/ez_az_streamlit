"""
    Easy Azure Streamlit Demo
    Author: Wolf Paulus
"""
from random import randint
import streamlit as st

def ui(items: [int])->None: 
    
    st.title("Streamlit Demo")
    st.subheader(".. on Azure")
    st.line_chart(items)


if __name__ == "__main__":
    data = [randint(0,10) for _ in range(25)]
    ui(data)

