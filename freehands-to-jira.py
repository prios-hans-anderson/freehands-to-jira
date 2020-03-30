#!/usr/bin/python3.7

# library modules
from jira import JIRA

# local data.py file
import data

user = 'hans.anderson@principles.com'
apikey = 'GDrEn5TfbaAHYou2B4ihF752'
server = 'https://mpllc-dev.atlassian.net'

options = {
 'server': server
}

jira = JIRA(options, basic_auth=(user,apikey) )

# for line in lines
for d in data.data:
    card = d[0]
    fhs = d[2:]
    #jira.add_comment(data.data[0], 'new comment')
    print( "IMPORTANT: Adding comments to card ", card )
    for f in fhs:
        print( "Original invision freehand: ", f )
    
#issue = jira.issue(ticket)
#comments_b = jira.comments(issue) 

