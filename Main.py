######################################################################################################################
### Initialisation
######################################################################################################################

import csv
import os
import glob
import psutil
import datetime
import pyperclip
import matplotlib.pyplot as plt
from tkinter import *
from decimal import Decimal
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

    maxSignalList = []

    maxSignalOutput.delete(1.0, END)
    roiOutput.delete(1.0, END)

    # Setup left single graph in GUI
    singleGraph = Figure(figsize=(5, 6), dpi=100)
    canvasSingleGraph = FigureCanvasTkAgg(singleGraph, master=mainWindow)
    canvasSingleGraph.get_tk_widget().place(x=10, y=62)

    # Setup right multiple graph in GUI
    multipleGraph = Figure(figsize=(8, 6), dpi=95)
    canvasMultipleGraph = FigureCanvasTkAgg(multipleGraph, master=mainWindow)
    canvasMultipleGraph.get_tk_widget().place(x=490, y=70)

    # Creates a list of all CSV's in the directory
    list_of_files = glob.glob("*.csv")

    # Restarts 'startProgram' function if no files are present within the directory
    if len(list_of_files) == 0:
        errorOutput.delete("1.0", "end")
        errorOutput.insert(END, 'No files in directory @ ' + str(datetime.datetime.now())[:19])
        return

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

        # Creates a dictionary for each potential ROI.
        x1d, x2d, x3d, x4d, x5d = ({} for i in range(5))

        # Selects specific information from the CSV
        for row in reader:
            timePoint = (row[0])[-2:]
            roi = (row[1])[-1]
            signal = row[3]

            # Assigns specific information to the relevant dictionary.
            if roi == '1':
                x1d[int(timePoint)] = float(signal)
            if roi == '2':
                x2d[int(timePoint)] = float(signal)
            if roi == '3':
                x3d[int(timePoint)] = float(signal)
            if roi == '4':
                x4d[int(timePoint)] = float(signal)
            if roi == '5':
                x5d[int(timePoint)] = float(signal)

        errorOutput.delete("1.0", "end")  # Debug Window in GUI
        errorOutput.insert(END, 'No error @ ' + str(datetime.datetime.now())[:19])  # Debug Window in GUI
        plt = singleGraph.add_subplot(111)

        # If any values exist in the associated ROI list, the values are plotted.
        # Dictinaries are converted into lists for plotting.
        if len(x1d) > 0:
            x1List = x1d.items()
            x1List = sorted(x1List)
            x1, y1 = zip(*x1List)
            plt.plot(x1, y1, label='ROI 1')
            maxSignalOutput.insert(END, '%.2E' % Decimal(float(max(y1))) + '\n')
            roiOutput.insert(END, 'ROI 1:\n')
        if len(x2d) > 0:
            x2List = x2d.items()
            x2List = sorted(x2List)
            x2, y2 = zip(*x2List)
            plt.plot(x2, y2, label='ROI 2')
            maxSignalOutput.insert(END, '%.2E' % Decimal(float(max(y2))) + '\n')
            roiOutput.insert(END, 'ROI 2:\n')
        if len(x3d) > 0:
            x3List = x3d.items()
            x3List = sorted(x3List)
            x3, y3 = zip(*x3List)
            plt.plot(x3, y3, label='ROI 3')
            maxSignalOutput.insert(END, '%.2E' % Decimal(float(max(y3))) + '\n')
            roiOutput.insert(END, 'ROI 3:\n')
        if len(x4d) > 0:
            x4List = x4d.items()
            x4List = sorted(x4List)
            x4, y4 = zip(*x4List)
            plt.plot(x4, y4, label='ROI 4')
            maxSignalOutput.insert(END, '%.2E' % Decimal(float(max(y4))) + '\n')
            roiOutput.insert(END, 'ROI 4:\n')
        if len(x5d) > 0:
            x5List = x5d.items()
            x5List = sorted(x5List)
            x5, y5 = zip(*x5List)
            plt.plot(x5, y5, label='ROI 5')
            maxSignalOutput.insert(END, '%.2E' % Decimal(float(max(y5))) + '\n')
            roiOutput.insert(END, 'ROI 5:\n')

        data = maxSignalOutput.get(1.0, "end-1c")
        pyperclip.copy(data)

        plt.set_ylabel('Signal (photons/second')
        plt.set_xlabel('Timepoint (minutes)')
        plt.set_title("All ROI's (same scale)")
        plt.legend(loc='lower right')

        # Determine number of ROI's
        roi_count = 0
        if len(x1d) > 0:
            roi_count += 1
        if len(x2d) > 0:
            roi_count += 1
        if len(x3d) > 0:
            roi_count += 1
        if len(x4d) > 0:
            roi_count += 1
        if len(x5d) > 0:
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

            maxSignalList.append(max(y1))
            maxSignalList.append(max(y2))

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

            maxSignalList.append(max(y1))
            maxSignalList.append(max(y2))
            maxSignalList.append(max(y3))

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

            maxSignalList.append(max(y1))
            maxSignalList.append(max(y2))
            maxSignalList.append(max(y3))
            maxSignalList.append(max(y4))



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

            maxSignalList.append(max(y1))
            maxSignalList.append(max(y2))
            maxSignalList.append(max(y3))
            maxSignalList.append(max(y4))
            maxSignalList.append(max(y5))


def useGuide():
    messagebox.showinfo('Use Guide', message="1. Click the 'Export Location' button and select a folder where you will export your .csv files from the IVIS Living Image software, then press OK.\n\n"
                                             "2. Click the 'Start / Update' button\n\n"
                                             "3. Whenever you export a new .csv file from the IVIS Living Image software, click the 'Start / Update' button to refresh the graphs using the most recently generated data.\n\n"
                                             "4. The highest value of each ROI is automatically copied to the computer's clipboard. At the end of the imaging series, paste this data into a seperate spreadsheet to easily get the peak value of each ROI.")


def about():
    messagebox.showinfo('About', message='IVIS_Peak_Bagger\n\n'
                                         'Version 1.3.0\n\n'
                                         '31st January 2022\n\n'
                                         'IVIS_Peak_Bagger visualises csv data generated by the IVIS Spectrum and outputs the peak value of each ROI\n\n'
                                         'Copyright (c) 2022 Kamil Sokolowski\n\n'
                                         'Any suggestions of features you would like added?\n\n'
                                         'Email me: thatKamil@pm.me\n\n'
                                         'Source code & license (MIT) available at:\n\n'
                                         'https://github.com/thatKamil/Peak_Bagger'
                                         '')

################################################################################`######################################
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

Button(mainWindow, text="Use Guide", command=useGuide, height=2, width=10, bg='white',
       bd=1, font='Courier', activeforeground='blue', relief='ridge').place(x=1037, y=10)

Button(mainWindow, text="About", command=about, height=2, width=10, bg='white',
       bd=1, font='Courier', activeforeground='yellow', relief='ridge').place(x=1155, y=10)

# Error text box
errorOutput = Text(mainWindow, width=30, height=1, bg='white', bd=0)
errorOutput.place(x=480, y=10)
errorOutput.insert(END, 'Program has not started.')

# Filename text box
filenameOutput = Text(mainWindow, width=52, height=1, bg='white', bd=0)
filenameOutput.place(x=479, y=32)
filenameOutput.insert(END, 'No directory selected.')

# Memory text box
memoryOutput = Text(mainWindow, width=20, height=1, bg='white', bd=0)
memoryOutput.place(x=730, y=10)
memoryOutput.insert(END, ('Memory usage: ' + str(psutil.virtual_memory().percent)) + '%')

# Small outputs showing the peak value of each ROI in a text box on screen.
maxSignalOutput = Text(mainWindow, width=9, height=5, bd=0, font="Courier 8")
maxSignalOutput.place(x=957, y=1)
roiOutput = Text(mainWindow, width=6, height=5, bd=0, font="Courier 8")
roiOutput.place(x=912, y=1)

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

# Displays the above art work in a text box at the start of the program.
artOutput = Text(mainWindow, width=150, height=30, bg='white', bd=0)
artOutput.place(x=280, y=130)
artOutput.insert(END, artASCII)

mainWindow.mainloop()
