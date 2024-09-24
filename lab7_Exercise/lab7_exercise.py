""" 
lab7_Exercise
Md Abu Shajed
September 24, 2024
"""

def email_read():
    try:
        # Open the file 'user_email.txt' in read mode
        with open('user_email.txt', 'r') as infile:
            # Initialize counters for different email domains
            gmail_count = 0
            yahoo_count = 0
            hotmail_count = 0

            # Loop through each line in the file to extract email addresses
            for line in infile:
                # Split each line by ',' to separate the name and email address
                parts = line.split(',')
                
                # Ensure there is more than one part (i.e., name and email)
                if len(parts) > 1:  
                    # Extract the email address part
                    email = parts[1]  

                    # Check if the email belongs to Gmail, Yahoo, or Hotmail
                    if '@gmail.com' in email:
                        gmail_count += 1
                    elif '@yahoo.com' in email:
                        yahoo_count += 1
                    elif '@hotmail.com' in email:
                        hotmail_count += 1
        
        # Open 'reportemail.txt' in append mode to add results
        with open('reportemail.txt', 'a') as outfile:
            # Write the number of users for each email domain
            outfile.write(f"Gmail users: {gmail_count}\n")
            outfile.write(f"Yahoo users: {yahoo_count}\n")
            outfile.write(f"Hotmail users: {hotmail_count}\n")
        
        # Print confirmation message once the report is appended
        print("Report appended successfully to 'reportemail.txt'.")
    
    # Catch the case where the file 'user_email.txt' is not found
    except FileNotFoundError:
        print("Error: The file 'user_email.txt' was not found.")
    
    # Catch any other exceptions that may occur and display the error
    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function to process the email addresses
email_read()
