from io import StringIO

class StreamProcessor(object):
    """
    Write a stream processor class that does the following:
        1. You initialize an instance with a stream of digits
          (AKA: file-like object, instance of StringIO), and
          store it as an instance variable.
        
          eg: f = io.StringIO("234761640930110349378289194")
              my_stream_processor = MyStreamProcessor(f)
              
        2. You call a `process` method of my_stream_processor.
        
          This method:
          
            1. Reads two digits at a time from the beginning of the stream
            2. Converts the two digits into a number, and adds that number
               to a running total.
            3. Once this number reaches 200 or more, the method returns how
               many two digit numbers it had to add together to reach its
               total.
            4. If `process` reaches the end of the stream BEFORE it has
               reached a sum of 200, then it will return how many two
               digit numbers it found before reaching the end of the
               stream.
            5. The method will add AT MOST 10 of these two digit numbers
               together: if it reaches the 10th two digit number and the
               sum has not yet reached 200, then the method will stop and
               return 10.

    For example, given a stream yielding "234761640930110349378289194", the
    process method will:

            1. Read two digits at a time from the stream: "23", "47", "61", etc.
            2. Convert these digits into a number: 23, 47, 61, etc., and  make a
               running total of these numbers: 23 + 47 equals 70. 70 + 61 equals
               131, etc.
            3. For this particular stream, the running total will exceed 200 after
               5 such additions: the `process` method should return 5.

    You can see the `tests.py` file for more examples of expected outcomes.
    """

    def __init__(self, stream):
        self._stream = stream
    def process(self):
       """
       Performs the Processes as Specified in Lesson02
       Activity

       returns: Count 
       """
       count = 0
       total = 0

       while count < 10 and total < 200:
          digits = self._stream.read(2)
          if len(digits) < 2:
             break
          count += 1
          n = int(digits)
          total += n
       return count

    def process_wrong(self):
       """
       Incorrectly Processes the Activity of lesson02 because
       I apparently don't know how to read
       """       
       # Determine the length of the String
       stream_length = len(self._stream.getvalue())

       # Create an empty variable for a running total
       total = 0

       # Count to maintain the number of two digit values processed
       count = 0

       # Create a counter to control the 'while' loop
       while_counter = 0

       # Establish 'while' loop that counts 2 digit numbers while running total
       # is less than 200 and less than (10) digits have been added 
       while while_counter < stream_length and count < 10:

          # Read the first two digits of the stream into a variable
          digits = self._stream.read(2)

          # Verify provided digits have a leading 0
          # i.e. a non two digit number
          check_list = [int(digit) for digit in str(digits)]

         # Try Except protects against indexing error when evaluating values
         # in the check list. 
          try:
             # Case statement where there is no leading 0, Sum is less than 201
             # and 10 iterations have not occurred
             if check_list[0] != 0 and total < 201 and while_counter < 10:
                count += 1
                total += int(digits)
                while_counter += 2
             # Case statement where there IS a leading 0, sum is less than 200
             # and 10 iterations have not occurred.
             elif check_list[0] == 0 and total < 201 and while_counter < 10:
                total += int(digits)
                while_counter += 2
             # Condition where the above constraints ahve failed.
             else:
                return count
          # Handles Exception errors while reading the check list
          # and increments the 'while' loop.
          except:
             print("Index Error Occured")
             while_counter += 2
             continue

