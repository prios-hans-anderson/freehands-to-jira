#!/usr/bin/python3.7

# library modules
from jira import JIRA

# local data.py file
from data import data
from urlsdata import urls

# this is fragile at least for case-sensitivity
def url(fhname, listofurls = urls):
    link = ""
    for u in urls:
        if u.count( fhname ) > 0:
            return u[4]
    return 0

user = 'hans.anderson@principles.com'
apikey = 'GDrEn5TfbaAHYou2B4ihF752'
server = 'https://mpllc-dev.atlassian.net'

options = {
 'server': server
}

jira = JIRA(options, basic_auth=(user,apikey) )

# for line in lines
for d in data:
    card = d[0]
    fhs = d[1:]
    print( "\nAdding comments to card ", card )
    
    for f in fhs:
        u = url( f )
        print( ".......... ", f )
        print( ">>>>>>>>>> ", ( "MISSING " + f ) if u == 0 else u )
       
        newcomment = card + " IMPORTANT: referenced invision freehand " + f + " is now " + ( "MISSING " if u == 0 else u )
        print( newcomment )
        
        # this is the money shot. 57 of the original fh's seem to be missing. not sure why.

        ###########################################################
        ########## jira.add_comment(card, newcomment)#############
        ###########################################################

        # this writing all to test card. seems to have worked. spot-check works
        #jira.add_comment('DSC-1485', newcomment)
    
#issue = jira.issue(ticket)
#comments_b = jira.comments(issue) 

