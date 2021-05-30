from os import system

class lib:
    
    def __init__(self, name):
        self.name = name
        self.books = {}

    def DisplayBooks(self):
        print("\nBooks Available:\n")
        
        if(len(self.books) == 0):
            print("NONE")

        else:
            x = 1
            for i in self.books:
                if(self.books[i] == None):
                    print(f"{x}. {i}")
                    x += 1
        input("\nPress a Key to Continue.")

    def AddBook(self):
        b_name = input("\nEnter the Name of the Book: ")
        if b_name in self.books:
            print("Book is Already Present in the Library.")
            input("\nPress a Key to Continue.")
            return 0

        self.books[b_name] = None
        print("Book Added Successfully.")

        input("\nPress a Key to Continue.")

    def LendBook(self):
        b_name = input("\nEnter the Name of the Book: ")
        
        if b_name in self.books:
            if( (self.books[b_name] == None) ):
                print(f"Book Is Available and Has Been Successfully Issued for {self.name}!!")
                self.books[b_name] = self.name

    
        else:
            print("Sorry the Book Is Not Available!!")

        input("\nPress a Key to Continue.")

    def ReturnBook(self):
        b_name = input("\nEnter the Name of the Book: ")

        self.books[b_name] = None
        print("Book Returned Successfully!!")
    
        input("\nPress a Key to Continue.")

if __name__ == '__main__':
    n = input("Enter Your Name: ")
    user = lib(n)
    
    _ = system('cls')
    
    while(1):
        n = int(input(f"\nHey {user.name}. Welcome to the City Library!!\n\nSelect from the following options:\n1. View the Available Books\n2. Add Books\n3. Lend Books\n4. Return Books\n5. Exit the Library\n\nEnter Your Choice: "))
        
        if(n == 1):
            user.DisplayBooks()

        elif(n == 2):
            user.AddBook()
        
        elif(n == 3):
            user.LendBook()
        
        elif(n == 4):
            user.ReturnBook()
        
        elif(n == 5):
            print("Thank You For Visiting The Library!!\n")
            exit(0)