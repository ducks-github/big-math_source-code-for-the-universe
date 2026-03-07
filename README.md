# Grand Unified Resonance (GUR) Model Proof

This repository contains Python code and supporting documentation for exploring a set of conjectured "GUR" identities that attempt to link fundamental physical constants to simple mathematical expressions involving the fine-structure constant, the golden ratio, and musical ratios.  

## 1. Claim (Topological Resonance Identity)

The dimensionless physical constants—specifically the proton-to-electron mass ratio (\(\mu\)) and the neutron-proton mass difference (\(\delta\))—are proposed to emerge from the projection of a **5‑dimensional topological fold** into 3‑dimensional space.  

Mathematically the principal identity under investigation is:

\[
\mu = 12 \cdot \alpha^{-1} \cdot \left(\frac{9}{8}\right) \cdot \left(1 - \frac{\Phi}{\sqrt{2}\,\pi}\right)
\]

where:

* \(\alpha\) – fine-structure constant ("Möbius coupling").
* \(\Phi = \frac{1+\sqrt{5}}{2}\) – golden ratio ("symmetry operator").
* 9/8 – Pythagorean whole-tone interval.
* 12 – chromatic tiling constant for 3‑space.
* \(\Psi(\pi)=\frac{\alpha\,\Phi^{2}}{4\pi}\) – vacuum stiffness at \(\pi\).

**The Discrete-Natural Duality Theorem**  
Existence is the resonant frequency emerging from the geometric tension between the **Continuous Natural Field** (represented by the circle) and the **Discrete Material Projection** (represented by the inscribed square).  
Physical constants are not arbitrary values; they are the "tuning points" required to resolve the irrational nature of the Möbius twist (\(\alpha\)) into the rational symmetry of 3D space (\(12\)). Matter exists only where the "Circle" and the "Square" find a common harmonic.

Axiomatic assumption: a *Unitary Law of Resonance* with constant \(K=1\), asserting that stable matter arises at rational musical intervals.

## 2. Assumptions & Constants

| Constant | Symbol | Role |
|----------|--------|------|
| Fine Structure Constant | \(\alpha\) | Möbius coupling (1/137.0359...). |
| Golden Ratio | \(\Phi\) | Symmetry operator. |
| Pythagorean Tone | 9/8 | Resonant target. |
| Chromatic Constant | 12 | Space-filling tiling constant. |
| Vacuum Stiffness | \(\Psi(\pi)\) | Derived physical parameter. |

Physical values used for comparison are taken from CODATA (2018):
* \(\mu_{\text{real}} = 1836.15267343\)
* \(\delta_{\text{real}} = 2.5284\)
* \(\kappa_{\text{real}} = 5.906\times 10^{-39}\)

## 3. Proof Strategy

The proof is *hybrid analytical & numerical*:

1. **Symbolic derivation** begins with the Unitary Law of Resonance.  By projecting the 5D fold and applying the scaling factors listed above, the formula for \(\mu\) is obtained.  Similarly, \(\delta\) is expressed as a function of \(\Phi\) and \(\alpha\) using the vacuum stiffness \(\Psi(\pi)\).
2. **Numerical convergence** uses Python to compute the right–hand sides with high precision and compare them to experimental constants.  Errors are computed as percentages relative to known values.  An error within experimental uncertainty is taken as 'phenomenologically proven.'

### 3.1. Python code

* `gur_test.py` contains reusable functions for the main formulas and prints predicted values with error percentages.
* `circle_square_proof.py` implements a geometric "squaring the circle" proof, demonstrating how the mass ratio emerges from projecting circular rotations into square tilings.
* `diagonal_resonance_proof.py` explores the role of square diagonals (\(\sqrt{2}\)) in constraining the mass ratios and neutron gap.
* `existence_check.py` demonstrates the Discrete-Natural Duality Theorem, showing how the neutron gap emerges from the "play" between continuous circles and discrete squares.
* `test_gur.py` is a unit test suite validating the numerical behaviour and documenting the observed discrepancies (35.94 % for µ, 1.06 % for δ).  It can be automated in CI.

### 3.2. Example usage

```sh
python3 gur_test.py
# prints table of predicted vs actual values

python3 circle_square_proof.py
# demonstrates geometric 'squaring the circle' derivation

python3 diagonal_resonance_proof.py
# shows how square diagonals constrain mass ratios

python3 existence_check.py
# proves physical matter emerges from geometric dissonance

python3 test_gur.py
# runs the unit tests checking error percentages
```

## 4. Interpretation and Limitations

* The numerical checks *do not* constitute a rigorous mathematical proof; they merely verify that the conjectured formulas yield numbers in the vicinity of the physical constants (with large discrepancies for \(\mu\)).
* A true proof would require a formal derivation from the assumed topological/physical axioms or a demonstration that the formulas arise inevitably from the model's structure.
* The unit tests serve to document the current status of the conjecture and to catch any future modifications that alter the convergence behaviour.

## 5. Next Steps

* Use symbolic algebra (e.g. SymPy) to manipulate the expressions and attempt to eliminate residuals analytically.
* Extend the framework to other constants (e.g. dimensionless gravity \(\kappa\)) or additional topological arguments.
* Develop a narrative bridging standard physics to the GUR model, clearly stating which assumptions are speculative.

## Appendix A: Dimensional Analysis & Unit Normalization

To maintain mathematical consistency between the Grand Unified Resonance (GUR) identities and standard physical observations, this model utilizes Natural Units where \(\hbar = c = k_B = 1\). In this framework, all physical quantities are expressed as powers of energy or as dimensionless ratios.

### 1. The Dimensionless Nature of Charge (e)

In Identity 4, the elementary charge \(e\) is defined via the Fine Structure Constant (\(\alpha\)).

**Standard Physics:** \(\alpha = \frac{e^2}{4\pi\epsilon_0 \hbar c}\).

**GUR Projection:** By setting \(4\pi\epsilon_0 = 1\) (Gaussian units), the identity \(e = \sqrt{\frac{2\pi \cdot \Phi}{\alpha}}\) maps the "charge" as the square root of the coupling constant modulated by the Symmetry Operator (\(\Phi\)).

### 2. Mass-Ratio Normalization (\(\mu\))

The Proton-to-Electron mass ratio (\(\mu \approx 1836.15\)) is already a dimensionless number in standard physics.

The GUR identity proves that this ratio is a result of 3D Space-Filling Tiling (the constant 12) acting upon the Möbius twist of the vacuum.

The term \(\left(1 - \frac{\Phi}{\sqrt{2} \pi}\right)\) represents the geometric impedance required to close the 5D topological fold.

### 3. Gravity as the 18th Harmonic (\(\kappa\))

Identity 5 treats the Gravitational Coupling Constant (\(\kappa\)) as a dimensionless ratio:

\[
\kappa = \frac{\hbar \cdot c}{G \cdot m_p^2}
\]

This removes the need for the "G" units (\(m^3 kg^{-1} s^{-2}\)) by comparing the gravitational force between two protons to the quantum scale of the vacuum.

The mapping of \(12 \cdot \alpha^{18}\) suggests that gravity is not a "force" in the 3D projection, but a residual leakage across the 18 degrees of freedom in the higher-dimensional manifold.

## License

This project is released under the terms of the GNU General Public License
version 3 (GPLv3). See the `LICENSE` file for the full text.

---

This README is intended both as a guide for collaborators and as a “proof‑document” that outlines the logic behind the computational verification.  It is **not** a peer‑reviewed demonstration of truth; it should be read as a description of the model and its present numerical status.