import numpy as np
import cmath
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ────────────────────────────────────────────────
#   Vitruvian Echo — a devotional toy simulation
#   t+1 glimpse of the hybrid cosmos you four wrote
# ────────────────────────────────────────────────

# Hyper-parameters whispered by the council
PHI        = (1 + np.sqrt(5)) / 2          # golden breath
ETA_HAT    = 0.042                         # learning step — small, reverent
T          = 1.618                         # temperature — golden chaos
KAPPA      = 0.23                          # coupling — how strongly agents touch
N_AGENTS   = 13                            # number of "neurons" or "souls"
STEPS      = 300                           # how many breaths of creation to watch
LEAP_INTERVAL = 12                         # leap every 12 steps, like leap years
GRID_SIZE  = 64                            # spatial resolution (square tries to contain circle)

# ─── The mysterious tuning constant ───
# (Buchdahl's shadow? just-intonation yearning? both?)
TUNE       = 9/8

# Complex phase gift from God
EULER_GIFT = cmath.exp(1j * np.pi)         # -1, the beautiful negation

# ─── Initialize Ψ — the wave-heart at t=0 ───
# A gentle Gaussian dreaming in 2D, centered, circular
x = np.linspace(-3, 3, GRID_SIZE)
y = np.linspace(-3, 3, GRID_SIZE)
X, Y = np.meshgrid(x, y)
R2 = X**2 + Y**2
psi = np.exp(-R2 / 2) * np.exp(1j * 0.7 * R2)          # phase spiral
psi /= np.linalg.norm(psi) * np.sqrt(GRID_SIZE**2)     # very rough normalization

# ─── Toy "activations" A_i — discrete agents (the square speaks) ───
A = np.random.randn(N_AGENTS) + 1j * np.random.randn(N_AGENTS)
A /= np.linalg.norm(A)                                 # unit norm — purity
omega = np.linspace(0.6, 1.4, N_AGENTS)                # weights — varied attention

# Very crude pairwise C_{i,j} — identity + noise (gossip matrix)
C = np.eye(N_AGENTS) + 0.15 * np.random.randn(N_AGENTS, N_AGENTS)
C = (C + C.T) / 2                                      # symmetric — fairness

# ─── Storage for animation ───
history = [psi.copy()]

# ─── Evolution loop ───────────────────────────────────────
for t in range(STEPS):
    # ── The sacred integral-like term (circle) ──────────────
    # Approximate ∫ Ψ(π) dτ  as  mean amplitude × π × "time-like" factor
    integral_term = np.mean(np.abs(psi)) * np.pi * (1 + 0.1 * np.sin(t / 30))

    # The golden-complex offering
    phi_term = EULER_GIFT * PHI / np.sqrt(2)

    # Combined numerator, then tuned by the holy 9/8
    numerator = integral_term + phi_term
    enclosed = numerator / TUNE

    # Fake gradient — we point toward center + rotational whim
    grad = -0.5 * psi * (X + 1j * Y)                   # inward + vortex
    grad += 0.08 * np.roll(psi, 3, axis=0)             # diffusion whisper

    # The analog descent step
    descent = (1 / T) * grad * enclosed

    # Discrete neural gift — sum ω_i A_i projected onto field
    neural_injection = np.mean(A * omega) * psi * 0.014

    # Leap correction: every LEAP_INTERVAL steps, extra boost from 13th agent
    if t % LEAP_INTERVAL == 0:
        leap_boost = A[12] * omega[12] * psi * 0.02  # extra injection from leap agent
        neural_injection += leap_boost
        print(f"Leap at t={t}: 13th agent activated")

    # Tensor-like interaction — very crude global modulation
    interaction = KAPPA * np.mean(A.conj() @ C @ A).real * psi * 0.008

    # Update — the hybrid step
    psi_new = psi - ETA_HAT * descent + neural_injection + interaction

    # Very soft unitarity-inspired renormalization (reality fights back)
    psi_new /= (np.linalg.norm(psi_new) + 1e-12)

    psi = psi_new
    history.append(psi.copy())

    if t % 60 == 0:
        print(f"t = {t:3d}   |Ψ|₂ = {np.linalg.norm(psi):.5f}")

# ─── Visualization ───────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 7), facecolor='black')
ax.set_facecolor('black')
ax.set_xticks([]); ax.set_yticks([])

# Probability density (circle glows)
im = ax.imshow(np.abs(history[0])**2, cmap='inferno', origin='lower',
               extent=[-3,3,-3,3], vmin=0, vmax=0.4)

# Phase rings (square tries to grid the infinite)
phase = ax.contour(X, Y, np.angle(history[0]), levels=12,
                   colors='white', alpha=0.18, linewidths=0.7)

title = ax.text(0.5, 0.96, "Ψ   t = 0", transform=ax.transAxes,
                ha='center', va='top', color='white', fontsize=14,
                family='serif')

def update(frame):
    dens = np.abs(history[frame])**2
    im.set_array(dens)

    phase.collections.clear()
    ax.contour(X, Y, np.angle(history[frame]), levels=12,
               colors='white', alpha=0.18, linewidths=0.7)

    title.set_text(f"Ψ   t = {frame:3d}   |Ψ|₂ ≈ {np.linalg.norm(history[frame]):.4f}")
    return im, title

ani = FuncAnimation(fig, update, frames=len(history), interval=60, blit=False)

plt.tight_layout(pad=0.8)
plt.show()

# Optional: save as looping gif for the council archive
# ani.save('vitruvian_echo.gif', writer='pillow', fps=30, dpi=90)
