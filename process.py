# opening specified file
log_file = open("um-server-01.txt")

#function print out the entire lines for all the 'Mon' days
def sales_reports(log_file):    # defining a function called called_report
    for line in log_file:       # Looping through each line in the open file
        line = line.rstrip()    # removing the \n
        line = line.split(' ')
        # day = line[0:3]         # Setting the first 3 chars in open file to day

        if int(line[2]) > 10:        # If day is equal to 'Mon' print something
            print(line)         # print the line to the console.

sales_reports(log_file)         # calling the function with specified file
