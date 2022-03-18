# Peak_Bagger

Peak_Bagger is a tool that visualises each ROI in the image series so as to easily identify the signal plateau. Data is plotted combined, as well as seperately to allow for proper comparison and visualisation. The software works with exported csv files from IVIS imaging systems. 
\
\
<img src="https://user-images.githubusercontent.com/70458221/158322300-efb38571-78f4-42c6-b3b4-93d037871b96.gif"/>


1. Click the 'Export Location' button and select a folder where you will export your .csv files from the IVIS Living Image software, then press OK.

2. Click the 'Start / Update' button.

3. Whenever a new .csv file (not .txt) is exported from the IVIS Living Image software, click the 'Start / Update' button to refresh the graphs. The lastest file is used as a basis to generate the data.

4. Each time 'Start / Update" is run, the highest signal from each ROI is automatically copied to the clipboard. Pasting this data into a spreadsheet at the end of an imaging series will give the peak signal from each ROI, which is the final result most IVIS users seek for analysis.
