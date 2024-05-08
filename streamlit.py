import streamlit as st
import api
import chatgpt

st.header("Suricata Generator")

report_type = st.sidebar.selectbox("Select CTI report platform.",('AlienVault','MISP','MITRE ATT&CK'))
generateReport = st.sidebar.button("Export report from "+ report_type)
createRule = False

if generateReport == True:
    report = chatgpt.read_report()
    st.sidebar.json(report)
    createRule = st.button('Creating Suricata Rule...')

    rule = chatgpt.generate_suricata_rule(report)
    print(rule)
    st.write(rule)