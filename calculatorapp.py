import streamlit as st

# Title of the app
st.title("Simple Calculator App")

# Display your photo
st.sidebar.image("0002.jpg", caption="Dillip Meher", width=100)  # Adjust the width to your preference

# Input numbers
num1 = st.number_input("Enter the first number", value=0)
num1 = st.slider("Select the first number", min_value=0, max_value=100, value=0)  # Adjust range as needed
num2 = st.number_input("Enter the second number", value=0)
num2 = st.slider("Select the second number", min_value=0, max_value=100, value=0)  # Adjust range as needed

    
    


# Dropdown for operation selection
operation = st.selectbox("Choose the operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation based on user input
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result of {num1} + {num2} is: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result of {num1} - {num2} is: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result of {num1} * {num2} is: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of {num1} / {num2} is: {result}")
        else:
            st.error("Error: Division by zero is not allowed.")
