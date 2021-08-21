"""
   * Author - Shardul Khapke
   * Date -  18-AUG-2021
   * Time -  6:58 PM
   * Title - User Input and Replace String Template
"""
flag = True
while flag == True:
    try:
        """
           Description:
           :we are replace the string Template "Hello <<UserName>>, How are you?"
           parameters:
           :in we are assign input String format"""
        name = input("Please Enter Your Name:")
        name = str(name)
        nameLength = len(name)
        if nameLength >= 3:
            print(nameLength)
            print("Hello " + name + ", How are You ?")
            flag = False
            raise NameError
        else:
            print("Invalid Name")
    except NameError:
        print("Enter Correct Name")
