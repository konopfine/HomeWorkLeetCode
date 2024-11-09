def roman_to_int(s: str) -> int:
    # Define values for each Roman numeral symbol
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    # Iterate over the Roman numeral string in reverse order
    for symbol in reversed(s):
        # Get the integer value of the current Roman numeral
        current_value = roman_values[symbol]
        
        # Apply subtraction rule
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
            
        # Update the previous value for the next iteration
        prev_value = current_value
        
    return total
