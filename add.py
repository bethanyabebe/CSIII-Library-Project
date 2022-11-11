import wx
from user import User
from library import Library

def addbook(request):
    Book = AddBook.objects.all()
    return render(request,'add book',{'Book':Book})

def AddBookSubmission(request):
    if request.session.has_key('logged'):
        if request.method == "post":
            user_id = request.session["user id"]
            user1 = User.objects.get(id = user_id)
            bookname = request.POST["book name"]
            subject = request.POST["subject"]
            category=request.POST["category"]
            add = AddBook(user = )
            add.save()
            Book = AddBook.objects.all()
            return render(request,'dashboard',{'Book':Book})
    return redirect('/')
