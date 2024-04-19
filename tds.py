import streamlit as st

def largest(a,b,c):
  l=[]
  l.append(a)
  l.append(b)
  l.append(c)
  return max(l)

st.title("Largest in three numbers")

x = st.number_input("Enter first number:")
y = st.number_input("Enter second number:")
z = st.number_input("Enter third number:")

st.text("The largest among these three numbers:")
st.write(largest(x,y,z))

         
