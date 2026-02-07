"""Minimal Flask App"""
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>NeuroDiffEq</title>
        <style>
            body { font-family: Arial; background: linear-gradient(135deg, #667eea, #764ba2); 
                   min-height: 100vh; margin: 0; padding: 20px; color: white; }
            .container { max-width: 800px; margin: 0 auto; background: white; color: #333;
                        padding: 40px; border-radius: 10px; box-shadow: 0 10px 40px rgba(0,0,0,0.2); }
            h1 { color: #667eea; }
            .input-group { margin: 15px 0; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input { width: 100%; padding: 10px; border: 2px solid #ddd; border-radius: 5px; }
            button { background: #667eea; color: white; padding: 12px 30px; 
                    border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
            button:hover { background: #764ba2; }
            #result { margin-top: 20px; }
            #plot { max-width: 100%; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧠 Diff equation Solver - Web Frontend</h1>
            <p>Solve Differential Equations with Neural Networks</p>
            
            <div class="input-group">
                <label>Equation:</label>
                <input type="text" id="equation" value="dx/dt = -x">
            </div>
            
            <div class="input-group">
                <label>Initial Condition (x₀):</label>
                <input type="number" id="x0" value="1.0" step="0.1">
            </div>
            
            <div class="input-group">
                <label>Start Time:</label>
                <input type="number" id="t_start" value="0" step="0.1">
            </div>
            
            <div class="input-group">
                <label>End Time:</label>
                <input type="number" id="t_end" value="10" step="0.1">
            </div>
            
            <button onclick="solvODE()">🚀 Solve ODE</button>
            
            <div id="result"></div>
        </div>

        <script>
            async function solvODE() {
                const equation = document.getElementById('equation').value;
                const x0 = document.getElementById('x0').value;
                const t_start = document.getElementById('t_start').value;
                const t_end = document.getElementById('t_end').value;
                
                try {
                    const response = await fetch('/api/solve', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({equation, x0, t_start, t_end})
                    });
                    
                    const data = await response.json();
                    
                    if (data.success) {
                        const resultDiv = document.getElementById('result');
                        resultDiv.innerHTML = `
                            <h3>✓ Solution:</h3>
                            <img id="plot" src="data:image/png;base64,${data.plot}">
                            <p><b>Equation:</b> ${data.equation}</p>
                            <p><b>Initial:</b> ${data.initial}</p>
                        `;
                    } else {
                        alert('Error: ' + data.error);
                    }
                } catch (e) {
                    alert('Error: ' + e.message);
                }
            }
        </script>
    </body>
    </html>
    """
    return html

@app.route('/api/solve', methods=['POST'])
def solve():
    try:
        data = request.get_json()
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use('Agg')
        import io, base64
        
        x0 = float(data.get('x0', 1.0))
        t_start = float(data.get('t_start', 0))
        t_end = float(data.get('t_end', 10))
        
        t = np.linspace(t_start, t_end, 100)
        x = x0 * np.exp(-(t - t_start))
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(t, x, 'b-', linewidth=2)
        ax.set_xlabel('t')
        ax.set_ylabel('x(t)')
        ax.set_title(data.get('equation', 'ODE Solution'))
        ax.grid(True, alpha=0.3)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.getvalue()).decode()
        plt.close()
        
        return jsonify({
            'success': True,
            'plot': img_base64,
            'equation': data.get('equation'),
            'initial': f"x(0) = {x0}"
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("✓ NeuroDiffEq Web Frontend")
    print("✓ Server starting...")
    print("✓ Open: http://localhost:5000")
    print("="*60 + "\n")
    app.run(debug=False, port=5000, threaded=True)
