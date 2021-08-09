######################################################################################################################
### Initialisation
######################################################################################################################

import csv
import os
import glob
import time
import psutil
import datetime
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

######################################################################################################################
### Functions
######################################################################################################################

def selectDirectory():
    """Select directory where output CSV's are located.
       Outputs the absolute path of the oldest CSV in the directory."""
    mainWindow.directory = filedialog.askdirectory()
    directoryFlag = mainWindow.directory
    if directoryFlag == '':
        filenameOutput.delete("1.0", "end")
        filenameOutput.insert(END, 'PLEASE SELECT AN EXPORT DIRECTORY')
        return
    os.chdir(mainWindow.directory)
    filenameOutput.delete("1.0", "end")
    filenameOutput.insert(END, mainWindow.directory)


def startProgram():
    '''Main program. Finds newest csv, parses the information and plots it'''

    # Setup left single graph in GUI
    singleGraph = Figure(figsize=(5, 6), dpi=100)
    canvasSingleGraph = FigureCanvasTkAgg(singleGraph, master=mainWindow)
    canvasSingleGraph.get_tk_widget().place(x=10, y=62)

    # Setup right multiple graph in GUI
    multipleGraph = Figure(figsize=(8, 6), dpi=100)
    canvasMultipleGraph = FigureCanvasTkAgg(multipleGraph, master=mainWindow)
    canvasMultipleGraph.get_tk_widget().place(x=470, y=60)

    # Creates a list of all CSV's in the directory
    list_of_files = glob.glob("*.csv")

    # Restarts 'startProgram' function if no files are present within the directory
    if len(list_of_files) == 0:
        errorOutput.delete("1.0", "end")
        errorOutput.insert(END, 'No files in directory @ ' + str(datetime.datetime.now())[:19])
        time.sleep(5)
        mainWindow.after(100, startProgram)

    # Finds the newest file in the directory
    fileName = max(list_of_files, key=os.path.getctime)  # Max value = newest file
    filenameOutput.delete("1.0", "end")
    filenameOutput.insert(END, 'Plotted data: ' + fileName)
    fileLocation = mainWindow.directory + '/' + fileName  # Creates absolute path of the newest CSV

    # Displays total system memory usage for the
    memoryOutput.delete("1.0", "end")
    memoryOutput.insert(END, ('~ Memory usage: ' + str(psutil.virtual_memory().percent)) + '%')

    # Tells user to restart program if memory allocation is too large.
    if (psutil.virtual_memory().percent) > 90:
        restartWarning = Label(mainWindow, text='PLEASE RESTART PROGRAM',
                               relief=RAISED, background='red')
        restartWarning.place(x=750, y=32)

    # Opens newest CSV from directory
    with open(fileLocation, 'r') as fh:
        reader = csv.reader(fh)
        next(reader)

        # Creates a list for each potential ROI.
        x1, x2, x3, x4, x5 = ([] for i in range(5))
        y1, y2, y3, y4, y5 = ([] for i in range(5))

        # Selects specific information from the CSV
        for row in reader:
            timePoint = (row[0])[-2:]
            roi = (row[1])[-1]
            signal = row[5]

            # Assigns specific information to the relevant list.
            if roi == '1':
                x1.append(int(timePoint))
                y1.append(float(signal))
            if roi == '2':
                x2.append(int(timePoint))
                y2.append(float(signal))
            if roi == '3':
                x3.append(int(timePoint))
                y3.append(float(signal))
            if roi == '4':
                x4.append(int(timePoint))
                y4.append(float(signal))
            if roi == '5':
                x5.append(int(timePoint))
                y5.append(float(signal))

        errorOutput.delete("1.0", "end")  # Debug Window in GUI
        errorOutput.insert(END, 'No error @ ' + str(datetime.datetime.now())[:19])  # Debug Window in GUI
        print('x1 = ' + str(x1))  # Debug Tool in command line
        print('y1 = ' + str(y1))  # Debug Tool in command line
        plt = singleGraph.add_subplot(111)

        # If any values exist in the associated ROI list, the values are plotted
        if len(x1) > 0:
            plt.plot(x1, y1, label='ROI 1')
        if len(x2) > 0:
            plt.plot(x2, y2, label='ROI 2')
        if len(x3) > 0:
            plt.plot(x3, y3, label='ROI 3')
        if len(x4) > 0:
            plt.plot(x4, y4, label='ROI 4')
        if len(x5) > 0:
            plt.plot(x5, y5, label='ROI 5')

        plt.set_ylabel('Signal (photons/second')
        plt.set_xlabel('Timepoint (minutes)')
        plt.set_title("All ROI's (same scale)")
        plt.legend(loc='lower right')

        # Determine number of ROI's
        roi_count = 0
        if len(x1) > 0:
            roi_count += 1
        if len(x2) > 0:
            roi_count += 1
        if len(x3) > 0:
            roi_count += 1
        if len(x4) > 0:
            roi_count += 1
        if len(x5) > 0:
            roi_count += 1


        # Generate output graph for 2 ROI's
        if roi_count == 2:
            ax1 = multipleGraph.add_subplot(221)
            ax1.plot(x1, y1, color='royalblue', linewidth=1.5)
            ax1.set_title('ROI 1')
            ax1.set_ylabel("Signal")
            ax1.set_xlabel("Time")

            ax2 = multipleGraph.add_subplot(222)
            ax2.plot(x2, y2, color='orange', linewidth=1.5)
            ax2.set_title('ROI 2')
            ax2.set_xlabel("Time")

            multipleGraph.tight_layout()

        # Generate output graph for 3 ROI's
        if roi_count == 3:
            ax1 = multipleGraph.add_subplot(221)
            ax1.plot(x1, y1, color='royalblue', linewidth=1.5)
            ax1.set_title('ROI 1')
            ax1.set_ylabel("Signal")

            ax2 = multipleGraph.add_subplot(222)
            ax2.plot(x2, y2, color='orange', linewidth=1.5)
            ax2.set_title('ROI 2')
            ax2.set_xlabel("Time")

            ax3 = multipleGraph.add_subplot(223)
            ax3.plot(x3, y3, color='green', linewidth=1.5)
            ax3.set_title('ROI 3')
            ax3.set_xlabel("Time")
            ax3.set_ylabel("Signal")

            multipleGraph.tight_layout()

        # Generate output graph for 4 ROI's
        if roi_count == 4:
            ax1 = multipleGraph.add_subplot(221)
            ax1.plot(x1, y1, color='royalblue', linewidth=1.5)
            ax1.set_title('ROI 1')
            ax1.set_ylabel("Signal")

            ax2 = multipleGraph.add_subplot(222)
            ax2.plot(x2, y2, color='orange', linewidth=1.5)
            ax2.set_title('ROI 2')

            ax3 = multipleGraph.add_subplot(223)
            ax3.plot(x3, y3, color='green', linewidth=1.5)
            ax3.set_xlabel("Time")
            ax3.set_title('ROI 3')
            ax3.set_ylabel("Signal")

            ax4 = multipleGraph.add_subplot(224)
            ax4.plot(x4, y4, color='firebrick', linewidth=1.5)
            ax4.set_title('ROI 4')
            ax4.set_xlabel("Time")


            multipleGraph.tight_layout()

        # Generate output graph for 5 ROI's
        if roi_count == 5:
            ax1 = multipleGraph.add_subplot(231)
            ax1.plot(x1, y1, color='royalblue', linewidth=1.5)
            ax1.set_title('ROI 1')
            ax1.set_ylabel("Signal")

            ax2 = multipleGraph.add_subplot(232)
            ax2.plot(x2, y2, color='orange', linewidth=1.5)
            ax2.set_title('ROI 2')

            ax3 = multipleGraph.add_subplot(233)
            ax3.plot(x3, y3, color='green', linewidth=1.5)
            ax3.set_title('ROI 3')

            ax4 = multipleGraph.add_subplot(234)
            ax4.plot(x4, y4, color='firebrick', linewidth=1.5)
            ax4.set_title('ROI 4')
            ax4.set_xlabel("Time")
            ax4.set_ylabel("Signal")

            ax5 = multipleGraph.add_subplot(235)
            ax5.plot(x5, y5, color='darkorchid', linewidth=1.5)
            ax5.set_title('ROI 5')
            ax5.set_xlabel("Time")

            multipleGraph.tight_layout()

def useGuide():
    messagebox.showinfo('Use Guide', message="1. Click the 'Export Location' button and select a folder where you will export your .csv files from the IVIS Living Image software, then press OK.\n\n"
                                             "2. Click the 'Start / Update' button\n\n"
                                             "3. Whenever you export a new .csv file from the IVIS Living Image software, click the 'Start / Update' button to refresh the graphs using the most recently generate data.")

def about():
    messagebox.showinfo('About', message='IVIS_Peak_Bagger\n\n'
                                         'Version 1.1\n\n'
                                         '9th August 2021\n\n'
                                         'IVIS_Peak_Bagger visualises csv data generated by the IVIS Spectrum\n\n'
                                         'Copyright (c) 2021 Kamil Sokolowski\n\n'
                                         '')


######################################################################################################################
### ''' GUI Interface Setup '''
######################################################################################################################
# Main windows setup
mainWindow = Tk()  # Links main window to the interpreter
mainWindow.title("IVIS Peak Bagger by Kamil_Sokolowski")
mainWindow.geometry("1270x650+10+10")  # Window size and initial position
mainWindow['bg'] = 'white'  # Background colour

# Changes default font for Matplotlib
plt.rcParams["font.family"] = "Courier New"

# Main buttons
Button(mainWindow, text="Export Location", command=selectDirectory, height=2, width=21, bg='white',
       bd=1, font='Courier', activeforeground='red', relief='ridge').place(x=10, y=10)

Button(mainWindow, text="Start / Update", command=startProgram, height=2, width=21, bg='white',
       bd=1, font='Courier', activeforeground='green', relief='ridge').place(x=240, y=10)

Button(mainWindow, text="Use Guide", command=useGuide, height=2, width=15, bg='white',
       bd=1, font='Courier', activeforeground='blue', relief='ridge').place(x=942, y=10)

Button(mainWindow, text="About", command=about, height=2, width=15, bg='white',
       bd=1, font='Courier', activeforeground='yellow', relief='ridge').place(x=1105, y=10)

# Error text box
errorOutput = Text(mainWindow, width=30, height=1, bg='white', bd=0)
errorOutput.place(x=500, y=10)
errorOutput.insert(END, 'Program has not started.')

# Filename text box
filenameOutput = Text(mainWindow, width=52, height=1, bg='white', bd=0)
filenameOutput.place(x=499, y=32)
filenameOutput.insert(END, 'No directory selected.')

# Memory text box
memoryOutput = Text(mainWindow, width=20, height=1, bg='white', bd=0)
memoryOutput.place(x=750, y=10)
memoryOutput.insert(END, ('Memory usage: ' + str(psutil.virtual_memory().percent)) + '%')

artASCII = ("""

                                                          _
                            ___                          (_)
                          _/XXX\\
           _             /XXXXXX\_                                   __
          /X\__    __   /X XXXX XX\                         _       /XX\__      ___
         /     \__/  \_/__       \ \                      _/X\__   /XX XXX\____/XXX\\    _
        /    \___     \/  \_      \ \              __   _/      \_/  _/  -   __  -  \__/ \\
     __/  ___/   \__/   \ \__       \\\            /  \_//  _ _ \  \     __  /  \____//    \\
    /    /   __    \  /     \ \_   _//_\___     _/    //           \___/  \/     __/       \_
___/________/_______\________\__\_/________\_ _/_____/_____________/_______\____/_______ _____\___
                                            /|\\
                                           / | \\
                                          /  |  \\
                                         /   |   \\
                                        /    |    \\
                                       /     |     \\
                                      /      |      \\
                                     /       |       \\
                                    /        |        \\
                                   /         |         \\
                  _                  _   _            _       _   	                    _
   _____  ___ __ | | ___  _ __ ___  | |_| |__   ___  (_)_   _(_)___   _ __   ___  __ _| | _____
  / _ \ \/ / '_ \| |/ _ \| '__/ _ \ | __| '_ \ / _ \ | \ \ / / / __| | '_ \ / _ \/ _` | |/ / __|
 |  __/>  <| |_) | | (_) | | |  __/ | |_| | | |  __/ | |\ V /| \__ \ | |_) |  __/ (_| |   <\__ \\
  \___/_/\_\ .__/|_|\___/|_|  \___|  \__|_| |_|\___| |_| \_/ |_|___/ | .__/ \___|\__,_|_|\_\___/
           |_|							             |_|
""")

artOutput = Text(mainWindow, width=150, height=30, bg='white', bd=0)
artOutput.place(x=280, y=130)
artOutput.insert(END, artASCII)

mainWindow.mainloop()