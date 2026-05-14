user = input("Enter a number - 1000 , 900 , 500 , 400 , 100")    
    

class RomanConverter:
    roman_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        # ... more values ...
    }

    def convert_to_roman(self, num): 
        result = "" 
        sorted_values = sorted(self.roman_map.keys(), reverse=True)

        return result 
