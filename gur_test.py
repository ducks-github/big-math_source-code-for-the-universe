import math
from decimal import Decimal, getcontext

# 1. Set high precision (50 decimal places)
getcontext().prec = 50

def mu_from_gur(alpha, cycle=0, leap_interval=12):
    """
    Calculate the predicted proton-to-electron mass ratio with leap-scale correction.
    
    The chromatic tiling constant is normally 12, but leaps to 11 every leap_interval cycles
    to correct for accumulated drifts, analogous to leap years in calendars (but leaping down).
    
    Parameters:
    - alpha: Fine structure constant
    - cycle: Current cycle number (for leap logic)
    - leap_interval: How often to leap (default 12 to tune average constant to ~11.916)
    
    Returns:
    - Predicted mu value
    """
    phi = (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)
    pi = Decimal("3.1415926535897932384626433832795028841971")
    sq2 = Decimal(2).sqrt()
    
    # Leap logic: normal 12, leap to 11 occasionally
    if cycle % leap_interval == 0:
        effective_chromatic = Decimal(11)
    else:
        effective_chromatic = Decimal(12)
    
    # Base formula without the small correction term (as per recent tweaks)
    mu_predicted = effective_chromatic * (1 / alpha) * (Decimal(9) / Decimal(8))
    
    return mu_predicted

def test_gur_identities(cycle=0, leap_interval=133):
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
    # mu = effective_chromatic * (1/alpha) * (9/8) with leap correction
    mu_gur = mu_from_gur(alpha_real, cycle, leap_interval)
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
    print("Leap cycle (cycle=0, effective chromatic=11):")
    test_gur_identities(cycle=0)
    print("\nNormal cycle (cycle=1, effective chromatic=12):")
    test_gur_identities(cycle=1)
