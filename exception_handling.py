
try:
   print(x)
#except  NameError:
  # print("Variable x is not difined")
#except:
   #print("An exception occurred")
#except:
  # print("Something went wrong")
#finally:
   #print("The 'try except' is finished")
   
except NameError:
   print("Variable x is not difined")
else:
   print("Everything went wrong")
   
x = -1

if x  < 0:
    raise Exception("Sorry, no numbers below zero")