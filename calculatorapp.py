import streamlit as st

# Title of the app
st.title("Simple Calculator App")

# Display your photo
st.image(r"D:\Photo\0002.jpg", caption="Dillip Meher", use_column_width=True)  # Use raw string to handle backslashes

# Input numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

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
