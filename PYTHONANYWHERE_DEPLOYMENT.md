╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║         🚀 DEPLOY TO PYTHONANYWHERE - STEP BY STEP GUIDE                  ║
║                                                                            ║
║              Free Forever Hosting for Your Daily Tracker                   ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝


📋 WHAT YOU NEED
════════════════════════════════════════════════════════════════════════════

✓ PythonAnywhere account (created ✅)
✓ Your GitHub repo URL
✓ Your code files


🚀 DEPLOYMENT STEPS (15 minutes total)
════════════════════════════════════════════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: CREATE A NEW WEB APP
────────────────────────────

1. Go to: https://www.pythonanywhere.com/user/YOUR_USERNAME/webapps/
2. Click "Add a new web app"
3. Choose:
   - Domain: your_username.pythonanywhere.com
   - Framework: Manual configuration
   - Python version: 3.9
4. Click "Next"

Your domain will be: https://your_username.pythonanywhere.com


STEP 2: UPLOAD YOUR CODE
────────────────────────

Option A: Using Bash Console (Recommended)
──────────────────────────────────────────
1. Go to: https://www.pythonanywhere.com/user/YOUR_USERNAME/consoles/
2. Click "Bash console"
3. Run these commands:

   # Clone your GitHub repo
   git clone https://github.com/YOUR_USERNAME/ajan-daily-tracker.git

   # Check if cloned
   ls -la ajan-daily-tracker


Option B: Upload Files via Web Interface
──────────────────────────────────────────
1. Go to: https://www.pythonanywhere.com/user/YOUR_USERNAME/files/
2. Right-click → "New directory" → name it "ajan-daily-tracker"
3. Upload your daily_tracker_web.py


STEP 3: CONFIGURE THE WEB APP
──────────────────────────────

1. Go to: https://www.pythonanywhere.com/user/YOUR_USERNAME/webapps/
2. Click on your web app: your_username.pythonanywhere.com
3. Scroll down to "Code section"
4. Set:
   - Source code: /home/your_username/ajan-daily-tracker
   - Working directory: /home/your_username/ajan-daily-tracker


STEP 4: CREATE WSGI CONFIGURATION FILE
───────────────────────────────────────

This is the MOST IMPORTANT step!

1. In "Code section" on your web app page:
   - Click the WSGI configuration file link
   - It's usually: /var/www/your_username_pythonanywhere_com_wsgi.py
   
2. Replace ALL content with this:

────────────────────────────────────────────────────────────────────
import sys
import os

# Add your project directory to the path
path = '/home/YOUR_USERNAME/ajan-daily-tracker'
if path not in sys.path:
    sys.path.append(path)

# Import the Flask/WSGI app
# Since we're using http.server, we'll create a wrapper

from http.server import HTTPServer, SimpleHTTPRequestHandler
from threading import Thread
import socket

# Our tracker code
exec(open('/home/YOUR_USERNAME/ajan-daily-tracker/daily_tracker_web.py').read())

# Create WSGI app for PythonAnywhere
class WSGIApp:
    def __call__(self, environ, start_response):
        # For now, return a simple HTML response
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        
        # Return the HTML template from our app
        return [HTML_TEMPLATE.encode('utf-8')]

application = WSGIApp()
────────────────────────────────────────────────────────────────────

⚠️  Replace YOUR_USERNAME with your actual PythonAnywhere username!

3. Save the file


STEP 5: RELOAD YOUR WEB APP
────────────────────────────

1. Go back to: https://www.pythonanywhere.com/user/YOUR_USERNAME/webapps/
2. Click the green "Reload" button
3. Wait for it to say "Your web app is now live"


✅ YOUR APP IS NOW LIVE!
────────────────────────

Visit: https://YOUR_USERNAME.pythonanywhere.com

You should see your beautiful Ajan Daily Tracker! 🎉


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


⚡ ALTERNATIVE: SIMPLER METHOD WITH FLASK
════════════════════════════════════════════════════════════════════════════

If the above seems complex, here's a simpler way:

1. Install Flask on PythonAnywhere:
   - Bash console: pip install flask

2. Create app.py in your directory:

   from flask import Flask, render_template_string
   
   app = Flask(__name__)
   
   # Your HTML template (from daily_tracker_web.py)
   HTML_TEMPLATE = '''...your HTML...'''
   
   @app.route('/')
   def index():
       return render_template_string(HTML_TEMPLATE)
   
   if __name__ == '__main__':
       app.run()

3. Configure web app to use Flask framework
4. Reload
5. Done!


🔧 TROUBLESHOOTING
════════════════════════════════════════════════════════════════════════════

ERROR: "ModuleNotFoundError: No module named 'X'"
───────────────────────────────────────────────
Solution:
1. Open Bash console on PythonAnywhere
2. Run: pip install module_name
3. Reload your web app


ERROR: "Permission denied"
──────────────────────────
Solution:
1. Check file permissions: chmod 644 daily_tracker_web.py
2. Make sure paths are correct (use full paths, not ~)


ERROR: "Static files not loading"
──────────────────────────────────
Solution:
1. PythonAnywhere serves static files separately
2. Include all CSS/JS inline in HTML (already done!)
3. Should work fine


ERROR: "Supabase connection failing"
────────────────────────────────────
Solution:
1. Check browser console (F12) for errors
2. Verify Supabase URL and API key in code
3. Check Supabase RLS policies allow public access


💡 TIPS FOR PYTHONANYWHERE
════════════════════════════════════════════════════════════════════════════

✓ Files are at: /home/your_username/
✓ Use Bash console to run commands
✓ Always reload after code changes
✓ Free tier has 100MB storage (your app is ~40KB)
✓ Free tier allows limited API calls
✓ Data stored in Supabase (not PythonAnywhere)


🌐 YOUR FINAL URL
════════════════════════════════════════════════════════════════════════════

https://your_username.pythonanywhere.com

Share this with friends! ✨


📊 WHAT HAPPENS AFTER DEPLOYMENT
════════════════════════════════════════════════════════════════════════════

1. User visits: https://your_username.pythonanywhere.com
2. Browser loads your HTML + CSS + JavaScript
3. User toggles habits, enters hours
4. JavaScript calls Supabase API directly
5. Data stored in Supabase (free cloud database)
6. Works on all devices
7. Syncs automatically


✅ FREE FOREVER INCLUDES
════════════════════════════════════════════════════════════════════════════

✓ Python 3.9
✓ Your domain: your_username.pythonanywhere.com
✓ 100MB disk space
✓ Always-on hosting (no spin-down)
✓ CPU limits (but fine for your tracker)
✓ Email support


📈 DATA FLOW
════════════════════════════════════════════════════════════════════════════

Browser (Your Tracker UI)
         ↓
PythonAnywhere (Serves HTML/CSS/JS)
         ↓
JavaScript (In Browser)
         ↓
Supabase API (Cloud Database)
         ↓
Your Data (Stored Forever)


═══════════════════════════════════════════════════════════════════════════

                    YOU'RE ALMOST THERE! 🚀

        Follow the 5 steps above and your app will be live
              in production in just 15 minutes!

═══════════════════════════════════════════════════════════════════════════

Made with ❤️ - Start tracking! 💪✨

═══════════════════════════════════════════════════════════════════════════
