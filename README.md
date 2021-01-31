# TempUpload

Initial project repository for a RaspberryPi with sensors.  Starting off with temperature for now.

tempread.py was the original code that reads the temperature and prints it out on the screen
tempupload.py Runs every 30 seconds and makes a call to API Gateway which stores the values in DynamoDB (for now) 

The tempupload.py code expects a file called temp.ini with the values for API gateway URL and key as follows: 
[api]
url = https://your-api-gateway-url
key = your-api-key
