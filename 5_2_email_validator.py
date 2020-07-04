class EmailValidator:

    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return len(name) >= self.min_length

    def __validate_mail(self, mails):
        return mails in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email):
        user_position = email.index("@")
        user = email[: user_position]
        mail_position = user_position + email[user_position:].index(".")
        mail = email[user_position + 1: mail_position]
        domain = email[mail_position + 1:]
        return self.__validate_name(user) and self.__validate_domain(domain) and self.__validate_mail(mail)


mail_list = ["gmail", "abv"]
domain_list = ["com", "bg"]
email_validator = EmailValidator(6, mail_list, domain_list)
print(email_validator.validate("pavlin@gmail.bg"))
