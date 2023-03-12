import streamlit as st
import numpy as np
import pandas as pd

x = st.checkbox('Show dataframe') # boolean

if x:
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data