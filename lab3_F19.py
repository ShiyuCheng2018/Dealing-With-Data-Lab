'''
Lab 3 ISTA 131 Fall 2019

This lab is intended to give you practice with ord(), chr(), built-in classes, user-defined
classes and using matrices.
'''

def codes_to_str(array):
    '''
    Takes a list of code points and returns its resulting string
    '''

    string = ""
    for each in array:
        string += chr(each)
    return string

def str_to_codes(string):
    '''
    This function takes a string as its single argument and creates a dictionary that maps
    individuals string characters to its code point. If the string contains
    letters, create keys for both it's upper and lower case and map those code points to it. Sort the 
    dictionary and then print key value pairs as strings, seperated by a single line
    
    ie
    str_to_codes("hI!") 
    
    !: 33
    H: 72
    I: 73
    h: 104
    i: 105
                            
    '''

    my_dict = {}
    for each in string:
        if 47 >= ord(each) >= 33:
            my_dict[each] = ord(each)
        else:
            my_dict[each.lower()] = ord(each.lower())
            my_dict[each.upper()] = ord(each.upper())

    for key in sorted(my_dict.keys()):
        print(key+": "+str(my_dict.get(key)))

    
class Matrix:
    def __init__(self, rows, cols,start_pos, integer):
        '''
        The Matrix class represents a single matrix.
        It should have oen method: an init
        It has four parameters, the number of rows and columns,
        a start postion, and a interger.
        This instance method should create a matrix using the given number of rows and columns. 
        The matrix will contain numbers beginning at our start position, incremented
        by the given integer.
        '''

        self._rows = rows
        self._cols = cols
        self._position = start_pos
        self._integer = integer
        self._matrix = []

        for row in range(self._rows):
            self._each = []
            for col in range(self._cols):
                self._each.append(self._position)
                self._position += integer
            self._matrix.append(self._each)

        
    def dimensions(self):
        '''
        Returns the shape of the matrix, as a tuple
        '''

        return self._rows, self._cols
    
    def change(self, i, j, given_int):
        '''
        Change the number at given row and column to the given
        integer, returns None. 
        '''

        for row in range(self._rows):
            for col in range(self._cols):
                if row == i and col == j:
                    self._matrix[row][col] = given_int
        return None

        
def main():
    '''
    Create an instance of a Matrix class, make up your own arguments
    Print its shape
    Change one of your created matrix's values to any integer
    '''
    print("............codes_to_str...........")
    print(codes_to_str([65, 66, 67, 68, 69, 70]))
    print("............end of codes_to_str.... \n")

    print("............ str_to_codes..........")
    str_to_codes("hI!")
    print("............ end of str_to_codes.... \n")

    print("............ Matrix.................")


    matrix = Matrix(4, 5, 5, 6)
    print(matrix._matrix)
    print(matrix.change(0, 0, 1))
    print(matrix._matrix)
    print("dimensions of the matrix: "+str(matrix.dimensions()))

    print("............ end of Matrix..........")





if __name__ == "__main__":
    main()
    
    
        