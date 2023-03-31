#!/usr/bin/env python
# coding: utf-8

# In[53]:


import csv

grouped_reports = []
max_group_size = 0

with open(r"C:\Users\sunny.chandel\Desktop\SSRS\Similarity_0_to_29.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Create a dictionary to store the related reports
    related_reports = {}
    for row in csv_reader:
        # Skip any rows that do not have exactly two values
        if len(row) != 2:
            continue
        report1, report2 = row
        # Check if report1 is already in a group
        for group in grouped_reports:
            if report1 in group:
                group.append(report2)
                # Check if report2 is already in a group
                for report in group:
                    if report != report1 and report in related_reports:
                        group += related_reports[report]
                        del related_reports[report]
                break
        # Check if report2 is already in a group
        for group in grouped_reports:
            if report2 in group:
                group.append(report1)
                # Check if report1 is already in a group
                for report in group:
                    if report != report2 and report in related_reports:
                        group += related_reports[report]
                        del related_reports[report]
                break
        # If neither report is in a group, create a new group
        else:
            grouped_reports.append([report1, report2])
        # Store the related reports in the dictionary
        if report1 == report2:
            if report1 in related_reports:
                related_reports[report1].append(report2)
            else:
                related_reports[report1] = [report2]
        # Update the maximum group size
        max_group_size = max(max_group_size, len(grouped_reports[-1]))

# Write the groups to a new CSV file
with open(r"C:\Users\sunny.chandel\Desktop\SSRS\Grouped_reports_0_to_29.csv", 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header row
    header_row = ['Group Name']
    for i in range(1, max_group_size + 1):
        header_row.append('Report ' + str(i))
    csv_writer.writerow(header_row)
    # Write the data rows
    for i, group in enumerate(grouped_reports):
        row = ['Group ' + str(i+1)] + group
        # Add blank cells to pad the row to the correct length
        row += [''] * (max_group_size - len(group))
        csv_writer.writerow(row)


# In[ ]:




