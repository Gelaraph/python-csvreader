"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

import csv


def read_csv_fieldnames(filename, separator, quote):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=separator, quotechar=quote)
        return reader.fieldnames



def read_csv_as_list_dict(filename, separator, quote):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=separator, quotechar=quote)
        return list(reader)


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    nested_dict = {}
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=separator, quotechar=quote)
        for row in reader:
            nested_dict[row[keyfield]] = row
    return nested_dict


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=separator, quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in table:
            writer.writerow(row)
