from string import Template

CONFIG = {

    "API_KEY": "'you've just exposed your secret_key'"
}
class User:

    name = ""
    email = ""

    def __init__(self, name, email):

        self.name = name
        self.email = email

    def __str__(self):

        return self.name
        
if __name__ == '__main__':
    name = input()
    email = input()
    
    user = User(name, email)
    
    # FIXME:  Here is where you want to use the template class
    template = Template("Hello, my name is $name.")

    print(f"{template.substitute(name=user.name)}")