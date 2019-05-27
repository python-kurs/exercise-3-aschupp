# Exercise 3
from pathlib import Path
import utils as u
import csv

# import functions from utils here

basedir = Path("C:/Users/Alex/Documents/GitHub/exercise-3-aschupp")
data_dir = Path("C:/Users/Alex/Documents/GitHub/exercise-3-aschupp/data")
output_dir = Path("C:/Users/Alex/Documents/GitHub/exercise-3-aschupp/solution")

print(basedir)
print(data_dir)
print(output_dir)

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]

cars_txt = Path(data_dir, "cars.txt")

# 2. Read the text file [2P]

all_cars=open(str(cars_txt), "r").read()

# 3. Count the occurences of each item in the text file [2P]

carslist = list(all_cars.split("\n"))
occ = u.countelem(carslist)    

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

Path("C:/Users/Alex/Documents/GitHub/exercise-3-aschupp/solution").mkdir(parents=True, exist_ok=True)

dir_ex = output_dir.exists
print("Verzeichnis vorhanden: {}".format(dir_ex))

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...

counts = output_dir/"counts.csv"

with open(counts, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["item", "count"]) 
    writer.writeheader()
    for key in occ.keys():
        file.write("%s,%s\n"%(key,occ[key]))