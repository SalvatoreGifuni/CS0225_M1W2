# Constants

CHECK_MESSAGE = "Please check the values. Enter numeric values only."

# Function to check if the input values are numbers
# Returns True and the converted value as a float if the input value is a number, False otherwise

def check_value(numb_str):
    try:
        n = float(numb_str)   #Try to convert the value from string (input) to float
        return True, n        
    except ValueError as e:
        print(f"Error message: {e}")
        return False, False
    except Exception as e:
        print(f"Error message: {e}")
        return False, False


# Function to split the input into different elements of a list and check if the input values are numbers

def split_input(numb_str):
    l = list((numb_str.replace(",", " ")).split())   #replace the ',' if present and split by whitespace
    l_float = []

    for e in l:
        t_f_input, value_input = check_value(e)
        if t_f_input:
            l_float.append(value_input) 
    
    return l_float

# While loop to ask for input and calculate the perimeter of three different geometric shapes based on user choice
    
while True:
    # User choice
    input_user = input("\n\
Welcome! \n\
Enter the corresponding number of shape to calculate perimeter.\n\
1. Square\n\
2. Circle\n\
3. Rectangle\n\
4. Exit the program\n\
")
    
    # Calculate the perimeter of a square
    if input_user == "1":
        print("Square Perimeter")
        l_sq = input("\nEnter value of the square's side in cm: ")
        t_f_input_sq, value_input_sq = check_value(l_sq)
        if t_f_input_sq:    #if control return True the perimeter will be calculated
            p_sq = value_input_sq*4
            print(f"The square's perimeter is: {p_sq:.2f}")
        else:
            print(CHECK_MESSAGE)
    
    # Calculate the perimeter of a circle
    elif input_user == "2":
        print("Circle Perimeter")
        r_cl = input("\nEnter the radius of the circle in cm: ")
        t_f_input_cl, value_input_cl = check_value(r_cl)
        if t_f_input_cl:    #If control returns True, the perimeter will be calculated
            p_cl = 2*value_input_cl*3.14
            print(f"The circle's perimeter is: {p_cl:.2f}")
        else:
            print(CHECK_MESSAGE)

    # Calculate the perimeter of a rectangle
    elif input_user == "3":
        print("Rectangle Perimeter")
        l_rt = input("\nEnter the values of base and height of rectangle in cm (b, h): ")
        l2_rt = split_input(l_rt)  #the control is improved in the split_input function
        if len(l2_rt) == 2:        #checks that the list is composed of two elements: base and height of rectangle
            p_rt = 2*l2_rt[0] + 2*l2_rt[1]
            print(f"The rectangle's perimeter is: {p_rt:.2f}")
        else:
            print("Please, check the values! Enter only two numeric values - base and height of rectangle (b, h).")
    
    # Allow the user to exit the program
    elif input_user == "4": 
        print("Bye, hope to see you soon!")  
        break