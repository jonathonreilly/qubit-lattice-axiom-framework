# Supervisor's own thread on OBS-4 (written before the worker returns)

**The flavour-changing coupling.** B-gen has one common complex diagonal d·1 in the corner basis. That is the on-site, k = 0 Higgs part. The off-diagonal corner entries come from carriers at the hw2 momenta Q.
- In the mass basis, the carrier coupling is W†(Y − d·1)X = diag(y_i) − d·W†X.
- So its flavour-changing part is about |d|·offdiag(W†X), with |d| ≈ y/3 for each sector.
- For the down sector, |d| ≈ y_b/3 ≈ 0.008, so the s–d coupling is about 0.008 × O(1) unless W†X happens to be nearly diagonal.

**The bound.** Isidori–Nir–Perez put Λ ≳ 10⁴–10⁵ TeV on ΔS = 2 scalar operators with O(1) coefficients. A coefficient of about (0.008)² ≈ 6e-5 then gives M* ≈ 10⁵ TeV × √(6e-5), roughly 10²–10³ TeV, with ε_K likely binding.

**The key structural point (suggested).** Unit translations conserve the corner label, so the k = 0 Higgs and the k = Q carriers cannot mix in a translation-invariant quadratic potential. The carrier vev at Q is a separate, translation-breaking (staggered) condensate. It is not the vev-less heavy doublet of a type-III 2HDM written in the Higgs basis.
- To give off-diagonal Yukawas of order y/3, the Q-condensate needs a vev of order v (times couplings of order 1).
- Its physical fluctuations then sit at about √λ·v_Q, i.e. at the electroweak scale, unless the potential is tuned.
- To get carriers at M* of about 10²–10³ TeV while keeping v_Q ~ v, the tuning is about (v/M*)², roughly 10⁻⁸–10⁻¹⁰.
- Coupling-proportional alignment could avoid this, but B-gen's carrier matrix is not proportional to the mass matrix.

**Prediction.** FCNC-PRICE, with M* of order 10²–10³ TeV and a carrier-potential tuning of order 1e-8. If the carrier modes are forced light, it is FCNC-KILL. The way out is mechanism 1: flavour breaking only in the k = 0 Higgs vev through lattice-scale operators. But that conflicts with the corner label: a k = 0 vev cannot change the corner.

**What I would check in the worker's report.**
- Does it respect corner-label conservation, i.e. not mix the k = 0 and k = Q scalars?
- Is the "condensate at Q breaks unit translations" point addressed? In OBS-1's construction, is that breaking spontaneous or explicit?
