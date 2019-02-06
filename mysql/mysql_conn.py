import MySQLdb
import re

def transform_regex(regex):
   # This is for Prod
   s = re.search("(.+)(\(\.html\)\?\$)", regex)
   # This is for PTEST
   #s = re.search("(.+)(.html)$", regex)
    if s is None:
      return
    return "%s%s" % (s.group(1), "((.html)?(\\\?)?(.+)?)?$")

db = MySQLdb.connect(host="127.0.0.1",
                     user="root",         # your username
                     passwd="pass",  # your password
                     port=3306,
                     db="db")        # name of the data base

cur = db.cursor()

# execute sql query
cur.execute("SELECT id, reg_exp FROM redirect_rules where reg_exp like '%(.html)?$'")

# process the response
for row in cur.fetchall():
    new_regex = transform_regex(row[1])
    if new_regex is None:
       continue
    n = "update redirect_rules set reg_exp='%s' where id=%s" % (new_regex, row[0])
    print n

db.close()
