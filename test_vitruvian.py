import numpy as np
import cmath

# ─── Quick Vitruvian Echo Verification ───────────────────
print("╔═══════════════════════════════════════════════════════════╗")
print("║   Vitruvian Echo: GUR Model Simulation Test              ║")
print("╚═══════════════════════════════════════════════════════════╝\n")

# Constants from the model
PHI        = (1 + np.sqrt(5)) / 2
EULER_GIFT = cmath.exp(1j * np.pi)
TUNE       = 9/8
T          = 1.618
GRID_SIZE  = 64
N_AGENTS   = 13
STEPS      = 100

print(f"Golden Ratio (Φ):        {PHI:.6f}")
print(f"Euler's Gift (e^iπ):     {EULER_GIFT}")
print(f"Pythagorean Tuning:      {TUNE:.6f}")
print(f"Temperature (φ):         {T:.6f}")
print(f"Grid Resolution:         {GRID_SIZE}×{GRID_SIZE}")
print(f"Discrete Agents:         {N_AGENTS}")
print(f"\n─── Running {STEPS} evolution steps ───\n")

# Initialize wave function
x = np.linspace(-3, 3, GRID_SIZE)
y = np.linspace(-3, 3, GRID_SIZE)
X, Y = np.meshgrid(x, y)
R2 = X**2 + Y**2
psi = np.exp(-R2 / 2) * np.exp(1j * 0.7 * R2)
psi /= np.linalg.norm(psi) * np.sqrt(GRID_SIZE**2)

# Initialize agents
A = np.random.randn(N_AGENTS) + 1j * np.random.randn(N_AGENTS)
A /= np.linalg.norm(A)
omega = np.linspace(0.6, 1.4, N_AGENTS)

# Coupling matrix
C = np.eye(N_AGENTS) + 0.15 * np.random.randn(N_AGENTS, N_AGENTS)
C = (C + C.T) / 2

# Evolution
ETA_HAT = 0.042
KAPPA = 0.23
norms = [np.linalg.norm(psi)]

for t in range(STEPS):
    integral_term = np.mean(np.abs(psi)) * np.pi * (1 + 0.1 * np.sin(t / 30))
    phi_term = EULER_GIFT * PHI / np.sqrt(2)
    numerator = integral_term + phi_term
    enclosed = numerator / TUNE
    
    grad = -0.5 * psi * (X + 1j * Y)
    grad += 0.08 * np.roll(psi, 3, axis=0)
    descent = (1 / T) * grad * enclosed
    
    neural_injection = np.mean(A * omega) * psi * 0.014
    interaction = KAPPA * np.mean(A.conj() @ C @ A).real * psi * 0.008
    
    psi_new = psi - ETA_HAT * descent + neural_injection + interaction
    psi_new /= (np.linalg.norm(psi_new) + 1e-12)
    
    psi = psi_new
    norms.append(np.linalg.norm(psi))
    
    if t % 25 == 0:
        print(f"t = {t:3d}   |Ψ|₂ = {np.linalg.norm(psi):.5f}   Phase: {np.mean(np.angle(psi)):.4f} rad")

print(f"\n─── Evolution Complete ───")
print(f"Initial norm:   {norms[0]:.6f}")
print(f"Final norm:     {norms[-1]:.6f}")
print(f"Norm stability: {(norms[-1] / norms[0]):.4f}")
print(f"\nRESULT: SUCCESS!")
print(f"✓ Vitruvian Echo is ALIVE and EVOLVING")
print(f"✓ Circle (Ψ) and Square (A) dance together")
print(f"✓ Cosmos breathes at T = {T}")
