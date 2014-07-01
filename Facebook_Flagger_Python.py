#!/usr/bin/env python

"""
Facebook Flagger
by Colin Karpfinger, Punch Through Design LLC
Release r1-0

https://github.com/PunchThrough/FacebookFlagger

Released under MIT license. See LICENSE for details.
"""

import config
import serial
import time
from datetime import datetime
from gmail import Gmail

# Don't forget to replace the email and password in config.py!
g = Gmail()
g.login(config.email, config.password)

# Runs every 10 seconds
while True:
    # Connect to the Bean via virtual serial port. Wait 250ms at most.
    # Set up the Bean you want to use as a virtual serial device in the
    # Bean Loader App for OS X.
    ser = serial.Serial('/tmp/tty.LightBlue-Bean', 9600, timeout=0.25)
    twitter_emails = g.inbox().mail(sender='notify@twitter.com')
    facebook_emails = g.inbox().mail(sender='facebookmail.com')
    all_emails = g.inbox().mail(unread=True)

    # Display how many emails were found in the inbox
    print datetime.now()
    print 'Twitter notifications:', len(twitter_emails)
    print 'Facebook notifications:', len(facebook_emails)
    print 'All unread emails:', len(all_emails)
    print

    # Mark all emails as read so we don't trigger on the same email each time
    for email in twitter_emails:
        email.read()
    for email in facebook_emails:
        email.read()
    for email in all_emails:
        email.fetch()
        if 'test' in email.subject:
            ser.write("FT")  # Send both Twitter and Facebook notifications
            email.read()

    # If we're connected, send notifications
    if ser:
        if len(twitter_emails) > 0:
            ser.write("T")
        if len(facebook_emails) > 0:
            ser.write("F")
        ser.flush()
    ser.close()

    time.sleep(10)  # Sleep for 10 seconds
