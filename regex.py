import re
pattern = r"([\w\.-]+)@([\w\.-]+)(\w\.-]+)"
emailStr = "info@github.com,user@yahoomail.com,user@gmail.com,user@good-mail.com"
emails  = re.findall(pattern, emailStr)
if emails:
    for email in emails:
     em = email[0] + "@"
     for i in range(1, len(email)):
      em += email[i]
    print(em)