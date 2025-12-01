email_u_bazi = "korisnik@gmail.com"
password_u_bazi = "1234"

uneti_email = "kor@gmail.com"
uneti_password = "1234"

print(email_u_bazi == uneti_email) # True / False
print(password_u_bazi == uneti_password)

# and
       # False                             True                          # False
print(email_u_bazi == uneti_email and password_u_bazi == uneti_password)

# registracija
# unesite email adresu ili broj telefona
email = ""
broj_telefona = "064123123"

print(email != "" or broj_telefona != "")

imao_uplatu = False
# korisnik izvrsio transakciju
imao_uplatu = not imao_uplatu

broj = 3
print(broj)
print(bin(broj))
print(3 & 2)
print(3 | 2)