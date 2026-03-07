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
* `test_gur.py` is a unit test suite validating the numerical behaviour and documenting the observed discrepancies (35.94 % for µ, 1.06 % for δ).  It can be automated in CI.

### 3.2. Example usage

```sh
python3 gur_test.py
# prints table of predicted vs actual values

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

## License

This project is released under the terms of the GNU General Public License
version 3 (GPLv3). See the `LICENSE` file for the full text.

---

This README is intended both as a guide for collaborators and as a “proof‑document” that outlines the logic behind the computational verification.  It is **not** a peer‑reviewed demonstration of truth; it should be read as a description of the model and its present numerical status.