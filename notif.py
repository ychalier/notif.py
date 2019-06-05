"""Notifpy 1.0, a custom YouTube subscription system.
Usage: python notif.py [FLAGS] <ACTION> <ARGUMENTS>

Flags:
    --help      display this message
    --version   display current program version

Actions:
    clean       remove old videos from the database
    create      add a new channel or pattern to the database
    delete      remove a channel or a pattern from the database
    html        generate an HTML page with recent videos
    list        list all channels and patterns in the database
    update      check for new videos using YouTube API

Arguments:
    create
        channel <ID> <PRIORITY> add a new channel to the database, ID is either
                                  the channel id (24 characters starting with":
                                  'UC') or the username, both are found in the
                                  channel URL, and PRIORITY is the update
                                  priority for this channel
        pattern <ID> <REGEX>    add a new pattern th the database, ID is the
                                  channel id and REGEX is the matching pattern

    delete
        channel <ID>            remove the channel with id ID from the database
        pattern <ID>            remove the pattern with id ID from the database

    html
        videos <PARAMETERS>     print HTML of a cluster of videos to stdout
        body <PARAMETERS>       only print HTML body of `videos`
        channels <PARAMETERS>   print HTML of videos grouped by channel to
                                  stdout

    update:
                                force update of all channels
        schedule                let the program decide which channels to update
        priority <PRIORITY>     force update of channels of a given PRIORITY
        channel <ID>            force update of a channel, given by its ID

Parameters:
    Pass parameters with the format `key=value`, by quoting it if there is a
    space inside it. Default values are the following:

    limit=50                pagination size
    offset=0                pagination offset
    order=publishedAt\ DESC videos ordering field (`creation` might be another
                              field worth of interest)
    channel=None            channel id to filter out the results
    query=None              query to filter out video titles or channel titles

The automatic schedule should be setup using cron tasks. The `update schedule`
rule should be called every hour of the day. If more than that, API's quotas can
be exceeded. Channels with priority 0 are updated on Saturdays at midnight.
Channels with priority 1 are updated every day at 7pm. Channels with priority 2
are updated every day at 8am, 12am, 4pm, 6pm, 8pm and 10pm."""

from notifpy.db import Database
from notifpy.yt import Endpoint
from notifpy import Manager
import sys


if __name__ == "__main__":
    if "--help" in sys.argv:
        print(__doc__)
        exit()
    elif "--version" in sys.argv:
        print("Notifpy 1.0")
        exit()
    db = Database("db.sqlite3")
    endpoint = Endpoint("secret.json")
    if not Manager(db, endpoint).process(sys.argv[1:]):
        print(__doc__.split("\n")[1] + "\nTry 'python notif.py --help' for more information.")
    db.close()
