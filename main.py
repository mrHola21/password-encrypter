import tradeMark.TM
import tradeMark.main
SECURE=(("s","$"),("i","!"),("I","|"),("o","0"),("and","&"),("=","=>"),("N","|\|"),("a","@"))
def securePassword(password):
    for a,b in SECURE:
        password=password.replace(a,b)
    return password



if __name__ == "__main__":
    password=input("please enter your password:")
    password=securePassword(password)
    print(f"your password is {password}")
