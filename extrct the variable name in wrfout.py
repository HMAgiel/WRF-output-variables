from netCDF4 import Dataset
from wrf import getvar

# Specify the path to your WRF output file
wrfout_file = "wrfout_d01_2024-01-01_00:00:00" #use the wrfoutput file

# Specify the output text file path
output_file = "variables_list.txt"

# Open the WRF output file
ncfile = Dataset(wrfout_file)

# List all variables in the WRF output file
variables = list(ncfile.variables.keys())

# Save variables to a text file in a single line
with open(output_file, "w") as f:
    f.write(", ".join(variables))

# Print a success message
print(f"Variable names have been written to {output_file} in a single line.")

# Close the file
ncfile.close()
