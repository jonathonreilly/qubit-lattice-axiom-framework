# Staggered Vector Ward Identity on the Q_L Block: Lattice Noether Derivation, with the H_unit Matrix-Element Corollary y_t_bare = g_bare / sqrt(6)

**Date:** 2026-04-17 (audit-prep refresh: 2026-05-25;
dependency-registration repair: 2026-06-06; Ward-identity derivation
restored as the load-bearing theorem: 2026-06-09)
**Status:** bounded source theorem. The load-bearing content is now an
actual lattice Ward-identity **derivation**: the exact point-split vector
Ward identity of the staggered `Q_L` action on the qubit-on-`Z^3` baseline
(equivalently the physical `Cl(3)` local-algebra reading on `Z^3`),
derived by the lattice Noether / Schwinger-Dyson change-of-variables
argument from the action's exact `U(1)_B x U(2)_iso` vector symmetry, and
verified by the runner as a **computed residual** on explicit small-lattice
constructions — vanishing exactly under the derived conditions and
**provably nonzero** when the current or the symmetry is deliberately
broken (falsification legs). The previously reviewed `1/sqrt(6)`
scalar-singlet matrix element `(T1)` is kept as a corollary whose
"singlet uniformity" step is now derived (Schur/commutant) rather than
asserted. This note is **not** a derivation of the Standard Model top
Yukawa value, a Planck-surface ratio theorem, or a shared
tadpole-transport closure.
**Type:** bounded_theorem.
**Status authority:** this note declares source scope only. The independent
audit lane sets audit status; effective status is pipeline-derived.
**Primary runner:** `scripts/frontier_yt_ward_identity_derivation.py`
(58 PASS / 0 FAIL on current source; runtime < 10 s; includes an
exact-arithmetic sympy certificate and explicit falsification legs).
**Dependency-registration companion runner:**
`scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py`
(31 PASS / 0 FAIL on current source). Companion note:
`YT_WARD_IDENTITY_DEPENDENCIES_REGISTERED_BOUND_NARROW_THEOREM_NOTE_2026-06-05.md`.
**Support (NOT part of the authority chain):**
`UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md`
documents the perturbative 1-loop vertex correction, which is OPEN
for quantitative lane reuse (not part of this bounded theorem).

---

## Audit boundary (crisp, load-bearing — read first)

The auditable claims of this note are **(W1)-(W3)** (the Ward-identity
derivation and its symmetry corollaries) and **(T1)** (the `H_unit`
scalar-singlet matrix element). The explicit boundaries:

- **(B1) Staggered-Dirac realization surface — an explicit condition.** The
  staggered `Q_L` action on which (W1)-(W3) and (T1) are stated is the
  condition tracked by the claim
  `staggered_dirac_realization_gate_note_2026-05-03`
  ([`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)).
  That gate is cited as a **declared condition by claim id**: this note
  does not close it, and the condition supplies no premise or dependency
  readiness. Every theorem below is conditional on that stated action
  surface. Inside the surface, the derivations are exact
  finite-dimensional mathematics.
- **(B2) `g_bare = 1` is a rescaling convention.** The form
  `y_t_bare = g_bare/sqrt(6)` uses the canonical bare gauge unit. The
  load-bearing form factor `y_t_bare/g_bare = 1/sqrt(6)` is
  `g_bare`-flat; the algebraic basis for the convention is
  [`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md`](BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md).
- **(B3) No SM readout, no transport, no precision.** `y_t_bare` is local
  shorthand for the matrix element defined in Eq. (3.7). No Standard
  Model Yukawa identification, no Planck-surface tadpole transport, no
  RG/precision/NLO claim is made. Equation (4.3) is conditional context
  only.
- **(B4) Which symmetries the Ward identity covers.** The derived Ward
  identities are those of the exact vector symmetries of the staggered
  `Q_L` action at fixed color links: the `U(1)_B` fermion-number phase
  and the global `U(2)_iso` isospin rotations (links act on color only).
  The gauged color non-singlet currents, axial/taste currents, and any
  anomaly statement are **out of scope**. The Lorentz-Clifford Fierz
  scalar-projection input is standard 4D Clifford algebra (standard
  mathematics), used only in the Step-3 consistency check.

The dependency-routing repair of 2026-06-06 is kept: the two
load-bearing context dependencies (B1, B2) are routed through the
registered bridge
[`YT_WARD_IDENTITY_DEPENDENCIES_REGISTERED_BOUND_NARROW_THEOREM_NOTE_2026-06-05.md`](YT_WARD_IDENTITY_DEPENDENCIES_REGISTERED_BOUND_NARROW_THEOREM_NOTE_2026-06-05.md).
That routing does **not** close `AC_phi_lambda` and does **not** assign an
audit status.

Review history note: earlier passes correctly identified that the old
source row did not derive a Ward identity; its load-bearing step was the
definition of `y_t_bare` plus a narrowed matrix-element core. A later
dependency pass flagged the unregistered staggered-Dirac / `g_bare = 1`
surfaces, which the 2026-06-06 repair routed to registered sources. The
2026-06-09 refresh addresses the remaining honest weakness of the row: a
note named "Ward identity derivation" whose load-bearing step was still a
normalization definition. The Ward identity is now **derived** (Step 0)
from the action's symmetry by the lattice Noether / Schwinger-Dyson
argument, and the runner computes the Ward residual on explicit lattice
constructions with falsification legs, so the load-bearing step is a
first-principles derivation on the declared surface, not a definition or
renaming.

---

## Theorem statements

All statements are on the registered staggered-Dirac / canonical-`Q_L`
surface (B1) with the `g_bare = 1` convention (B2) where indicated.
Notation: finite periodic block of `Z^3`, sites `x`; staggered phases
`eta_1 = 1`, `eta_2(x) = (-1)^{x_1}`, `eta_3(x) = (-1)^{x_1+x_2}` (D2);
fermions `psi_{alpha,a}(x)` on the `Q_L = (2,3)` block (D8); fixed SU(3)
color link background `U_mu(x)` acting trivially on isospin; bare action

```
    S = psibar M psi,    M = m_hat + D,
    D(x, x+mu) = +eta_mu(x)/2 * (1_iso ⊗ U_mu(x)),
    D(x+mu, x) = -eta_mu(x)/2 * (1_iso ⊗ U_mu(x)†),                     (0.1)
```

with `m_hat` a site-independent iso-diagonal bare mass. `E_x` denotes the
site-`x` projector and `Delta^-_mu f(x) := f(x) - f(x - mu)` the backward
lattice divergence.

**(W1) Exact point-split vector Ward identity (derived, Step 0).**
For every finite block, every fixed link background, and every
iso-degenerate `m_hat = m * 1`: the point-split current

```
    V_mu(x) = psibar J_mu(x) psi,
    J_mu(x): +eta_mu(x)/2 (1 ⊗ U_mu(x))   at (x, x+mu),
             +eta_mu(x)/2 (1 ⊗ U_mu(x)†)  at (x+mu, x)                  (0.2)
```

obtained by the lattice Noether procedure from the exact global `U(1)_B`
vector symmetry of `S` satisfies the kernel-level Noether identity

```
    sum_mu [ J_mu(x) - J_mu(x - mu) ] = [ E_x, M ]                       (0.3)
```

and hence the exact Schwinger-Dyson Ward identity with contact terms

```
    sum_mu Delta^-_mu < V_mu(x) psi(y) psibar(z) >
        = ( delta_{x,z} - delta_{x,y} ) < psi(y) psibar(z) >,            (0.4)

    sum_mu Delta^-_mu < V_mu(x) > = 0.                                   (0.5)
```

These hold configuration-by-configuration (hence also after any link
average), exactly, with no continuum or weak-coupling limit.

**(W2) Iso-vector Ward identity with exact breaking form.** For any
isospin matrix `t` (acting trivially on color, hence commuting with all
links), the charged current `V^t_mu(x) = psibar J_mu(x) t psi` satisfies

```
    sum_mu Delta^-_mu < V^t_mu(x) F > + < (psibar E_x [t, m_hat] psi) F >
        = contact terms(t),                                              (0.6)
```

so it is exactly conserved iff `[t, m_hat] = 0` (degenerate bare mass),
and at split mass `m_hat = diag(m_1, m_2) ⊗ 1_c` with `t = tau^+` the
violation is **exactly** the `(m_2 - m_1) psibar tau^+ psi` insertion —
nothing else.

**(W3) Symmetry corollary — singlet uniformity and uniqueness.** The
invariant unit-norm bilinear on `Q_L ⊗ Q_L*` under the actual product
symmetry content of the channel, `U(2)_iso` together with color-singlet
`SU(3)` gauge invariance, is unique up to phase and equals
`s = (1/sqrt(6)) * 1`: the commutant of the product action on
`C^2 ⊗ C^3` is 1-dimensional (Schur), so all six diagonal
Clebsch-Gordan components are **forced** equal to `1/sqrt(6)`. The exact
vector symmetries of the gauged action at fixed links, `U(1)_B x
U(2)_iso` (from W1/W2), together with color gauge invariance, select the
same `(1,1)` scalar-singlet channel used by `H_unit` (D17).

**(T1) Matrix-element corollary (bounded core).**
With the canonical unit-residue normalization (Step 1) and the
uniformity forced by (W3),

```
    y_t_bare = g_bare / sqrt(2 N_c) = g_bare / sqrt(6)                  (T1)
```

where `y_t_bare` denotes the `H_unit` matrix element defined in Eq. (3.7)
and the equality to `g_bare/sqrt(6)` uses the canonical bare gauge unit
`g_bare = 1` (B2); no physical Yukawa readout is asserted by this
notation.

The older Planck-surface ratio statement
`y_t(M_Pl) / g_s(M_Pl) = 1/sqrt(6)` is not part of this note's auditable
core. It requires a separate accepted tadpole-transport bridge and a
separate accepted physical readout map.

**Scope of this note:**
- (W1)-(W2) are exact lattice operator identities on the declared (B1)
  surface; (W3) and (T1) are exact finite-dimensional algebra.
- It makes NO quantitative precision claim (no `±%`, no NLO bound,
  no lane budget).
- Perturbative 1-loop corrections, higher-order topology corrections,
  physical Yukawa readout, shared tadpole transport, and any quantitative
  lane reuse are OUT OF SCOPE and are discussed only as non-load-bearing
  context.
- Downstream quantitative reuse of (T1) inherits whatever systematic the
  downstream package carries independently. This note does not narrow or
  claim such systematics.

---

## Inputs and dependency table

| # | Input | Status | Source |
|---|-------|--------|--------|
| Quantum | **one-qubit operator algebra per site, equivalently physical `Cl(3)` local algebra** | **AXIOM** | [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) |
| Lattice | **`Z^3` lattice** | **AXIOM** | [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) |
| D1 | Z³ bipartite → Z₂ parity ε = (-1)^{x+y+z} | DERIVED from Lattice | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):14-18 |
| D2 | Staggered fermion η phases on Z³ | DERIVED from D1 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):14-18 |
| D3 | Taste doubling: 2³ = 8 internal species | DERIVED from D2 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):16 |
| D4 | η phases → physical `Cl(3)` action in taste space | DERIVED from D3 + Quantum | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):17 |
| D5 | Cl(3) ⊃ su(2) → SU(2) weak gauge symmetry | DERIVED from D4 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):18 |
| D6 | Graph-first axis selector on taste cube {0,1}³ | DERIVED from D3 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):52-66 |
| D7 | Residual swap on complementary axes → `su(3)` closure | DERIVED from D6 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):69-75 |
| D8 | Selected nonabelian `(2,3)` block, dim `N_iso N_c = 6` | DERIVED from D5 + D7 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):93-95 |
| D9 | Local scalar-singlet bilinear operator on the Q_L block, `phi = Z^{-1} sum_{alpha,a} psi-bar_{alpha,a} psi_{alpha,a}` | DEFINED in this note from D8 + canonical state normalization | Eq. (1.1), runner Block 2 |
| D10 | Composite 2-point residue `<phi phi>_free = (N_c N_iso / Z²) G_0²` | DERIVED from D9 by explicit index contraction | Eq. (1.2), runner Block 2 |
| D11 | Unit-residue normalization `Z² = N_c N_iso = 6` | DERIVED from D10 | Eq. (1.3), runner Block 2 |
| D12 | Exact SU(N_c) Fierz identity on fundamental generators | STANDARD finite-dimensional Lie-algebra identity | Eq. (3.3), runner Block 4 |
| D13 | Wilson plaquette coupling `β = 2 N_c/g_bare²` at canonical surface | DERIVED from D5 + D7 + standard Wilson action | standard lattice QFT applied to D5, D7 |
| D14 | CMT change-of-variables tadpole identity | NON-LOAD-BEARING CONTEXT for the older Planck-ratio statement | not used in `(W1)`-`(T1)` |
| D15 | `n_link` power counting for shared tadpole transport | NON-LOAD-BEARING CONTEXT for the older Planck-ratio statement | not used in `(W1)`-`(T1)` |
| C1 | Canonical `Q_L = (2,3)` staggered-Dirac action surface, Eq. (0.1) | **declared condition B1**; routes to `AC_phi_lambda`, cited by claim id, not closed here and carrying zero premise weight | [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md); [`YT_WARD_IDENTITY_DEPENDENCIES_REGISTERED_BOUND_NARROW_THEOREM_NOTE_2026-06-05.md`](YT_WARD_IDENTITY_DEPENDENCIES_REGISTERED_BOUND_NARROW_THEOREM_NOTE_2026-06-05.md) |
| C2 | `g_bare = 1` on canonical surface | RESCALING CONVENTION with accepted algebraic basis (boundary B2); the load-bearing form factor `y_t_bare/g_bare = 1/sqrt(6)` is `g_bare`-flat | [`BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md`](BETA_GBARE_RESCALING_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md); [`YT_WARD_IDENTITY_DEPENDENCIES_REGISTERED_BOUND_NARROW_THEOREM_NOTE_2026-06-05.md`](YT_WARD_IDENTITY_DEPENDENCIES_REGISTERED_BOUND_NARROW_THEOREM_NOTE_2026-06-05.md) |
| SU(3) Casimir | SU(3) fundamental Casimir `C_F = (N_c²-1)/(2N_c) = 4/3` | STANDARD Lie-algebra fact | applied to D7 |
| Lorentz-Clifford Fierz | Lorentz-group Fierz: `(γ^μ)(γ_μ)` scalar coefficient `|c_S| = 1` | STANDARD Clifford-algebra identity | Itzykson-Zuber §2-5; verified by Block 8 of runner |
| D16 | Tree-level Feynman-rule completeness of the bare action on the scalar-singlet channel: at O(α_LM) exactly ONE tree diagram (OGE) contributes to `Γ⁽⁴⁾(q²)` on the (1,1) Dirac-scalar channel | DERIVED from tree-level Feynman rules of the cited action + absence of any fundamental scalar or bare contact 4-fermion vertex | framework-native; follows from `MINIMAL_AXIOMS_2026-06-05.md` + registered C1/C2 + D9 |
| D17 | Scalar-singlet operator uniqueness on the Q_L block: `H_unit = (1/√6) Σ ψ̄ψ` is the unique unit-normalized (1,1) Dirac-scalar composite (`Z² = 6`; alternatives give `Z² = 8, 9/2, 24`) | DERIVED; numerically verified (Block 5) and symmetry-forced (Block W7, Schur) | D9-D11, W3, runner Blocks 5 + W7 |
| **D18** | **Exact global `U(1)_B x U(2)_iso` vector symmetry of the staggered `Q_L` action at fixed color links** | DERIVED by inspection of Eq. (0.1): every term is `psibar (...) psi` with link/η structure trivial on iso; Grassmann measure invariant (unit Jacobian) | Step 0.1; runner Blocks W1, W2, W5 |
| **D19** | **Kernel Noether identity `sum_mu Delta^-_mu J_mu(x) = [E_x, M]`** | DERIVED from D18 by localized change of variables (Step 0.2) | Eq. (0.3); runner Blocks W1, W6 (exact arithmetic) |
| **D20** | **Schwinger-Dyson Ward identity with contact terms, Eq. (0.4)-(0.6)** | DERIVED from D19 + Grassmann Gaussian integration (Step 0.3) | runner Blocks W2, W5, W6; falsification Blocks W3, W4 |

The only framework axioms consumed by this note are Quantum (one-qubit
operator algebra per site, equivalently physical `Cl(3)`) and Lattice
(`Z^3`) from `MINIMAL_AXIOMS_2026-06-05.md`. The Record axiom is not
load-bearing for any claim here. The remaining inputs are the framework
chain (D1-D20), the registered dependency routes (C1-C2), or STANDARD
group-theoretic identities independent of framework content.
**There is no separate "matching axiom" in this note**, and the Ward
identity is **not obtained by defining the current to be conserved**: the
current (0.2) is constructed by the Noether procedure from the action's
symmetry (D18), and its conservation (0.4)-(0.5) is then a derived,
runner-computed consequence that demonstrably **fails** when the current
is mismatched to the action (runner Blocks W3, W4) or when the symmetry
is explicitly broken (Block W5).

---

## Step 0: Derivation of the lattice Ward identity (the load-bearing step)

### Step 0.1: The exact vector symmetry of the staggered Q_L action

Every term of the action (0.1) is a fermion bilinear `psibar(x) K(x,y)
psi(y)` whose kernel acts on isospin as the identity (links are color
only; η phases and mass are iso-scalars for degenerate `m_hat`). Hence:

- the global phase rotation `psi(x) → e^{iθ} psi(x)`,
  `psibar(x) → psibar(x) e^{-iθ}` leaves `S` invariant exactly
  (`U(1)_B`);
- for degenerate mass, the global isospin rotation `psi → (V ⊗ 1_c) psi`,
  `V ∈ U(2)`, leaves `S` invariant exactly (`U(2)_iso`).

The Grassmann measure is invariant under both: the Jacobian of
`psi → e^{iθ}psi` is `e^{-iθ n}` and of `psibar → psibar e^{-iθ}` is
`e^{+iθ n}`; the product is 1 (and similarly `det(V)^{-n} det(V)^{n} = 1`
for the unitary iso rotation). The vector symmetries are therefore
non-anomalous on the lattice: the full path-integral weight is invariant.
This is the symmetry input (D18); it is read off the cited action
surface (C1), not postulated separately.

### Step 0.2: Localized variation → kernel Noether identity

Localize the phase: `psi(x) → e^{iα(x)} psi(x)`. The mass term is
invariant. Each hopping pair transforms as

```
    η/2 [ psibar(x) U psi(x+mu)  -  psibar(x+mu) U† psi(x) ]
      → first order in α:
    + i (α(x+mu) - α(x)) · η/2 [ psibar(x) U psi(x+mu) + psibar(x+mu) U† psi(x) ]
      = + i (α(x+mu) - α(x)) · V_mu(x),                                  (0.7)
```

i.e. the antisymmetric hopping difference emits the **symmetric**
point-split combination — this is the lattice Noether current (0.2),
produced by the variation itself. Summing and shifting the summation
variable (`Σ_x α(x+mu) f(x) = Σ_x α(x) f(x-mu)` on the periodic block):

```
    δS = - i Σ_x α(x) · sum_mu Delta^-_mu V_mu(x).                       (0.8)
```

Independently, writing the same first-order variation directly on
`S = psibar M psi` with the site projector `E_x`:

```
    δS = i Σ_x α(x) · psibar [M, E_x] psi.                               (0.9)
```

Equating the coefficient kernels of each independent `α(x)` in
(0.8) = (0.9) gives the kernel-level Noether identity (0.3):

```
    sum_mu [ J_mu(x) - J_mu(x - mu) ] = [ E_x, M ]      for every x.
```

This is a finite matrix identity on the explicit construction — the
runner verifies it at machine precision on random SU(3) link backgrounds
(Block W1) and **exactly** (sympy rational arithmetic, exact unimodular
links) in Block W6.

### Step 0.3: Schwinger-Dyson contact terms → the Ward identity

For any observable `F(psi, psibar)`, invariance of the Grassmann measure
under the change of variables gives `< δF > = < F δS >`. Take
`F = psi(y) psibar(z)`; then `δF = i (α(y) - α(z)) F`, and matching the
coefficient of `α(x)` using (0.8):

```
    sum_mu Delta^-_mu < V_mu(x) psi(y) psibar(z) >
        = ( delta_{x,z} - delta_{x,y} ) < psi(y) psibar(z) >.            (0.4)
```

Equivalently, at the propagator level with `G = M^{-1}` and the full Wick
value `< (psibar A psi) psi psibar > = -Tr(A G) G + G A G`:

```
    sum_mu Delta^-_mu (G J_mu(x) G) = G [E_x, M] G = G E_x - E_x G,      (0.10)
    sum_mu Delta^-_mu Tr(J_mu(x) G) = Tr([E_x, M] G) = 0,                (0.11)
```

where (0.10) uses only `M G = G M = 1` applied to (0.3), and (0.11) is
the exact conservation of `<V_mu>` (0.5). The contact terms
`(delta_{x,z} - delta_{x,y}) G` are exactly the right side of (0.10).
With `F = 1`, the same argument gives (0.5) directly. The Wilson
plaquette term of the full bare action is a pure-link functional: the
fermionic change of variables does not touch it, so it multiplies both
sides of the fixed-link identity and drops out — the identity therefore
holds for every fixed link configuration **and** under the full
plaquette-weighted link integral. No continuum limit, no weak coupling,
no gauge fixing is used.

### Step 0.4: Iso-vector currents and the exact breaking form (W2)

For `t` acting on iso only, `t` commutes with every hopping kernel
(links are color, η is scalar), so localizing `psi → e^{iα(x) t} psi`
gives the same algebra with `J_mu(x) → J_mu(x) t` except in the mass
term, which contributes `E_x [t, m_hat]`:

```
    sum_mu Delta^-_mu (J_mu(x) t) = [E_x t, M] - E_x [t, m_hat].         (0.12)
```

Hence the charged-current Ward identity (0.6): exactly conserved iff
`[t, m_hat] = 0`; with `m_hat = diag(m_1, m_2) ⊗ 1_c` and `t = tau^+`,
`[tau^+, m_hat] = (m_2 - m_1) tau^+`, so the violation is **exactly** the
`(m_2 - m_1) psibar tau^+ psi` insertion. The runner verifies the broken
identity at machine precision **with** the insertion and a residual of
order `(m_2 - m_1)` **without** it (Block W5). This is the strongest
falsification leg: the conservation law tracks the symmetry content of
the action exactly, including its explicit breaking.

### Step 0.5: What would falsify the derivation (and is computed to)

If the Ward identity were definitional — a current defined to be
conserved — then deformations of the current would not spoil it. They
do, and the runner computes the failure:

- **Link-stripped current** (gauge links removed from `J_mu` while the
  action keeps them): kernel residual `≈ 0.96`, propagator-level Ward
  residual `≈ 0.87` on a random SU(3) background (Block W3) — and the
  failure disappears at trivial links `U = 1`, locating it precisely in
  the gauge covariance the Noether procedure dictates.
- **η-mismatched current** (`η ≡ +1` in the current, staggered η in the
  action): kernel residual `≈ 0.99` at sites where some entering
  `η = -1`, and exactly zero at the all-`η = +1` site — the mismatch is
  local, exactly as the derivation predicts (Block W4).
- **Explicitly broken symmetry** (split iso mass): residual `≈ 0.2`
  without the mass insertion, machine zero with the exact insertion
  (Block W5).
- **Exact arithmetic**: on a 2x3 staggered block with exact unimodular
  Gaussian-rational links and `m = 7/10`, the kernel and propagator Ward
  residuals are the **exact zero matrix** (sympy), and the link-stripped
  falsification residual is an exact nonzero rational (Block W6).

---

## Structural identification fact: no physical Yukawa map is claimed

The corollary (T1) uses `y_t_bare` only as a local label for the matrix
element of the unit-normalized scalar-singlet operator `H_unit` on the
specified top-basis component of Q_L. It does not require, and does not
assert, an independent derivation of the Standard Model Yukawa readout.

The bare-action surface contains only the Wilson plaquette and the
staggered Dirac operator. That observation is used here only to motivate
the same-1PI scalar-singlet consistency check in Step 3. The auditable
content is (W1)-(W3) plus the direct operator normalization and matrix
element in Steps 1-2 and Eq. (3.8).

---

## Structural calculation (corollary chain to (T1))

### Step 1: Canonical kinetic normalization of phi on the Q_L block

Extend D9's color-only form to the full Q_L block (D8) by including the
isospin index α:

```
    phi(x) = (1/Z) * sum_{α,a} psi-bar_{α,a}(x) psi_{α,a}(x)           (1.1)
```

Compute `<phi(x) phi(y)>_{conn,free}` using D10's formula + the free
propagator δ_{αβ} δ_{ab} G_0(x,y). The internal δ-structure is not an
assumption here: at fixed links the propagator is **exactly**
iso-diagonal because `M` commutes with `U(2)_iso` (D18; runner Block W2
checks `max |G_iso-offdiag| = 0`), and the color δ on the free/tree
surface is the trivial-link case of the same statement:

```
    <phi(x) phi(y)>_{conn,free} = -(N_c · N_iso / Z²) · G_0(x,y)²      (1.2)
```

Canonical unit-residue (absorbing the fermion-loop sign):

```
    Z² = N_c · N_iso = 6  →  Z = sqrt(6)                              (1.3)
```

### Step 2: Clebsch-Gordan overlap of the unit-norm singlet

The (1,1) singlet state in the Q_L ⊗ Q_L* bilinear Hilbert space
(dim = 36), unit-normalized, is

```
    |S> = (1/sqrt(6)) * sum_{α,a} |α,a> ⊗ |α,a>*                      (2.1)
```

The top-channel basis bilinear `|top-pair> = |up, top-color> ⊗ |up, top-color>*`
has overlap

```
    <top-pair | S> = 1/sqrt(6)                                        (2.2)
```

The equality of all 6 component overlaps is **derived**, not asserted:
by (W3), the commutant of the `U(2)_iso x SU(3)_color` product action
on `C^2 ⊗ C^3` is the scalars (runner Block W7 computes the commutant
dimension = 1), so the invariant unit-norm bilinear is forced to
`(1/sqrt(6)) * 1` — uniform diagonal, each component `1/sqrt(6)`.

### Step 3: Same-1PI-function residue check (scalar-singlet channel)

This step records the consistency identity entirely within the cited
qubit-on-`Z^3` / physical-`Cl(3)` framework surface, as a single 1PI
Green's function computed two ways. There is no UV-vs-EFT matching, no
second "effective theory" to be defined; only one theory, one Green's
function, two algebraically equivalent representations of it.

**Object of the check.** Define the amputated, 1PI, color-singlet
× iso-singlet × Dirac-scalar-scalar projection of the four-fermion
Green's function on the Q_L block:

```
    Γ⁽⁴⁾(q²) := P_{S,(1,1)} · ⟨ψ̄ψ(q) ψ̄ψ(-q)⟩_{1PI,amp}            (3.1)
```

where `P_{S,(1,1)}` projects onto the single channel
`O_S = (ψ̄ψ)_{(1,1)} (ψ̄ψ)_{(1,1)}` — color-singlet, iso-singlet,
Dirac-scalar on both bilinears. **Only this one channel is the
subject of the note; no other Dirac or representation channel is
claimed.**

**Representation A — direct OGE computation in the bare action.**

The cited bare action contains only the Wilson plaquette and the
staggered Dirac operator (D16, on the registered `AC_phi_lambda`
staggered-Dirac / canonical-`Q_L` surface) — no fundamental scalar
field, no contact 4-fermion operator. At tree order in α_LM, the only
Feynman diagram contributing to `Γ⁽⁴⁾(q²)` is single-gluon exchange:

```
    Γ⁽⁴⁾(q²)|_OGE = -(g_bare² / q²) · Σ_a (T^a)_{ij}(T^a)_{kl}
                                    · (γ^μ)_{αβ}(γ_μ)_{γδ}        (3.2)
```

Project onto `O_S`: apply the exact SU(N_c) color-singlet Fierz
identity (D12, verified machine-precision by Block 4):

```
    Σ_a (T^a)_{ij}(T^a)_{kl}|_{δ_{ij}δ_{kl} channel} = -1/(2 N_c)  (3.3)
```

and the exact Lorentz-Clifford scalar projection
verified machine-precision by Block 8: `|c_S| = 1`):

```
    (γ^μ)_{αβ}(γ_μ)_{γδ}|_{(1)_{αβ}(1)_{γδ} channel} = c_S         (3.4)
```

Substituting (3.3) and (3.4) into (3.2):

```
    Γ⁽⁴⁾(q²)|_OGE = -c_S · g_bare² / (2 N_c · q²) · O_S            (3.5)
```

This is the COMPLETE tree-order value of `Γ⁽⁴⁾` from the bare
action: no other tree diagram contributes (D16 = Feynman-rule
completeness of the cited Wilson-staggered + plaquette action).

**Representation B — direct matrix-element computation of the local
`y_t_bare` shorthand from the H_unit operator content.**

The local scalar-singlet operator definition (D9) defines `H_unit`
on the Q_L block:

```
    H_unit(x) := (1/√(N_c · N_iso)) · Σ_{α,a} ψ̄_{α,a}(x) ψ_{α,a}(x)
              =  (1/√6) · (ψ̄ψ)_{(1,1)}(x)                          (3.6)
```

with the canonical normalization `Z = √6` derived in Step 1 and
shown UNIQUE in Step 2 / Blocks 5 + W7 (D17, W3): `H_unit` is the only
unit-normalized scalar bilinear operator on the Q_L block with
`Z² = N_c · N_iso = 6`.

**Local definition of y_t_bare via the H_unit-to-top-basis matrix element.**
On the canonical surface (`g_bare = 1`) this note uses `y_t_bare` as
local shorthand for the unit-norm-state matrix element of the H_unit
operator between the vacuum and a single top-pair basis state in the
(color = top-color, iso = up) component of the Q_L block:

```
    y_t_bare := ⟨0 | H_unit(0) | t̄_{top,up} t_{top,up}⟩            (3.7)
```

> **Identification-map boundary (audit-prep clarification, 2026-05-25).**
> Equation (3.7) is a local notation definition for this source note. The
> claim boundary is only that the defined matrix element satisfies `(T1)`.
> Whether this matrix element coincides with the Standard Model top-Yukawa
> observable, or transports to `M_Pl` with the same tadpole factor as the
> gauge vertex, is a separate downstream question. Prior review correctly
> identified that the SM map was not derived; that map remains outside the
> auditable core.

Computing this matrix element directly from (3.6):

```
    y_t_bare = (1/√(N_c · N_iso)) · ⟨0 | ψ̄_{top,up} ψ_{top,up}(0)
               | t̄_{top,up} t_{top,up} ⟩
            = (1/√6) · 1
            = 1 / √6                                                (3.8)
```

The first factor (1/√6) is the Clebsch-Gordan weight from (3.6),
forced uniform by (W3). The second factor (= 1) is the unit-amplitude
Wick contraction of the bilinear `ψ̄ψ` with the corresponding
fermion-pair external state in canonical fermion normalization — a
kinematic identity, not a dynamical input.

**This evaluation uses ONLY:**
- the explicit operator content of H_unit (3.6) — Clebsch-Gordan
  weight 1/√(N_c · N_iso), from D17 + Steps 1-2 + (W3);
- canonical fermion-state normalization;
- canonical scalar-composite normalization (Step 1, Z = √6).

It uses **no** information about OGE, no gauge coupling, no
4-fermion coefficient, no matching rule. It is a direct evaluation
of a matrix element of a defined composite operator on a defined
external state.

**Compute Γ⁽⁴⁾(q²)|_H_unit-rep from (3.8) independently.** Tree-level
H_unit-mediated contribution to the same Green's function, with
H_unit Yukawa vertices given by (3.8) on each side:

```
    Γ⁽⁴⁾(q²)|_H_unit-rep = -y_t_bare² / q² · O_S
                         = -(1/√6)² / q² · O_S
                         = -1 / (6 · q²) · O_S                      (3.9)
```

in the tree-level scalar-singlet residue normalization used by this
source note.

**The same-1PI-function consistency identity.**

Representations (A) and (B) are two INDEPENDENT computations of the
same Green's function `Γ⁽⁴⁾(q²)` in the same cited framework surface:
- (A) is computed from gauge-theory Feynman rules (OGE diagram
  + color/Dirac Fierz projection).
- (B) is computed from the H_unit operator's matrix element with
  the external top state (Clebsch-Gordan + canonical normalization).

Each is computed WITHOUT reference to the other. Comparing:

```
    Γ⁽⁴⁾_A = -c_S · g_bare² / (2 N_c · q²) · O_S
           = -1 · 1² / 6 / q² · O_S    (at canonical g_bare = 1, |c_S| = 1)
           = -1 / (6 q²) · O_S                                       (3.10)

    Γ⁽⁴⁾_B = -1 / (6 q²) · O_S      (3.9 above)                     (3.11)
```

The two values agree at the canonical surface (g_bare = 1). This
agreement is a non-trivial consistency check of the cited framework
surface: the bare action's gauge dynamics (Representation A) and the
operator content of `H_unit` (Representation B) give the same Green's
function on the scalar-singlet channel.

**The local matrix element y_t_bare = 1/√6 is therefore defined and
evaluated** from H_unit operator content (3.7-3.8). The agreement
(3.10 = 3.11) confirms internal consistency of the framework but is
not the source of the value.

**Inputs used (cited framework inputs plus exact group-theoretic identities):**

1. The bare qubit-on-`Z^3` / physical-`Cl(3)` lattice action
   (`MINIMAL_AXIOMS_2026-06-05.md` plus registered `AC_phi_lambda`
   staggered-Dirac / canonical-`Q_L` surface and algebraic
   `g_bare = 1` rescaling convention) — contains exactly Wilson
   plaquette and staggered Dirac, no fundamental scalar, no contact
   4-fermion.
2. D9-D11: local scalar-singlet operator definition and unit-residue
   normalization on the Q_L block, derived in Steps 1-2 and runner
   Block 2, with the internal δ-structure of the propagator supplied by
   the exact symmetry D18 (Block W2).
3. D16: Feynman-rule completeness of the bare action — at O(α_LM)
   only the OGE diagram contributes to `Γ⁽⁴⁾`.
4. D17 + (W3): scalar-uniqueness of `H_unit` on the Q_L block (Z² = 6
   unique among (1,1) Dirac-scalar composites, Block 5; uniformity
   forced by the Schur/commutant computation, Block W7).
5. SU(N_c) color-singlet Fierz coefficient `-1/(2 N_c)` (D12,
   exact SU(N_c) identity, Block 4 verified to machine precision).
6. Lorentz-Clifford scalar projection coefficient `|c_S| = 1`
   (exact Clifford-algebra identity, Block 8 verified).
7. No physical IR scale separation or Standard Model matching statement
   is load-bearing for `(W1)`-`(T1)`.

There is no second theory, no matching rule, no auxiliary mass
freedom, no spectral assumption.

### Step 4: Non-load-bearing canonical-surface ratio context

This section records the historical tadpole-ratio context only. It is
not part of the auditable claims and does not import the older
tadpole-transport rows as one-hop dependencies.

If a later accepted tadpole-transport bridge supplies the shared
single-link dressing for both the scalar-singlet matrix element and the
gauge vertex, then the Wilson gauge coupling on the canonical surface
would be written:

```
    g_s(M_Pl) = sqrt(4 pi alpha_LM) = g_bare / sqrt(u_0)              (4.1)
```

with `alpha_LM = alpha_bare / u_0`.

Under that additional, non-load-bearing premise, the matrix element
(3.8) would inherit the same `1/sqrt(u_0)` factor:

```
    y_t(M_Pl) = y_t_bare / sqrt(u_0)
              = (g_bare / sqrt(6)) / sqrt(u_0)
              = g_s(M_Pl) / sqrt(6)                                   (4.2)
```

and the ratio would be:

```
    y_t(M_Pl) / g_s(M_Pl) = 1 / sqrt(6)                               (4.3)
```

Equation (4.3) is conditional context only in this revision. It is not
claimed as support by this note. The runner attaches **no
PASS/FAIL line** to any tadpole or plaquette-helper quantity.

### Boundary of the identification

```
    (W1)  exact point-split vector Ward identity         (derived, Step 0)
    (T1)  y_t_bare = g_bare / sqrt(6)        (exact matrix-element algebra)
```

`(W1)` is exact on the declared (B1) action surface, for every finite
block and every fixed link background. `(T1)` is the exact algebraic
identity on the stated canonical bare-action surface; `y_t_bare` is the
source-note shorthand for the matrix element in Eq. (3.7), not the SM
observable; see the identification-map boundary following Eq. (3.7).

No precision bound, no NLO claim, no systematic is attached. Perturbative
and higher-order corrections are out of scope and are discussed in the
support note `UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md`.
Downstream quantitative reuse carries whatever systematic the downstream
package carries independently; the note does not narrow that.

This is a framework-native derivation within the qubit-on-`Z^3` baseline
plus two explicitly routed dependency surfaces: the registered
`AC_phi_lambda` staggered-Dirac / canonical-`Q_L` surface (B1) and the
algebraic `g_bare = 1` rescaling convention (B2). It uses the chain
D1-D13, D16-D20, exact SU(N_c) / Clifford algebra, and canonical
normalization choices C1-C2. No new axioms. No framework conventions
beyond canonical normalization. No package-status-doc imports.

---

## Scale/scheme statement

What is identified where:

1. **On the declared staggered action surface (B1), any finite block,
   any fixed link background**: the exact point-split vector Ward
   identity (0.3)-(0.6), configuration-by-configuration.

2. **On the canonical bare-action surface**: the source-note matrix
   element `y_t_bare := <0 | H_unit | t-bar t>` equals
   `g_bare/sqrt(6)` when `g_bare = 1` is used as the canonical bare gauge
   unit (B2).

3. **At M_Pl or v**: no physical Yukawa value, RGE bridge, color-readout
   correction, or shared tadpole transport is claimed by this note. The
   accepted no-go row for `yt_color_projection_correction_note` remains
   compatible with this boundary because no `sqrt(8/9)` Yukawa correction
   is imported here.

4. **No blanket equality** is claimed across bare, Planck, and matching
   schemes; only the bare-surface statements (W1)-(W3), (T1) are
   identified.

---

## Changelog

- **2026-06-09** (science repair, author lane): restored the
  Ward-identity derivation as the load-bearing theorem of this row.
  Added Step 0 (lattice Noether / Schwinger-Dyson derivation of the
  exact point-split vector Ward identity (W1), iso-vector identity with
  exact breaking form (W2), and the Schur/commutant uniformity corollary
  (W3)); added dependency rows D18-D20. Rewrote the runner: new Blocks
  W1-W7 compute the Ward residual on explicit `(2,3,4)` Z^3 blocks with
  random SU(3) link backgrounds (machine zero), an exact-arithmetic
  sympy certificate (exact zero), and falsification legs (link-stripped
  current, η-mismatched current, split-mass breaking) where the residual
  is computed to be **nonzero**; singlet uniformity in Step 2 is now
  derived by a computed commutant (Block W7). Demoted every runner check
  that consumed the canonical-plaquette helper constants to log-only
  context (Blocks 9, 10, 12) so no PASS line rests on a helper-imported
  number. Runner: 58 PASS / 0 FAIL. Boundaries restated crisply as
  (B1)-(B4); claim-type author hint stays `bounded_theorem` with the
  staggered-Dirac realization gate (B1) as the expected bound.
- **2026-06-06 (historical):** dependency-registration attempt (C1 was then
  labeled Tier-A `AC_phi_lambda`; that label now supplies no premise; C2 →
  β–g_bare rescaling basis).
- **2026-05-25**: audit-prep refresh; claim narrowed to the
  matrix-element core; SM-map and tadpole transport moved outside the
  auditable boundary.
- **2026-04-17**: original note.
