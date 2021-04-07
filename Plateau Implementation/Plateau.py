import csv
import matplotlib.pyplot as plt

with open('../Data/example8.1.csv', 'r') as fh:
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

    roi_count = 0
    if len(x1) > 0:
        roi_count += 1

    plateauFlag = False

    if len(y1) > 5:
        ROIsToCheck = len(y1) - 5
        newList = y1[:ROIsToCheck]
        for i in newList:
            if float(y1[-1]) < float(i):
                plateauFlag = True

    # Generate output graph for 1 ROI's
    if roi_count == 1:
        plt.subplots(figsize=(7, 7))
        plt.tight_layout(h_pad=2)
        plt.subplots_adjust(top=0.85, bottom=.12, left=.1)

        ax1 = plt.subplot(111)
        if plateauFlag == True:
            ax1.plot(x1, y1, marker='o', color='red')
        else:
            ax1.plot(x1, y1, marker='o',color='green')
        ax1.set_title('ROI 1')
        ax1.set_ylabel("Signal")
        ax1.set_xlabel("Time")
        ax1.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

    plt.suptitle('IVIS Plateau Graphs')
    plt.show()