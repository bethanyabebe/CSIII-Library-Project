import wx
from user import User
from library import Library

def removerbook(request):
    Book = RemoveBook.objects.all()
    return render(request,'remove book',{'Book':Book})

def RemoveBookSubmission(request):
    if request.session.has_key('logged'):
        if request.method == "post":
            user_id = request.session["user id"]
            user1 = User.objects.get(id = user_id)
            bookname = request.POST["book name"]
            subject = request.POST["subject"]
            category=request.POST["category"]
            remove = RemoveBook(user = )
            remove.save()
            Book = RemoveBook.objects.all()
            return render(request,'dashboard',{'Book':Book})
    return redirect('/')
