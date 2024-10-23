from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login
from django.core.cache import cache
from appback.models import *
from userapp.models import User
from appback.models import InvestmentTerm,Investment,Slot,Company,News,Admin
from django.contrib.auth.hashers import make_password, check_password
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.utils.decorators import method_decorator


def admin_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if 'admin_id' not in request.session:
            return redirect('adminapp:login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func


@admin_required
def index(request):
    user_count = cache.get('user_count')
    
    if user_count is None:
        user_count = User.objects.count()
        cache.set('user_count', user_count, 60 * 15) 

    adjusted_user_count = user_count - 1  # Subtracting 1 from the total user count
    
    return render(request, 'index.html', {'user_count': adjusted_user_count})

@admin_required
def add_company(request):
    investment_terms = InvestmentTerm.objects.filter(id__in=[3, 4])
    context = {'investment_term': investment_terms}
    
    if request.method == 'POST':
        investment_term_id = request.POST['investment_term']
        try:
            investment_term = InvestmentTerm.objects.get(id=investment_term_id)
        except InvestmentTerm.DoesNotExist:
            # Handle the case where the investment term does not exist
            return render(request, 'add_company.html', context)

        name = request.POST['name']
        description = request.POST['description']
        subscription_model = request.POST['subscription_model']
        company_type = request.POST['type']
        duration = request.POST['duration']
        percentage = request.POST['percentage']
        logo = request.FILES['logo']
        print(investment_term, subscription_model, logo)

        company = Company.objects.create(
            name=name,
            logo=logo,
            description=description,
            subscription_model=subscription_model,
            type=company_type,
            duration=duration,
            percentage=percentage,
            investment_term=investment_term
        )

        # Check if the investment term ID is 4 and process slots
        if investment_term.id == 4:
            for i in range(1, 5):
                slot_percentage = request.POST.get(f'slot_percentage_{i}')
                slot_fixed_amount = request.POST.get(f'slot_fixed_amount_{i}')
                if slot_percentage and slot_fixed_amount:
                    Slot.objects.create(
                        investment_term=investment_term,
                        company=company,
                        percentage=slot_percentage,
                        fixed_amount=slot_fixed_amount
                    )
                print(slot_percentage, slot_fixed_amount)

        if investment_term.id == 3:
                e_percentage = request.POST['e_percentage']
                e_amount = request.POST['e_amount']
                if e_percentage and e_amount:
                    eqAP.objects.create(
                        investment_term=investment_term,
                        company=company,
                        e_percentage=e_percentage,
                        e_amount=e_amount
                    )
                print(e_percentage, e_amount)

        return redirect('adminapp:add_company')
    
    return render(request, 'add_company.html', context)

@admin_required
def company_list(request):
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }
    return render(request, 'company_list.html', context)

@admin_required
def edit_company(request,company_id):
    investment_terms = InvestmentTerm.objects.filter(id__in=['3','4'])
    edit_company=Company.objects.filter(id=company_id)
    edit_slot=Slot.objects.filter(company=company_id)
    edit_eqAP=eqAP.objects.filter(company=company_id)
    context = {'investment_term': investment_terms,'edit_company':edit_company,'edit_slot':edit_slot,'edit_eqAP':edit_eqAP}
    
    if request.method == 'POST':
        investment_term_id = request.POST['investment_term']
        try:
            investment_term = InvestmentTerm.objects.get(id=investment_term_id)
        except InvestmentTerm.DoesNotExist:
            # Handle the case where the investment term does not exist
            return render(request, 'add_company.html', context)

        name = request.POST['name']
        description = request.POST['description']
        subscription_model = request.POST['subscription_model']
        company_type = request.POST['type']
        duration = request.POST['duration']
        percentage = request.POST['percentage']
        try:
            logo = request.FILES['logo']
            fs1=FileSystemStorage()
            file1=fs1.save(logo.name,logo)
        except MultiValueDictKeyError:
            file1=Company.objects.get(id=company_id).logo     
        print(investment_term,subscription_model,file1)  

        company=Company.objects.filter(id=company_id).update(name=name,logo=file1,description=description,subscription_model=subscription_model,type=company_type,duration=duration,percentage=percentage,investment_term=investment_term)
  # Check if the investment term is "foco" and process slots
# Check if the investment term is "foco" and process slots
        if investment_term.id == 4:
            # Clear existing slots for the company
            Slot.objects.filter(company=company_id).delete()

            # Iterate over the slots and create/update them
            for i in range(1, 5):
                slot_percentage = request.POST.get(f'slot_percentage_{i}')
                slot_fixed_amount = request.POST.get(f'slot_fixed_amount_{i}')
                
                if slot_percentage and slot_fixed_amount:
                    Slot.objects.create(
                        investment_term=investment_term,
                        company=edit_company.first(),  # Retrieve the Company object
                        percentage=slot_percentage,
                        fixed_amount=slot_fixed_amount
                    )

        if investment_term.id == 3:
            # Clear existing slots for the company
            eqAP.objects.filter(company=company_id).delete()
            e_percentage = request.POST['e_percentage']
            e_amount = request.POST['e_amount']
                
            if e_percentage and e_amount:
                eqAP.objects.create(
                    investment_term=investment_term,
                    company=edit_company.first(),  # Retrieve the Company object
                    e_percentage=e_percentage,
                    e_amount=e_amount
                )


# Note: You may need to adjust the logic based on your exact requirements for handling slots.
        return redirect('adminapp:company_list')
    
    return render(request, 'edit_company.html', context)

@admin_required
def delete_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    
    if request.method == 'POST':
        company.delete()
        return redirect('adminapp:company_list') 
    
    return render(request, 'confirm_delete_company.html', {'company': company})


@admin_required
def add_investment_term(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        short_title = request.POST['short_title']
        description = request.POST['description']
        minimum_investment = request.POST['minimum_investment']
        duration = request.POST['duration']
        returns = request.POST['returns']
        deliverables = request.POST['deliverables']
        video = request.POST['video']
    
        print(title,duration,returns) 
        InvestmentTerm.objects.create(title=title,short_title=short_title,description=description,minimum_investment=minimum_investment,duration=duration,returns=returns,deliverables=deliverables,video=video)
    return render(request, 'terms.html')

@admin_required
def investment_terms_list(request):
    investment_terms = InvestmentTerm.objects.all()
    context = {
        'investment_terms': investment_terms,
    }
    return render(request, 'term_list.html', context)

@admin_required
def edit_investment_term(request, term_id):
    term = get_object_or_404(InvestmentTerm, id=term_id)

    if request.method == 'POST':
        term.title = request.POST['title']
        term.short_title = request.POST['short_title']
        term.description = request.POST['description']
        term.minimum_investment = request.POST['minimum_investment']
        term.duration = request.POST['duration']
        term.returns = request.POST['returns']
        term.deliverables = request.POST['deliverables']
        term.video = request.POST['video']
        
        term.save()
        return redirect('adminapp:investment_term_list')  
    
    return render(request, 'edit_term.html', {'term': term})

@admin_required
def delete_investment_term(request, term_id):
    term = get_object_or_404(InvestmentTerm, id=term_id)
    
    if request.method == 'POST':
        term.delete()
        return redirect('adminapp:investment_term_list')  
    
    return render(request, 'confirm_delete.html', {'term': term})

@admin_required
def investment_list(request):
    investments = Investment.objects.all()
    return render(request, 'usertable.html', {'investments': investments})


from django.http import HttpResponse
from userapp.models import User

@admin_required
def block_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_blocked = True
    user.save()
    return redirect('adminapp:investment_list') 


@admin_required
def unblock_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_blocked = False
    user.save()
    return redirect('adminapp:investment_list')  

@admin_required
def add_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image') 
        
        if title and description and image:
            News.objects.create(title=title, description=description, image=image)
            return redirect('adminapp:news_list')
            
    return render(request, 'add_news.html')

@admin_required
def news_list(request):
    news_articles = News.objects.all()
    context = {
        'news_articles': news_articles,
    }
    return render(request, 'news_list.html', context)

@admin_required
def edit_news(request, news_id):
    news_article = get_object_or_404(News, pk=news_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image') if 'image' in request.FILES else None
        
        # Update news article fields
        news_article.title = title
        news_article.description = description
        if image:
            news_article.image = image
        news_article.save()
        
        return redirect('adminapp:news_list')  
    
    context = {
        'news_article': news_article,
    }
    return render(request, 'edit_news.html', context)

@admin_required
def delete_news(request, news_id):
    news_article = get_object_or_404(News, pk=news_id)
    
    if request.method == 'POST':
       
        news_article.delete()
        return redirect('adminapp:news_list')  
    
    context = {
        'news_article': news_article,
    }
    return render(request, 'delete_news.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if Admin.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:

            admin = Admin(username=username, password=make_password(password))  # Hash the password
            admin.save()
            messages.success(request, 'Registration successful')
            return redirect('adminapp:login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            admin = Admin.objects.get(username=username)
            if admin.check_password(password):
                # Log the user in by setting the session or other means
                request.session['admin_id'] = admin.id  # Example of setting session
                return redirect('adminapp:index')
            else:
                messages.error(request, 'Invalid username or password')
        except Admin.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')
   
def logout_view(request):
    logout(request)
    return redirect('adminapp:login')

