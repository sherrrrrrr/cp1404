def main():
    emails_dic = {}
    while True:
        email = input("Email: ")
        if email == "":
            break

        name = extract_name_from_email(email)
        confirm_name = input(f"Is your name {name}? (Y/n) ").strip()

        if confirm_name.lower() == 'n':
            name = input("Name: ").strip()

        emails_dic[email] = name

    for email, name in emails_dic.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    name = email.split('@')[0]
    name_components = name.split('.')
    formatted_name = ' '.join(name_component.title() for name_component in name_components)
    return formatted_name


if __name__ == '__main__':
    main()