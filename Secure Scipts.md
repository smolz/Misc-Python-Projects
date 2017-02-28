# Sort of better than nothing security

  		  
## Setup csv file
 - Create a file in the directory called pass.csv no column heading
 - Enter something you want to keep secret on each line
 
 
## Add to code
```
import csv
import os           # only needed if file is not in the same folder as script
cred_detail = []
os.chdir("Folder where the csv file is stored")
for row in csv.reader(open("pass.csv","rb")):       
        cred_detail.append(row)
```
## Use list elements in code
```
mqtt_user = cred_detail[0][0]
mqtt_pass = cred_detail[1][0]
mqtt_host = cred_detail[2][0]
```
