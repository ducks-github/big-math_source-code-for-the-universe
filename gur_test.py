import math
from decimal import Decimal, getcontext

# 1. Set high precision (50 decimal places)
getcontext().prec = 50

def test_gur_identities():
    # --- PHYSICAL CONSTANTS (CODATA 2018/Current) ---
    # These are the "Real World" values we are testing against
    alpha_real = Decimal("0.0072973525693")         # Fine Structure Constant
    mu_real    = Decimal("1836.15267343")           # Proton-to-Electron Mass Ratio
    delta_real = Decimal("2.5284")                  # Neutron-proton mass diff / me
    kappa_real = Decimal("5.906e-39")               # Dimensionless Gravity (G*mp^2 / hbar*c)

    # --- MATHEMATICAL TARGETS ---
    phi = (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)
    pi  = Decimal("3.1415926535897932384626433832795028841971")
    sq2 = Decimal(2).sqrt()

    print(f"{'GUR Identity':<30} | {'Predicted Value':<20} | {'Error %'}")
    print("-" * 75)

    # 1. Vacuum Stiffness (Psi at Pi)
    psi_pi = (alpha_real * phi**2) / (4 * pi)
    
    # 3. Unified Mass-Ratio (mu)
    # mu = 12 * (1/alpha) * (9/8) * (1 - (phi / (sqrt(2)*pi)))
    mu_gur = 12 * (1/alpha_real) * (Decimal(9)/Decimal(8)) * (1 - (phi / (sq2 * pi)))
    error_mu = abs((mu_gur - mu_real) / mu_real) * 100
    print(f"{'3. Mass-Ratio (mu)':<30} | {float(mu_gur):<20.4f} | {float(error_mu):.6f}%")

    # 5. Gravitational Leakage (kappa)
    # kappa = 12 * alpha^18
    kappa_gur = 12 * (alpha_real**18)
    error_kappa = abs((kappa_gur - kappa_real) / kappa_real) * 100
    print(f"{'5. Gravity Leakage (kappa)':<30} | {float(kappa_gur):<20.2e} | {float(error_kappa):.2f}%")

    # 6. Neutron Dissonance Gap (delta)
    # delta = (sqrt(2) + phi/sqrt(2)) - 2*psi_pi
    delta_gur = (sq2 + (phi / sq2)) - (2 * psi_pi)
    error_delta = abs((delta_gur - delta_real) / delta_real) * 100
    print(f"{'6. Neutron Gap (delta)':<30} | {float(delta_gur):<20.4f} | {float(error_delta):.2f}%")

if __name__ == "__main__":
    test_gur_identities()
