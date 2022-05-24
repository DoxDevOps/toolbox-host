# toolbox-offline-exporter
App that exports a number of metrices from a host using QR code

## HOW IT WORKS
Toolbox Offline Exporter scans the status of a Client/Computer/Server/ installed at a facility. 
For example : If a site has EMC or POC installed, toolbox will scan the current tags on which EMC or POC is working. 

This information is displayed using a QR Image that is displayed on the web browser.
## INSTALLATION GUIDE 
1. Clone from github using <url>
2. cd into the toolbox-offline-exporter using **_cd_ _toolbox-offline-exporter_**
3. Inside the repo, you will find a script named **setup.py** and **reconfig.py**
4. Make both scripts executable  (setup.py and reconfig.py)

### 1. Fresh Installation 
For fresh installation(Installing toolbox for the first time), do the following 
1. run setup.py using **_./setup.py_**
2. Watch the script as it runs and enter your password when prompted. Then you will be prompted to enter the name of the facility you are installing toolbox.
3. Follow the instructions and select appropriately.
4. when done got to your web browser and type **_0.0.0.0:6070/_**
5. If the QR image generates, then your site is fully configured with Toolbox

### 2. Re-configuring Toolbox
This will happen if a user has wrongly configured a site on toolbox and would like to change site details.
1. run script named reconfig.py using **_./reconfig.py_**
2. The script will take you through setting up a site byt prompting the user to enter the name of the facility.
3. Select the correct site name and follow the instructions appropriately.