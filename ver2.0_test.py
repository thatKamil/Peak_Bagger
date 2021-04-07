def openCSV():
    # Get username for correct file directory
    username = getpass.getuser()
    print(username)

    # Create new directory on desktop where data will be read
    user_directory = r"C:\Users\" + username + r"\Desktop\IVIS_temp"

    newpath = r(user_directory)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    list_of_files = glob.glob(user_directory)  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    tf = lastest_file

    return tf