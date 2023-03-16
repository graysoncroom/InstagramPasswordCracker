# *InstagramPasswordCracker*

Takes an argument of a username and a password list from standard input. Brute forces instagram account based on provided password list.

'b' I take NO responsibility for the use of this script. This code is intended for educational purposes. Please DO NOT use this program for malicious purposes.</b>

This program uses the library known splinter to interact with the instagram website. This library is well documented and has few dependencies.

The program uses firefox, but if you use google chrome all you have to do is change "with Browser('firefox', headless=True)" to "with Browser('chrome', headless=True)". Simple as that.

If you use firefox, you must be running at least version 55 to run this program in headless mode.

Instagram gives a timeout of about 11 mins after 14 to 25 invalid passwords are tested. The program will wait for that time when it gets a certain error message before attempting to crack again.

On average, the program will be able to test around 60 to 125 passwords in an hour.

The slow speeds are due to the timeout and not the fact that this program is written in Python.

The password list file provided must seperate passwords with a newline.

Usage:

./insta_cracker [username] < [password list file]
