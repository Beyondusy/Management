import json
import time
import pandas as pd

# Function to load records from a file
def load_records():
    try:
        with open("records.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save records to a file
def save_records(records):
    with open("records.json", "w") as file:
        json.dump(records, file)

# Initialize a variable to track if the new field has been created
new_field_created = False

# Function to add a new record
def add_record(records):
    name = input("Enter Name: ")
    mobile = input("Enter Mobile Number: ")
    address = input("Enter Address: ")
    qualification = input("Enter Qualification: ")
    status = input("Enter Status: ")
    
    if new_field_created:
        new_field = input("Enter the New Field: ")
    else:
        new_field = ""  # Initialize the new field if not created
    
    records[name] = {
        "Mobile Number": mobile,
        "Address": address,
        "Qualification": qualification,
        "Status": status,
        "New Field": new_field  # Add the new field to the record
    }
    save_records(records)

# Function to delete a record
def delete_record(records, name):
    if name in records:
        del records[name]
        save_records(records)
        print(f"Record for {name} deleted.")
    else:
        print(f"Record for {name} not found.")

# Function to update an existing record
def update_record(records, name):
    if name in records:
        print(f"Updating record for {name}:")
        mobile = input(f"Enter New Mobile Number for {name}: ")
        address = input(f"Enter New Address for {name}: ")
        qualification = input(f"Enter New Qualification for {name}: ")
        status = input(f"Enter New Status for {name}: ")
        
        records[name]["Mobile Number"] = mobile
        records[name]["Address"] = address
        records[name]["Qualification"] = qualification
        records[name]["Status"] = status
        save_records(records)
    else:
        print(f"Record for {name} not found.")

# Function to find and show a record in a specific format
def find_record(records, name):
    if name in records:
        print(f"Record for {name}:\n")
        record_data = records[name]
        for key, value in record_data.items():
            print(f"{key:<15}: {value}")
        print("-" * 40)  # Add a separator line
    else:
        print(f"Record for {name} not found.")

# Load existing records from the file
records = load_records()


# Function to display all records with a readable format
def show_all_records(records):
    count = 0  # Initialize a counter for the number of records

    for name, data in records.items():
        print(f"Record for {name}:\n")
        for key, value in data.items():
            print(f"{key:<15}: {value}")
        print("-" * 40)  # Add a separator line
        print()  # Add two empty lines to separate records
        count += 1

    print(f"Number of recorded data: {count}\n")  # Display the number of recorded data


# Function to get mobile number by name
def get_mobile_number(records):
    name = input("Enter Name to retrieve mobile number: ")
    if name in records:
        print(f"Mobile Number for {name}: {records[name]['Mobile Number']}")
    else:
        print(f"Record for {name} not found.")


# Function to export data to an Excel file with a custom filename
def export_to_excel(records):
    custom_filename = input("Enter your Excel file name (without extension): ")
    filename = f"{custom_filename}.xlsx"  # Add the extension to the filename
    df = pd.DataFrame.from_dict(records, orient='index')
    df.to_excel(filename)
    print(f"Data exported to '{filename}'")


# Function to filter records by various criteria
def filter_records(records):
    print("\nFilter Options:")
    print("1. Filter By Name")
    print("2. Filter By Mobile Number")
    print("3. Filter By Address")
    print("4. Filter By Qualification")
    print("5. Filter By Status")
    
    filter_choice = input("Enter your filter choice (1-5): ")

    filtered_records = {}

    if filter_choice == "1":
        filter_value = input("Enter Name to filter by: ")
        for name, data in records.items():
            if filter_value.lower() in name.lower():
                filtered_records[name] = data
    elif filter_choice == "2":
        filter_value = input("Enter Mobile Number to filter by: ")
        for name, data in records.items():
            if filter_value in data.get("Mobile Number", ""):
                filtered_records[name] = data
    elif filter_choice == "3":
        filter_value = input("Enter Address to filter by: ")
        for name, data in records.items():
            if filter_value.lower() in data.get("Address", "").lower():
                filtered_records[name] = data
    elif filter_choice == "4":
        filter_value = input("Enter Qualification to filter by: ")
        for name, data in records.items():
            if filter_value.lower() in data.get("Qualification", "").lower():
                filtered_records[name] = data
    elif filter_choice == "5":
        filter_value = input("Enter Status to filter by: ")
        for name, data in records.items():
            if filter_value.lower() in data.get("Status", "").lower():
                filtered_records[name] = data
    else:
        print("Invalid filter choice.")
        return

    if not filtered_records:
        print("No records match the filter criteria.")
    else:
        show_all_records(filtered_records)


# Function to show data based on various sub-options
def show_data_options(records):
    while True:
        print("\nShow Data Options:")
        print("1. Name")
        print("2. Address")
        print("3. Mobile Number")
        print("4. Qualification")
        print("5. Status")
        print("6. Show Full Data")
        print("7. Export in Excel")
        print("8. Back to Main Menu")

        sub_choice = input("Enter your sub-choice: ")

        if sub_choice == "1":
            show_names(records)
        elif sub_choice == "2":
            show_addresses(records)
        elif sub_choice == "3":
            show_mobile_numbers(records)
        elif sub_choice == "4":
            show_qualifications(records)
        elif sub_choice == "5":
            show_statuses(records)
        elif sub_choice == "6":
            show_all_records(records)
        elif sub_choice == "7":
            export_to_excel_with_custom_name(records)
        elif sub_choice == "8":
            break
        else:
            print("Invalid sub-choice. Please select a valid option.")

# Function to show all recorded names with serial numbers
def show_names(records):
    print("\nRecorded Names:")
    for index, name in enumerate(records.keys(), start=1):
        print(f"{index}. {name}")

# Function to show all recorded addresses
def show_addresses(records):
    print("\nRecorded Addresses:")
    for name, data in records.items():
        print(f"{name}: {data['Address']}")

# Function to show all recorded mobile numbers
def show_mobile_numbers(records):
    print("\nRecorded Mobile Numbers:")
    for name, data in records.items():
        print(f"{name}: {data['Mobile Number']}")

# Function to show all recorded qualifications
def show_qualifications(records):
    print("\nRecorded Qualifications:")
    for name, data in records.items():
        print(f"{name}: {data['Qualification']}")

# Function to show all recorded statuses
def show_statuses(records):
    print("\nRecorded Statuses:")
    for name, data in records.items():
        print(f"{name}: {data['Status']}")

# Function to export data to an Excel file with a custom filename
def export_to_excel_with_custom_name(records):
    custom_filename = input("Enter your Excel file name (without extension): ")
    filename = f"{custom_filename}.xlsx"
    df = pd.DataFrame.from_dict(records, orient='index')
    df.to_excel(filename)
    print(f"Data exported to '{filename}'")


# Function to add a new field to existing records
def add_new_field(records):
    new_field_name = input("Enter the Name of the New Field: ")
    
    for name in records:
        new_field_value = input(f"Enter the value of the new field for {name}: ")
        records[name][new_field_name] = new_field_value
    
    save_records(records)

# Main menu
while True:
    print("\nHome Option Menu:")
    print("1. Record Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Find Data")
    print("5. Show Data")
    print("6. Get Mobile Number")
    print("7. Export In Excel")
    print("8. Filter")
    if not new_field_created:
        print("9. Add New Column for Record")  # Add the new option if the new field hasn't been created
    print("10. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_record(records)
    elif choice == "2":
        name = input("Enter Name to Update: ")
        update_record(records, name)
    elif choice == "3":
        name = input("Enter Name to Delete: ")
        delete_record(records, name)
    elif choice == "4":
        name = input("Enter Name to Find: ")
        find_record(records, name)
    elif choice == "5":
        show_data_options(records)
    elif choice == "6":
        get_mobile_number(records)
    elif choice == "7":
        export_to_excel(records)
    elif choice == "8":
        filter_records(records)
    elif choice == "9" and not new_field_created:
        add_new_field(records)  # Invoke the function to add a new field
        new_field_created = True  # Set the flag to indicate the new field has been created
    elif choice == "10":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")



# Function to add a new record with a timestamp
def add_record(records):
    name = input("Enter Name: ")
    mobile = input("Enter Mobile Number: ")
    address = input("Enter Address: ")
    qualification = input("Enter Qualification: ")
    status = input("Enter Status: ")
    
    # Get the current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    records[name] = {
        "Mobile Number": mobile,
        "Address": address,
        "Qualification": qualification,
        "Status": status,
        "Timestamp": timestamp  # Add the timestamp to the record
    }
    save_records(records)

