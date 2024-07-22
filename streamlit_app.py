# Streamlit Operations by Age 

# Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Settings
st.set_page_config(layout="wide")


# Data

df = pd.read_excel("data.xlsx")

# Title columns
col1,col2,col3,col4,col5,col6= st.columns(6)


with col1:
	st.image("HACA 24 Logo. Colour.png")
	
with col6:
	st.image("WorcsAcute logo.png")

col10,col11,col12 = st.columns(3)

with col11:
	st.title("Operations by Age")	






# Introduction
st.subheader("**Introduction**")

st.write("This project looked to investigate the frequency of common operations by age and sex for patients undergoing surgery over a 10 year period at a District General Hospital.")
st.write("300,000 anonymised records, with information on age, sex and operation name was extracted from a theatre management system. Using the Pandas library from the Python programming language, common operations were grouped and given generic operation names. Each operation was counted with reference to specific age and sex so that a ranked order of the 10 most common operations for a given age and sex was ascertained and plotted by operation name.")


# Selection Values

#Operation names
ops = sorted(df["Operation"].unique())



# Operation Selection

st.subheader("Operation selection")

#with st.form("Select variables"):
	
ops_select = st.selectbox("Operation name",ops)

	#st.form_submit_button('Submit')


# The Graphs
fig,ax = plt.subplots(figsize=(12,5))
 
# The Data
ops_order_male = df.loc[ (df["Operation"]==ops_select) & (df["Sex"]=="Male"),"Order"]
ops_age_male   = df.loc[ (df["Operation"]==ops_select) & (df["Sex"]=="Male"),"Age"]

ops_order_female = df.loc[ (df["Operation"]==ops_select) & (df["Sex"]=="Female"),"Order"]
ops_age_female   = df.loc[ (df["Operation"]==ops_select) & (df["Sex"]=="Female"),"Age"]
 
# Scatter Plot
ax.scatter(ops_age_male, ops_order_male,marker="2",label="Male",s=150,c="blue")
ax.scatter(ops_age_female, ops_order_female, marker="1",label="Female",s=150,c="red")
 
# Label the Plot
ax.set(xlabel="Age (years)",ylabel="Rank")
ax.set_title(f"{ops_select}",fontsize=15,fontweight='bold')
ax.legend(loc=0)
 
# Formatting the plot
ax.set(xlim=(0,100),ylim=(0,11))
ax.set_xticks(ticks= range(0,101,10))
ax.set_xticks(ticks= range(0,101,2),minor=True)
ax.set_yticks(ticks= range(1,11))
ax.spines[['top','right','left']].set_visible(False)
 
ax.grid(axis='y')
 
plt.tight_layout()
plt.gca().invert_yaxis()

st.pyplot(fig)



# Results

st.subheader("Results")
st.write("From an initial dataset of 298,868 records, 4,634 unique operations were identified. 49.3% of these had a count of 5 or less showing a large number of individually named operations. After data cleaning, the number of unique operations reduced by 32% as there are many related operations with different operation names. This is also seen by the number of records of the top 100 unique operations increasing by 70% from 165,485 to 235,141.")

st.write("**Examples of operation types that been grouped together are:**")

col15,col20, col25 = st.columns(3)

with col15:
	st.write("**• hernia repair** (repair of a weak point that leads to bulging of an organ)")
	st.write("**• hysteroscopy operations** (visualisation of the uterus).")
	st.write("**• excision of lesion operations** (any superficial abnormal tissue on the body).")

with col20:
	st.image("before_1.png")

with col25:
	st.image("after_1.png")

st.write("The final dataset to be plotted contained 79 unique operations for Males (56,852 records, 45% original male dataset) and 83 unique operations for Females (90,105 records, 53% original female dataset).")

col30,col35,col40 = st.columns(3)

with col30:
	st.image("heatmap_male.jpg")

with col35:
	st.image("heatmap_female.jpg")

with col40:
	st.write("This heatmap shows the number of records by age and rank of the final dataset. \n - For both male and female patients there is a significant concentration of records at higher ages (65-90 years). \n - There is a low concentration at lower ages and at lower ranks.")



# Conclusion

st.subheader("Conclusion")

st.write("This project has found many common operations that have a clear pattern of distribution with a patients age and sex. These patterns are determined by variations in a persons lifestyle, health, frailty and disease processes as we age.")

st.write("At a **younger age**, the build up of fluid behind the ear is common, requiring drainage with the insertion of grommets.")
st.write("In **middle age**, the accumulation of cholesterol is more common in females, obesity and recent weight loss. It has an overall prevalence of 15% of all adults and this reaches its peak at 50 to 54 years.")
st.write("In our **later years**, as we age the osteoarthritis is more prevalent causing inflammation and damage within our joints such as the hip. This can result in pain and stiffness requiring the joint to be replacement. The elderly population are particularly vulnerable to hip fractures from simple falls, this is often multifactorial but age related reduced bone mineral density is a key factor, occurring earlier in females than males due to the decline of oestrogen from the onset of menopause.") 


# Author information

st.subheader("Author Information")

st.write("**Dr David Freeman**")
st.write("david.freeman5@nhs.net")
st.write("**Worcestershire Acute Hospitals NHS Trust**")





