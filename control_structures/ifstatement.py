# instead of doing like this:
# mark = input('Enter your mark')
# mark = int(mark)

# you can shorten the code as below
mark = int(input('Enter your mark'))

# for if else statement it is always recommended to have indent after the if/else statement or it will give error
# important to have colon(:) after each if/else statement to tell what to execute if the condition is true
if mark >= 90:
    print('Grade A')
elif mark >= 70:
    print('Grade B')
elif mark >= 60:
    print('Grade C')
elif (mark>0 and mark<60):
    print('Grade D')
else:
    print('Invalid numbers')
