"""
Script for validating email addresses
Author: Md Mehedi Hasan
Email: meheditrips@gmail.com
"""

import re
import pandas as pd
import os

def validate_emails() -> None:
    # Ask the user for the file path
    file_path = input("Please enter the path of your file: ")

    # Infer the file format from the file extension
    _, file_extension = os.path.splitext(file_path)
    file_format = file_extension[1:]  # Remove the leading '.'

    # Depending on the file format, we need to read the data differently
    if file_format == 'csv':
        emails = pd.read_csv(file_path, encoding='utf-8').iloc[:,0].str.lower().tolist()
    elif file_format == 'txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            emails = [line.strip().lower() for line in f]
    else:
        print(f"Unsupported file format: {file_format}")
        return

    # Regex pattern to match a valid email
    pattern = re.compile(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$')

    # Separate valid and bad emails using list comprehension
    valid_emails = [email for email in emails if pattern.match(email)]
    bad_emails = [email for email in emails if not pattern.match(email)]

    # Prepare output paths
    dir_path = os.path.dirname(file_path)
    valid_output_path = os.path.join(dir_path, 'valid_emails.txt')
    invalid_output_path = os.path.join(dir_path, 'invalid_emails.txt')

    # Save valid emails to a file
    with open(valid_output_path, 'w', encoding='utf-8') as f:
        for email in valid_emails:
            f.write(email + '\n')

    # Save invalid emails to a file
    with open(invalid_output_path, 'w', encoding='utf-8') as f:
        for email in bad_emails:
            f.write(email + '\n')

    print("---------------------%d emails are not correct----------------------------" % len(bad_emails))
    print("---------------------------------------------------------------------------")
    print(bad_emails)

# Usage:
validate_emails()
