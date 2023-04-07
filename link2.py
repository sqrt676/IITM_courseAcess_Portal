import streamlit as st

st.title("IITM BS Degree Course Access Portal")

st.header("Developed by Sumit")


course = st.selectbox(
    'Select your course',
    ('Machine Learning Foundations',
'Business Data Management',
'Business Data Management - Project',
'Machine Learning Techniques',
'Machine Learning Practice',
'Machine Learning Practice - Project',
'Business Analytics',
'Tools in Data Science',
'Database Management Systems',
'Programming, Data Structures and Algorithms using Python',
'Modern Application Development I',
'Modern Application Development I - Project',
'Programming Concepts using Java',
'Modern Application Development II',
'Modern Application Development II - Project',
'System Commands',
'Mathematics for Data Science I',
'Statistics for Data Science I',
'Computational Thinking',
'English I',
'Mathematics for Data Science II',
'Statistics for Data Science II',
'Programming in Python',
'English II'))
#year=int(input())
#term=int(input())

#cc={a:"1"}
year=st.selectbox('Select the year in which you registered for the course',('20','21','22','23'))
term=st.selectbox('Select your term in which you registered',('t1','t2','t3'))

coursearray=['Machine Learning Foundations',
'Business Data Management',
'Business Data Management - Project',
'Machine Learning Techniques',
'Machine Learning Practice',
'Machine Learning Practice - Project',
'Business Analytics',
'Tools in Data Science',
'Database Management Systems',
'Programming, Data Structures and Algorithms using Python',
'Modern Application Development I',
'Modern Application Development I - Project',
'Programming Concepts using Java',
'Modern Application Development II',
'Modern Application Development II - Project',
'System Commands',
'Mathematics for Data Science I',
'Statistics for Data Science I',
'Computational Thinking',
'English I',
'Mathematics for Data Science II',
'Statistics for Data Science II',
'Programming in Python',
'English II']
codearray=['CS2004',
'MS2001',
'MS2001P',
'CS2007',
'CS2008',
'CS2008P',
'MS2002',
'SE2002',
'CS2001',
'CS2002',
'CS2003',
'CS2003P',
'CS2005',
'CS2006',
'CS2006P',
'SE2001',
'MA1001',
'MA1002',
'CS1001',
'HS1001',
'MA1003',
'MA1004',
'CS1002',
'HS1002']
#https://seek.onlinedegree.iitm.ac.in/courses/ns_22t3_ms2001
cc=(codearray[coursearray.index(course)])
finallink="https://seek.onlinedegree.iitm.ac.in/courses/ns_"+year+term+"_"+cc.lower()


url = finallink
st.write("Click on the [link](%s)" % url)