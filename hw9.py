#!/usr/bin/python
# CS288 Homework 9
# Read the skeleton code carefully and try to follow the structure
# You may modify the code but try to stay within the framework.

# -- coding: utf-8 --  

#!/usr/bin/env python
 
import libxml2
import sys
import os
import commands
import re
import sys
import pdb
 
import MySQLdb
 
from xml.dom.minidom import parse, parseString
 
# for converting dict to xml
from cStringIO import StringIO
from xml.parsers import expat
 
def get_elms_for_atr_val(tag):
   lst=[]
   elms = dom.getElementsByTagName(tag)
   lst = lst + elms
   #print elms
   return lst
 
# get all text recursively to the bottom
def get_text(e):
   lst=[]
   #print e.nodeType
   if e.nodeType in [3, 4]:
      lst.append(e.data)
      #print e.data
   else:
      for y in e.childNodes:
         lst.append(get_text(y))
   return lst
 
# replace whitespace chars
def replace_white_space(str):
   p = re.compile(r'\s+')
   new = p.sub(' ',str)   # a lot of \n\t\t\t\t\t\t
   return new.strip()
 
# replace but these chars including ':'
def replace_non_alpha_numeric(s):
   p = re.compile(r'[^a-zA-Z0-9:-]+')
   #   p = re.compile(r'\W+') # replace whitespace chars
   new = p.sub(' ',s)
   return new.strip()
 
# convert to xhtml
# use: java -jar tagsoup-1.2.jar --files html_file
def html_to_xml(fn):
   if __name__ == "__main__":
      os.system("java -jar tagsoup-1.2.1.jar --files '%s'" % fn)
      xhtml_fn = fn.replace('.html','.xhtml')
      
   return xhtml_fn
 
def extract_values(dm):
   lst = []
   vals = []
   l = get_elms_for_atr_val('tr')
   lst = lst + l
   # ............
   for x in lst:
      vals = vals + get_text(x)
   # ............
   #print vals
   return vals
 
# mysql> describe most_active;
def insert_to_db(l,tbl):
   
   return
 
# show databases;
# show tables;
def main():
   html_fn = sys.argv[1]
   xhtml_fn = html_to_xml(html_fn)
   #pdb.set_trace()
   fn = html_fn.replace('.html','')
   global dom
   dom = parse(xhtml_fn)
   lst = extract_values(dom)
   stock = 0
   volist=[]
   sylist=[]
   stolist=[]
   prilist=[]
   pclist=[]
   perlist=[]
   while stock < 100:
      key = stock * 6
      symbolname = re.findall(r"\((.+)\)", str(lst[9+(6*stock)][1][0]))
      stockname = re.findall(r"u'(.+)\ \(", str(lst[9+(6*stock)][1][0]))
      volumename = re.findall(r"u'(.+)'", str(lst[10+(6*stock)][0]))
      pricename = re.findall(r"u'(.+)'", str(lst[11+(6*stock)]))
      pricechange = re.findall(r"u'(.+)'", str(lst[12+(6*stock)][0]))
      percentchange = re.findall(r"u'(.+)'", str(lst[13+(6*stock)][0]))
      volist.append("".join(volumename))
      sylist.append("".join(symbolname))
      stolist.append("".join(stockname))
      prilist.append("".join(pricename))
      pclist.append("".join(pricechange))
      perlist.append("".join(percentchange))
      stock = stock + 1
   stock = 0
 
   conn = MySQLdb.connect(host="", user="root", password=".Zlj20082114", db="stocks")
   cursor = conn.cursor()
   cursor.execute("DROP TABLE IF EXISTS stock")
   S = """CREATE TABLE stock ( symbol CHAR(4), name CHAR(70), volume CHAR(20), price CHAR(10), pc CHAR(10), perc CHAR(10) )"""
   cursor.execute(S)
   while stock < 100:
      ins = 'INSERT INTO stock (symbol, name, volume, price, pc, perc) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")' % ( sylist[stock], stolist[stock], volist[stock], prilist[stock], pclist[stock], perlist[stock])
      cursor.execute(ins)
      stock = stock + 1   
   cursor.close()
   conn.commit()
   conn.close()
   # make sure your mysql server is up and running
   #cursor = insert_to_db(lst,fn) # fn = table name for mysql
 
   #l = select_from_db(cursor,fn) # display the table on the screen
 
   # make sure the Apache web server is up and running
   # write a PHP script to display the table(s) on your browser
 
   return
# end of main()
 
if __name__ == "__main__":
    main()