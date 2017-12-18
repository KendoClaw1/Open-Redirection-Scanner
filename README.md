# Open-Redirection-Scanner
a python tool used to scan for Open redirection vulnerability

###How to Use:

what makes this tool diffrent is that you can use it for auth-based scanning because you can provide a cookie if u want, example:

python openredir.py -u test.com -c "Cookie=test"

Also this tool supports 2 types of scanning:

1- Url based

2-parameter based

the tool uses different wordlists for each type of scans

example for using parameter based:

python openredir.py -u test.com/file.php?redirc= -p test.com

you must specify a domain when using parameter based scanning, the tool will use the domain name while scanning




usage: openredirectionscanner.py [-h] [-u URL] [-p domain.com] [-f FILEPATH]
                                 [-c Cookie=value] [-v]

Open Redirection Scanner
arguments:

  -h, --help       show this help message and exit
  
  -u (URL)           Url to test
  
  -p (domain.com)    Parameter based scan (Uses a diffrent payload list),you
                   must Specify a domain to be used in the payloads
  -f (FILEPATH)      load URLs from a file (Optional)
  
  -c (Cookie=value)  scan with a specific Cookie (Optional)
  
  -v               Verbose mode (Optional)
  
  
  
