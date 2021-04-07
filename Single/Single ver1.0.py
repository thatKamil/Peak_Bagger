import csv
import matplotlib.pyplot as plt

with open('../Data/example2.csv', 'r') as fh:
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