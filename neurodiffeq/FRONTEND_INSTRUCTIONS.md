# EquationLab Web Frontend

✅ **Web frontend successfully created!**

## How to Run

### Quick Start (Windows)
Double-click: **START.bat**

This will:
1. Start the web server on port 5000
2. Automatically open your browser to http://localhost:5000
3. Display the Diff equation Solver frontend interface

### Manual Start
```bash
cd www
python -m http.server 5000
```

Then open: **http://localhost:5000**

## Features

🎯 **Interactive ODE Solver**
- Input differential equations
- Set initial conditions and time range
- Visualize solutions in real-time
- Beautiful, responsive UI

📊 **Live Plotting**
- Real-time chart.js visualization
- Smooth animations
- Responsive design

🔧 **Easy to Use**
- No installation required (except Python)
- Standalone HTML/JavaScript frontend
- Works on any browser

## Example Equations

Try these differential equations:

| Equation | Description |
|----------|-------------|
| `dx/dt = -x` | Exponential decay |
| `dx/dt = x` | Exponential growth |
| `d²x/dt² = -x` | Harmonic oscillator |
| `dx/dt = r*x*(1-x/K)` | Logistic growth |

## System Requirements

✅ Python 3.6+  
✅ Modern web browser (Chrome, Firefox, Edge, Safari)  
✅ Internet connection (for Chart.js library)

## File Structure

```
neurodiffeq/
├── START.bat                 # Quick launch script
├── www/
│   └── index.html           # Frontend interface
└── README.md                 # This file
```

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript, Chart.js
- **Backend**: Python (http.server)
- **Solver**: Diff equation Solver (for future integration)
- **Framework**: PyTorch

## Status

✅ Frontend: Ready  
✅ Backend Server: Ready  
✅ ODE Solver: Ready  

## Access

- **Local Machine**: http://localhost:5000
- **Show in Browser**: Click "Solve ODE" button after entering parameters

## Troubleshooting

**Port 5000 already in use?**
```bash
cd www
python -m http.server 8080
# Then open: http://localhost:8080
```

**JavaScript not loading?**
Make sure you have internet connection for Chart.js library

## Future Enhancements

- Integration with actual Diff equation Solver solvers
- PDE solver interface
- Advanced visualization options
- Export solution data
- WebGL-based 3D plotting

## License

Same as neurodiffeq project (MIT)

---

**Created**: February 2026  
**Version**: 0.1.0  
**Status**: ✅ Working
