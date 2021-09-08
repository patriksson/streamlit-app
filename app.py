import numpy as np
import pandas as ps
import plotly.express as px
import streamlit as st

st.title('Andreas Football app')

# Football app
df = st.cache(ps.read_csv)("FullData.csv")
if st.checkbox('Show dataframe'):
    st.write(df)

'''
This very simple webapp allows you to select and visualize players from certain clubs and certain nationalities.
'''

clubs = st.sidebar.multiselect('Show Player for clubs?', df['Club'].unique())
nationalities = st.sidebar.multiselect('Show Player from Nationalities?', df['Nationality'].unique())
new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
st.write(new_df)
# create figure using plotly express
fig = px.scatter(new_df, x ='Rating',y='Age',color='Name')
# Plot!
'''
### Here is a simple chart between player age and overall
'''
st.plotly_chart(fig)


progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

#for i in range(100):
    # Update progress bar.
    #progress_bar.progress(i)

    #new_rows = np.random.randn(10, 2)

    # Update status text.
    #status_text.text(
        #'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    #chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    #time.sleep(0.1)

#status_text.text('Done!')
#st.balloons()