from Crypto.Hash import *
# type of hash
type = MD4.new()
# hash to compare
hash = ''
# path to wordlist/s
lists = ['wordlist']
# line counter
count = 0
found = False

##
# open wordlists
##
def open_files():
	global count

	for list in lists:
		print '[!] start searching in ' + list
		if(crack(open(list,"r"))):
			break;
		print '[!] ' + str(count) + ' lines have been checked'
		print '[!] file has finished \r\n'



##
# param(list) type:file
#
# run through each line
# encrypt and compare the hashes
##
def crack(list):
	global count
	global found
	global type

	for line in list.readlines():
		count += 1
		type.update(line)
		if type.hexdigest() == hash:
			print '[+] hash found:'
			print line.strip()
			found = True
			return True
##
# Begin cracking
##
if __name__ == "__main__":
	open_files()

	print '[!] ' + str(count) + ' lines have been searched'

	if found == False:
		print '[!] nothing was found'

	print '[!] script has finished'
