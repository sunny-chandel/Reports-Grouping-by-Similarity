# Reports-Grouping-by-Similarity
Reports of tools like PowerBI, MSTR , SSRS etc

The code reads in a CSV file containing pairs of related reports and groups them together based on their relatedness. It then writes the groups to a new CSV file, where each row represents a group and each column represents a report within that group. If a group does not have enough reports to fill all of the columns, the remaining cells are left blank.

# The main steps of the code are as follows:

  1.	Open the input CSV file using the csv.reader() function.
  2.	Create a dictionary to store related reports.
  3.	Iterate through each row in the CSV file, checking if it contains exactly two values. If not, skip the row. Otherwise, add the reports to the related         reports dictionary if they are related, and group them together if they are already in a group or create a new group if neither of them is in a group.
  4.	Open the output CSV file using the csv.writer() function.
  5.	Write the header row, which includes the names of the columns.
  6.	Iterate through each group, write each group to a row in the output CSV file. If a group does not have enough reports to fill all of the columns, leave       the remaining cells blank.

