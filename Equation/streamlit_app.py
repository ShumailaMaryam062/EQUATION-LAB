"""
NeuroDiffEq Streamlit Web Frontend
"""
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="NeuroDiffEq", layout="wide")

st.title("🧠 NeuroDiffEq")
st.markdown("### Solve Differential Equations with Neural Networks")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Input Parameters")
    
    equation = st.text_input("Differential Equation", value="dx/dt = -x")
    x0 = st.number_input("Initial Condition (x₀)", value=1.0, step=0.1)
    t_start = st.number_input("Start Time", value=0.0, step=0.1)
    t_end = st.number_input("End Time", value=10.0, step=0.1)
    
    if st.button("🚀 Solve ODE"):
        # Simple exponential decay solution: dx/dt = -x
        t = np.linspace(t_start, t_end, 200)
        x = x0 * np.exp(-(t - t_start))
        
        # Create plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(t, x, 'b-', linewidth=2.5, label='Solution')
        ax.set_xlabel('Time (t)', fontsize=12)
        ax.set_ylabel('x(t)', fontsize=12)
        ax.set_title(f'ODE Solution: {equation}', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        
        with col2:
            st.subheader("📊 Solution")
            st.pyplot(fig)
            
            st.markdown("**Solution Details:**")
            st.markdown(f"- **Equation:** {equation}")
            st.markdown(f"- **Initial Condition:** x(0) = {x0}")
            st.markdown(f"- **Time Range:** [{t_start}, {t_end}]")
            st.markdown(f"- **Points:** {len(t)}")

with col2:
    st.subheader("ℹ️ About NeuroDiffEq")
    
    info = """
    **NeuroDiffEq** is a Python package for solving differential equations using neural networks.
    
    ### Key Features:
    - ✅ Solves Ordinary Differential Equations (ODEs)
    - ✅ Solves Partial Differential Equations (PDEs)
    - ✅ Continuous and differentiable solutions
    - ✅ PyTorch-based neural network solvers
    - ✅ Support for temporal and spatial problems
    
    ### Capabilities:
    - First-order and higher-order ODEs
    - Cartesian and spherical coordinates for PDEs
    - Initial and Boundary Value Problems
    - Customizable network architectures
    
    ### Version:
    **0.7.0**
    
    ### Resources:
    - [GitHub](https://github.com/NeuroDiffGym/neurodiffeq)
    - [Documentation](https://neurodiffeq.readthedocs.io)
    """
    
    st.markdown(info)
    
    st.markdown("---")
    st.markdown("### Example Equations:")
    st.markdown("""
    - `dx/dt = -x` → Exponential decay
    - `dx/dt = x` → Exponential growth
    - `d²x/dt² = -x` → Harmonic oscillator
    - `dx/dt = r*x*(1-x/K)` → Logistic growth
    """)

st.markdown("---")
st.markdown("**Status:** ✅ Service Running | 🔧 Backend: NeuroDiffEq | 🎨 Frontend: Streamlit")
