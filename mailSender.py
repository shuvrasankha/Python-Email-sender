import smtplib as s
ob =s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("email_id","password")
subject="Sending using python"
body="Hello , this is Shuvrasankha . !!!!"

message="Subject:{}\n\n{}".format(subject,body)



listOfAddress=["shuvrasankha1@gmail.com","debasish828313@gmail.com","Saikatanddustu@gmail.com"]
ob.sendmail("shuvrasankha.sp@gmail.com",listOfAddress,message)

print('Send successfully ')
ob.quit()
