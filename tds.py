import streamlit as st

def largest(a,b,c):
  l=[]
  l.append(a)
  l.append(b)
  l.append(c)
  return max(l)

st.title("Largest in three numbers")

x = st.number_input("Enter first number:", step = 0.0001, value = 0.0000, format = "%5.4f")
y = st.number_input("Enter second number:" step = 0.0001, value = 0.0000, format = "%5.4f")
z = st.number_input("Enter third number:" step = 0.0001, value = 0.0000, format = "%5.4f")

st.text("The largest among these three numbers:")
st.write(largest(x,y,z))

         
