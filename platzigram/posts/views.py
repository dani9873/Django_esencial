"""Posts views."""

#Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://picsum.photos/536/354'
        },       
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/536/354',
    },
    {
        'title': 'Via lactea',
        'user': {
            'name': 'C. Vander',
            'picture': 'https://picsum.photos/536/354'
    },    
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': "https://picsum.photos/id/237/536/354",
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Thespianartist',
            'picture': 'https://picsum.photos/536/354'
            },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': "https://picsum.photos/seed/picsum/536/354",
    }
]
@login_required
def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})

    #posts = [1, 2, 4]
    '''content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><strong>{user} - <i>{timestamp}</i></strong></p>
            <figure><img src= "{picture}"/></figure>
        """.format(**post))'''            
        
    #return HttpResponse(str(posts))
    #return HttpResponse('<br>'.join(content))
