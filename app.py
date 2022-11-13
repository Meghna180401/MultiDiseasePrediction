# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:04:28 2022

@author: USER
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('heart_model.sav', 'rb'))

liver_model = pickle.load(open('liver_model.sav', 'rb'))

diabKeys = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
heartKeys = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
liverKeys = ['Age','Gender','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin','Albumin_and_Globulin_Ratio']
dict_of_diseases= dict(diab= diabKeys, heart= heartKeys, liver= liverKeys)

#Function to check for validating inputs
def valid_input(inputs):
    for inp in inputs:
        try:
            float(inp)
        except:
            return False
    return True

#Function to clear form on button click
def clear_form(disease):
	for key in dict_of_diseases[disease]:
		 st.session_state[key]=""

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Liver Disease Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    submitted = False
    clear = False
    
    with st.form(key="diabetesForm"):
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)
        
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies',key="Pregnancies")
            
        with col2:
            Glucose = st.text_input('Glucose level',key='Glucose')
        
        with col3:
            BloodPressure = st.text_input('Diastolic Blood Pressure (mm Hg)',key='BloodPressure')
        
        with col1:
            SkinThickness = st.text_input('Skin Thickness (mm)',key='SkinThickness')
        
        with col2:
            Insulin = st.text_input('Insulin (mu U/ml)',key='Insulin')
        
        with col3:
            BMI = st.text_input('BMI',key='BMI')
        
        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value',key='DiabetesPedigreeFunction')
        
        with col2:
            Age = st.text_input('Age',key='Age')
        
        
        # code for Prediction
        diab_diagnosis = ''
        
        inputData = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        
        # creating buttons for Prediction and Clear
        c1, c2, c3 = st.columns([3, 1, 1],gap="large")
        
        with c1:
            submitted = st.form_submit_button(label="Diabetes Test Result")
        with c2:
            pass
        with c3:
            clear = st.form_submit_button(label="Clear",on_click=clear_form,args=("diab", ))
        
        
        
    if submitted:
        if(valid_input(inputData)):   
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                     
            if (diab_prediction[0] == 0):
                diab_diagnosis = 'The person is not diabetic'
            else:
                diab_diagnosis = 'The person is diabetic'
            st.success(diab_diagnosis)
               
        else:
            st.error("All fields are required and must have appropriate values")
      

# Heart Disease Prediction Page: Used RF model 94.634% accuracy
# =============================================================================
if (selected == 'Heart Disease Prediction'):
#     
     #page title
     st.title('Heart Disease Prediction using ML')
     
     validSelect = True
     submitted = False
     clear = False
     
     with st.form(key="heartForm"):
             
         col1, col2, col3 = st.columns(3)
         
         with col1:
             age = st.text_input('Age',key='age')
             
         with col2:
             sex = st.selectbox('Gender',('','Male', 'Female'),key='sex')
             
         with col3:
             cp = st.selectbox('Chest Pain Level',('','Absent', 'Faint', 'Moderate', 'Severe'),key='cp')
             
         with col1:
             trestbps = st.text_input('Resting Blood Pressure (mm Hg)',key='trestbps')
             
         with col2:
             chol = st.text_input('Serum Cholestoral (mg/dL)',key='chol')
             
         with col3:
             fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl',('', 'Yes', 'No'),key='fbs')
             
         with col1:
             restecg = st.selectbox('Resting Electrocardiographic results',('', '0', '1', '2'),key='restecg')
             
         with col2:
             thalach = st.text_input('Maximum Heart Rate achieved',key='thalach')
             
         with col3:
             exang = st.selectbox('Exercise Induced Angina',('', 'Yes', 'No'),key='exang')
             
         with col1:
             oldpeak = st.text_input('ST depression induced by exercise',key='oldpeak')
             
         with col2:
             slope = st.text_input('Slope of peak exercise ST segment',key='slope')
             
         with col3:
             ca = st.selectbox('Major vessels colored by flourosopy',('' ,'0', '1', '2', '3'),key='ca')
             
         with col1:
             thal = st.selectbox('Thalassemia', ('', 'Not examined', 'Normal', 'Fixed Defect', 'Reversable Defect'),key='thal')
         
         if(sex == 'Male'):
             sex = '1'
         elif(sex == 'Female'):
             sex = '0'
         else:
             validSelect = False
             
         if(cp=='Absent'):
             cp = '0'
         elif(cp=='Faint'):
             cp = '1'
         elif(cp=='Moderate'):
             cp = '2'
         elif(cp=='Severe'):
             cp = '3'
         else:
             validSelect = False
      
         if(fbs=='Yes'):
             fbs = '1'
         elif(fbs=='No'):
             fbs = '0'
         else:
             validSelect = False
             
         if(exang=='Yes'):
             exang = '1'
         elif(exang=='No'):
             exang = '0'
         else:
             validSelect = False
             
         if(thal=='Not examined'):
             thal = '0'
         elif(thal=='Normal'):
             thal = '1'
         elif(thal=='Fixed Defect'):
             thal = '2'
         elif(thal=='Reversable Defect'):
             thal = '3'
         else:
             validSelect = False
             
         # code for Prediction
         heart_diagnosis = ''
         
         inputData = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
         
         # creating buttons for Prediction and Clear
         c1, c2, c3 = st.columns([3, 1, 1],gap="large")
         
         with c1:
             submitted = st.form_submit_button(label="Heart Disease Test Result")
         with c2:
             pass
         with c3:
             clear = st.form_submit_button(label="Clear",on_click=clear_form,args=("heart", ))
         
        
         if submitted:
             if(valid_input(inputData) and validSelect==True):   
                 heart_prediction = heart_model.predict([[age,sex,cp,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
                      
                 if (heart_prediction[0] == 0):
                     heart_diagnosis = 'The person does not have heart disease'
                 else:
                     heart_diagnosis = 'The person has some heart disease'
                 st.success(heart_diagnosis)
             else:
                st.error("All fields are required and must have appropriate values")
        
         if clear:
            validSelect = True

# Liver Disease Prediction Page --- used rf model : 95.348 accuracy

if (selected == 'Liver Disease Prediction'):
    
     #page title
     st.title('Liver Disease Prediction using ML')
     
     submitted = False
     clear = False
     
     with st.form(key="liverForm"):
         col1, col2, col3 = st.columns(3)
         
         with col1:
             Age = st.text_input('Age',key='Age')
             
         with col2:
             Gender = st.selectbox('Gender',('','Male', 'Female'),key='Gender')
         
         with col3:
             Total_Bilirubin = st.text_input('Total Bilirubin (mg/dL)',key='Total_Bilirubin')
         
         with col1:
             Direct_Bilirubin = st.text_input('Direct Bilirubin (mg/dL)',key='Direct_Bilirubin')
         
         with col2:
             Alkaline_Phosphotase = st.text_input('Alkaline Phosphotase (IU/L)',key='Alkaline_Phosphotase')
         
         with col3:
             Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase (IU/L)',key='Alamine_Aminotransferase')
         
         with col1:
             Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase (IU/L)',key='Aspartate_Aminotransferase')
         
         with col2:
             Total_Protiens = st.text_input('Total Proteins (g/dL)',key='Total_Protiens')
             
         with col3:
             Albumin = st.text_input('Albumin (g/dL)',key='Albumin')
             
         with col1:
             Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio',key='Albumin_and_Globulin_Ratio')
             
         # code for Prediction
         liver_diagnosis = ''
         
         inputData = [Age,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]
         
         # creating buttons for Prediction and Clear
         c1, c2, c3 = st.columns([3, 1, 1],gap="large")
         
         with c1:
             submitted = st.form_submit_button(label="Liver Disease Test Result")
         with c2:
             pass
         with c3:
             clear = st.form_submit_button(label="Clear",on_click=clear_form,args=("liver", ))
         
         
         if submitted:
             if(valid_input(inputData) and len(Gender)!=0):   
                 liver_prediction = liver_model.predict([[Age,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Albumin_and_Globulin_Ratio]])
                      
                 if (liver_prediction[0] == 0):
                     liver_diagnosis = 'The person does not have liver disease'
                 else:
                     liver_diagnosis = 'The person has some liver disease'
                 st.success(liver_diagnosis)
             else:
                st.error("All fields are required and must have appropriate values")
     
# Kidney Disease Prediction Page

#if (selected == 'Kidney Disease Prediction'):
    
     #page title
#     st.title('Kidney Disease Prediction using ML') 

# =============================================================================
