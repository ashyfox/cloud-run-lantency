import subprocess

subprocess.run("curl -w '@/home/bill/latency/curl-format.txt' -o /dev/null -s 'www.ukservers.com/' ",shell=True)

#subprocess.run("curl -o null -w  ' Time_namelookup：%{time_namelookup}:\n TCP_Connect time:%{time_connect}\n SSL_Connect time:%{time_appconnect}\n Redirect time:%{time_redirect}\n Pretransfer:%{time_pretransfer}\n Starttransfer:%{time_starttransfer}\n time_total:%{time_total}\n speed_download:%{speed_download}' https://www.gov.uk/ ",shell=True)
#subprocess.run("touch /Users/bill/Desktop/Python/curl-fomat.txt",shell=True)
 

#subprocess.run("curl -o /dev/null -s -w 'Total: %{time_total}s\n'  https://www.gov.uk/ ",shell=True)
