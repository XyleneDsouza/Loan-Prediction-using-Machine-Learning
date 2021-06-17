import pickle
import streamlit as st
import math
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, Dependents, Education, Self_Employed, Property_Area, Loan_Amount, Total_Income, EMI, Balance_Income, Credit_History):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
        
    if Dependents == "Zero":
        Dependents = 0
    elif Dependents == "One":
        Dependents = 1
    elif Dependents == "Two":
        Dependents = 2
    else:
        Dependents = 3
        
    if Education == "NonGraduate":
        Education = 0
    else:
        Education = 1
        
    if Self_Employed == "Self-employed":
        Self_Employed = 0
    else:
        Self_Employed = 1  
 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
        
    if Property_Area == "Rural":
        Property_Area = 0
    elif Property_Area == "Semiurban":
        Property_Area = 1
    else:
        Property_Area = 2
        
    Loan_Amount = math.log(Loan_Amount)
    
    Total_Income = math.log(Total_Income)
    
    EMI = math.log(EMI)
    
    Balance_Income = math.log(Balance_Income)
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married, Dependents, Education, Self_Employed, Property_Area, Loan_Amount, Total_Income, EMI, Balance_Income, Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:purple;padding:20px"> 
    <h1 style ="color:black;text-align:center;">Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    account_no = st.text_input('Account Number')
    full_name = st.text_input('Full Name')
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    Dependents = st.selectbox('Number of Dependents',("Zero","One","Two","More than Two"))
    Education = st.selectbox('Education',("Graduate", "NonGraduate"))
    Self_Employed = st.selectbox('Employment Status',("Self-employed", "Employee"))
    Property_Area = st.selectbox('Property Area',("Rural", "Semiurban", "Urban"))
    Loan_Amount = st.number_input("Total loan Amount")
    Loan_Amount_Term = st.selectbox("Loan Duration",("2 months","6 months","8 months","1 year","16 months"))
    Total_Income = st.number_input("Applicants Monthly Income") 
    EMI = st.number_input("Equated Monthly Installment (EMI)")
    Balance_Income = st.number_input("Balance Income")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Submit"): 
        result = prediction(Gender, Married, Dependents, Education, Self_Employed, Property_Area, Loan_Amount, Total_Income, EMI, Balance_Income, Credit_History) 
        if result == "Rejected":
            st.error("Dear "+full_name+", We regret to inform that your application for loan is rejected.")
        else:
            st.success("Congratulations "+full_name+", Your application for loan is approved.")
        
     
if __name__=='__main__': 
    main()