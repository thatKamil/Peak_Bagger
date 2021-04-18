######################################################################################################################
### Initialisation
######################################################################################################################

import csv
import os
import glob
import time
import datetime
from tkinter import *
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
    os.chdir(mainWindow.directory)


def startProgram():
    '''Main program. Finds newest csv, parses the information and plots it'''
    print('Program started: ' + str(datetime.datetime.now()))

    list_of_files = glob.glob("*.csv")  # Creates a list of all CSV's in the directory
    fileName = max(list_of_files, key=os.path.getctime)  # Determines the newest CSV
    fileLocation = mainWindow.directory + '/' + fileName  # Creates absolute path of the newest CSV
    print(fileLocation)

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

            # Appends collected information to the associated list.
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

        singleGraph = Figure(figsize=(5, 6), dpi=100)
        canvas = FigureCanvasTkAgg(singleGraph, master=mainWindow)
        canvas.get_tk_widget().place(x=10, y=50)

        canvas3 = Canvas(mainWindow,height=50,width=200,bg='white')
        canvas3.place(x=500,y=10)


        if len(x1) <= 1:
            canvas3.create_text(80,20,text="not enough datapoints")
            print(x1)
            time.sleep(5)
            canvas3.delete('all')
            mainWindow.after(100, startProgram)
        else:

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


            plt.set_ylabel('Signal (Photons/second)')
            plt.set_xlabel('Timepoint (Minutes)')
            plt.set_title('All ROIs')
            plt.legend(loc='lower right')



            multipleGraph = Figure(figsize=(8, 6), dpi=100)

            with open(fileLocation, 'r') as fh:
                reader = csv.reader(fh)
                next(reader)

                x1, x2, x3, x4, x5 = ([] for i in range(5))
                y1, y2, y3, y4, y5 = ([] for i in range(5))

                for row in reader:
                    timePoint = (row[0])[-2:]
                    roi = (row[1])[-1]
                    signal = row[5]

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

                # Generate output graph for 1 ROI's
                if roi_count == 1:
                    ax1 = multipleGraph.add_subplot(221)
                    ax1.plot(x1, y1)
                    ax1.set_title('ROI 1')
                    ax1.set_ylabel("Signal")
                    ax1.set_xlabel("Time")

                # Generate output graph for 2 ROI's
                if roi_count == 2:
                    ax1 = multipleGraph.add_subplot(221)
                    ax1.plot(x1, y1)
                    ax1.set_title('ROI 1')
                    ax1.set_ylabel("Signal")
                    ax1.set_xlabel("Time")

                    ax2 = multipleGraph.add_subplot(222)
                    ax2.plot(x2, y2)
                    ax2.set_title('ROI 2')
                    ax2.set_xlabel("Time")

                # Generate output graph for 3 ROI's
                if roi_count == 3:
                    ax1 = multipleGraph.add_subplot(221)
                    ax1.plot(x1, y1)
                    ax1.set_title('ROI 1')
                    ax1.set_ylabel("Signal")
                    ax1.set_xlabel("Time")

                    ax2 = multipleGraph.add_subplot(222)
                    ax2.plot(x2, y2)
                    ax2.set_title('ROI 2')
                    ax2.set_xlabel("Time")

                    ax3 = multipleGraph.add_subplot(223)
                    ax3.plot(x3, y3)
                    ax3.set_title('ROI 3')
                    ax3.set_xlabel("Time")

                # Generate output graph for 4 ROI's
                if roi_count == 4:
                    ax1 = multipleGraph.add_subplot(221)
                    ax1.plot(x1, y1)
                    ax1.set_title('ROI 1')
                    ax1.set_ylabel("Signal")

                    ax2 = multipleGraph.add_subplot(222)
                    ax2.plot(x2, y2)
                    ax2.set_title('ROI 2')

                    ax3 = multipleGraph.add_subplot(223)
                    ax3.plot(x3, y3)
                    ax3.set_title('ROI 3')

                    ax4 = multipleGraph.add_subplot(224)
                    ax4.plot(x4, y4)
                    ax4.set_title('ROI 4')
                    ax4.set_xlabel("Time")
                    ax4.set_ylabel("Signal")

                # Generate output graph for 5 ROI's
                if roi_count == 5:
                    ax1 = multipleGraph.add_subplot(231)
                    ax1.plot(x1, y1)
                    ax1.set_title('ROI 1')
                    ax1.set_ylabel("Signal")

                    ax2 = multipleGraph.add_subplot(232)
                    ax2.plot(x2, y2)
                    ax2.set_title('ROI 2')

                    ax3 = multipleGraph.add_subplot(233)
                    ax3.plot(x3, y3)
                    ax3.set_title('ROI 3')

                    ax4 = multipleGraph.add_subplot(234)
                    ax4.plot(x4, y4)
                    ax4.set_title('ROI 4')
                    ax4.set_xlabel("Time")
                    ax4.set_ylabel("Signal")

                    ax5 = multipleGraph.add_subplot(235)
                    ax5.plot(x5, y5)
                    ax5.set_title('ROI 5')
                    ax5.set_xlabel("Time")

                canvas2 = FigureCanvasTkAgg(multipleGraph, master=mainWindow)
                canvas2.get_tk_widget().place(x=470, y=50)

        mainWindow.after(5000, startProgram)


######################################################################################################################
### ''' GUI Interface Setup '''
######################################################################################################################
# Main windows setup
mainWindow = Tk()  # Links main window to the interpreter
mainWindow.title("IVIS Peak Grabber by Kamil_Sokolowski")
mainWindow.geometry("1260x650+10+10")  # Window size and initial position
mainWindow['bg'] = 'white'  # Background colour

# Main buttons
Button(mainWindow, text="Open Export Location", command=selectDirectory, height=2, width=30).place(x=10, y=10)
Button(mainWindow, text="Start", command=startProgram, height=2, width=25).place(x=250, y=10)

mainWindow.mainloop()