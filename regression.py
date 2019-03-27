import csv

# Your code for regression here

if __name__ == "__main__":
    # Here, we load the boston dataset
    boston = csv.reader(open('boston.csv'))  # The boston housing dataset in csv format
    header = boston.next()  # First line contains the header, short info for each variable
    data, target = [], []  # Data will hold the 13 data variables, target is what we are trying to predict
    for row in boston:
        data.append(row[:-1])  # All but the last are the data points
        target.append(row[-1]) # The last is the median house value we are trying to predict
    # Now, use the dataset with your regression functions to answer the exercise questions
    print("Names of the columns")
    print(header)
    print("First row of data ->variable to predict")
    print(data[0], " -> ", target[0])

    # Plot, regression here

    # Example of writing out the R2.txt file, with 0.0 guess for coefficient of correlation
    fout = open('R2.txt', 'w')
    for i in range(13):
        R2 = 0.0  # Fill with the real value from your code
        fout.write('%f\n' % R2)  # One line per variable
    fout.close()
