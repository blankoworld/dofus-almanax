#!/usr/bin/env python
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

# Local variables
base_url = "http://www.krosmoz.com/fr/almanax"
date_format = '%Y-%m-%d'
temporary_file_extension = '.html'
directory = dirname(realpath(__file__))
header = directory + '/header.tmpl'
footer = directory + '/footer.tmpl'

#####
## FUNCTIONS
###
def download(url):
    """
    Download a given URL
    """
    # create a browser object
    br = mechanize.Browser()
    # browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    # User-Agent
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    # open a webpage
    response = br.open(url)
    html = response.read()
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
        for div in tree.xpath("//div[@id='almanax_meryde_effect']//div[@class='more-infos-content']//p[@class='fleft']"):
            text = div.text
            if isinstance(text, unicode):
                text = text.encode('utf-8')
            # Delete useless part of string by just taking chars before "et rapporter"
            text = text.split('et rapporter')[0]
            result += text #etree.tostring(div)
        # Bonus
        for div2 in tree.xpath("//div[@id='almanax_meryde_effect']//div[@id='achievement_dofus']//div[@class='more']"):
            text2 = etree.tostring(div2)
            if isinstance(text2, unicode):
                text2 = text2.encode('utf-8')
            # Delete useless part of string by just taking chars before the point.
            text2 = text2.split('.')[0]
            bonus += text2
    filestream.close()
    # Delete all "&#13;"
    bonus = bonus.replace('&#13;', '')
    return result, bonus

def main():
    """
    Get today's date.
    Fetch 7 HTML pages from next week from 'base_url' variable.
    Read the pages and fetch some info.
    """
    # Prepare some values
    today = datetime.today()
    headerfile = open(header, 'r')
    headercontent = headerfile.read()
    headerfile.close()
    footerfile = open(footer, 'r')
    footercontent = footerfile.read()
    footerfile.close()
    # Create page's header
    result = headercontent
    # Browse next 6 days (including today)
    for i in xrange(0, 7):
        new_date = today + timedelta(i)
        formated_new_date = datetime.strftime(new_date, '%Y-%m-%d')
        newdate_string = new_date.strftime(date_format)
        filename = "%s%s" % (newdate_string, temporary_file_extension)
        # Fetch remote file if not exist locally
        if not exists(directory + '/' + filename):
            try:
                # Create file
                f = open(directory + '/' + filename, 'w')
                # Write result of given url in the file
                new_date_url = "%s/%s" % (base_url, newdate_string)
                f.write(download(new_date_url))
                f.close()
            except Exception as e:
              return e
        # Read local file
        result += '<li><time class="jour" datetime="%s">%s</time> : \n\t<ul>\n\t\t<li class="ingredient">' % (formated_new_date, newdate_string)
        offrande, bonus = fetch_infos_from(directory + '/' + filename)
        result += '%s</li>\n\t\t<li class="bonus">%s</div></li>\n\t</ul>\n</li>\n' % (offrande, bonus)
    # Close page
    result += footercontent
    # Display result
    print result

#####
## MAIN / BEGIN / END
###

if __name__ == '__main__':
    main()
