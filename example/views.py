# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        api_key = request.POST['api_key']
        # Use api_key...
        
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
            <form method="POST">
                <input type="text" name="api_key">
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>
    '''
    return HttpResponse(html)
