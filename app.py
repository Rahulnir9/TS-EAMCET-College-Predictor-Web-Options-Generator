
import streamlit as st
import pandas as pd
import joblib

# Load saved model and encoders
model = joblib.load("emcet_college_predictor_model.pkl")
le_category = joblib.load("le_category.pkl")
le_gender = joblib.load("le_gender.pkl")
le_branch = joblib.load("le_branch.pkl")
le_college = joblib.load("le_college.pkl")

# Load data
df = pd.read_csv(r"C:\Users\rahul\Downloads\all_years_combined.csv", low_memory=False)

# Clean up text fields
df['Place'] = df['Place'].astype(str).str.upper()
df['Branch Name'] = df['Branch Name'].astype(str)

# Branch generalization mapping
branch_mapping = {
    'COMPUTER SCIENCE AND ENGINEERING': 'CSE',
    'COMPUTER SCIENCE AND ENGINEERING (DATA SCIENCE)': 'CSE-DS',
    'COMPUTER SCIENCE AND ENGINEERING (ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING)': 'CSE-AIML',
    'ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING': 'CSE-AIML',
    'INFORMATION TECHNOLOGY': 'IT',
    'ELECTRONICS AND COMMUNICATION ENGINEERING': 'ECE',
    'ELECTRICAL AND ELECTRONICS ENGINEERING': 'EEE',
    'MECHANICAL ENGINEERING': 'MECH',
    'CIVIL ENGINEERING': 'CIVIL',
    'BIO-TECHNOLOGY': 'BT',
    'BIO-MEDICAL ENGINEERING': 'BME',
    'ELECTRONICS AND COMPUTER ENGINEERING': 'ECE',
    'ELECTRONICS AND TELEMATICS': 'ECE',
    # Add more mappings if needed
}

# Standardize and map general_branch
df['Branch Name Clean'] = df['Branch Name'].str.replace('\n', ' ', regex=True).str.upper().str.strip()
df['general_branch'] = df['Branch Name Clean'].map(branch_mapping).fillna('OTHER')

# --- Streamlit UI ---
st.set_page_config("TSEAMCET Predictor", layout="wide")
st.title("🎓 Telangana EAMCET College Predictor + Web Options Generator")

# Inputs
rank = st.number_input("Enter your EAMCET Rank:", min_value=1, max_value=200000, step=1)
category = st.selectbox("Select your Category:", le_category.classes_)
gender = st.selectbox("Select Gender:", le_gender.classes_)
branch = st.selectbox("Select Preferred Branch:", le_branch.classes_)

if st.button("🔍 Predict College & Generate Options"):
    try:
        # Prepare input sample
        sample = [[
            rank,
            le_category.transform([category])[0],
            le_gender.transform([gender])[0],
            le_branch.transform([branch])[0]
        ]]
        
        # Predict
        predicted_college = model.predict(sample)
        predicted_college_name = le_college.inverse_transform(predicted_college)[0]
        st.success(f"🎯 Predicted College: **{predicted_college_name}**")

        # 🎯 Generate realistic web options
        st.markdown("### 📋 Suggested Web Options Based on Your Inputs")
        options_df = df[
            (df["Category"] == category) &
            (df["Gender"] == gender) &
            (df["Branch Name"] == branch) &
            (df["Closing Rank"].astype(float) >= rank)
        ][["Institute Name", "Place", "Closing Rank"]].sort_values(by="Closing Rank").drop_duplicates()

        if not options_df.empty:
            st.dataframe(options_df.reset_index(drop=True), use_container_width=True)
        else:
            st.warning("No colleges found matching your criteria. Try other branches or categories.")

    except Exception as e:
        st.error(f"Error: {e}")
