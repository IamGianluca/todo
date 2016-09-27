# Highly Import Task (HIT) manager

Hit is a tool that lets you manage your TODO lists and sync them with popular apps like Evernote. Hit provides a command line interface (CLI) which you can use to add, remove and update events in your list. These events will then be synched with a SQLite3 database locally and then in Evernote. Hit also regularly checks for updates on the apps you synched (for instance you might have had ticked a box next to an item) and updates the same item in your local database in order to maintain your items up-to-date on all interfaces. 

Hit aims to be your only TODO lists manager and offer you the flexibility of using some of the most popular tools out there to communicate with it, when you can't access the CLI.  

# Requirements
 
The project assumes you have the following environment variables in your `/etc/environment` (in Linux):

* `EVERNOTE_DEV_TOKEN`
