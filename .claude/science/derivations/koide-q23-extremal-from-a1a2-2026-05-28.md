# Derivation: Charged-lepton Koide ratio Q = 2/3 from A1+A2

## Date
2026-05-28

## Target Behavior
The charged-lepton mass spectrum satisfies the Koide relation

    Q = (m_e + m_mu + m_tau) / (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2 = 2/3.

Empirically (PDG masses, runner
`koide_q23_extremal_first_principles_2026_05_28.py`):
`Q_emp = 0.66666051`, a 0.0009% deviation from 2/3.

The open question this note targets: **what forces the physical packet
to this value?** A prior result (not read here) reportedly writes
`Q = (1 + n_doublets)/d` with `n_doublets = 1`, `d = 3`; the missing
piece is the *extremal / constraint principle* that pins the packet.

## Axioms Used
- **A1**: per-site reality is a qubit; local algebra `M_2(C) = Cl(3,0)`
  (the defining number "2").
- **A2**: lattice sites form `Z^3` (the defining number "3"); supplies
  the three-fold (`Z_3`) generation label via cubic structure /
  `Cl(3)` color automorphism.

No other primitives. Dynamics, records, Born rule are not used.

## Minimal Example
Three generations carrying a `Z_3` label `k in {0,1,2}`. The sqrt-mass
packet is the vector `s = (s_0, s_1, s_2)`, `s_k = sqrt(m_k) >= 0`, in
the 3-dim generation space. Democratic direction `1 = (1,1,1)`.

## Derivation

### Step 1 (definition -> purity). Q is the purity of the sqrt-mass distribution.
Let `p_k = s_k / sum_j s_j`. Then `sum_k p_k = 1`, `p_k >= 0`, and

    Q = sum_k m_k / (sum_j s_j)^2 = sum_k s_k^2 / (sum_j s_j)^2 = sum_k p_k^2.

So **Q is exactly the purity / inverse-participation-ratio (Simpson
index)** of the sqrt-mass distribution `p`. Verified numerically:
`sum p_k^2 = 0.66666051 = Q`. Consequences:
- `Q in [1/d, 1]`. `Q = 1/d` iff `p` uniform (all generations equal =
  the `Z_d`-democratic packet, i.e. the diagonal of the **tracial
  reference state** `rho_ref = (x) I/2` native to A1); `Q = 1` iff `p`
  is a delta (single generation = maximal symmetry breaking).
- `n_eff := 1/Q` is the participation number. `Q = 2/3` <=>
  `n_eff = 3/2 = d/2 = (Z^3 dim)/(qubit dim)`.

### Step 2 (geometry). Q = 1/(d cos^2 theta); Q=2/3 <=> 45 deg tilt.
With `theta = angle(s, 1)`, `s.1 = |s| sqrt(d) cos theta`, so
`Q = 1/(d cos^2 theta)`. Splitting `s = s_par + s_perp` into democratic
(`|| 1`) and traceless parts:

    Q = 2/3  <=>  cos^2 theta = 1/2  <=>  |s_perp|^2 = |s_par|^2.

i.e. **Q=2/3 is the EQUIPARTITION of squared-amplitude between the
democratic (mean) mode and the traceless (fluctuation) modes.** Verified
(`cos^2 theta = 0.50000`, `theta = 44.9997 deg`,
`|s_perp|^2/|s_par|^2 = 0.99998`).

### Step 3 (Z_3 coordinates). Equipartition <=> Fourier amplitude r = sqrt(2).
In the `Z_3`-Fourier parametrization `s_k = A(1 + r cos(delta + 2 pi k/3))`
(valid in the non-negativity cone), Plancherel gives
`sum s_k = 3A`, `sum s_k^2 = 3A^2(1 + r^2/2)`, hence
`Q = (1 + r^2/2)/3`, and `Q = 2/3 <=> r = sqrt(2)`, which is precisely
`power(k=0 mean mode) = power(k=+-1 fluctuation doublet)`. (Non-negativity
of sqrt-mass is a genuine constraint, recorded in the runner.)

### Step 4 (A1 forces equipartition via pure-state purity). The crux.
A1 gives a per-site qubit `rho = (I + n . sigma)/2`. Its Hilbert-Schmidt
norm splits into identity (democratic) and Pauli (fluctuation) parts:

    Tr(rho^2) = Tr((I/2)^2) + Tr(((n.sigma)/2)^2) = 1/2 + |n|^2/2.

For a **PURE** qubit state `|n| = 1`: identity-power = Pauli-power = 1/2.
**A pure single qubit has equal democratic and fluctuation HS-power.**
Identifying the sqrt-mass packet's democratic/fluctuation power-split
with the qubit's identity/Pauli HS-split, a *persistent (pure) particle*
excitation (`|n|=1`, not a mixed/decohered state) carries exactly
equipartition -> Step 2 -> `Q = 2/d`.

### Step 5 (A2 fixes d=3; double characterization unique to d=3).
`d = 3` is the number of generations = dim `Z^3` = number of `Cl(3)`
generators (A2 / A1). Two *independent* native balance principles meet:
- **P_equi** (Step 4): equipartition -> `Q_equi = 2/d`.
- **P_mid**: `Q = 2/3` is the arithmetic midpoint of the allowed range
  `[1/d, 1]` -> `Q_mid = (1+d)/(2d)`.

These agree iff `2/d = (1+d)/(2d)` iff `4 = 1+d` iff **`d = 3`**
(unique), common value **2/3**. Verified for d=2..6: only d=3 agrees.

### Step N: Therefore Q = 2/3.
A pure qubit excitation (A1, |n|=1) equipartitions democratic vs
fluctuation power; equipartition gives `Q = 2/d`; A2 fixes `d = 3`; and
`d = 3` is the unique dimension where the equipartition value coincides
with the range-midpoint value. Hence `Q = 2/3`.

## Novel Prediction
**Exactly three Koide-coherent charged-fermion generations.** The two
balance principles (P_equi `= 2/d` and P_mid `= (1+d)/(2d)`) agree ONLY
at `d = 3`. A hypothetical 4th charged-lepton generation forming a
`Z_4`-democratic packet would require `Q_equi = 1/2` but
`Q_mid = 5/8` -- mutually inconsistent. Therefore the framework forbids
any 4th charged-lepton generation from joining a single
Koide-coherent multiplet at the balance point; the observed 3 is a
consistency condition, not an input.

Sharper quantitative corollary: any *additional* charged-lepton-like
state, if it exists, must sit OUTSIDE the `Q = 2/3` triple (it cannot be
absorbed into a `d=4` Koide quadruplet preserving both balance
principles). This is falsifiable by any future heavy charged lepton:
its mass cannot extend the `(e, mu, tau)` triple to a 4-state Koide set
at 2/3.

## Weakest Link
**Step 4's identification** is the least certain: *why* does the
charged-lepton sqrt-mass packet's democratic/fluctuation power-split
equal the qubit `rho`'s identity/Pauli HS-split, and *why* is the
relevant qubit state pure (`|n|=1`) rather than mixed? Steps 1-3, 5 are
exact identities; Step 4 is a structural mapping hypothesis.

Test of the weakest link: derive the map from sqrt-mass amplitudes to
the per-site Bloch decomposition explicitly (e.g. via the staggered
generation realization), and check that the *persistence* condition
(self-maintaining pattern) selects `|n|=1`. If persistence instead
allowed `|n| < 1`, the prediction is `Q < 2/3` by
`Q = 2/(d) * f(|n|)`-type scaling; the observed `Q = 2/3` to 0.001%
then bounds `|n| = 1 - O(10^-5)`, a quantitative target for the
persistence-purity derivation.

## Status
PROPOSED

Steps 1, 2, 3, 5 are verified exact identities (two runners, cached).
Step 4 (A1 -> equipartition via pure-state purity) is a proposed forcing
whose sqrt-mass <-> Bloch identification remains to be derived. The
result is honestly a *near-closure*: it reduces "why 2/3" to the single
question "why is the persistent generation packet a pure-qubit
equipartition," plus the independent (exact) observation that d=3 is the
unique dimension where two distinct balance principles coincide at 2/3.

## Runners
- `scripts/koide_q23_extremal_first_principles_2026_05_28.py`
  (empirical anchor, geometry, Z_3 Fourier, dimension formula, Bloch).
- `scripts/koide_q23_forcing_principle_2026_05_28.py`
  (purity identity, range endpoints, two-balance-principle d=3
  uniqueness, pure-qubit equipartition, novel prediction).
Cached: `logs/runner-cache/koide_q23_*_2026_05_28.txt`.
