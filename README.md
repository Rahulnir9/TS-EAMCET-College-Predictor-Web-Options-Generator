TS-EAMCET-College-Predictor-Web-Options-Generator
---
Predict your **top engineering colleges and branches** using your EMCET rank, category, gender, and preferences — all powered by Machine Learning.
About the Project
This tool is built to help students make informed decisions during **EMCET counselling** by predicting suitable colleges and branches based on their profile.
Using past years' cutoff data and a trained ML model, the app gives **smart suggestions** tailored to your inputs.
---
 Key Features
College Prediction Based on Your Profile
Input your:
- EMCET Rank
- Category (OC, BC, SC, ST, etc.)
- Gender
- Preferred Branch
Smart Machine Learning Model
Trained using a **Random Forest Classifier** on real historical TSEAMCET counselling data.

Machine Learning Powered
Built using Random Forest Classifier
Trained on real historical TSEAMCET counselling data
Predicts top-fit colleges for your rank and category
Saved encoders (joblib) ensure consistent model performance

Downloadable Results
After prediction, you can download a personalized list of predicted colleges in CSV format
Ideal for offline reference, counselling prep, and parental review

Streamlit Web App
Clean, responsive, and user-friendly UI built with Streamlit

Run locally or deploy to the cloud with minimal setu
After prediction, you can **download your personalized college prediction list** as a **CSV file** — perfect for reference and sharing!  
Clean, simple, and responsive UI built with [Streamlit](https://streamlit.io). Run it locally or deploy it on the cloud. 
Encoders for category, gender, and branches are saved using `joblib` for consistent performance.
---
Machine Learning Details
- Model:Random Forest Classifier  
- Target Variable: College Name  
- Input Features:
  - Closing Rank
  - Gender
  - Category
  - Branch Preference
