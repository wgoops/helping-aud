#IMPORT STUFF


####============ Requirements ============####

#   What is the goal output
#   What are some of the inputs that could help us get there
#   What can be used as-is
#   What requires a bit of additional elbow grease 

####============ ETL STUFF ============####

## Extract 

#   0. Set up variables
#   1. Bring in some files

#   Read the CSV in Python
#       this is probably fine: https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
#
#   Write code which will open the CSV, and convert it to a "list of lists" (nested list): https://www.freecodecamp.org/news/list-within-a-list-in-python-initialize-a-nested-list/
    #   example of a list: 
    #       cool_list = [1,0,14,243]
    #   example of a nested list: 
    #       cool_nested_list = [[1,0,3,4], [10,4,21,32,4]]
#
#   2. Get something from the files, and put it in a list/dict/whatever so that python can work with it

## Transform
# 

# we are going to iterate through these lists of lists to generate another list of lists
#   
#   Goal 1: get variable with number of appointments (ex. appointment_count)
#   Goal 2: get variable with number of perscriptions
#   Goal 3: get number of individual patients
#   Goal 4: find last appointment date for doctors 
#   Goal 5: find total cost billed
# 
## Load

#   
# Get the thing