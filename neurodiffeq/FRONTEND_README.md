# EquationLab Web Frontend

A beautiful web interface for solving differential equations with neural networks.

## Features

✨ **Interactive ODE Solver**
- Solve ordinary differential equations
- Visualize solutions in real-time
- Adjust parameters and initial conditions

📊 **Beautiful UI**
- Modern gradient design
- Responsive layout
- Real-time plotting
- Easy parameter adjustment

🚀 **Quick Start**

### Option 1: Run the batch file (Windows)
Double-click `run_frontend.bat`

### Option 2: Run from command line
```bash
cd neurodiffeq
python app.py
```

Then open your browser to: **http://localhost:5000**

## Requirements

Install dependencies:
```bash
pip install flask matplotlib numpy torch
```

## Usage

1. **Enter the differential equation** (e.g., `dx/dt = -x`)
2. **Set initial condition** (e.g., x₀ = 1.0)
3. **Define time range** (e.g., 0 to 10 seconds)
4. **Click "Solve"** to compute the solution
5. **View the plot** and results

## Example Equations

- `dx/dt = -x` - Exponential decay
- `dx/dt = x` - Exponential growth  
- `d²x/dt² = -x` - Harmonic oscillator
- `dx/dt = r*x*(1-x/K)` - Logistic growth

## Files

- `app.py` - Flask backend
- `templates/index.html` - Web interface
- `run_frontend.bat` - Windows batch file to run the app

## Architecture

```
Frontend (HTML/CSS/JavaScript)
    ↓
Flask Web Server (REST API)
    ↓
NeuroDiffEq Library
    ↓
PyTorch + Neural Networks
```

## Browser Compatibility

✓ Chrome/Chromium  
✓ Firefox  
✓ Edge  
✓ Safari  

## Access

- **Local**: http://localhost:5000
- **Network**: http://<your-ip>:5000

Enjoy solving differential equations! 🎉
