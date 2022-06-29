from fileinput import filename
import pyrebase
import urllib.request

firebaseConfig = {
    'apiKey': "AIzaSyAttWDnwWsv4c5LiEhf_hMbb16tNCRcB58",
    'authDomain': "fir-course-23ffa.firebaseapp.com",
    "databaseURL": "https://fir-course-23ffa-default-rtdb.firebaseio.com/",
    'projectId': "fir-course-23ffa",
    'storageBucket': "fir-course-23ffa.appspot.com",
    'messagingSenderId': "9010692408",
    'appId': "1:9010692408:web:ba98887fa35cbae571c1cd",
    'measurementId': "G-5FXP21K5JY"
    
}
firebase=pyrebase.initialize_app(firebaseConfig)


db=firebase.database()
auth=firebase.auth()
storage=firebase.storage()

# Authentification
# LogIN

email=input("Enter your email")
password=input("Enter your password")
try:
    auth.sign_in_with_email_and_password(email,password)
    print("SignIn successfuly")
except:
    print("Invalid user of password. Try again!")


####################################


#SignUp

email=input("Enter your email")
password=input("Enter your password")
confirmpass=input("Confirm password")
if password==confirmpass:
    try:
        auth.create_user_with_email_and_password(email,password)
        print("Success!")
    except:
        print("Email already exist")


#####################################

#Storage

filename=input("Enter the name of the file you want to upload")
cloudfilename=input("Enter the name of the file on the cloud")
storage.child(cloudfilename).put(filename)

print(storage.child(cloudfilename).get_url(None))

# Download

cloudfilename=input("Enter the name of the file you want to download")
storage.child("google.txt").download("","downloaded.txt")

# Reading_file

cloudfilename=input("Enter the name of the file you want to download")
url=storage.child(cloudfilename).get_url(None)
f=urllib.request.urlopen(url).read()
print(f)





#####################################

#Database


#Create

data={'age':25, 'address':'LA', 'employed':False, 'name':'Mark'}
db.child("people").child("id").push(data) 


#Update

db.child("people").child("id").update({'name':'Jane'})


people=db.child("people").get()
for person in people.each():
    if person.val()['name']=='Vlad':
        db.child("people").child(person.key()).update({'name':'Jane'})
  

#Delete

db.child("people").child("person").remove()

people=db.child("people").get()
for person in people.each():
    if person.val()['name']=='John Smith':
        db.child("people").child(person.key().child("age").remove())
        
  

#Read

people=db.child("people").child("-N5iBq9PRrWaSgYlRoiG").get()
print(people.val())

people=db.child("people").order_by_child("name").equal_to("Jane").get()
for person in people.each():
    print(person.val()['name'])

