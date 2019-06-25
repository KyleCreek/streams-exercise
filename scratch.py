# 1. Reads two digits at a time from the beginning of the stream
# 2. Converts the two digits into a number, and adds that number to a running total.
# 3. Once this number reaches 200 or more, the method returns how
#    many two digit numbers it had to add together to reach its
#    total.
# 4. If `process` reaches the end of the stream BEFORE it has
#   reached a sum of 200, then it will return how many two
#    digit numbers it found before reaching the end of the
#   stream.
# 5. The method will add AT MOST 10 of these two digit numbers
#   together: if it reaches the 10th two digit number and the
#   sum has not yet reached 200, then the method will stop and
#   return 10.

from io import StringIO

# Create an instance of the StringIO Stream
f = StringIO("234761640930110349378289194")
f2 = StringIO("01020304050607080910111213")

# Determine the Lenght of the String 
stream_length = len(f.getvalue())

# Create an empty variable for a running total
total = 0
# Count the number of two digit numbers processes
count = 0

# Create a counter for the 'while' loop. 
while_counter = 0

# Create a counter of 2 digit numbers added
while while_counter < stream_length and count < 10:

    # Read the first two digits of the stream into a variable
    digits = f2.read(2)
    
    ### Note: Need to Check to see if there is a 0 in the obtained digit 
    # i.e. a non two digit number

    # Create a list to check against the read values
    check_list = [int(digit) for digit in str(digits)]

    try:
        # Case statement where the two digits contain a leading 0
        if check_list[0] == 0 or check_list[0] is None:
            pass
        # Case statement where this is no leading 0 and sum is less than 200
        elif total <= 201:
            count += 1
        # Case statement where there is no leading 0 and sum is greater than 200
        else:
            pass
                # Add to the running total
        total += int(digits)    
        # Increase Counter by an amount of 2
        while_counter += 2
    except IndexError:
        print("index Error Occurred")
        while_counter += 2
        continue
        


print("total", total)
print("count", count)