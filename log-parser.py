#!/usr/bin/python
import argparse
import os.path

def main():
	#Create an object to hold all our command line arguments
	objParser = argparse.ArgumentParser(description='Parse, dedupe and priortize log files from network devices.')
	#Add the file argument. 
	objParser.add_argument(
		"-f", "--file", #these are the command line options that we take for this variable
		dest="strFileName", #this is the actual variable inside code
	    help="Logfile you'd like to parse. The full path is required.", #pretty description of the argument 
	    metavar="FILE",
	    nargs='?',
	    default="check_string_for_empty" #this is here for our logic later on. 
	    )
	#This is the type of log file we want to parse. 
	objParser.add_argument(
		"-t", 
		"--type", 
		dest="strLogType",
		help="The type of logfile to parse. Available options are: cisco-ios,cisco-nxos,junos", 
		metavar="TYPE",
		nargs='?',
		default="check_string_for_empty"
		)

	#Parse all our arguments into an object to be used later
	objArguments = objParser.parse_args()
	#After we have arguments built into a different argument object. We pass that to our sanitation functions. 
	boolFileError = error_check_file_exists(objArguments.strFileName)
	boolTypeError = error_check_type_arg(objArguments.strLogType)
	if (boolTypeError == True) or (boolFileError == True):
		objParser.print_help()

def process_cisco_ios_logs():
	print 'Processing Cisco IOS Logs'

def process_cisco_nxos_logs():
	print 'Processing Cisco NX-OS Logs'

def process_junos_logs():
	print 'Processing Juniper JunOS Logs'

def error_check_type_arg(strLogType):
	if strLogType in dicLogType.keys():
		dicLogType[strLogType]()
	else:
		print 'ERROR: You specified an invalid file type'
		return True

def error_check_file_exists(strFileName):
	if os.path.isfile(strFileName):
		objLogFile = open(strFileName)
		return objLogFile
	else:
		print 'ERROR: You specified an invalid file. Be sure to give full path.'
		return True

#If the user didn't input any of the required arguments let them know. I didn't feel like passing an parser object just to print the pretty help.
def empty_argument_warning():
	print 'ERROR: You didn\'t specify a type of file or file that exists. Use -h for help.'

#This is the dictionary of possible file types and associated functions. It also includes the default value we set in the argument definition for empty file type. 
dicLogType = {
	"check_string_for_empty": empty_argument_warning,
	"cisco-ios": process_cisco_ios_logs,
	"cisco-nxos": process_cisco_nxos_logs,
	"junos": process_junos_logs,
}

#Let's get this party started!
main()
