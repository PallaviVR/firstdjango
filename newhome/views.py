from django.shortcuts import render
from .forms import BookForms,ModelBookForms, SearchForms
from newhome.models import Book
#from django.utils import timezone
#from .forms1 import BookForms


#from newhome.models import Book
# Create your views here.

def form_view(request):
    msg=''
    if request.method =='POST':
        form=BookForms(request.POST)
        if form.is_valid():
            #print(form.cleaned_data.get('name'))
            book=Book.objects.create(
                name=form.cleaned_data.get('name'),
                book_author=form.cleaned_data.get('book_auhtor')
                #purchase_date=form.cleaned_data.get('purchase_date')
            )
            book.save()
            msg='Book Added Successfully!!!'
        else:
            msg=form.errors
    else:
        form=BookForms()
    return render(request,'forms.html',{"msg":msg,"forms":form})


def html_form(request):
    value=''
    if request.method== "POST":
        value=request.POST.get('name')
        #print('name',name)
        return render(request,'values.html',{'value':value})
    else:
        #value="Wrong Input"
        return render(request,'base/design.html')

def booksearch(request):
    if request.method == 'POST':
        form=SearchForms(request.POST)
        if form.is_valid():
            q=form.cleaned_data.get('q')
            book=Book.objects.filter(name__contains=q)
            #book=Book.objects.filter(name__contains=q,purchase_date_lte=timezone.now)
            #form = None
            return render(request,'showtables.html',{'book':book,'form':SearchForms()})
    else:
        form = SearchForms()
        book = Book.objects.all()

    return render(request,'showtables.html',{'book':book,'form':form})


def model_view(request):
    msg=''
    if request.method =='POST':
        form=ModelBookForms(request.POST)
        if form.is_valid():
            #print(form.cleaned_data.get('name'))
             #book=Book.objects.create(
                 #name=form.cleaned_data.get('name'),
                 #book_author=form.cleaned_data.get('book_auhtor')
             #)
            form.save()
            msg ='Book Added Successfully!!!'
        else:
            msg=form.errors
    else:
        form=ModelBookForms()
    return render(request,'forms.html',{"msg":msg,"forms":form})

    
    
    
    
    #form=CustomForms()
    #book=Book.Objects.all()
    #book=Book.Objects.filter(name='',purchase_date='')
    


"""def newform_view(request):
    form=BookForms()
    #book=Book.Objects.all()
    #book=Book.Objects.filter(name='',purchase_date='')
    context={
        "head":"Book form created here using python",
        "forms":form,
        
        #"books":book
    }
    return render(request,'newforms.html',context)


def form1_view(request):
    form1=BookForms()
    #book=Book.Objects.all()
    #book=Book.Objects.filter(name='',purchase_date='')
    context={
        "head":"Book form created here using python",
        "forms":form1,
        
        #"books":book
    }
    return render(request,'forms1.html',context)"""

