#Define the look book of beautysalon,
look_book={
    'Threading':70,
    'Manicure':500,
    'Facial':1000,
    'Haircut':150,
    'Makeup':1500,
    'Mehndi':100,

}
#greet

print("Threading:Rs70\nManicure:Rs500\nFacial:Rs1000\nHaircut:Rs150\nMakeup:Rs1500\nMehndi:Rs100\n")

Beauty_bill=0 # initialise the total bill
#70+500=570

service_name=input("Enter the name of service you want to add in beauty bill=")
if service_name in look_book:
    Beauty_bill+=look_book[service_name] #0+70

    print("Your service {service_name} has been added to your beauty bill")

else:
    print("Added service (service_name) is not available currently!")
    

    another_service=input("Do you want to add another service?(Yes/No)")
    another_service="yes" # initialise to enter the loop
    while another_service.lower()=="Yes":#loop as long as the user wants to add services
        service_name=input("Enter the name of service you want to add in beauty bill:")
        if service_name in  look_book:
           Beauty_bill += look_book[service_name]
           print(f"Service ({service_name}) has been added to your beauty bill ")
        else:
           print(f"Added service({service_name}) is not available currently! ")
           another_service=input("Do you want to add another service?(Yes/No):")
           
           print(f"The total amount of services to pay is Rs.{Beauty_bill} ")
           

