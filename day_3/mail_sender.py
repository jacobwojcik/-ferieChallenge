import csv, smtplib, ssl, time, yagmail

list_of_receivers={}

with open('database.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count=0
    for row in csv_reader:
        if line_count>0:
            name=row[1].split()
            list_of_receivers[row[0]]=name
        line_count+=1
      
#mail sending

message="""Hi {name}! It's a file for you!"""

yag = yagmail.SMTP("testcodeandfun@gmail.com")

for mail in list_of_receivers:
    receiver=mail
    filename="images/{name}_{surname}_image.png"
    try:
        yag.send(
        to=receiver,
        subject="Your image",
        contents=message.format(name=list_of_receivers[mail][0]), 
        attachments=filename.format(name=list_of_receivers[mail][0],surname=list_of_receivers[mail][1]),
        )
        print("Email has been sent succesfully!")

    except:
        print("Error occurred while sending email")

