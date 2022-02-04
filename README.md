# Toolbox
Toolbox is a platform for version tracking, system diagnostics and support. This repo is for the host module of Toolbox. The host module runs at a facility server and it's core responsibilty is to produce a QR code that contains encrypted data for that facility. The data contained in the QR code includes:
1. Application name
2. Site name
3. IP address
4. @tiwonge, to add the rest 

#TOOLBOX FILE FORMAT
Data sent to the QR Image is in String format with punctuations in it. The following is a sample :

*************************************************************************************************
"system_type:{POC or EMC};site_name:{Kamuzu Central Hospital};ip_address:{0.0.0.0};"

*************************************************************************************************
