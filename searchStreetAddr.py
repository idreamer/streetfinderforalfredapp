
# -*- coding: utf8 -*-
from urllib import quote_plus, urlencode, quote
import urllib2
import sys 
import json 
import ast
from urlparse import urlparse, parse_qs
import unicodedata 

reload(sys)
sys.setdefaultencoding("utf-8")

keyword = u"{query}"
# keyword = u"모현동"
keyword = unicodedata.normalize('NFC', keyword)

queryParams = urlencode({ quote_plus('currentPage') : '1' , quote_plus('countPerPage') : '10', quote_plus('resultType') : 'json', quote_plus('keyword') : keyword, quote_plus('confmKey') : 'U01TX0FVVEgyMDIxMDQxMTA5Mzc0NTExMTAzNTQ=' })

url = "https://www.juso.go.kr/addrlink/addrLinkApi.do?" + queryParams

def getAddrItemForAlfred(item, keyword):
	result = { 
		"type": "file:skipcheck",
		"title": item["roadAddr"],
		"subtitle": item["roadAddr"] + ' ' + item["zipNo"],
		"arg": item["roadAddr"] + ' ' + item["zipNo"],
		"autocomplete": item["roadAddr"] + ' ' + item["zipNo"],
		"text": {
			"copy": item["roadAddr"] + ' ' + item["zipNo"],
			"largetype": item["roadAddr"] + ' ' + item["zipNo"],
		}, 
		"quicklookurl": item["roadAddr"] + ' ' + item["zipNo"],
	}	
	return result

def app():
	results = []
	if len(keyword) > 0:
		response = urllib2.urlopen(url)
    
		jsonData = response.read()
		# jsonData = str(response.read())
		d = eval(jsonData)
		addrs = d["results"]["juso"]
		for item in addrs:
			if len(results) == 0:
				results = [getAddrItemForAlfred(item, keyword)]
			else:
				results.append(getAddrItemForAlfred(item, keyword))

		final = json.dumps({	"items": results })
	else:
		final = json.dumps({	"items": results })

	print(final)

app() 
