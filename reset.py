x = input("Are u sure? (Y/n): ")
if x.lower() =='y':
    reset = """LICENS_KEY=
    ID_INSTADDR=
    PASSWORD_INSTADDR=
    PASSWORD_PAYCO="""
    open('.env', 'w', encoding='utf-8').write(reset)
    print('Successfully reset!')
else :
    print("Canceled")
