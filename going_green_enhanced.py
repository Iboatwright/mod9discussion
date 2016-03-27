# going_green_enhanced.py
# Exercises selected: Lab 10.4 - Going Green and File Interaction
# Name of program: Going Green
# Description of program: This program prompts the user with a menu of
#   options.  The first option has the user enter energy bills for
#   each month of the year prior to going green and the year after going
#   green.  Option 2 reports the entered values and calculated savings.
#   Option 3 writes the savings to a file.  Option 4 reads the savings
#   from the file.
#
# Ivan Boatwright
# March 27, 2016

def main(debug=False):
    # Declare local variables/constants
    MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December')
    HEADERS = ('SAVINGS', 'NOT GREEN', 'GONE GREEN', '  MONTH')

    # Menu control options passed to the menu function.  A list with each
    #   entry a tuple of [0] the display text and [1] the function to call.
    #   Menu numbers start at 1), option 0) defaults to Exit.
    customMenuOptions = [('Enter energy bills', enter_bills),
                         ('Display Savings Report', display_report),
                         ('Save Results to File', write_Savings),
                         ('Display Results from File', read_Savings)]

    # Any custom persistant variables are added to this dictionary.
    cVars = dict(months=MONTHS, headers=HEADERS, fileName='savings.txt', report='',
                 notGreenCost=[], goneGreenCost=[], savings=[])

    cVars['headDesign'] = '{0:^4}{{0:>10}}{0:^6}{{1:>10}}{0:^6}{{2:>10}}' \
                          '{0:^6}{{3:<8}}\n'.format('')
    cVars['reportDesign'] = '{0:^3}{{0:>10}}{0:^6}{{1:>10}}{0:^6}{{2:>10}}' \
                            '{0:^8}{{3:<8}}\n'.format('')

    # Displays an introduction to the program and describes what it does.
    fluffy_intro()

    # Call the menu loop program.  The menu options are: 1) Average Test
    #   Scores and 0) Exit the program.
    main_menu(customMenuOptions, cVars)

    # Exit main.
    return None

# Section Block: Misc Output ------------------------------------------------>

# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print(page_header('Going Green'))
    print('{0}{0}Welcome to the Going Green program.\n'
          '{0}This program takes the monthly energy costs from the year\n'
          '{0}prior to going green and the year since going green.  It\n'
          '{0}then calculates the monthly savings and displays everything\n'
          '{0}in a savings report.'.format('    '))
    return None


# Returns a string used to identify a new part(i.e. page) of the program.
def page_header(title):
    return '{0:-<62}\n\n{1:^67}\n{0:_<62}\n'.format('    ', title)


# Section Block: Menu ------------------------------------------------------->

# main_menu prints a list of options for the user to select from.  The user
#   enters the desired option's number and the function paired with that
#   option is then executed.  If that option is 0 the while loop is terminated
#   and control returns to the calling function.  Otherwise after the selected
#   function is finished main menu is displayed again.
def main_menu(customMenuOptions, cVars):
    # Menu control options. A list with each entry a tuple of
    #   [0] the display text and [1] the function to call.
    menuOptions = [('Exit', exit_menu)]  # Set default menu options.
    menuOptions.extend(customMenuOptions)  # Add custom menu options.
    MENU_COUNT = len(menuOptions)

    # Initialize the loop control variable.
    menuSelection = True

    # While menuSelection does not equal 0 (the default exit option.)
    while menuSelection != 0:
        display_menu(menuOptions, cVars)
        # Calls the input request/validation function and converts the return
        #   value into an integer.  The number of menu elements is prepended
        #   to the input request and used as part of the validation testing.
        menuSelection = int(get_valid_inputs([[str(MENU_COUNT) +
                            ' menu options', 'Your Selection']]))

        # Use the validated user input to select the function reference and
        #   execute the function with the trailing ().
        menuSelection = menuOptions[menuSelection][1](cVars)

    # By design the exit_menu function runs before the while loop breaks.
    return None


# Prints the menu header and menu options to stdout.  The menuOptions list
#   is the parameter and used to generate the option strings.
def display_menu(mOpts, cVars):
    print(page_header('Main Menu'))
    # This loops through the list starting at [1] and prints [0] (Exit)
    #   at the end.
    for l in range(1, len(mOpts)):
        print('  {0}) {1}'.format(l, mOpts[l][0]))
    print('  {0}) {1}'.format(0, mOpts[0][0]))
    return None


# Sets the loop control variable to 0 which ends the while loop.
def exit_menu():
    # "Until we meet again, farewell."
    print("\nJusqu'à ce que nous nous reverrons, adieu.")
    return 0


# Section Block: Input Validation ------------------------------------------->

# get_valid_inputs requests input from the user then tests the input.
#   If invalid, it will alert the user and request the correct input.
# The parameter is a nested List of ordered pair Lists.
#   First value is the validation test and second is the user prompt.
def get_valid_inputs(requestsList):
    # local List to hold user inputs for return to calling module
    userInputs = []

    # Loop through each entry in requestsList assigning each List pair
    #  to request.
    for request in requestsList:
        # untestedInput is a holding variable for testing user input validity.
        # First user prompt before testing loop.
        untestedInput = prompt_user_for_input(request[1])

        # If test_value returns True, Not converts it to False and the While
        #   Loop will not execute.
        # If test_value returns False, the While executes and the user is
        #   prompted to enter a valid value.
        while not test_value(request[0], untestedInput):
            print('!!! Error: {} is not a valid value.'.format(untestedInput))
            untestedInput = (prompt_user_for_input(request[1]))

        # The user input tested valid and is appended to the userInputs List.
        userInputs.append(untestedInput)
    # for loop terminates and userInputs are returned to calling Module.
    # With only a single test run in this program, only the first value
    #   in userInputs is returned.
    return userInputs[0]


# prompt_user_for_input is passed a String to print to screen as part of a user
#   prompt.  Then returns the input to the calling module.
def prompt_user_for_input(promptTerm):
    return input('{}  >>> '.format(promptTerm))


# test_value uses the testCondition to select the proper test.
# True or False is returned to the calling Module.
def test_value(testCondition, testItem):
    # The If-Then-Else structure functions as a Switch for test selection.
    if testCondition[1:] == ' menu options':
        # The number of menu items is prepended to the test condition string.
        #   testCondition[1:] strips the first character and then does the
        #   string comparison.
        # If (the number of menu items) is greater than int(testItem) and
        #   int(testItem) is greater than or equal to zero, True is
        #   returned.  If int(testItem) creates an error or fails the other
        #   logic tests, False is returned.
        try:
            if int(testItem) >= 0 and int(testCondition[:1]) > int(testItem):
                valid = True
            else:
                valid = False
        except:
            valid = False
    elif testCondition == 'integer':
        try:
            int(testItem)
            valid = True
        except:
            valid = False
    else:
        valid = None
    return valid



# Option 1
def enter_bills(cVars):
    get_not_green(cVars['notGreenCost'], cVars['months'])
    get_gone_green(cVars['goneGreenCost'], cVars['months'])
    energy_saved(cVars['notGreenCost'], cVars['goneGreenCost'],
                 cVars['savings'])
    return None

# Option 2
def display_report(cVars):
    if len(cVars['savings']) < 12:
        print('\n{0}Nothing to report.  Please enter monthly energy bills.'
              '\n'.format('    '))
    else:
        report = get_report(cVars['headers'][0], cVars['headers'],
                            cVars['hdesign'], cVars['design'],
                            cVars['savings'], cVars['notGreenCost'],
                            cVars['goneGreenCost'], cVars['months'])
    return None

# Option 3
def write_Savings(cVars):
    if len(cVars['savings']) < 12:
        print('\n{0}Nothing to write.  Please enter monthly energy bills.'
              '\n'.format('    '))
    else:
        outString = ''.join(['{}\n'.format(s) for s in cVars['savings']])
        write_to_file(cVars['fileName'], outString)
    return None

# Option 4
def read_Savings(cVars):
    title = 'Saved Savings from Savings File'
    headers = (cVars['headers'][0], cVars['headers'][-1])
    hdesign = '{0:^20}{{0:>10}}{0:^22}{{1:<8}}\n'.format('')
    design = '{0:^19}{{0:>10}}{0:^20}{{1:<8}}\n'.format('')
    data = get_from_file(cVars['fileName'])
    if len(data) > 0:
        print(get_report(title, headers, hdesign, design, data))
    return None

# Requests the user input the notGreenCosts.
def get_not_green(ngc, months):
    monthly_values(months, 'NOT GREEN energy costs', ngc)
    return None


# Requests the user input the goneGreenCosts.
def get_gone_green(ggc, months):
    monthly_values(months, 'GONE GREEN energy costs', ggc)
    return None


# Calculate the savings per month. The savings list is passed by reference.
#   The gone-green values are subtracted from the not-green values and each
#   result is appended to the savings list.
def energy_saved(ngc, ggc, sav):
    [sav.append(x[0] - x[1]) for x in zip(ngc, ggc)]
    return None


# Iterates through the list of months.  Each iteration has the user input
#   a value for that month.  The value is assigned to the reference array
#   with the same index as that month.  If an invalid integer is entered
#   an error message is displayed and the user is prompted to try again.
def monthly_values(months, name, vArray):
    print('{}\nPlease enter the {} for each month.\n'.format('_' * 79, name))
    for month in months:
        vArray.append(int(get_valid_inputs([['integer', month]])))
    return None


# moneyfy converts integer & float values in a variable number of lists
#   to strings prepended with a $ sign.  If the value is negative the - sign
#   is moved in front of the $ sign.
def moneyfy(*vArs):
    for vA in vArs:
       vA[:] = ['${}'.format(v) if v>0 else '-${}'.format(abs(v)) for v in vA]
    return None


# Takes a title, a set of headers, a header format string, a body format
#   string, a merged parallel array and returns a print friendly string.
def tablefy(title, headers, hdesign, design, data):
    title = page_header(title)
    head = hdesign.format(*headers)
    division = '{0:4}{0:_<58}\n'.format('')
    body = ''.join([design.format(*j) for j in data])
    return '{}{}{}{}'.format(title, head, division, body)


# get_report is an intermediary stage for generating and returning the
#   report string.
def get_report(title, headers, hdesign, design, *data):
    # Using moneyfy to turn all the integer values into strings with
    #   dollar signs.
    moneyfy(*data[:-1])

    # tablefy returns the report as a string which is then passed back
    #   to the calling module.
    return tablefy(title, headers, hdesign, design, zip(*data))


# This module accepts the filename as it's parameter and returns the contents
#   of the file as a string.
def get_from_file(fName):
    strArray = []
    try:
        with open(fName,'r') as f:
            strArray.extend([int(x) for x in f.read().split('\n')[:-1]])
    except FileNotFoundError:
        print('\n{0}File does not exist.  Please enter monthly energy bills\n'
              '{0}and save the results to file.\n'.format('    '))
    return strArray


def write_to_file(fName, outString):
    with open(fName, 'w') as f:
        f.write(outString)
    return None


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(report):
    print(report)
    return None


################ DEBUG CODE ##################
# This isn't part of the assignment but I left it in for others to reference.
#   I'm using it to populate the user input lists and bypass the need for me
#   to input data, but still able to evaluate the results of the program.
def generate_numbers(rMin=1, rMax=999, xNums=12):
    from random import sample
    # Uses the sample function from the random module to generate a list of
    #   integers.  The range function is used with the min and max variables
    #   to set the possible integer values generated.
    return sample(range(rMin, rMax), xNums)


# Call main.
main()