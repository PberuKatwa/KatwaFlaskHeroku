# csv_export.py
import csv


def export_to_csv(client):
    csv_file_path = 'data.csv'
    with open(csv_file_path, 'a', newline='') as csvfile:
        fieldnames = ['client_name', 'client_email', 'client_phone', 'client_legal_service', 'client_case_filed',
                      'client_additional_information']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if file is empty and write header
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'client_name': client.client_name,
            'client_email': client.client_email,
            'client_phone': client.client_phone,
            'client_legal_service': client.client_legal_service,
            'client_case_filed': client.client_case_filed,
            'client_additional_information': client.client_additional_information
        })
