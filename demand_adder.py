import math
import json

# The way the game handles demand is within a demand_data.json file
# Every demand bubble has an id, location, job amount, and resident amount
# A population bubble can have residential population, job population, or both
# Every resident has a corresponding job trip

# Variable for the index of the residence_id and the work_id

# Function that checks whether the inputted id actually exists in the demand_data.json file

def check_if_id_exists(id):
    global index
    index = 0
    for i in file['points']:
        if id == i['id']:
            return True
        index += 1
    return False

# Get the file loaded

file_name = input("What is your file name?: ")
with open(file_name) as f:
    file = json.load(f)

    # Get the residence id

    res_id = input("Enter the residence id of the bubble you want to add residents to: ")
    if not check_if_id_exists(res_id):
        print("Your residence id was not found")
    else:
        res_index = index

        # Get the work id

        work_id = input("Enter the work id of the bubble you want to add jobs to: ")
        if not check_if_id_exists(work_id):
            print("Your work id was not found")
        else:
            work_index = index

            # Get how much demand to add and sanitize for integer

            is_int = False
            while not is_int:
                demand_to_add = input("How much demand do you want to add between these two bubbles? ")
                try:
                    demand_to_add = int(demand_to_add)
                    is_int = True
                except:
                    print("Hey, you must enter an integer")

            # Commutes are handled better by the game if split into chunks
            # Your commuters will be stranded if the chunk is larger than what the train car can fit
            # (ie 2400 is the upper upper limit)
            # Feel free to mess with the size_of_commuters variable, up to around 500 should be fine

            size_of_commuters = 100

            demand_div_size = int(math.floor(demand_to_add) / size_of_commuters)
            leftover_demand = demand_to_add % size_of_commuters

            # Gets the last pop id in the file so it can add new pop ids without repeating

            beginning_pop_id = len(file['pops'])

            # Loop through to add the commutes

            for i in range(1, demand_div_size + 1):
                file['points'][res_index]['popIds'].append(f"{beginning_pop_id + i}")
                file['points'][work_index]['popIds'].append(f"{beginning_pop_id + i}")
                file['pops'].append({
                    "id": f"{beginning_pop_id + i}",
                    "size": size_of_commuters,
                    "residenceId": res_id,
                    "jobId": work_id,
                    "drivingSeconds": 2000,
                    "drivingDistance": 25000
                })

            # Add the leftover demand into a separate commute if applicable
            
            if leftover_demand != 0:
                file['points'][res_index]['popIds'].append(f"{demand_div_size + beginning_pop_id + 1}")
                file['points'][work_index]['popIds'].append(f"{demand_div_size + beginning_pop_id + 1}")
                file['pops'].append({
                    "id": f"{demand_div_size + beginning_pop_id + 1}",
                    "size": leftover_demand,
                    "residenceId": res_id,
                    "jobId": work_id,
                    "drivingSeconds": 2000,
                    "drivingDistance": 25000
                })

            # Updates the residence and work ids to reflect the increased population

            file['points'][res_index]['residents'] += demand_to_add
            file['points'][work_index]['jobs'] += demand_to_add

            # Writes end result to the file

            with open(file_name, 'w') as output_file:
                json.dump(file, output_file, indent=2)