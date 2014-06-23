#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2010-2014 emijrp
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import json
import MySQLdb
import os
import re
import sys
import time

def main():
    path="/data/project/wmcounter/public_html"
    if os.path.exists('%s/wmcounter.data.js' % path):
        f = open('%s/wmcounter.data.js' % path, 'r')
        data = f.read().splitlines()
        total_old = float(data[0].split('=')[1].split(';')[0].strip())
        timestamp_old = int(data[1].split('=')[1].split(';')[0].strip())
        f.close()
    else:
        [timestamp_old, total_old] = [0, 0]

    print "timestamp_old =", timestamp_old, "total_old =", total_old

    timestamp=int('%d' % time.time())*1000
    total=0.0

    conn = MySQLdb.connect(host='s3.labsdb', db='meta_p', read_default_file='~/replica.my.cnf', use_unicode=True)
    cursor = conn.cursor()
    cursor.execute("SELECT lang, family, slice, dbname FROM wiki WHERE 1;")
    result = cursor.fetchall()
    checked = 0
    families = ["wikibooks", "wikipedia", "wiktionary", "wikimedia", "wikiquote", "wikisource", "wikinews", "wikiversity", "commons", "wikispecies", "wikidata", "wikivoyage"]
    for row in result:
        lang = row[0]
        family = row[1]
        if family not in families:
            continue
        dbserver = row[2]
        dbname = row[3]+'_p'
        
        try:
            conn2 = MySQLdb.connect(host=dbserver, db=dbname, read_default_file='~/replica.my.cnf', use_unicode=True)
            cursor2 = conn2.cursor()
            #print "OK:", dbserver, dbname
            cursor2.execute("select ss_total_edits from site_stats where 1")
            result2 = cursor2.fetchall()
            for row2 in result2:
                edits = int(row2[0])
                total += edits
                checked += 1
                if edits>1:
                    print "%s.%s = %s edits" % (dbname, dbserver, edits)

            cursor2.close()
            conn2.close()
        except:
            print "Error in", dbserver, dbname

    print "timestamp =", timestamp, ", total =", total
    editrate = (total-total_old)/(timestamp-timestamp_old) # per milisecond
    print "editrate =", editrate
    print families
    print "databases =", checked

    if editrate <= 0:
        sys.exit() #wait to the next update

    if total>total_old:
        output = u"""var editinit = %s;
var timeinit = %s;
var editrate = %s; //edits per milisecond""" % (total, timestamp, editrate)
        outfile = open('%s/wmcounter.data.js' % path, 'w')
        outfile.write(output)
        outfile.close()
        
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
