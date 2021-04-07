import csv
import matplotlib.pyplot as plt

with open('../Data/Example4.csv', 'r') as fh:
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

    # Output for 4 ROI's
    if roi_count == 4:
        ax1 = plt.subplot(221)
        ax1.plot(x1, y1, color='C1')
        ax1.set_title('ROI 1')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Signal')

        ax2 = plt.subplot(222)
        ax2.plot(x2, y2)
        ax2.set_title('ROI 2')

        ax3 = plt.subplot(223)
        ax3.plot(x3, y3)
        ax3.set_title('ROI 3')

        ax4 = plt.subplot(224)
        ax4.plot(x4, y4)
        ax4.set_title('ROI 4')

    # Output for 5 ROI's
    if roi_count == 5:
        ax1 = plt.subplot(231)
        ax1.plot(x1, y1)
        ax1.set_title('ROI 1')

        ax2 = plt.subplot(232)
        ax2.plot(x1, y1)
        ax2.set_title('ROI 2')

        ax3 = plt.subplot(233)
        ax3.plot(x1, y1)
        ax3.set_title('ROI 3')

        ax4 = plt.subplot(234)
        ax4.plot(x1, y1)
        ax4.set_title('ROI 4')

        ax5 = plt.subplot(235)
        ax5.plot(x1, y1)
        ax5.set_title('ROI 5')

    plt.suptitle('IVIS Plateau Graphs')
    plt.legend()
    plt.show()