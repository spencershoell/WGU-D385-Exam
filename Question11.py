def CelciusToFahrenheit(Temperature):
    #insert assert statement for, "Colder than zero degrees Celsius!"
    return ((Temperature*9)/5)+32

if __name__ == '__main__':  
    Temperature = int(input())
    try:
        print(CelciusToFahrenheit(Temperature))
    except AssertionError as msg:
        print(msg)