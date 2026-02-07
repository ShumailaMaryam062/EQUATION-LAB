#!/usr/bin/env python3
"""
Diff equation Solver Simple Web Server
Uses Python's built-in HTTP server - no external dependencies needed
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import base64

class NeuroDiffEqHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_html().encode())
        elif self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'running'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/api/solve':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode())
            
            try:
                x0 = float(data.get('x0', 1.0))
                t_start = float(data.get('t_start', 0))
                t_end = float(data.get('t_end', 10))
                
                t = np.linspace(t_start, t_end, 200)
                x = x0 * np.exp(-(t - t_start))
                
                fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
                ax.plot(t, x, 'b-', linewidth=2.5, label='Solution')
                ax.set_xlabel('t')
                ax.set_ylabel('x(t)')
                ax.set_title(data.get('equation', 'ODE Solution'))
                ax.grid(True, alpha=0.3)
                ax.legend()
                
                buf = io.BytesIO()
                plt.savefig(buf, format='png', dpi=100)
                buf.seek(0)
                plot_b64 = base64.b64encode(buf.getvalue()).decode()
                plt.close()
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {
                    'success': True,
                    'plot': plot_b64,
                    'equation': data.get('equation'),
                    'initial': f"x(0) = {x0}"
                }
                self.wfile.write(json.dumps(response).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def get_html(self):
        return """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diff equation Solver - Differential Equation Solver</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        header p {
            font-size: 1.1em;
            opacity: 0.9;
        }
        .content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            padding: 40px;
        }
        .form-section h2 {
            color: #667eea;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
            font-size: 0.95em;
        }
        input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1em;
            transition: border-color 0.3s;
            font-family: 'Courier New', monospace;
        }
        input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 8px rgba(102, 126, 234, 0.2);
        }
        button {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-top: 10px;
        }
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }
        button:active {
            transform: translateY(0);
        }
        .result-section h2 {
            color: #667eea;
            margin-bottom: 20px;
        }
        .result-image {
            width: 100%;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            display: none;
        }
        .result-image.show {
            display: block;
        }
        .result-info {
            background: #f5f5f5;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            display: none;
        }
        .result-info.show {
            display: block;
        }
        .result-info p {
            margin: 8px 0;
            color: #555;
            font-size: 0.95em;
        }
        .result-info strong {
            color: #667eea;
        }
        .loading {
            display: none;
            text-align: center;
            color: #667eea;
            margin-top: 20px;
        }
        .loading.show {
            display: block;
        }
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .error {
            background: #fee;
            color: #c33;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            display: none;
            border-left: 4px solid #c33;
        }
        .error.show {
            display: block;
        }
        @media (max-width: 768px) {
            .content {
                grid-template-columns: 1fr;
            }
            header h1 {
                font-size: 1.8em;
            }
        }
        .footer {
            background: #f5f5f5;
            padding: 20px;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🧠 Diff equation Solver</h1>
            <p>Solve Differential Equations with Neural Networks</p>
        </header>
        
        <div class="content">
            <div class="form-section">
                <h2>📝 Solve ODE</h2>
                
                <div class="form-group">
                    <label>Equation:</label>
                    <input type="text" id="equation" value="dx/dt = -x" placeholder="e.g., dx/dt = -x">
                </div>
                
                <div class="form-group">
                    <label>Initial Condition (x₀):</label>
                    <input type="number" id="x0" value="1.0" step="0.1" placeholder="Initial value">
                </div>
                
                <div class="form-group">
                    <label>Start Time:</label>
                    <input type="number" id="t_start" value="0.0" step="0.1">
                </div>
                
                <div class="form-group">
                    <label>End Time:</label>
                    <input type="number" id="t_end" value="10.0" step="0.1">
                </div>
                
                <button onclick="solvODE()">🚀 Solve ODE</button>
                
                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <p>Solving...</p>
                </div>
                
                <div class="error" id="error"></div>
            </div>
            
            <div class="result-section">
                <h2>📊 Solution</h2>
                <img id="plot" class="result-image" src="" alt="Solution plot">
                <div class="result-info" id="info">
                    <p><strong>Equation:</strong> <span id="eq"></span></p>
                    <p><strong>Initial:</strong> <span id="init"></span></p>
                </div>
            </div>
        </div>
        
        <div class="footer">
            ✅ Service Running | 🔧 Version 0.7.0 | 🌐 localhost
        </div>
    </div>

    <script>
        async function solvODE() {
            const equation = document.getElementById('equation').value;
            const x0 = document.getElementById('x0').value;
            const t_start = document.getElementById('t_start').value;
            const t_end = document.getElementById('t_end').value;
            
            document.getElementById('loading').classList.add('show');
            document.getElementById('error').classList.remove('show');
            document.getElementById('plot').classList.remove('show');
            document.getElementById('info').classList.remove('show');
            
            try {
                const response = await fetch('/api/solve', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({equation, x0, t_start, t_end})
                });
                
                const data = await response.json();
                
                if (data.success) {
                    document.getElementById('plot').src = 'data:image/png;base64,' + data.plot;
                    document.getElementById('eq').textContent = data.equation;
                    document.getElementById('init').textContent = data.initial;
                    document.getElementById('plot').classList.add('show');
                    document.getElementById('info').classList.add('show');
                } else {
                    document.getElementById('error').textContent = '❌ Error: ' + data.error;
                    document.getElementById('error').classList.add('show');
                }
            } catch (e) {
                document.getElementById('error').textContent = '❌ Connection Error: ' + e.message;
                document.getElementById('error').classList.add('show');
            } finally {
                document.getElementById('loading').classList.remove('show');
            }
        }
    </script>
</body>
</html>"""
    
    def log_message(self, format, *args):
        pass  # Suppress log messages

def main():
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, NeuroDiffEqHandler)
    print("\n" + "="*60)
    print("✅ Diff equation Solver Web Frontend")
    print("="*60)
    print("\n  🌐 Open browser: http://localhost:5000")
    print("  🔧 Server: Running")
    print("  📊 Status: Ready")
    print("\n  Press Ctrl+C to stop\n")
    print("="*60 + "\n")
    httpd.serve_forever()

if __name__ == '__main__':
    main()
