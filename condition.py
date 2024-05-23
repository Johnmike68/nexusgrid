age=str(input('please input your age:\n'))

if (age<"18"):
    print('you are not allowed to enter\n')
elif(age<="30"):
    print('you are allowed to enter, drink and smoke\n')
elif(age<="45"):
    print('you are allowed to enter, drink, smoke and rent rooms \n')
else:
    print('you are allowed to enter but cant drink\n')

