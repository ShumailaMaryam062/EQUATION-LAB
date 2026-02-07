#!/usr/bin/env python3
import os
import sys
import http.server
import socketserver

# Change to www directory
os.chdir(os.path.join(os.path.dirname(__file__), 'www'))

PORT = 5000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(format % args)

try:
    Handler = MyHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("\n" + "="*60)
        print("✅ Diff equation Solver Web Frontend")
        print("="*60)
        print(f"\n🌐 Server running on: http://localhost:{PORT}")
        print(f"📁 Serving from: {os.getcwd()}")
        print("\n✅ Open browser: http://localhost:5000")
        print("⏹️  Press Ctrl+C to stop\n")
        print("="*60 + "\n")
        
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\n✋ Server stopped")
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
