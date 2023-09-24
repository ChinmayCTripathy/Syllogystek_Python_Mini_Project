from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    try:
        # Open the file and iterate through each line

        with open(fileName, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                try:
                    # Split the line into patient data fields

                    patient_data = line.strip().split(',')
                    if len(patient_data) != 8:
                        raise ValueError(f"Invalid number of fields ({len(patient_data)}) in line: {line_num}")
                    
                    # Convert patient data to appropriate data types
                    
                    patient_id = int(patient_data[0])
                    date = patient_data[1]
                    temp = float(patient_data[2])
                    hr = int(patient_data[3])
                    rr = int(patient_data[4])
                    sbp = int(patient_data[5])
                    dbp = int(patient_data[6])
                    spo2 = int(patient_data[7])
                    
                    # Validate data values
                    
                    if not (35 <= temp <= 42):
                        raise ValueError(f"Invalid temperature value ({temp}) in line: {line_num}")
                    if not (30 <= hr <= 180):
                        raise ValueError(f"Invalid heart rate value ({hr}) in line: {line_num}")
                    if not (5 <= rr <= 40):
                        raise ValueError(f"Invalid respiratory rate value ({rr}) in line: {line_num}")
                    if not (70 <= sbp <= 200):
                        raise ValueError(f"Invalid systolic blood pressure value ({sbp}) in line: {line_num}")
                    if not (40 <= dbp <= 120):
                        raise ValueError(f"Invalid diastolic blood pressure value ({dbp}) in line: {line_num}")
                    if not (70 <= spo2 <= 100):
                        raise ValueError(f"Invalid oxygen saturation value ({spo2}) in line: {line_num}")
                    
                    # Append patient data to dictionary
                    
                    if patient_id not in patients:
                        patients[patient_id] = []
                    patients[patient_id].append([date, temp, hr, rr, sbp, dbp, spo2])
                
                except ValueError as ve:
                    print(ve)
                except Exception as e:
                    print(f"An unexpected error occurred while reading line {line_num}: {e}")
    
    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")
        
    return patients


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    try:
        # Display data for all patients or a specific patient

        if patientId == 0:
            for patient_id, visits in patients.items():
                print(f"Patient ID: {patient_id}")
                for visit in visits:
                    print(" Visit Date:", visit[0])
                    print(" " * 2, "Temperature:", "%.2f" % visit[1], "C")
                    print(" " * 2, "Heart Rate:", visit[2], "bpm")
                    print(" " * 2, "Respiratory Rate:", visit[3], "bpm")
                    print(" " * 2, "Systolic Blood Pressure:", visit[4], "mmHg")
                    print(" " * 2, "Diastolic Blood Pressure:", visit[5], "mmHg")
                    print(" " * 2, "Oxygen Saturation:", visit[6], "%")
                    print()
        else:
            # Display data for a specific patient

            if patientId in patients:
                print(f"Patient ID: {patientId}")
                for visit in patients[patientId]:
                    print(" Visit Date:", visit[0])
                    print(" " * 2, "Temperature:", "%.2f" % visit[1], "C")
                    print(" " * 2, "Heart Rate:", visit[2], "bpm")
                    print(" " * 2, "Respiratory Rate:", visit[3], "bpm")
                    print(" " * 2, "Systolic Blood Pressure:", visit[4], "mmHg")
                    print(" " * 2, "Diastolic Blood Pressure:", visit[5], "mmHg")
                    print(" " * 2, "Oxygen Saturation:", visit[6], "%")
                    print()
            else:
                print(f"Patient with ID {patientId} not found.")
    except Exception as e:
        print("An error occurred:", e)



def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    try:
        patientId = int(patientId)  # Convert patientId to an integer
        # Display statistics for all patients or a specific patient
        
        if patientId == 0:
            print("Vital Signs for All Patients:")
            # Calculate and display average values
            num_patients = len(patients)
            temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = spo2_sum = 0
            num_visits = 0
            for visits in patients.values():
                for visit in visits:
                    num_visits += 1
                    temp_sum += visit[1]
                    hr_sum += visit[2]
                    rr_sum += visit[3]
                    sbp_sum += visit[4]
                    dbp_sum += visit[5]
                    spo2_sum += visit[6]
            if num_visits == 0:
                print("No data found")
                return
            print(" Average temperature:", "%.2f" % (temp_sum / num_visits), "C")
            print(" Average heart rate:", "%.2f" % (hr_sum / num_visits), "bpm")
            print(" Average respiratory rate:", "%.2f" % (rr_sum / num_visits), "bpm")
            print(" Average systolic blood pressure:", "%.2f" % (sbp_sum / num_visits), "mmHg")
            print(" Average diastolic blood pressure:", "%.2f" % (dbp_sum / num_visits), "mmHg")
            print(" Average oxygen saturation:", "%.2f" % (spo2_sum / num_visits), "%")
        else:
            # Display statistics for a specific patient
            if patientId in patients:
                print(f"Vital Signs for Patient {patientId}:")
                visits = patients[patientId]
                num_visits = len(visits)
                if num_visits == 0:
                    print("No data found")
                    return
                temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = spo2_sum = 0
                for visit in visits:
                    temp_sum += visit[1]
                    hr_sum += visit[2]
                    rr_sum += visit[3]
                    sbp_sum += visit[4]
                    dbp_sum += visit[5]
                    spo2_sum += visit[6]
                print(" Average temperature:", "%.2f" % (temp_sum / num_visits), "C")
                print(" Average heart rate:", "%.2f" % (hr_sum / num_visits), "bpm")
                print(" Average respiratory rate:", "%.2f" % (rr_sum / num_visits), "bpm")
                print(" Average systolic blood pressure:", "%.2f" % (sbp_sum / num_visits), "mmHg")
                print(" Average diastolic blood pressure:", "%.2f" % (dbp_sum / num_visits), "mmHg")
                print(" Average oxygen saturation:", "%.2f" % (spo2_sum / num_visits), "%")
            else:
                print(f"Patient with ID {patientId} not found.")
    except ValueError:
        raise ValueError("Error: 'patientId' should be an integer.")
    except Exception as e:
        print("An error occurred:", e)



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    try:
        # Validate patient ID
        if not str(patientId).isdigit() or int(patientId) <= 0:
            raise ValueError("Invalid patient ID. Please enter a positive integer.")
        
        # Validate date format using regular expression
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            raise ValueError("Invalid date format. Please enter date in the format 'yyyy-mm-dd'.")
        
        # Validate date values
        year, month, day = map(int, date.split('-'))
        if not (1900 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError("Invalid date. Please enter a valid date.")
        
        # Validate temperature
        if not (35.0 <= float(temp) <= 42.0):
            raise ValueError("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
        
        # Validate heart rate
        if not (30 <= int(hr) <= 180):
            raise ValueError("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
        
        # Validate respiratory rate
        if not (5 <= int(rr) <= 40):
            raise ValueError("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
        
        # Validate systolic blood pressure
        if not (70 <= int(sbp) <= 200):
            raise ValueError("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
        
        # Validate diastolic blood pressure
        if not (40 <= int(dbp) <= 120):
            raise ValueError("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
        
        # Validate oxygen saturation
        if not (70 <= int(spo2) <= 100):
            raise ValueError("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
        
        # Append new data to patients dictionary
        new_visit = [date, temp, hr, rr, sbp, dbp, spo2]
        if int(patientId) in patients:
            patients[int(patientId)].append(new_visit)
        else:
            patients[int(patientId)] = [new_visit]
        
        # Append new data to file
        with open(fileName, 'a') as file:
            file.write(f"\n{patientId},{','.join(map(str, new_visit))}")
        
        # Display success message
        print(f"Visit is saved successfully for Patient #{patientId}")
    
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An unexpected error occurred while adding new data:", e)



def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    #######################
    #### PUT YOUR CODE HERE
    #######################
    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    #######################
    #### PUT YOUR CODE HERE
    #######################
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    #######################
    #### PUT YOUR CODE HERE
    #######################




###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
