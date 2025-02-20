class Employee:
    
    def __init__(self):
        print('Employee created')

    def __del__(self):
        print("Destructor called")

def Create_odj():
    print('Making Object...')
    odj = Employee()
    print('function end...')
    return odj

print('Calling Create_odj() function...')
odj = Create_odj()
print ('Program End...')