from django.http import HttpResponse
from django.shortcuts import render

def greeting_view(request, *args, **kwargs):
    return render(request, "home.html",{})
    print(args, kwargs)
    print(request.user)

def contact_view(request, *args, **kwargs):
    return render(request,"contact.html",{} )


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is our about us page",
        "my_number" : 12334567890,
        "my_boolean" : True,
        "my_list" : [34, 23, 'ddf', 343, 'dssdf','bear'],
        "my_html" : "<h5> Its just us here</h5>"
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})


