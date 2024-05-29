class Book:
    def __init__(self,id,name,quantity) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity
        
class User:
    def __init__(self,id,name,passward) -> None:
        self.id = id
        self.name = name
        self.passward = passward
        self.borrowbooks = []
        self.returnbooks = []
    
class Library:
    def __init__(self,name) -> None:
        self.name = name
        self.books = []
        self.users = []
        
    def AddBook(self,id,name,quantity):
        for book in self.books:
            if book.id == id and book.name == name:
                book.quantity += quantity
                return
        book = Book(id,name,quantity)
        self.books.append(book)
    
    def AddUser(self,id,name,passward):
        user = User(id,name,passward)
        self.users.append(user)
    
    def BorrowBook(self,id,user):
        for book in self.books:
            if book.id == id:
                if book in user.borrowbooks:
                    print('\n\t This book already Borrowed')
                    return
                elif book.quantity <1:
                    print('Book are Not available Copies')
                    return
                else:
                    user.borrowbooks.append(book)
                    book.quantity -= 1
                    print(f'\n\t {book.name} borrowed successfully.')
                    return
        print('\n\t No found')            
    
    def ReturnBook(self,id,user):
        for book in self.books:
            if book.id == id:
                if book in user.borrowbooks:
                    book.quantity += 1
                    user.returnbooks.append(book)
                    user.borrowbooks.remove(book)
                    print(f"\n\tReturned {book.name} Succesfully !")
                    return
                elif book not in user.borrowbooks:
                    print("\nUser has not borrowed this book.\n")

l = Library('Libraray1')
l.AddUser(1,'Rajin','shakhawat123')
l.AddUser(2,'admin','admin')
l.AddBook(2020,'dsa',2)


run = True
cur_user = 'admin'

while run:
    if cur_user == None:
        print('\n\t No logged in User !')
        
        option = input('Login or Ragistration (L/R) : ')
        
        if option == 'R':
            id = int(input('\t Enter id : '))
            name = input('\t Enter name : ')
            passward = input('\t Enter passward : ')
            
            user = l.AddUser(id,name,passward)
            cur_user = user
            
        elif option == 'L':
            id = int(input('\t Enter id : '))
            passward = input('\t Enter passward : ') 
            
            match = False
            for user in l.users:
                if user.id == id and user.passward == passward:
                    cur_user = user
                    match = True
                    print('\t Log in Successful\n')
                    break
                
            if match==False:
                print('\t\n User not found. !')
                
    else:
        if cur_user == 'admin':
            
            print('\n Option : ')
            print('1. Add Book')
            print('2. Show Users')
            print('3. Show All Books')
            print('4. Logout')
            
            op = int(input('Choose Optione : '))
            
            if op == 1:
                id = int(input("Enter Book Id : "))
                name = input('Enter Book Name : ')
                q = int(input('Enter Quantity : '))
                l.AddBook(id,name,q)
            elif op == 2:
                for user in l.users:
                    if user.name != 'admin':
                        print(f'User_id : {user.id}\tUser_Name : {user.name}')
                    
            elif op == 3:
                print('\t\tShow Book List\n')
                for book in l.books:
                    print(f'Book Name : {book.name}\tBook Id : {book.id}\tBook Quantity : {book.quantity}')
            elif op == 4:
                cur_user = None
            else:
                print('\n\t Choose Current Option !')
        else:
            print('\nOption :\n')
            print('1. Borrow Book.')
            print('2. Return Book.')
            print('3. Show All Books.')
            print('4. Show Borrowed Books.') 
            print('5. Logout.')
            
            op = int(input('Enter Option : '))
            
            if op == 1:
                id = int(input('Enter Book Id : '))
                l.BorrowBook(id,cur_user)
            elif op == 2:
                id = int(input('Enter Book Id : '))       
                l.ReturnBook(id,cur_user)
            elif op == 3:
                print("\n\tAll Books:\n")
                for book in l.books:
                    print(f'Book Name : {book.name}\t Book id : {book.id}\t Quantity : {book.quantity}')
            elif op == 4:
                print("\n\tBorrowed Books:\n")
                if len(cur_user.borrowbooks) == 0:
                    print('No Borrowed Book')
                else :
                    for book in cur_user.borrowbooks:
                        print(f'Book Name : {book.name}\t Book id : {book.id}\t Quantity : {book.quantity}')
            elif op == 5:
                print('\n\t Log Out ! \n')
                cur_user = None
                break
            else:
                print('\n\tEnter Valid Option\n')
