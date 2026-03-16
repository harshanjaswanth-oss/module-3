
def circumference_of_circle(radius):
    """
    Calculate the circumference of a circle given its radius.
    Formula: C = 2 * π * r
    """
    
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    pi = 3.141592653589793  
    return 2 * pi * radius




r = float(input("Enter the radius of the circle: "))
c = circumference_of_circle(r)
print(f"The circumference of the circle is: {c:.2f}")



  