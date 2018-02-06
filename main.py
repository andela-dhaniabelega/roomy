"""
Roomy

Usage: 
	roomy create_room <room_type> <room_name>...
	roomy add_person <person_name> <FELL0W|STAFF> [wants_accomodation]
"""
from docopt import docopt

import commands as command_fns


COMMANDS = {'create_room', 'add_person'}

def is_command(cmd):
	return cmd in COMMANDS

def dispatch_cmd(cmd, arguments):
	cmd_fn = getattr(command_fns, cmd)
	return cmd_fn(arguments)

def main():
	arguments = docopt(__doc__, version='1.0.0')
	for key, value in arguments.items():
		if value and is_command(key):
			print(dispatch_cmd(key, arguments))


if __name__ == '__main__':
	main()