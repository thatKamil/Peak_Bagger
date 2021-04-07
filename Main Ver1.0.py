######################################################################################################################
### Initialisation
######################################################################################################################

from tkinter import *
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt


######################################################################################################################
### Functions
######################################################################################################################
def openCSV():
    csvPath.delete("1.0", "end")

    tf1 = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Csv file",
        filetypes=(("Csv File", "*.csv"),)
        )

    csvPath.insert(END, tf1) # Writes path address to text box in GUI



def singleGraph():
    tf = csvPath.get(1.0, END)
    tf1 = tf[:-1]
    with open(tf1, 'r') as fh:
        reader = csv.reader(fh)
        next(reader)

        x1, x2, x3, x4, x5 = ([] for i in range(5))
        y1, y2, y3, y4, y5 = ([] for i in range(5))

        for row in reader:
            time = (row[0])[-2:]
            roi = (row[1])[-1]
            signal = row[5]

            if roi == '1':
                x1.append(int(time))
                y1.append(float(signal))
            if roi == '2':
                x2.append(int(time))
                y2.append(float(signal))
            if roi == '3':
                x3.append(int(time))
                y3.append(float(signal))
            if roi == '4':
                x4.append(int(time))
                y4.append(float(signal))
            if roi == '5':
                x5.append(int(time))
                y5.append(float(signal))

        roi_count = 0

        if len(x1) > 0:
            plt.plot(x1, y1, label='ROI 1')
            roi_count += 1
        if len(x2) > 0:
            plt.plot(x2, y2, label='ROI 2')
            roi_count += 1
        if len(x3) > 0:
            plt.plot(x3, y3, label='ROI 3')
            roi_count += 1
        if len(x4) > 0:
            plt.plot(x4, y4, label='ROI 4')
            roi_count += 1
        if len(x5) > 0:
            plt.plot(x5, y5, label='ROI 5')
            roi_count += 1

        print(roi_count)

        plt.ylabel('Signal (Photons/second)')
        plt.xlabel('Timepoint (Minutes)')
        plt.title('IVIS Signal Peak')
        plt.legend()

        plt.show()

def multipleGraphs():
    tf = csvPath.get(1.0, END)
    tf1 = tf[:-1]

    with open(tf1, 'r') as fh:
        reader = csv.reader(fh)
        next(reader)

        x1, x2, x3, x4, x5 = ([] for i in range(5))
        y1, y2, y3, y4, y5 = ([] for i in range(5))

        for row in reader:
            time = (row[0])[-2:]
            roi = (row[1])[-1]
            signal = row[5]

            if roi == '1':
                x1.append(int(time))
                y1.append(float(signal))
            if roi == '2':
                x2.append(int(time))
                y2.append(float(signal))
            if roi == '3':
                x3.append(int(time))
                y3.append(float(signal))
            if roi == '4':
                x4.append(int(time))
                y4.append(float(signal))
            if roi == '5':
                x5.append(int(time))
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
            plt.subplots(figsize=(7, 7))
            plt.tight_layout(h_pad=2)
            plt.subplots_adjust(top=0.85, bottom=.12, left=.1)

            ax1 = plt.subplot(111)
            ax1.plot(x1, y1)
            ax1.set_title('ROI 1')
            ax1.set_ylabel("Signal")
            ax1.set_xlabel("Time")

        # Generate output graph for 2 ROI's
        if roi_count == 2:
            plt.subplots(figsize=(10, 4))
            plt.tight_layout(h_pad=2)
            plt.subplots_adjust(top=0.85, bottom=.12, left=.1)

            ax1 = plt.subplot(121)
            ax1.plot(x1, y1)
            ax1.set_title('ROI 1')
            ax1.set_ylabel("Signal")
            ax1.set_xlabel("Time")

            ax2 = plt.subplot(122)
            ax2.plot(x2, y2)
            ax2.set_title('ROI 2')
            ax2.set_xlabel("Time")

        # Generate output graph for 3 ROI's
        if roi_count == 3:
            plt.subplots(figsize=(10, 4))
            plt.tight_layout(h_pad=2)
            plt.subplots_adjust(top=0.85, bottom=.12, left=.1)

            ax1 = plt.subplot(131)
            ax1.plot(x1, y1)
            ax1.set_title('ROI 1')
            ax1.set_ylabel("Signal")
            ax1.set_xlabel("Time")

            ax2 = plt.subplot(132)
            ax2.plot(x2, y2)
            ax2.set_title('ROI 2')
            ax2.set_xlabel("Time")

            ax3 = plt.subplot(133)
            ax3.plot(x3, y3)
            ax3.set_title('ROI 3')
            ax3.set_xlabel("Time")

        # Generate output graph for 4 ROI's
        if roi_count == 4:
            fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 7))
            fig.tight_layout(h_pad=2)
            plt.subplots_adjust(top=0.92, bottom=.09, left=.1)

            axes[0, 0].set_title("ROI 1")
            axes[0, 0].plot(x1, y1, color='C0')
            axes[0, 0].set_ylabel("Signal")

            axes[0, 1].set_title("ROI 2")
            axes[0, 1].plot(x2, y2, color='C0')

            axes[1, 0].set_title("ROI 3")
            axes[1, 0].plot(x3, y3, color='C0')
            axes[1, 0].set_xlabel("Time")
            axes[1, 0].set_ylabel("Signal")

            axes[1, 1].set_title("ROI 4")
            axes[1, 1].plot(x4, y4, color='C0')
            axes[1, 1].set_xlabel("Time")

        # Generate output graph for 5 ROI's
        if roi_count == 5:
            plt.subplots(figsize=(10, 7))
            plt.tight_layout(h_pad=2)
            plt.subplots_adjust(top=0.9, bottom=.09, left=.1)

            ax1 = plt.subplot(231)
            ax1.plot(x1, y1)
            ax1.set_title('ROI 1')
            ax1.set_ylabel("Signal")

            ax2 = plt.subplot(232)
            ax2.plot(x2, y2)
            ax2.set_title('ROI 2')

            ax3 = plt.subplot(233)
            ax3.plot(x3, y3)
            ax3.set_title('ROI 3')

            ax4 = plt.subplot(234)
            ax4.plot(x4, y4)
            ax4.set_title('ROI 4')
            ax4.set_xlabel("Time")
            ax4.set_ylabel("Signal")

            ax5 = plt.subplot(235)
            ax5.plot(x5, y5)
            ax5.set_title('ROI 5')
            ax5.set_xlabel("Time")

        plt.suptitle('IVIS Plateau Graphs')
        plt.show()

######################################################################################################################
### ''' GUI Interface Setup '''
######################################################################################################################
# Main windows setup
ws = Tk()   # Links main window to the interpreter
ws.title("IVIS Plateua Visualiser by Kamil_Sokolowski")
ws.geometry("410x300+500+10") # Window size and initial position
ws['bg']='khaki1' # Background colour

# Log file path output text areas
csvPath = Text(ws, width=48, height=1, bg='old lace')
csvPath.place(x=10, y=60)

# Main buttons
Button(ws, text="Open CSV", command=openCSV, height=2, width=30).place(x=100, y=10)
Button(ws, text="Single Graph", command=singleGraph, height=2, width=25).place(x=9, y=90)
Button(ws, text="Multiple Graphs", command=multipleGraphs, height=2, width=25).place(x=210, y=90)

ws.mainloop()