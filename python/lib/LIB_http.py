#Reimplimentation of LIB_http.php from Michael Schrenk's book 
#"Webbots, Spiders, and Screen Scrapers"
#
#-----------------------------------------------------------------------
# LIB_http                                                              
#                                                                       
# F U N C T I O N S                                                     
#                                                                       
# http_get()                                                            
#    Fetches a file from the Internet with the HTTP protocol            
# http_header()                                                         
#    Same as http_get(), but only returns HTTP header instead of        
#    the normal file contents                                           
# http_get_form()                                                       
#    Submits a form with the GET method                                 
# http_get_form_withheader()                                            
#    Same as http_get_form(), but only returns HTTP header instead of   
#    the normal file contents                                           
# http_post_form()                                                      
#    Submits a form with the POST method                                
# http_post_withheader()                                                
#    Same as http_post_form(), but only returns HTTP header instead of  
#    the normal file contents                                           
# http_header()                                                         
#                                                                       
# http()                                                                
#   A common routine called by all of the previously described          
#   functions. You should always use one of the other wrappers for this 
#   routine and not call it directly.                                   
#                                                                       
#-----------------------------------------------------------------------
# R E T U R N E D   D A T A                                             
# All of these routines return a three dimensional array defined as     
# follows:	    												        
#    $return_array['FILE']   = Contents of fetched file, will also      
#                              include the HTTP header if requested    
#    $return_array['STATUS'] = CURL generated status of transfer        
#    $return_array['ERROR']  = CURL generated error status              
########################################################################

import pycurl
from StringIO import StringIO

curl = pycurl.Curl()

def http_get(url, referer = None):
  return http(url, referer, None, {}, False)

def http_header(url, referer = None):
  pass

    
def http(url, referer, method, data, incl_head):
  if referer:
    curl.setopt(pycurl.REFERER, referer)
  #method is not get
  if method:
    curl.setopt(method, True)
    
  response = StringIO()

  curl.setopt(pycurl.URL, url)
  curl.setopt(pycurl.WRITEFUNCTION, response.write)
  res = curl.perform()
  return { 'content': response.getvalue(),
           'status' : curl.getinfo(pycurl.HTTP_CODE),
           'error'  : curl.errstr()
         }

