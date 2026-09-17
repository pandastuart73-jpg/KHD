start_date = "2026-09-02"
waiver = 100000
deadline = "2026-10-30"
penalty = 100000
RF = 3000000
date_of_payment = input("\nEnter when fees was paid: ")
if date_of_payment < start_date:
    print("qaulify for a waiver of 100,000")
elif date_of_payment > deadline:
  print("you have paid after the deadline, you will be charged a penalty ",penalty)
  PF =int(input("\nPLEASE CONFIRM HOW MUCH YOU HAVE PAID FOR FEES: "))
  EP = (RF + penalty)
  if PF < EP:
     print("unable to sit for exams")
  else:
     print("able to sit for exams")
else:
   print("thank you for paying fees")
  