from django.shortcuts import render , get_object_or_404

# Create your views here.
from .models import Post , Customer , Recent_Post ,  Comment , About , Team  , Contact
from .forms import CommentForm , ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    post_list = Post.objects.all()
    users = Customer.objects.all()

    context = {
       'post_list': post_list,
       'users': users
    }
    return render(request , 'home/index.html' , context)


def post_detail(request , slug):
    post_detail = get_object_or_404(Post , slug=slug)
    recent_posts = Recent_Post.objects.all()
    # todo show all comments
    comments = Comment.objects.all()

      # todo make new comment
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST , request.FILES)
        if comment_form.is_valid():
            new_comment  = comment_form.save(commit=False)
            new_comment.post = post_detail
            new_comment.save()


    context = {
        'post_detail': post_detail,
        'recent_posts':recent_posts,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request , 'home/post_detail.html' , context)



def about_us(request):
    food_info = About.objects.all()
    teams = Team.objects.all()
    users = Customer.objects.all()

    context = {
        'food_info': food_info,
        'teams': teams,
        'users': users,
    }
    return render(request , 'about-us.html' , context)




def contact_us(request):
    contacts = Contact.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['text']

        send_mail(
            name,
            message,
            settings.EMAIL_HOST_USER,
            [email]
        )
        messages.info(request , 'thanks for buying from us! ')

    context = {
        'contacts': contacts,
        'form': form
    }
    return render(request , 'contact-us.html' , context)