#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# almanax_next_week.py
#

#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
# 
# Copyright (C) 2012 Olivier DOSSMANN 
#  <olivier+almanax@dossmann.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
# 0. You just DO WHAT THE FUCK YOU WANT TO.

# Libraries
from datetime import datetime
from datetime import timedelta
from os.path import exists
from os.path import realpath
from os.path import dirname
import mechanize
from lxml import etree
from string import Template
from distutils.dir_util import copy_tree
import sys

# Local variables
base_url = u"http://www.krosmoz.com/fr/almanax"
date_format = '%Y-%m-%d'
temporary_file_extension = u'.html'
directory = dirname(realpath(__file__))
header = directory + "/header.tmpl"
footer = directory + "/footer.tmpl"
day_duration = 15
# Directory name in which downloaded page will go
dl_directory = directory + "/dl"
# Static directory which contains CSS, pictures, etc.
static_directory = directory + "/static"
# Public directory in which result will go
public_directory = directory + "/public"

#####
## FUNCTIONS
###
def download(url):
    """
    Download a given URL
    """
    # create a browser object
    br = mechanize.Browser()
    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=5)
    # open a webpage
    response = br.open(url)
    html = response.read().decode('utf-8')
    return html or ''

def fetch_infos_from(filename):
    """
    Read 7 files from today and fetch specific infos about 
    """
    result = ''
    bonus = ''
    with open(filename, 'r') as filestream:
        content = filestream.read()
        if not content:
            return result, bonus
        tree = etree.HTML(content)
        # Offrande
        offer_html = tree.xpath("//div[@id='almanax_meryde_effect']//div[@class='more-infos-content']//p[@class='fleft']")
        if offer_html and len(offer_html) > 0:
            div = offer_html[0]
            text = div.text
            # Delete useless part of string by just taking chars before "et rapporter"
            text = text.split('et rapporter')[0]
            result += text
        # Bonus
        bonus_html = tree.xpath("//div[@id='almanax_meryde_effect']//div[@id='achievement_dofus']//div[@class='more']")
        if bonus_html and len(bonus_html) > 0:
            div2 = bonus_html[0]
            text2 = etree.tounicode(div2)
            # Delete useless part of string by just taking chars before the point.
            text2 = text2.split('.')[0]
            bonus += text2
    filestream.close()
    # Delete all "&#13;"
    bonus = bonus.replace('&#13;', '')
    return result, bonus

def generate_public_directory():
    """
    Copy static directory to public one
    """
    copy_tree(static_directory, public_directory)

def main(resultfile=None):
    """
    Get today's date.
    Fetch 7 HTML pages from next week from 'base_url' variable.
    Read the pages and fetch some info.
    """
    # Prepare some values
    today = datetime.today()
    headerfile = open(header, 'r')
    headercontent = Template(headerfile.read())
    headerfile.close()
    header_replace_content = headercontent.safe_substitute({
        'number': day_duration - 1,
    })
    footerfile = open(footer, 'r')
    footercontent = footerfile.read()
    footerfile.close()
    # Create page's header
    result = header_replace_content
    # Browse next xx days (including today)
    for i in range(0, day_duration):
        new_date = today + timedelta(i)
        formated_new_date = datetime.strftime(new_date, '%Y-%m-%d')
        newdate_string = new_date.strftime(date_format)
        filename = "%s%s" % (newdate_string, temporary_file_extension)
        # Fetch remote file if not exist locally
        calendar_file = dl_directory + '/' + filename
        if not exists(calendar_file):
            try:
                # Create file
                with open(calendar_file, 'w') as f:
                    # Write result of given url in the file
                    new_date_url = "%s/%s" % (base_url, newdate_string)
                    content = download(new_date_url)
                    f.write(content)
                    f.close()
            except Exception as e:
              return e
        # Read local file
        result += u'<li><time class="jour" datetime="%s">%s</time> : \n\t<ul>\n\t\t<li class="ingredient">' % (formated_new_date, newdate_string)
        offrande, bonus = fetch_infos_from(calendar_file)
        result += u'%s</li>\n\t\t<li class="bonus">%s</div></li>\n\t</ul>\n</li>\n' % (offrande, bonus)
    # Close page
    result += footercontent
    # Generate public directory content
    generate_public_directory()
    # Display result
    if resultfile:
        with open(resultfile, 'w') as f:
            f.write(result)
            f.close()
    else:
        print(result)

#####
## MAIN / BEGIN / END
###

if __name__ == '__main__':
    # Use first command line parameter as argument to main()
    args = sys.argv[1:]
    resultfile = None
    if len(args) > 0:
        resultfile = args[0]
    main(resultfile)
