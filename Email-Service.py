import smtplib
from password import password, email, domen

smtpObj = smtplib.SMTP('smtp.' + domen, 587)
smtpObj.starttls()

smtpObj.login(email, password)

smtpObj.sendmail(email, "BelovBadim2014@yandex.ru", "Hello!")

smtpObj.quit()