"""
drive link for the .csv files: https://drive.google.com/drive/u/0/folders/1OGvAvU0Ig5zBd30sX5S1GJy6COfKCzK-
"""

#-------------------------imports---------------------------------------
import pandas as pd
import csv
from csv import writer
import smtplib

from google.colab import drive
drive.mount('/content/drive')
#-----------------------------------------------------------------------


#------------------------login function---------------------------------
def login(name, password, students):
    c = students.loc[students["name"] == name]
    d = c.loc[c["password"] == password]
    if d.shape[0] == 1:
        print("Hello", name, "Welcome!")
        print("**********************************************************************************")
        collegename = input("Enter Your College Name : ")
        is_college_eligible(name, collegename)
    else:
        print("Wrong Login ID or Password, Please check again!")
        print("**********************************************************************************")

#-----------------------------------------------------------------------


#---------------------is_college_eligible function----------------------
def is_college_eligible(name, collegename):
  c = colleges.loc[colleges["collegename"] == collegename]
  #print(d.shape[0])
  if (c.shape[0]==1):
    print("Hello",name,"Welcome to the college", collegename, "Recruitment Process.")
    checkeligibility(name)
  else:
    print("Your college is not eligible in the recruitment process.")
    print("**********************************************************************************")
#-----------------------------------------------------------------------


#------------------------checkeligibility function----------------------
def checkeligibility(name):
  pointer=students.loc[students['name'] == name, 'cgpa'].iloc[0]
  backlog=students.loc[students['name'] == name, 'backlogs'].iloc[0]
  if backlog<=0:
    eligiblecompanies=company[company['com_cgpa'] <= pointer]
    company_list = eligiblecompanies['com_name'].tolist()
    print("**********************************************************************************")
    print("List of the companies in which you are eligible based on CGPA obtained and No. of Backlogs :")
    print(company_list)
    interested_companies(name)
  else:
    print("But unfortunately, you are not eligible for recruitment process because of CGPA/backlogs.")
    print("**********************************************************************************")
#-----------------------------------------------------------------------


#-------------------interested_companies function-----------------------
def interested_companies(name):
  print("**********************************************************************************")
  input_string = input("Please enter your interested companies from the above list : ")
  interested_companies_list = input_string.split(", ")
  print("So Your Final Interested Companies List : ", interested_companies_list)
  print_job_desc(interested_companies_list,name)
#-----------------------------------------------------------------------


#---------------------print_job_desc function---------------------------
def print_job_desc(interested_companies_list,name):
  job = pd.read_csv('/content/drive/My Drive/Colab Notebooks/job.csv')
  job_desc_df = job[job['company_name'].isin(interested_companies_list)]
  print("**********************************************************************************")
  print('Your interested companies with all job titles are shown below : ')
  print(job_desc_df)
  test_details(interested_companies_list,name)
#-----------------------------------------------------------------------


#-----------------------test_details function---------------------------
def test_details(interested_companies_list,name):
  date_time_venue = pd.read_csv('/content/drive/My Drive/Colab Notebooks/date_time_venue.csv')
  interested_date_time_venue = date_time_venue[date_time_venue['com_name'].isin(interested_companies_list)]
  print("**********************************************************************************")
  print('Your interested companies with test details : ')
  print(interested_date_time_venue)
  mail(interested_companies_list,name)
#-----------------------------------------------------------------------


#-----------------------------mail function-----------------------------
def mail(interested_companies_list,name):
  print("**********************************************************************************")
  print("If you are interseted in this job title then provide your email id to send these test details else provide \"Not Interested\".")
  stud_mail=input("Enter your Email : ")
  if("@gmail.com" in stud_mail):
    print("You entered a valid mail.")
    print("**********************************************************************************")
    send_mail(stud_mail,name)

  elif stud_mail == "Not Interested":
    print("Thanks! Try for other company.")
    print("**********************************************************************************")

  else:
    print("Please enter a valid email id.")
    print("**********************************************************************************")
#-----------------------------------------------------------------------


#----------------------------send_mail function-------------------------
def send_mail(stud_mail,name):
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  sender_mail="manavvrma17@gmail.com"
  password_mail="XXXXXXXXX"
  try:
    s.login("manavvrma17@gmail.com", password_mail)
    message = "You are shortlisted for company."
    s.sendmail(sender_mail, stud_mail, message)
    print("These details has sent successfully to your valid email id by T&P Head.")
    student_records(name)
    s.quit()
  except:
    print("These details will be mailed to your valid email id shortly by T&P Head.")
    student_records(name)
#-----------------------------------------------------------------------


#-------------------------student_records function----------------------
def student_records(name):
  record = pd.read_csv('/content/drive/My Drive/Colab Notebooks/record.csv')
  count_rec = len(record)
  current_year=2020
  print("**********************************************************************************")
  print("Enter your company records if you have appreared/cleared any company test.")
  company_name=input("Enter Company Name : ")
  test_status=input("Enter your placement status(Appeared/Cleared) : ")
  register_record("/content/drive/My Drive/Colab Notebooks/record.csv",[str(count_rec+1),name,current_year,company_name,test_status])
#-----------------------------------------------------------------------


#--------------------register_record function---------------------------
def register_record(file_name2, list_of_elem2):
    # Open file in append mode
    with open(file_name2, 'a', newline='') as write_obj2:
        # Create a writer object from csv module
        csv_writer2 = writer(write_obj2)

        # Add contents of list as last row in the csv file
        csv_writer2.writerow(list_of_elem2)
        print("You have updated placement record successfully.")
        print("**********************************************************************************")
#-----------------------------------------------------------------------


#-----------------------register function-------------------------------
def register(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)

        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        print("You have registered successfully.")
        print("**********************************************************************************")
#-----------------------------------------------------------------------


#-----------------------registercol function----------------------------
def registercol(file_name1, list_of_elem1):
    # Open file in append mode
    with open(file_name1, 'a', newline='') as write_obj1:
        # Create a writer object from csv module
        csv_writer1 = writer(write_obj1)

        # Add contents of list as last row in the csv file
        csv_writer1.writerow(list_of_elem1)
        print("You have added college successfully.")
        print("**********************************************************************************")
#-----------------------------------------------------------------------


#--------------------registercompany function---------------------------
def registercompany(file_name3, list_of_elem3,com_name):
  # Open file in append mode
  with open(file_name3, 'a', newline='') as write_obj3:
      # Create a writer object from csv module
      csv_writer3 = writer(write_obj3)

      # Add contents of list as last row in the csv file
      csv_writer3.writerow(list_of_elem3)
      print("You have added company successfully.")
      print("**********************************************************************************")
      result=1;
      if(result==1):
        print("Please Enter Test Details for this Company :")
        date=input("Please Enter Test Date(dd-mm-yyyy) : ");
        time=input("Please Enter Test Time(HH:MM AM/PM) : ");
        venue=input("Please Enter Venue : ")
        register_test_details("/content/drive/My Drive/Colab Notebooks/date_time_venue.csv",[com_name,date,time,venue])
#-----------------------------------------------------------------------


#-----------------register_test_details function------------------------
def register_test_details(file_name4, list_of_elem4):
    # Open file in append mode
    with open(file_name4, 'a', newline='') as write_obj4:
        # Create a writer object from csv module
        csv_writer4 = writer(write_obj4)

        # Add contents of list as last row in the csv file
        csv_writer4.writerow(list_of_elem4)
        print("You have added test details for this company successfully.")
        print("**********************************************************************************")
#-----------------------------------------------------------------------


#-----------------------------choice function---------------------------
def choice(i):
    switcher={
                1:'T&P LOGIN',
                2:'LOGIN',
                3:'REGISTER',
             }
    return switcher.get(i,"Invalid choice")
#-----------------------------------------------------------------------

#----------------------------choicetp function--------------------------
def choicetp(i):
    switcher={
                1:'ADD COLLEGE',
                2:'ADD COMPANY',
                3:'EXIT',
             }
    return switcher.get(i,"Invalid choice")
#-----------------------------------------------------------------------


#---------------------------Driven function-----------------------------
print("**********************CAMPUS RECRUITMENT PROCESS SYSTEM***************************")
print("1. Training & Placements Head LOGIN")
print("2. STUDENT LOGIN")
print("3. STUDENT REGISTER")

print("**********************************************************************************")
a = int(input("Select any one option... \n"))
print("**********************************************************************************")
choice = choice(a)
print(choice)

students = pd.read_csv("/content/drive/My Drive/Colab Notebooks/student.csv")
colleges = pd.read_csv("/content/drive/My Drive/Colab Notebooks/college.csv")
company = pd.read_csv("/content/drive/My Drive/Colab Notebooks/company.csv")
date_time_venue = pd.read_csv("/content/drive/My Drive/Colab Notebooks/date_time_venue.csv")

if(choice == "T&P LOGIN"):
  nametp = input("Enter T&P Head Name : ")
  passwordtp = input("Enter Password : ")
  if(nametp=="Manav" and passwordtp=="Manav@123"):
    print("Hello",nametp,"You have successfully logged in!")
    print("You can add new colleges/companies in the recruitment process.")
    print("**********************************************************************************")
    print("1. ADD COLLEGE")
    print("2. ADD COMPANY")
    print("3. EXIT")
    print("**********************************************************************************")
    inp = int(input("Select any one option... \n"))
    print("**********************************************************************************")
    choicetpvar = choicetp(inp)
    print(choicetpvar)

    if(choicetpvar == "ADD COLLEGE"):
      collegename = input("Enter College Name : ")
      rank = input("Enter NIRF Ranking : ")
      loc = input("Enter Location of College : ")
      aff = input("Enter Affiliation : ")
      countcol = len(colleges)
      registercol("/content/drive/My Drive/Colab Notebooks/college.csv",[str(countcol+1),collegename,rank,loc,aff])

    if(choicetpvar == "ADD COMPANY"):
      com_name = input("Enter Company Name : ")
      com_add = input("Enter Company Address : ")
      com_turn = input("Turnover of the Company (In Lakhs) : ")
      com_area = input("Enter Core Business Area of the Company : ")
      com_rev =input("Enter Review of the Company (Out of 5): ")
      com_cgpa =input("Enter Min CGPA for Company Eligibility (Out of 10): ")
      countcompany = len(company)
      registercompany("/content/drive/My Drive/Colab Notebooks/company.csv",[str(countcompany+1),com_name,com_add,com_turn,com_area,com_rev,com_cgpa],com_name)

    if(choicetpvar == "EXIT"):
      print("You have not any college/company to add.")
      print("**********************************************************************************")

  else:
    print("This is only for T&P Head login.")
    print("Please enter valid username and password.")
    print("**********************************************************************************")


if(choice == "LOGIN"):
  name = input("Enter Username : ")
  password = input("Enter Password : ")
  login(name,password,students)

if(choice == "REGISTER"):
  name = input("Enter Username : ")
  password = input("Enter Password : ")
  address = input("Enter Address : ")
  qualifications = input("Enter Highest Qualification : ")
  cgpa = input("Enter CGPA : ")
  backlogs = input("Enter no. of Backlogs : ")

  count = len(students) + 1
  register("/content/drive/My Drive/Colab Notebooks/student.csv",[str(count),name,address,cgpa,qualifications,password,backlogs])
#-----------------------------------------------------------------------
