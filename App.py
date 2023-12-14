import streamlit as st
from PIL import Image
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os
st.title('Welcome To Ibrahim Creation ')
st.header('Creator- Mohammod Ibrahim Hossain ')
st.write("Contributor- Saidur Rahman safim")
st.image('blood.jpg')
# model_url = "https://github.com/MohammoD2/CBc-/blob/main/model.pkl"
# scaler_url = "https://github.com/MohammoD2/CBc-/blob/main/scaler.pkl"

# model = joblib.load("E:\\Work files\\CBC prediction\\model.pkl")

# scaler = joblib.load("E:\Work files\CBC prediction\scaler.pkl")
model_path = os.path.join("E:/Work files/CBC prediction", "model.pkl")
scaler_path = os.path.join("E:/Work files/CBC prediction", "scaler.pkl")

# Check if the files exist before loading
if os.path.exists(model_path) and os.path.exists(scaler_path):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    st.success("Model and scaler loaded successfully.")
else:
    model, scaler = None, None
    st.error(f"Error: Model or scaler file not found. Check the file paths: {model_path}, {scaler_path}.")

def predict_result(data):
    if scaler is not None:
        dataframe = pd.DataFrame([data])
        numerical_features_transformed = scaler.transform(dataframe)
        predict = model.predict(numerical_features_transformed)
        return predict
    else:
        st.error("Error: Scaler is not loaded.")
        return None
def predict_result(data):

    dataframe = pd.DataFrame([data])

    # Use the same scaler that was fitted on the training data
    numerical_features_transformed = scaler.transform(dataframe)


    predict = model.predict(numerical_features_transformed)
    return predict

def main():
    st.title("Blood Test Result Predictor")


    Name =st.text_input('Enter Your name:')
    Hemoglobin = st.text_input('Enter Hemoglobin:')
    Neutrophils = st.text_input('Enter Neutrophils:')
    Lymphocytes = st.text_input('Enter Lymphocytes:')
    MPV = st.text_input('Enter MPV:')
    PCT = st.text_input('Enter PCT:')
    PDW = st.text_input('Enter PDW:')
    RBC = st.text_input('Enter RBC:')
    HCT = st.text_input('Enter HCT:')
    MCV = st.text_input('Enter MCV:')
    MCH = st.text_input('Enter MCH:')
    MCHC = st.text_input('Enter MCHC:')
    RDWCV = st.text_input('Enter RDWCV:')
    RDWSD = st.text_input('Enter RDWSD:')
    PLCR = st.text_input('Enter PLCR:')
    PLT = st.text_input('Enter PLT:')
    WBC = st.text_input('Enter WBC:')

    data = {
    'Hemoglobin': Hemoglobin,
    'Neutrophils': Neutrophils,
    'Lymphocytes': Lymphocytes,
    'MPV': MPV,
    'PCT': PCT,
    'PDW': PDW,
    'RBC': RBC,
    'HCT': HCT,
    'MCV': MCV,
    'MCH': MCH,
    'MCHC': MCHC,
    'RDWCV': RDWCV,
    'RDWSD': RDWSD,
    'PLCR': PLCR,
    'PLT': PLT,
    'WBC': WBC
    }
    if st.button("Check Your Condition "):
        prediction = predict_result(data)
        result_text = "Unhealthy" if prediction[0] == 0 else "Healthy"


        if result_text == "Healthy":
          st.success(f"Great news, {Name}! Your condition is Healthy.")
          st.subheader("1. **Maintain a Balanced Diet:**")
          st.write("- Consume a variety of fruits, vegetables, whole grains, and lean proteins.")
          st.write("- Ensure adequate intake of essential nutrients such as iron, vitamin B12, and folate.")

          st.subheader("2. **Stay Hydrated:**")
          st.write("- Drink an adequate amount of water daily to support overall health and blood circulation.")

          st.subheader("3. **Regular Exercise:**")
          st.write("- Engage in regular physical activity, such as walking, jogging, or other forms of exercise.")
          st.write("- Aim for at least 150 minutes of moderate-intensity exercise per week.")

          st.subheader("4. **Adequate Sleep:**")
          st.write("- Ensure you get enough quality sleep each night for overall well-being and immune function.")

          st.subheader("5. **Stress Management:**")
          st.write("- Practice stress-reducing techniques such as meditation, yoga, or deep breathing exercises.")

          st.subheader("6. **Regular Health Check-ups:**")
          st.write("- Schedule routine health check-ups and screenings to monitor overall health.")

          st.subheader("7. **Avoid Smoking and Excessive Alcohol:**")
          st.write("- If you smoke, consider quitting.")
          st.write("- Limit alcohol intake to moderate levels or as advised by healthcare professionals.")

          st.subheader("8. **Maintain a Healthy Weight:**")
          st.write("- Aim for a healthy body weight through a combination of diet and exercise.")

          st.subheader("9. **Sun Protection:**")
          st.write("- Use sunscreen to protect your skin from harmful UV rays when exposed to the sun.")

          st.subheader("10. **Follow Healthcare Provider Recommendations:**")
          st.write("- Adhere to any specific recommendations or advice provided by your healthcare provider based on your individual health profile.")

        else:
          st.error(f"Attention, {Name}! Your condition is Unhealthy.")
          st.subheader("Instructions for Addressing Unhealthy CBC Results:")

          st.subheader("1. Consult with a Healthcare Professional:")
          st.write("- Schedule an appointment with your healthcare provider to discuss the CBC results.")
          st.write("- Seek guidance from a hematologist or relevant specialist if necessary.")

          st.subheader("2. Follow-up Testing and Diagnosis:")
          st.write("- Undergo further diagnostic tests as recommended by your healthcare provider to identify the underlying cause.")

          st.subheader("3. Medication and Treatment Plan:")
          st.write("- Adhere to any prescribed medications or treatment plan provided by your healthcare professional.")

          st.subheader("4. Dietary Adjustments:")
          st.write("- Modify your diet as per the recommendations of a registered dietitian to address nutritional deficiencies.")
          st.write("- Ensure an adequate intake of nutrients such as iron, vitamin B12, and folate if deficiencies are identified.")

          st.subheader("5. Lifestyle Changes:")
          st.write("- Make necessary lifestyle changes, such as quitting smoking or reducing alcohol intake, if advised by your healthcare provider.")

          st.subheader("6. Manage Underlying Conditions:")
          st.write("- If the CBC abnormalities are associated with an underlying health condition (e.g., anemia, infection), work with your healthcare provider to manage the condition.")

          st.subheader("7. Monitor and Follow-up:")
          st.write("- Regularly monitor your CBC and other relevant health parameters as advised by your healthcare provider.")
          st.write("- Attend follow-up appointments to track progress and adjust the treatment plan if necessary.")

          st.subheader("8. Stay Informed:")
          st.write("- Educate yourself about the specific conditions associated with abnormal CBC results.")
          st.write("- Ask questions and seek clarification from your healthcare provider to enhance your understanding.")

          st.subheader("9. Psychosocial Support:")
          st.write("- Seek psychosocial support, such as counseling or support groups, if dealing with chronic health conditions that may affect mental well-being.")

          st.subheader("10. Emergency Situations:")
          st.write("- Be aware of signs and symptoms that may indicate an emergency situation, and seek immediate medical attention if necessary.")





      

if __name__ == "__main__":
    main()
