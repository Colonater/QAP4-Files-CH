import datetime
import calendar



#The One  Stop  Insurance  Companyneeds  a  program  to  enter  and  calculate
# new  insurance  policy information for its customers.

#Create a data file called OSICDef.dat that contains the next policy number,
#the basic premium, the discount for additional cars
#the cost of extra liability coverage, the cost of glass coverage
#the cost for loaner car coverage, the HST rate,
#And Processing Fee for the Monthly Payments
#(See QAP 4.pdf)
#Insurance  premiums  are  calculated  using  a  basic  rate of  $869.00
#As the program starts, read the values from the defaults file.

policynumber = 1944
INSURANCEPREM = 869.00
rentalcardiscount = 0.25
LIABILITYCOST = 130.00
GLASSRATE = 86.0
LOANERCARRATE = 58.00
HSTRATE = 0.15
PROCESSFEE = 39.99

f = open("B:\\DesktopB\\OSICDef.dat", "w")

f.write("{}\n".format(policynumber))
f.write("{}\n".format(INSURANCEPREM))
f.write("{}\n".format(rentalcardiscount))
f.write("{}\n".format(LIABILITYCOST))
f.write("{}\n".format(GLASSRATE))
f.write("{}\n".format(LOANERCARRATE))
f.write("{}\n".format(HSTRATE))
f.write("{}\n".format(PROCESSFEE))

f.close()




TotalExtraValue = 0
#The  user  will  input  the customer’s first  and  last name,
#address,  city,  province,  postal code,and  phone number.
while True:
    firstname = input('Enter Your firstname: ').title()
    lastname = input('Enter Your lastname: ').title()
    address = input('Enter Your Address: ')
    city = input('Enter Your City: ')
    province = input('Enter Your Province: ')
    postalcode = input('Enter Your Postal Code: ')
    cell = input('Enter Your Cell: ')

#They  will  also  enter  the  number  of  cars  being  insured,and  options  for
#extra  liability  up  to $1,000,000 (enter Y for Yes or N for No),
    # Convert the name to title case and the Y/N and F/M values upper case.
    # No validations required –but go for it if you want.
    # Be careful when testing that you enter values that are valid for each input.

    # for  the  first  automobile
    # with  each additional automobile offered at a discount of 25%.
    # Convert the name to title case and the Y/N and F/M values upper case.
    # No validations required –but go for it if you want.
    # Be careful when testing that you enter values that are valid for each input.

    numberofcars = int(input("Enter the Number of Cars you'll be Insuraning:"))
    if (numberofcars == 1):
        insurance = INSURANCEPREM
    elif (numberofcars > 1):
        insurance = INSURANCEPREM + (numberofcars - 1) * (INSURANCEPREM * (1 - rentalcardiscount))

    lonercar = input("will you be needing a loner car: (Y/N) ").upper()
    if(lonercar == "Y"):
        TotalExtraValue += LOANERCARRATE
    liability = input('Would You like extra Liability upto 1 Million Dolars: (y/n)').upper()
    if(liability == 'Y'):
        TotalExtraValue += LIABILITYCOST

    glasscovrage = input("Optional Glass Coverage: (y/n)").upper()
    if(glasscovrage == "Y"):
        TotalExtraValue += GLASSRATE

    payments = input("Would you Like to pay in Full or Monthly Payments: (F/M)").upper()

    insurancetotal = insurance + TotalExtraValue
    Tax = insurancetotal * HSTRATE
    netcost = insurancetotal + Tax

    mpayment = (netcost + PROCESSFEE) / 8

    print()
    print("      One Stop Insurance Company        ")
    print("========================================")
    print(f"Customer Name: " + firstname, lastname)
    print(f"Cell: " + cell)
    print(f"address: " + address)
    print(f"Province: " + province)
    print(f"City: " + city)
    print(f"Postal Code: " + postalcode)
    print('----------------------------------------')
    print(f"Cars Insured: ", numberofcars)
    print("Liability: ", liability)
    print('Glass Coverage: ', glasscovrage)
    print('Rental Car: ', lonercar)
    print(f"payment: ", payments)
    print("----------------------------------------")
    print(f"Insurance Premium: ", INSURANCEPREM)
    print(f"Total Extra Cost: ", TotalExtraValue)
    print(f"Insurance Premium Cost: ", insurancetotal)
    print(f"Newfoundland Sales TAX!: ", Tax)
    print(f"Grand Total: ", netcost)
    print(f"---------------------------------------")
    print(f"Monthly Payments: ", mpayment)
    print(f'Policy ID', policynumber)
    print("========================================")

    # for  the  first  automobile
#with  each additional automobile offered at a discount of 25%.






#All these values are added together for the total extra costs.

#The total insurance premiumis the premium plus the total extra costs.
#HST is calculated at 15% on the total insurance premium
#and the total cost is the total insurance premium plus the HST.
#Customers canpay for their insurance in full or in 8 monthly payments.
#Calculate  the monthly payment  by adding a processing fee  of $39.99
# to the total costand dividing the total cost by 8.

#Display all input and calculated values to the screenina well-designed receipt.
#Only display the monthly payment if the user enters M for the payment method.


#Save the Policy number, all input valuesand the total insurance premiumto
#a file called Policies.datfor future reference.
#Display themessage “Policyinformation processed and saved.
#And increase the next policy number by 1. A sample line in the file might appear as follows:

#policyinfo
    f = open("policies.dat", "a")
    f.write("{}, ".format(policynumber))
    f.write("{}, ".format(firstname, lastname))
    f.write("{}, ".format(address))
    f.write("{}, ".format(city))
    f.write("{}, ".format(postalcode))
    f.write("{}, ".format(province))
    f.write("{}, ".format(cell))
    f.write("{}, ".format(numberofcars))
    f.write("{}, ".format(liability))
    f.write("{}, ".format(lonercar))
    f.write("{}, ".format(glasscovrage))
    f.write("{}, ".format(payments))
    f.write("{}, ".format(TotalExtraValue))
    f.write("{}, ".format(netcost))
    policynumber += 1
    print('Policy is saved')


    Another1 = input("Another Customer?: (Y/N)").upper
    if(Another1 == "N"):
        break
    f.close()









#(1944, John, Smith, 12 Main St., St. John’s, NL, A1A8H4, 123-123-1234, 2, Y, N, Y, F, 1329.00)

#Allow the user to enter as many policies as they need.
#When the user is done entering policies and exits the program,
#write the current values back to the defaults file.



