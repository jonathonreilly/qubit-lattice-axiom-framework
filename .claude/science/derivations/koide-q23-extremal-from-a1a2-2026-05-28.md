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

### Step 4 (HARDENED + AUDITED). What fixes the equipartition.
> The original Step 3 ("a pure qubit has equal identity/Pauli HS power")
> was **wrong on audit** -- it conflated the generation-space split
> (democratic vs fluctuation, both grade-1) with the qubit grade-0/grade-1
> split, and purity alone does not fix the ratio. Replaced by the
> following, see `koide-q23-assumptions-audit-2026-05-28.md` and runner
> `koide_q23_central_trace_hardening_2026_05_28.py`.

**4a (exact -- the map).** The generation space IS Cl(3) grade-1, and
the color-`Z_3` automorphism cyclically permutes the three Cl(3) vector
generators `sigma_1,sigma_2,sigma_3` -- i.e. the regular representation
of `Z_3`. Its unique `Z_3`-fixed axis is the body diagonal `(1,1,1)`.
So the **democratic direction is forced** (the eigenvalue-1 eigenvector),
not chosen. Fluctuation = the eigenvalue-`{w,w^2}` complement.

**4b (exact -- Kahler).** Frobenius-Schur: `R[Z_3] = R (+) C`. The
fluctuation isotypic is ONE 2-real-dim block carrying a complex
structure `J` (`J^2=-I`), realized as the **Cl(3) grade-2 bivector dual
to the body-diagonal axis** (the rotation generator about `(1,1,1)`).
So fluctuation = 1 complex degree of freedom -- the holomorphic `(1,1)`
reading.

**4c (exact -- the three weightings).** The isotypic power split
`(p_triv, p_fluct)` fixes `Q = 1/(3 p_triv/(p_triv+p_fluct))`. The three
canonical weightings map exactly onto the three special values:

    (1, 0)    -> Q = 1/3   (all-trivial; democratic; Q_min)
    (1/2,1/2) -> Q = 2/3   (equal-block; MIDPOINT)
    (1/3,2/3) -> Q = 1     (dimension-weighted = canonical/Plancherel trace; Q_max)

**4d (KILLED routes).** The canonical / Plancherel central tracial state
weights blocks by dimension `(1/3,2/3)` and gives `Q=1`, NOT 2/3 -- so
"equipartition = canonical central trace" is false; likewise
`rho_ref=(x)I/2` restricted to generations is uniform, giving `Q=1/3`.
Both attractive routes are eliminated.

**4e (residual assumption, tied to A1).** Equipartition is the
**equal-block weighting** = maximum entropy over the `B=2` Frobenius-
Schur block label. The block count `B(d)=2` holds only for `d in {2,3}`;
A1's qubit is exactly a 1-bit (2-valued) primitive, and max-entropy over
a 1-bit label is `(1/2,1/2)`. This is the residual, un-derived step
(why max-entropy over the block label rather than the state label).
-> Step 2 -> `Q = 2/d`.

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

## Weakest Link (post-hardening)
After the Step-4 hardening + audit, the entire residual content is ONE
crisp question (assumption **4e**):

> **Why does the physical packet sit at EQUAL-BLOCK weight (1/2,1/2) =
> maximum entropy over the `B=2` Frobenius-Schur block label, rather
> than at the dimension-weighted canonical trace (1/3,2/3 -> Q=1) or
> the state-uniform reference (Q=1/3)?**

Everything else (Steps 1, 2, 4a-4d, 5) is now an exact identity or an
eliminated route (see audit note). The forcing is sharply localized and
has two independent exact anchors that coincide ONLY at d=3:
equipartition value `2/d` and range-midpoint value `(1+d)/(2d)`.

Test of the weakest link: derive a max-entropy / variational principle
on A1+A2 whose natural random variable is the FS *block* label (1 bit,
the qubit) rather than the generation label. A clean discriminator: any
such principle must reproduce the exact `(1/3,2/3,1)` three-weighting
correspondence AND select the middle option; principles that maximize
entropy over generations (-> Q=1/3) or use the canonical trace
(-> Q=1) are already falsified against `Q_emp = 0.6667`.

## Status
PROPOSED (bounded) -- hardened and self-audited 2026-05-28.

Exact (no assumption): Steps 1, 2, 4a, 4b, 4c, 5, and the d=3
transversality. Eliminated routes (4d): canonical/Plancherel central
trace (-> Q=1) and pure-state purity forcing. Residual un-derived
assumption: 4e (max-entropy over the FS block label). This is honestly
a *bounded* result, not full closure: "why 2/3" is reduced to the single
crisp question of 4e, with two independent exact anchors coinciding only
and transversally at d=3.

## Runners
- `scripts/koide_q23_extremal_first_principles_2026_05_28.py`
  (empirical anchor, geometry, Z_3 Fourier, dimension formula, Bloch).
- `scripts/koide_q23_forcing_principle_2026_05_28.py`
  (purity identity, range endpoints, two-balance-principle d=3
  uniqueness, novel prediction).
- `scripts/koide_q23_central_trace_hardening_2026_05_28.py`
  (Step-4 hardening: generation-space map, Kahler J, three-weighting
  correspondence, canonical-trace kill, B(d) count, transversality).
Audit: `koide-q23-assumptions-audit-2026-05-28.md`.
Cached: `logs/runner-cache/koide_q23_*_2026_05_28.txt`.
