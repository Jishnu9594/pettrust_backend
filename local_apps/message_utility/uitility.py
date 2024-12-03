# utils.py

import csv
from io import StringIO

def generate_leads_spreadsheet(lead_data_list):
    """
    Generate CSV spreadsheet from list of lead data.
    """
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=lead_data_list[0].keys())
    writer.writeheader()
    writer.writerows(lead_data_list)
    return output.getvalue()
