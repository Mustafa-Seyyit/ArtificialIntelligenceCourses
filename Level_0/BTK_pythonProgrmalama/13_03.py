#import operations
from operations import add

def greet():
    print("merhaba")

if __name__ =="__main__":
    print("ana program")
    greet()
    #print(f"toplam : {operations.add(1,2,3)})
    print(f"toplam : {add(1,2,3,4)}")