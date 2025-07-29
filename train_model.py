import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load your cleaned dataset
df = pd.read_csv(r"C:\Users\rahul\Downloads\all_years_combined.csv", low_memory=False)

# Keep necessary columns and drop missing values
df = df[["Closing Rank", "Category", "Gender", "Branch Name", "Institute Name"]].dropna()

# Sample a smaller subset to reduce memory usage
df = df.sample(n=25000, random_state=42)

# Encode categorical variables
le_category = LabelEncoder()
le_gender = LabelEncoder()
le_branch = LabelEncoder()
le_college = LabelEncoder()

df["category_encoded"] = le_category.fit_transform(df["Category"])
df["gender_encoded"] = le_gender.fit_transform(df["Gender"])
df["branch_encoded"] = le_branch.fit_transform(df["Branch Name"])
df["college_encoded"] = le_college.fit_transform(df["Institute Name"])

# Features and target
X = df[["Closing Rank", "category_encoded", "gender_encoded", "branch_encoded"]].astype(float)
y = df["college_encoded"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a lighter Random Forest model
model = RandomForestClassifier(n_estimators=20, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "emcet_college_predictor_model.pkl")
joblib.dump(le_category, "le_category.pkl")
joblib.dump(le_gender, "le_gender.pkl")
joblib.dump(le_branch, "le_branch.pkl")
joblib.dump(le_college, "le_college.pkl")

print("✅ Model and encoders saved successfully!")
