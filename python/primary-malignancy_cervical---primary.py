# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"23936.0","system":"med"},{"code":"2747.0","system":"med"},{"code":"28311.0","system":"med"},{"code":"3230.0","system":"med"},{"code":"32955.0","system":"med"},{"code":"43435.0","system":"med"},{"code":"48820.0","system":"med"},{"code":"50285.0","system":"med"},{"code":"50297.0","system":"med"},{"code":"53103.0","system":"med"},{"code":"57235.0","system":"med"},{"code":"57719.0","system":"med"},{"code":"58094.0","system":"med"},{"code":"95505.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_cervical-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["primary-malignancy_cervical---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["primary-malignancy_cervical---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["primary-malignancy_cervical---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
