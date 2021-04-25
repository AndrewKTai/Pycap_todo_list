import argparse
import database as db

parser = argparse.ArgumentParser(description='No arguments to list all current lists.')
group = parser.add_mutually_exclusive_group()

##create list.db if not already exists
db.create_list()

#mutually exclusive groups mean that the arguments won't collide
group.add_argument('-cl', '--create-list', help='Creates a new list', dest='db.create_list')
# group.add_argument('-c', '--create', help='Create an item in the list', action='store_true')
# group.add_argument('-la', '--list-all', help='List all the current items to do', action='store_true')
# group.add_argument('-t', '--toggle', help='Update the description to do', choices=['new', 'update','complete'], action='store_true')

#note the dash on the short form and the double dash on the second
group.add_argument('-u', '--update', help='Update the state of a to do, if no state is provided, then update in the following order: new -> progress -> expired(if time provided), complete', action='store_true', dest='update_stuff')
# group.add_argument('-d','--delete', help='Delete a todo', action='store_true')
# group.add_argument('-da','--delete_all', help='Delete all todos', action='store_true')
# group.add_argument('-al', '--add_list', help="adds existing list from excel, column a = ", action='store_true')

args = parser.parse_args()

print(args)
if args.update_stuff:
    print('wow')

def stub():
    pass