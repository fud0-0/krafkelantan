from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Performance, Stall, Activity, StarredItem, Client, Feedback
from django.http import JsonResponse

def search_item(request):
    if request.method == 'GET':
        item_id = request.GET.get('id')

        if item_id:
            first_char = item_id[0].upper()

            if first_char == 'P':
                item = Performance.objects.filter(performanceID=item_id).first()
            elif first_char == 'S':
                item = Stall.objects.filter(stallID=item_id).first()
            elif first_char == 'A':
                item = Activity.objects.filter(activityID=item_id).first()
            else:
                return render(request, 'search_item.html', {'error': 'Invalid item code'})

            if item:
                return render(request, 'search_item.html', {'item': item})
            else:
                return render(request, 'search_item.html', {'error': 'Item not found'})

    return render(request, 'search_item.html')



def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']  
        password = request.POST['password']

       
        if Client.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        if Client.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('register')

        new_client = Client(username=username, email=email, password=password)
        new_client.save()
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')

    return render(request, 'register.html')


from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

     
        try:
            client = Client.objects.get(username=username, password=password)
            request.session['clientID'] = client.clientID  
            messages.success(request, 'You are now logged in.')
            return redirect('index')
        except Client.DoesNotExist:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')



def logout(request):
    request.session.flush()  
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def activity(request):
    clientID = request.session.get('clientID')
    starred_activity = []
    if clientID:
        starred_activity = StarredItem.objects.filter(clientID_id=clientID, content_type='activity').values_list('object_id', flat=True)
    return render(request, 'activity.html', {'starred_activity': starred_activity})

def performance(request):
    clientID = request.session.get('clientID')
    starred_performances = []
    if clientID:
        starred_performances = StarredItem.objects.filter(clientID_id=clientID, content_type='performance').values_list('object_id', flat=True)
    return render(request, 'performance.html', {'starred_performances': starred_performances})

def stall(request):
    clientID = request.session.get('clientID')
    starred_stall = []
    if clientID:
        starred_stall = StarredItem.objects.filter(clientID_id=clientID, content_type='stall').values_list('object_id', flat=True)
    return render(request, 'stall.html', {'starred_stall': starred_stall})



def star_item(request, content_type, object_id):
    clientID = request.session.get('clientID')  
    if clientID:
        starred_item = StarredItem.objects.filter(clientID_id=clientID, content_type=content_type, object_id=object_id).first()

        if starred_item:
            
            starred_item.delete()
        else:
            
            StarredItem.objects.create(clientID_id=clientID, content_type=content_type, object_id=object_id)

        return redirect('starred_list')
    return redirect('login')



def starred_list(request):
    clientID = request.session.get('clientID')
    if clientID:
        
        starred_items = StarredItem.objects.filter(clientID_id=clientID)
        
        
        performances = Performance.objects.filter(performanceID__in=[item.object_id for item in starred_items if item.content_type == 'performance'])
        stalls = Stall.objects.filter(stallID__in=[item.object_id for item in starred_items if item.content_type == 'stall'])
        activities = Activity.objects.filter(activityID__in=[item.object_id for item in starred_items if item.content_type == 'activity'])

        return render(request, 'starred_list.html', {'performances': performances, 'stalls': stalls, 'activities': activities})
    return redirect('login')

def submit_feedback(request):
    clientID = request.session.get('clientID')  
    if not clientID:
        return redirect('login') 

    client = Client.objects.get(clientID=clientID)  
    
    if request.method == 'POST':
        message = request.POST.get('message')  
        

        Feedback.objects.create(
            clientID=client,
            username=client.username,  
            email=client.email,  
            message=message
        )
        return redirect('feedback_thanks')  

    return render(request, 'submit_feedback.html')

def feedback_list(request):
    feedbacks = Feedback.objects.all()  
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})

def update_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    
    if request.method == 'POST':  
        feedback.message = request.POST.get('message')
        feedback.save()
        return redirect('feedback_list')  
    
    return render(request, 'feedback_list.html')  

def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    
    if request.method == 'POST':  
        feedback.delete()  
        return redirect('feedback_list')
    
def feedback_thanks(request):
    return render(request, 'feedback_thanks.html')

def update_profile(request, client_id):
    client = get_object_or_404(Client, clientID=client_id)

    if request.method == 'POST':
        client.username = request.POST.get('username')
        client.email = request.POST.get('email')
        client.save()
        
        messages.success(request, 'Profile updated successfully!')
        
    return render(request, 'update_profile.html', {'client': client})