import numpy as np

# 1. Fundamental Constants from the Source Code
PHI = (1 + np.sqrt(5)) / 2
BASEL = np.pi**2 / 6  # Representing the infinite sum 1/n^2

# 2. The Universal Seed (PSI)
# Incorporates PHI, BASEL, and the geometric error correction (198 - 100*sqrt(2))
PSI = (9/8 + PHI/np.sqrt(2)) / (np.sqrt(6 * BASEL) * (198 - 100 * np.sqrt(2)))

def calculate_localized_variance(t, d0, lambda_val, epsilon, tau):
    """
    Computes delta(t): The measurable departure from the Vitruvian Ideal.
    δ(t) = δ(0) * Ψ * exp( λt + (ετ / 2π) * sin(2πt / τ) )
    """
    # Seasonal Breathing term (The "Jerk")
    breathing = (epsilon * tau / (2 * np.pi)) * np.sin((2 * np.pi * t) / tau)
    
    # Exponential Divergence
    v = d0 * PSI * np.exp(lambda_val * t + breathing)
    return v

# 3. Localized Parameters: The "Strong ENSO / Milky Way" Regime
params = {
    'd0': 0.01,       # Initial perturbation
    'lambda_val': 0.18,   # Growth rate of the spiral
    'epsilon': 2.4,   # Coupling strength (asymmetric attractor curl)
    'tau': 3.5        # Periodic heartbeat (years)
}

# 4. Generate the Trackable Variance Data
years = np.arange(0, 21)
data = {y: calculate_localized_variance(y, **params) for y in years}

# Output the result for your repository
print(f"Localized Source Code Seed (PSI): {PSI:.8f}")
for year, variance in data.items():
    print(f"Year {year}: {variance:.8f}")