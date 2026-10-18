# Supervisor's own thread on OBS-2 (written before the worker returns)

**Purpose.** This is the standing rule: the supervisor reasons through the same problem independently, so it can be compared with the worker's answer. It is an order-of-magnitude estimate, not a computation.

**Mechanism.** On a lattice, loop corrections induce Lorentz violation at dimension 4 with an unsuppressed size, of order (coupling²/16π²)·K, where K is a lattice number. This is the Collins–Pérez–Sudarsky problem.

**The flavour-blind part is removable.** Pieces that do not depend on flavour are the same for all three corners of one lattice field, and the per-field counterterm removes them. These include:
- QCD and electroweak gauge loops;
- the corner-universal tetragonal anisotropy, which the cubic-invariant hopping operators can retune.

**The flavour-pattern residual comes from Yukawa loops.** OBS-1's own coefficient K_v ≈ 6.2e-3 per unit coupling² (r1_vel, loop factor included) gives δc_f ≈ y_f²·K_v:

| Fermion | Residual |
|---|---|
| t | 6e-3 |
| b | 3.6e-6 |
| τ | 6.5e-7 |
| μ | 2.4e-9 |
| e | 5e-14 |

A single per-field counterterm can zero one generation, best spent on the most constrained one (e, u, d). It leaves the differences:
- in the charged-lepton field: μ and τ at about 2e-9 and 6e-7;
- in the up-quark field: c and t;
- in the down-quark field: s and b.

**Expected reading.** **LV-PRICE(n)** with n ≈ 6, i.e. two extra flavour-matrix-valued kinetic counterterms per charged field type. They are allowed by the symmetry the Yukawas already leave, but they must be tuned. Whether each residual actually exceeds its bound depends on the bounds:
- the top-quark c-coefficient bounds are weak, perhaps 1e-1 to 1e-3, so top may be near the bound;
- μ and τ bounds are sparse.

So the outcome could also be **LV-SAFE**, if only the e/u/d bounds are tight and the counterterm is spent there.

**LV-KILL is unlikely,** because the residuals are local terms.

**What I would check in the worker's report.**
- Does it use only the counterterm freedom the fixed reading allows, i.e. one cubic-invariant counterterm per SM field?
- Does it map lattice coefficients to SME c-coefficients correctly, with the right normalisation?
- Does it notice that in circulant branch-B sectors each mass eigenstate spreads equally over the three corners, so its tetragonal anisotropy averages to an isotropic shift?
