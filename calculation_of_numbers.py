class Calculation:
    def counting_significant(self, number: str) -> str:
        number = number.replace(',', '.')
        
        if number[0] != '0':
            return number
        
        for i in range(len(number)):
            if number[i] != '0' and number[i] != '.':
                return number[i:]
        
        return '0' 

test = Calculation()
print(test.counting_significant('0.04021'))
            
            
