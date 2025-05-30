import openpyxl


def save_to_excel(data, filename):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Salons Data"
    ws.append(
        [
            "Salon Name",
            "Address",
            "Phone Number",
            "Website",
            "Rating",
            "Number of Reviews",
            "Opening Hours",
            "Google Maps URL",
        ]
    )
    for row in data:
        ws.append(row)
    wb.save(filename)
