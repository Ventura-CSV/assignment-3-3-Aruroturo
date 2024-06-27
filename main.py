def main():
    email = input('Enter your email: ')
    if not email.isalpha():
        result = False
    elif len(email) <=5 or len(email) >= 30:
        result = False
    elif '@' not in email:
        result = False
    else:
        at_index = email.index('@')
        if '.' not in email[at_index]:
            result = False
    print(result)

        
        
    """
    
    ########################################
    Code Your Program here
    ########################################
    """


    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
