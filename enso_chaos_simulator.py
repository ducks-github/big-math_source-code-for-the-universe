import numpy as np
import matplotlib.pyplot as plt

# --- 1. Brutally Honest Constants [cite: 2, 3] ---
PHI = (1 + np.sqrt(5)) / 2
BASEL = np.pi**2 / 6
# Your specific "source code for the universe" constant
PSI = (9/8 + PHI/np.sqrt(2)) / (np.sqrt(6 * BASEL) * (198 - 100 * np.sqrt(2))) # [cite: 3]

# --- 2. Regime Definitions [cite: 4, 5] ---
REGIMES = {
    "strong_elnino": {"label": "Strong El Niño", "lambda": 0.18, "tau": 3.5, "epsilon": 2.4, "color": "#ff4d2e"},
    "weak_elnino":   {"label": "Weak El Niño",   "lambda": 0.09, "tau": 5.0, "epsilon": 1.2, "color": "#ffaa44"},
    "lanina":        {"label": "La Niña",        "lambda": 0.06, "tau": 4.0, "epsilon": 0.8, "color": "#44aaff"},
    "neutral":       {"label": "ENSO Neutral",   "lambda": 0.01, "tau": 6.5, "epsilon": 0.3, "color": "#88ccaa"}
}

# --- 3. The Delta Function (Perturbation Growth) [cite: 6] ---
def calculate_delta(t, d0, params):
    """
    δ(t) = δ(0) * Ψ * exp( λt + (ετ / 2π) * sin(2πt / τ) )
    """
    l, e, tau = params['lambda'], params['epsilon'], params['tau']
    seasonal_term = (e * tau / (2 * np.pi)) * np.sin((2 * np.pi * t) / tau)
    v = d0 * PSI * np.exp(l * t + seasonal_term)
    return v # [cite: 6]

# --- 4. Simulation Setup ---
d0 = 0.01  # Initial perturbation [cite: 8]
t_max = 20 # Years [cite: 8]
t_steps = np.linspace(0, t_max, 600) # [cite: 11]

# --- 5. Visualization ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('#07090d')
ax.set_facecolor((1, 1, 1, 0.03))

for key, p in REGIMES.items():
    deltas = [calculate_delta(t, d0, p) for t in t_steps]
    ax.plot(t_steps, deltas, label=p['label'], color=p['color'], linewidth=2)

# Styling to match your "Aesthetic Outline" [cite: 20, 21]
ax.set_title(f"ENSO Chaos Simulator (Ψ = {PSI:.7f})", color="#e8c090", fontsize=16, pad=20)
ax.set_xlabel("Years", color="#445", family='monospace')
ax.set_ylabel("δ(t) Perturbation", color="#445", family='monospace')
ax.grid(color=(1, 1, 1, 0.05), linestyle='--')
ax.legend(frameon=False)

plt.tight_layout()
plt.show()