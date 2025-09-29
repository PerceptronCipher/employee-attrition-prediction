import streamlit as st
import pickle
import pandas as pd

# Page configuration
st.set_page_config(page_title="Employee Attrition Predictor", page_icon="👔", layout="wide")

# Load model
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

st.title("Employee Attrition Prediction System")
st.markdown("Predict the likelihood of an employee leaving based on various factors.")

# Input form
col1, col2 = st.columns(2)

with col1:
    st.subheader("Personal & Job Information")
    age = st.number_input("Age", 18, 65, 30)
    cf_age_band = st.selectbox("Age Band", [0, 1, 2, 3, 4], help="0=Under 25, 1=25-34, 2=35-44, 3=45-54, 4=Over 55")
    business_travel = st.selectbox("Business Travel", [0, 1, 2], help="0=Non-Travel, 1=Travel Rarely, 2=Travel Frequently")
    distance_from_home = st.number_input("Distance From Home (km)", 0, 50, 10)
    education_tech = st.selectbox("Technical Degree?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    over_time = st.selectbox("Works Overtime?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    marital_single = st.selectbox("Single?", [0, 1], format_func=lambda x: "Yes" if x else "No")

with col2:
    st.subheader("Job Details")
    job_level = st.slider("Job Level", 1, 5, 2)
    monthly_income = st.number_input("Monthly Income", 1000, 20000, 5000)
    hourly_rate = st.number_input("Hourly Rate", 30, 100, 65)
    percent_salary_hike = st.number_input("Last Salary Hike (%)", 10, 25, 15)
    years_at_company = st.number_input("Years at Company", 0, 40, 5)
    years_current_role = st.number_input("Years in Current Role", 0, 20, 2)
    years_curr_manager = st.number_input("Years with Current Manager", 0, 20, 2)

st.subheader("Job Roles & Satisfaction")
col3, col4 = st.columns(2)

with col3:
    sales_exec = st.selectbox("Sales Executive?", [0, 1], format_func=lambda x: "Yes" if x else "No")
    lab_tech = st.selectbox("Laboratory Technician?", [0, 1], format_func=lambda x: "Yes" if x else "No")

with col4:
    env_satisfaction = st.slider("Environment Satisfaction", 1, 4, 3)
    job_satisfaction = st.slider("Job Satisfaction", 1, 4, 3)
    relationship_satisfaction = st.slider("Relationship Satisfaction", 1, 4, 3)
    job_involvement = st.slider("Job Involvement", 1, 4, 3)

if st.button("Predict Attrition Risk", type="primary"):
    # Create input in exact order
    input_data = pd.DataFrame([[
        business_travel, env_satisfaction, hourly_rate, distance_from_home,
        education_tech, job_satisfaction, relationship_satisfaction, sales_exec,
        percent_salary_hike, years_curr_manager, over_time, marital_single,
        years_at_company, cf_age_band, years_current_role, monthly_income,
        lab_tech, job_involvement, age
    ]], columns=[
        'Business Travel', 'Environment Satisfaction', 'Hourly Rate', 
        'Distance From Home', 'Education Field_Technical Degree', 
        'Job Satisfaction', 'Relationship Satisfaction', 'Job Role_Sales Executive',
        'Percent Salary Hike', 'Years With Curr Manager', 'Over Time', 
        'Marital Status_Single', 'Years At Company', 'CF_age band', 
        'Years In Current Role', 'Monthly Income', 'Job Role_Laboratory Technician',
        'Job Involvement', 'Age'
    ])
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    
    st.markdown("---")
    col_r1, col_r2 = st.columns(2)
    
    with col_r1:
        if prediction == 1:
            st.error("⚠️ High Risk: Employee likely to leave")
        else:
            st.success("✅ Low Risk: Employee likely to stay")
    
    with col_r2:
        st.metric("Leave Probability", f"{probability[1]*100:.1f}%")
        st.metric("Stay Probability", f"{probability[0]*100:.1f}%")

st.markdown("---")
st.markdown("**Model:** Logistic Regression (Balanced) | **Recall:** 73%")