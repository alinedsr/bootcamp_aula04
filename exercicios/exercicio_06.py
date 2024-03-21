#    Dada uma lista de emails, remover todos os duplicados.

emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos: list = set(emails)

for email in emails_unicos:
    print(email)