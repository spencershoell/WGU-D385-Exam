#check if the zipcode input is numeric

if __name__ == '__main__': 
        
    zipCode = input()
    try:
        zipCode = int(zipCode) 
        #check that zip code is an integer value
        print(f'Your zip code is {zipCode}.')

    except:
        print('Please use numeric digits for the zip code.')