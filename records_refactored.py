##!/usr/bin/env python3
import json
import pandas as pd
from pandas import DataFrame 
import argparse

def parse_args():
    ap = argparse.ArgumentParser(description='Accepts JSON file of student records and returns passing students',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument( 'json_file', help='Student records in JSON format')
    return ap.parse_args()

ARGS = parse_args()


with open(ARGS.json_file) as json_data:
    data = json.load(json_data)
    
records = []

for record in data['report']:
    name = record['name']
    enroll = record['enrollment']
        
    for fields in record['subject']:
        code = fields['code']
        grade = fields['grade']
        
        if grade != 'F':
            records.append([
            code,
            grade,
            enroll,
            name
            ])

#create dataframe of passing student records and sort accordingly
df = DataFrame.from_records(records,columns=['codes','grades','enroll','name'])
df = df.sort_values(by=['codes', 'grades','enroll','name'])

#iterate over df and print values 
for index, row in df.iterrows():
    print(row['codes'], row['grades'], row['enroll'], row['name'])
