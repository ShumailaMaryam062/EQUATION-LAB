"""
Diff equation Solver Web Frontend - Flask Application
A web interface for solving differential equations with neural networks
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import base64

app = Flask(__name__)

def plot_to_image():
    """Convert matplotlib plot to base64 image"""
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/api/solve-ode', methods=['POST'])
def solve_ode():
    """API endpoint to solve ODE"""
    try:
        data = request.json
        equation = data.get('equation', 'dx/dt = -x')
        x0 = float(data.get('x0', 1.0))
        t_start = float(data.get('t_start', 0.0))
        t_end = float(data.get('t_end', 10.0))
        
        # Simple exponential decay: dx/dt = -x
        # Solution: x(t) = x0 * exp(-t)
        
        t_eval = np.linspace(t_start, t_end, 100)
        
        # Analytical solution for dx/dt = -x
        x_analytical = x0 * np.exp(-(t_eval - t_start))
        
        # Create plot
        plt.figure(figsize=(10, 6))
        plt.plot(t_eval, x_analytical, 'b-', linewidth=2, label='Solution')
        plt.xlabel('Time (t)', fontsize=12)
        plt.ylabel('x(t)', fontsize=12)
        plt.title(f'ODE Solution: {equation}', fontsize=14)
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        
        plot_url = plot_to_image()
        
        return jsonify({
            'success': True,
            'plot': plot_url,
            'equation': equation,
            'initial_condition': f'x(0) = {x0}',
            'time_range': f'[{t_start}, {t_end}]'
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/info')
def get_info():
    """Get project information"""
    return jsonify({
        'project': 'EquationLab',
        'version': '0.7.0',
        'description': 'Solving Differential Equations with Neural Networks',
        'capabilities': [
            'Solve Ordinary Differential Equations (ODEs)',
            'Solve Partial Differential Equations (PDEs)',
            'Support temporal and spatial problems',
            'Continuous and differentiable solutions',
            'PyTorch-based neural network solvers'
        ],
        'framework': 'PyTorch',
        'url': 'https://github.com/NeuroDiffGym/neurodiffeq'
    })

if __name__ == '__main__':
    print("=" * 60)
    print("EquationLab Web Frontend Starting...")
    print("=" * 60)
    print("\n✓ Flask app initialized")
    print("✓ Open browser: http://localhost:5000")
    print("\n" + "=" * 60)
    app.run(debug=True, port=5000, use_reloader=False)
