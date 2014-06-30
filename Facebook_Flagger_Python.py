# Facebook Flagger
# Release r1-0
# by Colin Karpfinger, Punch Through Design LLC
# Released under MIT license. See LICENSE for details.

from gmail import Gmail 
import serial
import time

while True:
	ser = serial.Serial('/tmp/tty.LightBlue-Bean', 9600, timeout=0.25) # wait 250msec for bean
	g = Gmail()
	g.login('email', 'password')

	twitter_emails = g.inbox().mail(sender="notify@twitter.com")
	facebook_emails = g.inbox().mail(sender="facebookmail.com")
	all_emails = g.inbox().mail(unread=True)

	print "Twitter Notifications: "+str(len(twitter_emails))
	print "Facebook Notifications: "+str(len(facebook_emails))
	print "All Emails: "+str(len(all_emails))

	for email in twitter_emails:
		email.read()
	for email in facebook_emails:
		email.read()
	for email in all_emails:
		email.fetch()
		if 'test' in email.subject:
			ser.write("FT") #send both twitter and facebook notifications 
			email.read()

	if ser :
		if len(twitter_emails)>0:
			ser.write("T")	
		if len(facebook_emails)>0:
			ser.write("F")
		ser.flush()

	g.logout()
	ser.close()
	time.sleep(10) #sleep for n seconds