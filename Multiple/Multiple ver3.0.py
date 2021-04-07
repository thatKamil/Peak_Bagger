######################################################################################################################
### Version 3.0
######################################################################################################################
# Graph changes colour if plateuing

import csv
import matplotlib.pyplot as plt

with open('../Data/example5.csv', 'r') as fh:
    reader = csv.reader(fh)
    next(reader)

    # Creates the plot points for the maximum of five potential ROI's
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

    # Determine number of ROI's by checking if there's anything in the
    # corresponding ROI signal list.
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

    # Plateau flag starts as false.
    plateauFlag1 = False
    plateauFlag2 = False
    plateauFlag3 = False
    plateauFlag4 = False
    plateauFlag5 = False

    # Determines the time after the most up to date signal
    # is the comparison list
    plateuaTimeLag = 5

    # Determines if signal data reaches my criteria of a plateua for
    if len(y1) > plateuaTimeLag:
        roi1Length = len(y1) - 5
        newList1 = y1[:roi1Length]
        for i in newList1:
            if float(y1[-1]) < float(i):
                plateauFlag1 = True
    if len(y2) > plateuaTimeLag:
        roi2Length = len(y2) - 5
        newList2 = y2[:roi2Length]
        for i in newList2:
            if float(y2[-1]) < float(i):
                plateauFlag2 = True
    if len(y3) > plateuaTimeLag:
        roi3Length = len(y3) - 5
        newList3 = y3[:roi3Length]
        for i in newList3:
            if float(y3[-1]) < float(i):
                plateauFlag3 = True
    if len(y4) > plateuaTimeLag:
        roi4Length = len(y4) - 5
        newList4 = y4[:roi4Length]
        for i in newList4:
            if float(y4[-1]) < float(i):
                plateauFlag4 = True
    if len(y5) > plateuaTimeLag:
        roi5Length = len(y5) - 5
        newList5 = y5[:roi5Length]
        for i in newList5:
            if float(y5[-1]) < float(i):
                plateauFlag5 = True

    # Generate output graph for 1 ROI's
    if roi_count == 1:
        plt.subplots(figsize=(7, 7))
        plt.tight_layout(h_pad=2)
        plt.subplots_adjust(top=0.85, bottom=.12, left=.1)

        ax1 = plt.subplot(111)
        if plateauFlag1 == True:
            ax1.plot(x1, y1, marker='o', color='red')
        else:
            ax1.plot(x1, y1, marker='o', color='green')
        ax1.set_title('ROI 1')
        ax1.set_ylabel("Signal")
        ax1.set_xlabel("Time")
        ax1.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)


    # Generate output graph for 2 ROI's
    if roi_count == 2:
        plt.subplots(figsize=(10, 4))
        plt.tight_layout(h_pad=2)
        plt.subplots_adjust(top=0.85, bottom=.12, left=.1)

        ax1 = plt.subplot(121)
        if plateauFlag1 == True:
            ax1.plot(x1, y1, marker='o', color='red')
        else:
            ax1.plot(x1, y1, marker='o', color='green')
        ax1.set_title('ROI 1')
        ax1.set_ylabel("Signal")
        ax1.set_xlabel("Time")
        ax1.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

        ax2 = plt.subplot(122)
        if plateauFlag2 == True:
            ax2.plot(x2, y2, marker='o', color='red')
        else:
            ax2.plot(x2, y2, marker='o', color='green')
        ax2.set_title('ROI 2')
        ax2.set_xlabel("Time")
        ax2.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)


    # Generate output graph for 3 ROI's
    if roi_count == 3:
        plt.subplots(figsize=(10, 4))
        plt.tight_layout(h_pad=2)
        plt.subplots_adjust(top=0.85, bottom=.12, left=.1)

        ax1 = plt.subplot(131)
        if plateauFlag1 == True:
            ax1.plot(x1, y1, marker='o', color='red')
        else:
            ax1.plot(x1, y1, marker='o', color='green')
        ax1.set_title('ROI 1')
        ax1.set_ylabel("Signal")
        ax1.set_xlabel("Time")
        ax1.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

        ax2 = plt.subplot(132)
        if plateauFlag2 == True:
            ax2.plot(x2, y2, marker='o', color='red')
        else:
            ax2.plot(x2, y2, marker='o', color='green')
        ax2.set_title('ROI 2')
        ax2.set_xlabel("Time")
        ax2.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

        ax3 = plt.subplot(133)
        if plateauFlag3 == True:
            ax3.plot(x3, y3, marker='o', color='red')
        else:
            ax3.plot(x3, y3, marker='o', color='green')
        ax3.set_title('ROI 3')
        ax3.set_xlabel("Time")
        ax3.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

    # Generate output graph for 4 ROI's
    if roi_count == 4:
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 7))
        fig.tight_layout(h_pad=2)
        plt.subplots_adjust(top=0.92, bottom=.09, left=.1)

        if plateauFlag1 == True:
            axes[0, 0].plot(x1, y1, marker='o', color='red')
        else:
            axes[0, 0].plot(x1, y1, marker='o',color='green')
        axes[0, 0].set_title("ROI 1")
        axes[0, 0].set_ylabel("Signal")
        axes[0, 0].grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

        if plateauFlag2 == True:
            axes[0, 1].plot(x2, y2, marker='o', color='red')
        else:
            axes[0, 1].plot(x2, y2, marker='o', color='green')
        axes[0, 1].set_title("ROI 2")
        axes[0, 1].grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

        axes[1, 0].set_title("ROI 3")
        if plateauFlag3 == True:
            axes[1, 0].plot(x3, y3, marker='o', color='red')
        else:
            axes[1, 0].plot(x3, y3, marker='o', color='green')
        axes[1, 0].set_xlabel("Time")
        axes[1, 0].set_ylabel("Signal")
        axes[1, 0].grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

        axes[1, 1].set_title("ROI 4")
        if plateauFlag3 == True:
            axes[1, 1].plot(x4, y4, marker='o', color='red')
        else:
            axes[1, 1].plot(x4, y4, marker='o', color='green')
        axes[1, 1].set_xlabel("Time")
        axes[1, 1].grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)


    # Generate output graphs for 5 ROI's
    if roi_count == 5:
        plt.subplots(figsize=(10, 7))
        plt.tight_layout(h_pad=2)
        plt.subplots_adjust(top=0.9, bottom=.09, left=.1)

        ax1 = plt.subplot(231)
        if plateauFlag1 == True:
            ax1.plot(x1, y1, marker='o', color='red')
        else:
            ax1.plot(x1, y1, marker='o', color='green')
        ax1.set_title('ROI 1')
        ax1.set_ylabel("Signal")
        ax1.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

        ax2 = plt.subplot(232)
        if plateauFlag2 == True:
            ax2.plot(x2, y2, marker='o', color='red')
        else:
            ax2.plot(x2, y2, marker='o', color='green')
        ax2.set_title('ROI 2')
        ax2.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

        ax3 = plt.subplot(233)
        if plateauFlag3 == True:
            ax3.plot(x3, y3, marker='o', color='red')
        else:
            ax3.plot(x3, y3, marker='o', color='green')
        ax3.set_title('ROI 3')
        ax3.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

        ax4 = plt.subplot(234)
        if plateauFlag4 == True:
            ax4.plot(x4, y4, marker='o', color='red')
        else:
            ax4.plot(x4, y4, marker='o', color='green')
        ax4.set_title('ROI 4')
        ax4.set_xlabel("Time")
        ax4.set_ylabel("Signal")
        ax4.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

        ax5 = plt.subplot(235)
        if plateauFlag5 == True:
            ax5.plot(x5, y5, marker='o', color='red')
        else:
            ax5.plot(x5, y5, marker='o', color='green')
        ax5.set_title('ROI 5')
        ax5.set_xlabel("Time")
        ax5.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

    plt.suptitle('IVIS Plateau Program')
    plt.show()