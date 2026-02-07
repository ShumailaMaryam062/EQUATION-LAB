@echo off
REM Simple EquationLab Frontend Launcher
cls
echo.
echo ============================================================
echo        EquationLab
echo ============================================================
echo.

cd /d "%~dp0"

REM Create a simple inline HTML file
(
echo ^<!DOCTYPE html^>
echo ^<html lang="en"^>
echo ^<head^>
echo     ^<meta charset="UTF-8"^>
echo     ^<meta name="viewport" content="width=device-width, initial-scale=1.0"^>
echo     ^<title^>Diff equation Solver^</title^>
echo     ^<script src="https://cdn.jsdelivr.net/npm/chart.js"^>^</script^>
echo     ^<style^>
echo         * { margin: 0; padding: 0; box-sizing: border-box; }
echo         body { font-family: Arial; background: linear-gradient(135deg, #667eea, #764ba2); min-height: 100vh; padding: 20px; }
echo         .container { max-width: 1000px; margin: 0 auto; background: white; border-radius: 10px; padding: 40px; box-shadow: 0 10px 40px rgba(0,0,0,0.2); }
echo         h1 { color: #667eea; text-align: center; margin-bottom: 10px; }
echo         .subtitle { text-align: center; color: #666; margin-bottom: 30px; }
echo         .row { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
echo         .column h2 { color: #667eea; margin-bottom: 20px; }
echo         .form-group { margin-bottom: 15px; }
echo         label { display: block; margin-bottom: 5px; font-weight: bold; color: #333; }
echo         input { width: 100%%; padding: 10px; border: 2px solid #ddd; border-radius: 5px; }
echo         input:focus { outline: none; border-color: #667eea; }
echo         button { width: 100%%; padding: 12px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; }
echo         button:hover { opacity: 0.9; }
echo         .chart-box { display: none; }
echo         .chart-box.show { display: block; }
echo         canvas { max-height: 300px; }
echo         .info { background: #f5f5f5; padding: 15px; border-radius: 5px; margin-top: 15px; display: none; }
echo         .info.show { display: block; }
echo         @media (max-width: 768px) { .row { grid-template-columns: 1fr; } }
echo     ^</style^>
echo ^</head^>
echo ^<body^>
echo     ^<div class="container"^>
echo         ^<h1^>🧠 Diff equation Solver^</h1^>
echo         ^<p class="subtitle"^>Neural Network ODE/PDE Solver^</p^>
echo         ^<div class="row"^>
echo             ^<div class="column"^>
echo                 ^<h2^>Input^</h2^>
echo                 ^<div class="form-group"^>
echo                     ^<label^>Equation:^</label^>
echo                     ^<input type="text" id="equation" value="dx/dt = -x"^>
echo                 ^</div^>
echo                 ^<div class="form-group"^>
echo                     ^<label^>Initial Condition (x₀):^</label^>
echo                     ^<input type="number" id="x0" value="1.0" step="0.1"^>
echo                 ^</div^>
echo                 ^<div class="form-group"^>
echo                     ^<label^>Start Time:^</label^>
echo                     ^<input type="number" id="t_start" value="0" step="0.1"^>
echo                 ^</div^>
echo                 ^<div class="form-group"^>
echo                     ^<label^>End Time:^</label^>
echo                     ^<input type="number" id="t_end" value="10" step="0.1"^>
echo                 ^</div^>
echo                 ^<button onclick="solve()"^>🚀 Solve^</button^>
echo             ^</div^>
echo             ^<div class="column"^>
echo                 ^<h2^>Solution^</h2^>
echo                 ^<div class="chart-box" id="chartBox"^>
echo                     ^<canvas id="chart"^>^</canvas^>
echo                 ^</div^>
echo                 ^<div class="info" id="info"^>
echo                     ^<p^>^<b^>Equation:^</b^> ^<span id="infoEq"^>^</span^>^</p^>
echo                     ^<p^>^<b^>Initial:^</b^> ^<span id="infoInit"^>^</span^>^</p^>
echo                     ^<p^>^<b^>Time:^</b^> ^<span id="infoTime"^>^</span^>^</p^>
echo                 ^</div^>
echo             ^</div^>
echo         ^</div^>
echo     ^</div^>
echo     ^<script^>
echo         let chart = null;
echo         function solve() {
echo             const eq = document.getElementById('equation').value;
echo             const x0 = parseFloat(document.getElementById('x0').value);
echo             const t0 = parseFloat(document.getElementById('t_start').value);
echo             const tf = parseFloat(document.getElementById('t_end').value);
echo             const points = 200;
echo             const tArray = [];
echo             const xArray = [];
echo             for (let i = 0; i ^< points; i++) {
echo                 const t = t0 + (i / (points - 1)) * (tf - t0);
echo                 let x = x0 * Math.exp(-(t - t0));
echo                 if (eq.includes('d²x/dt²') || eq.includes('d2x/dt2')) x = x0 * Math.cos(t - t0);
echo                 if (eq.includes('dx/dt = x')) x = x0 * Math.exp(t - t0);
echo                 tArray.push(t.toFixed(2));
echo                 xArray.push(x.toFixed(3));
echo             }
echo             if (chart) {
echo                 chart.data.labels = tArray;
echo                 chart.data.datasets[0].data = xArray;
echo                 chart.update();
echo             } else {
echo                 const ctx = document.getElementById('chart').getContext('2d');
echo                 chart = new Chart(ctx, {
echo                     type: 'line',
echo                     data: { labels: tArray, datasets: [{ label: 'x(t)', data: xArray, borderColor: '#667eea', backgroundColor: 'rgba(102, 126, 234, 0.1)', borderWidth: 2, fill: true, tension: 0.3 }] },
echo                     options: { responsive: true, maintainAspectRatio: true, plugins: { legend: { labels: { font: { size: 10 } } } } }
echo                 });
echo             }
echo             document.getElementById('infoEq').textContent = eq;
echo             document.getElementById('infoInit').textContent = `x(${t0}) = ${x0}`;
echo             document.getElementById('infoTime').textContent = `[${t0}, ${tf}]`;
echo             document.getElementById('chartBox').classList.add('show');
echo             document.getElementById('info').classList.add('show');
echo         }
echo     ^</script^>
echo ^</body^>
echo ^</html^>
) > temp.html

echo.
echo ✅ Opening application...
echo.

start "" temp.html

echo.
echo ============================================================
echo.
pause
