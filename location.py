import csv
from geopy.geocoders import Nominatim

# Initialize the geocoder
geolocator = Nominatim(user_agent="university-locator")

# Open the input CSV file
with open('cities.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)
    
    # Skip the header row
    next(csv_reader)
    
    # Create a list to store the updated rows
    updated_rows = []
    
    # Iterate through each row in the CSV
    for row in csv_reader:
        pk, name, location = row
        # Find the location details using the university name
        location_details = geolocator.geocode(name)
        
        if location_details:
            # Extract the city from the location details
            city = location_details.raw.get("address", {}).get("city", "")
        else:
            # If the location cannot be found, set the city as "Unknown"
            city = "Unknown"
        
        # Append the updated row with the city information
        updated_row = [pk, name, location, city]
        updated_rows.append(updated_row)

# Write the updated data to a new CSV file
with open('universities_with_cities.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    
    # Write the header row
    csv_writer.writerow(['pk', 'name', 'location', 'city'])
    
    # Write the updated rows
    csv_writer.writerows(updated_rows)
    
print("City information added to universities_with_cities.csv")
