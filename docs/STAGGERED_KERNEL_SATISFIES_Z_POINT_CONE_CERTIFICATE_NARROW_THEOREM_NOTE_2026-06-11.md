# Staggered Kernel Satisfies (Z) — Point-Like Isotropic Linear-Cone Zero-Set Certificate for the Flux-(−1) Realized Kernel, with the Companion (Z)-Violation Certificate for the Flux-(+1) Kernel (Narrow Theorem)

**Date:** 2026-06-11
**Type:** positive_theorem
**Claim type:** positive_theorem
**Scope note:** narrow finite/exact computation on two constructed
kernels; no flux selection, no thermal content.
**Claim scope:** On the `Z³` nearest-neighbor one-particle hopping
surface (axiom adjacency + retained Fock bridge), the flux-`(−1)`
Kawamoto-Smit realized kernel `h_K1` satisfies hypothesis (Z) of the
fermionic Stefan-Boltzmann theorem FSB-K **exactly**: (Z-i) its
massless set is finite and equal to the 8 Brillouin-zone corner points
`{0, π}³` — constant in volume (eigensolver kernel dimensions
`8, 8, 8` at `L = 4, 8, 12`; exact at all volumes by the symbolic
Bloch identity `H(κ)² = 4 Σ_μ cos²(κ_μ/2) · I₈`, equivalently band
family `±2√(Σ_μ sin² q_μ)`); (Z-ii) every corner branch carries the
SAME exact cone `|E(p_j + q)| = |V q| + O(|q|²)` with `V = 2·I₃`
(exact: `sin²(c + q) = sin² q` for `c ∈ {0, π}`), with explicit
quantitative cone data `(V, C_j, r_j) = (2I, 2/3, 1)` proven by an
elementary inequality chain; (Z-iii) `V` is invertible and isotropic
(`det V = 8`, `σ_min = 2`; directional speeds all `= 2`). Cone
weights: `|det V_j| = 8` per corner branch in the unit-hopping
normalization, cone-weight sum `Σ_j |det V_j|⁻¹ = 1` per site
(= 8 species per `2³` cell, speed 2); in the staggered
central-difference normalization `h/2` (the retained det-positivity
row's Euclidean operator at `U = 1`), `V_j = I₃`, `|det V_j| = 1`, and
`Σ |det V|⁻¹ = 8` per cell (speed 1) — the two conventions tied by the
exact `λ³` covariance, with the convention-invariant datum the species
count 8. **Companion negative fact (re-derived self-contained, needed
by the downstream consumer):** the flux-`(+1)` kernel `h_K0` VIOLATES
(Z) in both clauses — zero-mode counts `20/68/140` at `L = 4/8/12`
(the extensive lattice trace of the codim-1 surface
`Σ_μ cos p_μ = 0`); the EXACT one-parameter zero line
`p(t) = (π/2 + t, π/2 − t, π/2)` kills finiteness on any neighborhood;
and every candidate cone matrix is forced singular along the zero-line
direction (tangent speed exactly 0, normal speed `2√3`). The
certificate machinery is quantitative and branch-sensitive
(falsification legs: a weighted kernel detects `V = diag(2,2,1)` and
still passes with a different weight sum; a broken-cone kernel and a
quadratic point-zero comparator are rejected with singular-`V`
detection). This note **performs no selection** of the flux bit and
carries **no thermal content**: it is pure kernel geometry for the
named downstream composer.
**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome; audit verdict and effective
status are set only by the independent audit lane.
**Primary runner:** [`scripts/staggered_kernel_z_certificate_check_2026_06_11.py`](../scripts/staggered_kernel_z_certificate_check_2026_06_11.py)
**Cache:** [`logs/runner-cache/staggered_kernel_z_certificate_check_2026_06_11.txt`](../logs/runner-cache/staggered_kernel_z_certificate_check_2026_06_11.txt)
(`TOTAL: PASS=18 FAIL=0`, deterministic, runtime well under one
minute)
**Authority role:** source-note proposal supplying the kernel-geometry
certificate that FSB-K's boundary B-3 names as the missing external
input ("which kernel satisfies (Z) is a separate, external, computable
kernel-geometry fact, not certified here"). It changes no existing
row's status and decides no branch fact.

## 0. Changelog

- **2026-06-11.** First version. Written as the first of the two
  closing notes of the P-FLUX supply line: the finite-species-density
  no-go (2026-06-10) pinned the missing B-Z2 supplier to a retained
  SB row binding the realized kernel; the FSB-K re-scope (2026-06-11)
  produced that row conditionally on hypothesis (Z) and declared the
  (Z)-status of the realized kernel an external computable fact
  (its boundary B-3). This note computes that fact, both ways, with
  exact cone data.

## 1. Question and method

**Question.** Theorem FSB-K holds for every realized-class kinetic
kernel satisfying hypothesis (Z): finite massless set, each branch a
linear cone `|E_b(p_j + q)| = |V_jb q| + O(|q|²)` with invertible
`V_jb`. Its boundary B-3 deliberately leaves open which kernels
satisfy (Z). On the licensed two-flux-class surface (`K0` = uniform
plaquette flux `+1`, scalar tight-binding; `K1` = uniform flux `−1`,
Kawamoto-Smit class): does the `K1` realized kernel satisfy (Z), with
what exact cone data — and does the `K0` kernel violate it?

**Method.** Pure finite/exact computation on the two constructed
kernels (derivations over admissions): construct both representatives
self-contained from the axioms' adjacency; obtain the all-volume band
closed form by an exact symbolic Bloch identity (8×8, symbolic
momentum and symbolic direction-3 weight); certify each clause of (Z)
separately and exactly (sympy identities for the zero set and the cone
function; an elementary inequality chain for the explicit
`(V, C_j, r_j)`); re-derive the companion `K0` violation in the same
machinery; then attack the machinery itself with perturbed kernels
(singular-`V` detection; quantitative weight tracking). No flux value,
branch label, count, species name, or thermal probe enters any
certificate; the two licensed branches are separated only by their
computed geometry.

## 2. Setup and statements

**Surface and kernels.** Sites `Z³` (periodic `L³` boxes for
eigensolves), one mode per site on the retained finite periodic Fock
surface. `h_K0` = scalar NN hopping (`t ≡ 1`); `h_K1` = Kawamoto-Smit
NN hopping (`t_1 = 1, t_2 = (−1)^{x₁}, t_3 = (−1)^{x₁+x₂}`). Both
Hermitian; uniform plaquette flux `+1` / `−1` respectively (runner
check 1) — the two licensed class representatives, re-derived
self-contained. Two normalizations are declared (boundary B-Z-N): the
unit-hopping kernel `h` and the staggered central-difference kernel
`h/2` (same kernel at scale `λ = 1/2`; `|spec(iD_E)| = |spec(h_K1)|/2`,
check 4).

**Hypothesis (Z) (restated self-contained; definition text matches the
FSB-K note, check 10).** The massless set
`Z(h) = {(p_j, b) : E_b(p_j) = 0}` is finite, and for each branch
there are an invertible real `3×3` matrix `V_jb`, a radius `r_j > 0`,
and `C_j < ∞` with `| |E_b(p_j + q)| − |V_jb q| | ≤ C_j |q|²` for
`|q| ≤ r_j`.

### 2.1 Theorem Z-K1 (the K1 kernel satisfies (Z) exactly)

**The Kawamoto-Smit kernel `h_K1` satisfies (Z) with the following
exact data.**

1. **(All-volume closed form.)** The 8×8 Bloch symbol obeys
   `H(κ)² = 4 Σ_μ cos²(κ_μ/2) · I₈` identically (exact symbolic
   identity, proven with the direction-3 weight `c` symbolic:
   `H_c(κ)² = 4(cos²(κ₁/2) + cos²(κ₂/2) + c² cos²(κ₃/2)) I₈`); hence
   the band family is `±2√(Σ_μ sin² q_μ)`, `q_μ = (π − κ_μ)/2`, at
   every volume. (Check 2; eigensolver tie at `L = 4, 8`, check 3.)
2. **(Z-i.)** `E = 0` iff `sin p_μ = 0` for all `μ` iff
   `p ∈ {0, π}³`: the massless set is exactly the 8 BZ corner points.
   Kernel dimensions `8, 8, 8` at `L = 4, 8, 12` (PBC, `4 | L`;
   boundary B-Z-L). (Check 5.)
3. **(Z-ii.)** `sin²(c + q) = sin² q` for `c ∈ {0, π}`, so every
   corner carries the SAME exact cone function
   `E(p_j + q) = 2√(Σ sin² q_μ)`, with
   `E²/4 = |q|² − (1/3)Σ q_μ⁴ + O(q⁶)`: the cone term is exactly
   `|2I q|`, i.e. `V_j = 2·I₃` at every corner. Quantitatively,
   `| |E(p_j + q)| − |2Iq| | ≤ (2/3)|q|³ ≤ (2/3)|q|²` for `|q| ≤ 1`:
   the data `(V, C_j, r_j) = (2I, 2/3, 1)` witness (Z-ii) explicitly.
   (Checks 6-7; proof in §2.3.)
4. **(Z-iii.)** `det V = 8 ≠ 0`, `σ_min(V) = 2`; the cone is
   isotropic (directional speeds all `= 2`). (Check 8.)
5. **(Cone weights.)** Unit hopping: `Σ_j |det V_j|⁻¹ = 8 × 1/8 = 1`
   per site (8 species per `2³` cell at speed 2). Central-difference
   normalization `h/2`: `V_j = I₃`, `|det V_j| = 1`,
   `Σ |det V|⁻¹ = 8` per cell (speed 1). Exact `λ³` covariance
   `det(λV)⁻¹ = λ⁻³ det(V)⁻¹`; the invariant is the count 8.
   (Check 9.) ∎

### 2.2 Theorem Z-K0 (the K0 kernel violates (Z), both clauses)

**(i)** The massless set of `h_K0` is the codim-1 surface
`Σ_μ cos p_μ = 0`: lattice-trace counts `20, 68, 140` at
`L = 4, 8, 12` (growth exponent `1.78`), and the EXACT zero line
`p(t) = (π/2 + t, π/2 − t, π/2)` (identity
`cos(π/2+t) + cos(π/2−t) + cos(π/2) = 0` for all `t`) makes the zero
set uncountable in every neighborhood of `(π/2, π/2, π/2)` — (Z-i)
fails. **(ii)** Along the zero-line direction `u`, the cone inequality
`|E(p₀ + tu)| ≥ |Vu|t − Ct²` with `E(p₀ + tu) = 0` forces `Vu = 0`:
every candidate cone matrix is singular — (Z-ii)/(Z-iii) fail.
Measured: tangent speed exactly `0`, normal speed `2√3`. ∎
(Checks 11-13.)

### 2.3 Proof of the quantitative cone bound (Theorem Z-K1, item 3)

For `|q| ≤ 1`: (a) `sin² x ≤ x²` always; (b) `sin x ≥ x − x³/6 ≥ 0`
on `[0, 1]` (alternating Taylor bound; scanned with margin in check
7), so `sin² x ≥ (x − x³/6)² ≥ x² − x⁴/3`; (c)
`Σ q_μ⁴ ≤ (Σ q_μ²)² = |q|⁴` exactly (the difference is
`2 Σ_{μ<ν} q_μ² q_ν² ≥ 0`). Hence
`0 ≤ |q|² − Σ sin² q_μ ≤ |q|⁴/3`, and with
`√a − √b = (a − b)/(√a + √b)` and `√a = |q|`:
`0 ≤ 2|q| − E(p_j + q) ≤ 2(|q|⁴/3)/|q| = (2/3)|q|³ ≤ (2/3)|q|²`.
The measured worst sampled deviation ratio is `1/3` (the axis
direction), inside the bound. ∎

## 3. Boundaries (stated up front)

| ID | Boundary | Where it bites |
|---|---|---|
| B-Z-L | Finite-`L` sampling is wrap-convention data: the PBC kernel realizes the 8 corner zeros iff `4 | L` (certified at `L = 4, 8, 12`; e.g. `L = 6` PBC has empty kernel — the same B-H wrap class as the kinetic-class note). The (Z) statement itself is about the Bloch band family on the Brillouin torus, exact at all volumes by the symbolic identity | checks 2, 5 |
| B-Z-N | Two normalizations declared (unit-hopping `h`; central-difference `h/2`); all cone data stated in both, tied by exact `λ³` covariance; neither claimed canonical | checks 4, 9 |
| B-Z-D | The FSB-K note is consumed for its DEFINITION text of (Z) only (string-matched, check 10); no theorem content and no grade is drawn from it — this certificate stands as kernel geometry whether or not FSB-K retains | check 10 |
| B-Z-S | No selection: which kernel is realized (the P-FLUX bit) is neither assumed nor decided; the K0 violation is companion content for the named downstream composer | check 14 |
| B-Z-W | The falsification witnesses (`K1(c=1/2)`, `K1(c=0)`, quadratic comparator) are declared OFF the licensed two-class surface (anisotropic amplitude / on-site sector); they exercise the machinery only | checks 15-17 |

## 4. Cited authorities (one hop, with license statements)

Load-bearing (markdown links):

1. [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) —
   axiom premise node. License used: Lattice (`Z³`, translations, NN
   cubic adjacency) for the kernel constructions and the plaquette
   set; Quantum (per-site qubit) for the one-mode-per-site reading.
   No dynamics drawn.
2. [`TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md)
   — retained. License used: the finite periodic Fock surface whose
   one-particle blocks the computed matrices are; nothing else.

Plain-text pointers (NOT load-bearing):

- `AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md`
  (unaudited) — names and defines hypothesis (Z) and declares its
  boundary B-3 (the (Z)-status of the realized kernel is an external
  computable fact). Only the DEFINITION text of (Z) is consumed
  (string-matched in check 10; boundary B-Z-D); no theorem content,
  no grade. This note is written to be exactly the external
  certificate B-3 names.
- `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`
  (unaudited) — declares the licensed two-class surface and B-BIT;
  both representatives and their flux certificates are re-derived
  self-contained in runner check 1, so nothing is drawn from it.
- `STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md` (retained)
  — its Euclidean staggered operator `M_KS` at `U = 1` is the
  central-difference normalization tied in check 4; the tie is a
  multiset equality computed here, not a license drawn from that row.
- `P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md`
  (unaudited) — context: its §7/N6 pins the missing B-Z2 supplier
  whose (Z) leg this note computes; nothing from it is load-bearing.
- `U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md`
  (currently `audited_renaming`) — the single-mode-per-site framing;
  deliberately NOT load-bearing here (the constructions consume only
  the axiom adjacency and the retained Fock bridge).
- `INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md`
  (unaudited) — the turn-1 inversion guards; nothing here consumes a
  matched-3=3 count (no count 3 appears in any certificate; guard
  compliance is certified in the downstream composer, which performs
  the composition).

Forbidden imports: no PDG values, no lattice-MC values, no fitted
coefficients, no species names, no flux or branch input to any
certificate, no new axioms.

## 5. No selection, no thermal content

This note computes kernel geometry only. It performs no selection of
the flux bit, consumes no thermal probe (`g_eff`, `u(T)`, and the SB
currency appear nowhere in the runner), and asserts nothing about
which kernel is realized. The (Z)-decision machinery never reads the
flux certificates (runner check 18). The downstream composer
(`P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md`)
is the only place where this certificate meets FSB-K's conclusion.

## 6. What the runner computes

[`scripts/staggered_kernel_z_certificate_check_2026_06_11.py`](../scripts/staggered_kernel_z_certificate_check_2026_06_11.py)
— deterministic, no network, no randomness; numpy + sympy; runtime
well under one minute. 18 checks in four sections:

- **[A]** (4 checks) both representatives constructed; Hermiticity +
  uniform flux `±1` over all 192 plaquettes at `L = 4`; the exact
  symbolic Bloch identity
  `H_c(κ)² = 4(cos²(κ₁/2) + cos²(κ₂/2) + c² cos²(κ₃/2)) I₈`
  (symbolic `κ` AND symbolic weight `c`) giving the all-volume band
  closed form; Bloch-decomposition/eigensolver multiset tie at
  `L = 4, 8` (`c = 1` and `c = 1/2`) plus the K0 closed form; the
  central-difference normalization tie
  `|spec(iD_E)| = |spec(h_K1)|/2`.
- **[B]** (6 checks) hypothesis (Z) clause by clause: zero set
  `= {0, π}³` exactly (sympy solveset) with kernel dims `(8, 8, 8)` at
  `L = 4, 8, 12` and symbol-grid count 8 at `L = 128`; the exact cone
  identity at all 8 corners with series
  `E²/4 = |q|² − (1/3)Σq_μ⁴ + O(q⁶)` (so `V_j = 2I` exactly); the
  quantitative `(V, C_j, r_j) = (2I, 2/3, 1)` bound (inequality chain
  + measured worst ratio `1/3`); invertibility/isotropy
  (`det V = 8`, `σ_min = 2`, directional speeds `2.000000` at two
  corners along axis/face/body/skew directions); the cone weights in
  both normalizations with the exact `λ³` covariance; the (Z)
  definition-text match against the FSB-K note.
- **[C]** (4 checks) the companion negative fact: K0 zero counts
  `(20, 68, 140)` = symbol-surface lattice trace, growth exponent
  `1.78`; the EXACT zero line (sympy identity); singular-`V` forcing
  with measured tangent speed `0` and normal speed `2√3 = 3.4641`;
  the own-file discipline strings (no selection, no thermal content,
  status authority).
- **[D]** (4 checks) falsification legs: `K1(c = 1/2)`
  passes (Z) with detector `V = diag(2, 2, 1)` and weight sum 2 (the
  machinery is quantitative); `K1(c = 0)` is rejected with singular-`V`
  detection AND extended zero set `(16, 32) = 4L`; the quadratic
  comparator is point-like `(1, 1, 1)` yet `V = 0` singular (the
  clauses are detected independently); the (Z)-decision over all five
  witnesses is `{pass, pass, fail, fail, fail}` through one code path
  with no flux label consumed.

Five `RESIDUAL (declared-open): ...` lines mark boundaries B-Z-L,
B-Z-N, B-Z-S, B-Z-W (and the definition-only consumption B-Z-D inside
check 10's message) at the points where they are load-bearing.

Runner check classes per the audit rubric: checks 1-9, 11-13, 15-18
are class (A)/(C) (exact symbolic identities and algebraic/spectral
computations on constructed finite objects); checks 10 and 14 conjoin
class (B) components (cross-note/own-note text verification) with
class (A) content.

## 7. What this does NOT close

- **The P-FLUX bit.** No selection is performed or implied. This row
  certifies geometry of both constructed kernels; composing it with
  FSB-K's conclusion is the downstream composer's job, conditional on
  that chain's grades.
- **FSB-K itself.** Nothing here audits, grades, or consumes FSB-K's
  theorem; only its (Z) definition text is matched (B-Z-D).
- Wrap-convention classification beyond `4 | L` PBC (B-Z-L).
- Whether either normalization is canonical (B-Z-N).
- Nothing here changes any existing row's status.

## 8. What this supports (downstream citable text)

- The FSB-K note's boundary B-3 can cite this row as: "the
  kernel-geometry fact is computed: the flux-`(−1)` Kawamoto-Smit
  realized kernel satisfies (Z) exactly with
  `(V, C, r) = (2I, 2/3, 1)` at all 8 corner branches and cone-weight
  sum 1 per site (8 per cell in the central-difference normalization);
  the flux-`(+1)` kernel violates both clauses
  (`staggered_kernel_satisfies_z_point_cone_certificate_narrow_theorem_note_2026-06-11`,
  Theorems Z-K1/Z-K0)."
- The P-FLUX composer consumes Z-K1 and Z-K0 as the (Z)-leg of the
  conditional selection chain.
- The exact zero-line identity and the singular-`V` forcing argument
  are reusable against any future claim that the K0 zero set is
  point-like or conical.

## 9. Command

```bash
python3 scripts/staggered_kernel_z_certificate_check_2026_06_11.py
```

Expected output (deterministic, byte-for-byte):

```text
========================================================================
[A] the two licensed representatives re-derived; the exact
    symbolic Bloch closed form (all volumes); eigensolver tie
========================================================================
[PASS]  1. [A] both representatives Hermitian; frame-invariant uniform plaquette flux over all 192 plaquettes at L=4: K0 phi=+1, K1 phi=-1 -- the two-class surface re-derived self-contained (no kinetic-class-note import)
[PASS]  2. [A] exact symbolic Bloch identity (symbolic kappa AND symbolic direction-3 weight c): H_c(kappa)^2 = 4(cos^2(k1/2) + cos^2(k2/2) + c^2 cos^2(k3/2)) I_8 -- at c = 1 the band family is +-2 sqrt(sum_mu sin^2 q_mu), q_mu = (pi - kappa_mu)/2, on the reduced Brillouin torus at ALL volumes (the all-L closed-form license)
[PASS]  3. [A] Bloch decomposition tied to the explicit lattice eigensolver at L = 4, 8 (multiset equality, c = 1 and c = 1/2), and the K0 closed form 2 sum_mu cos p_mu tied likewise -- the symbol evaluations below ARE realized lattice-kernel spectra
[PASS]  4. [A] normalization tie: the staggered central-difference Euclidean operator D_E (the retained det-positivity row's M_KS at U = 1) has |spec(i D_E)| = |spec(h_K1)| / 2 (multiset, L = 4) -- the two declared normalizations are the SAME kernel at scale lambda = 1/2, and cone data transforms exactly as V -> lambda V

========================================================================
[B] hypothesis (Z) certified for the K1 kernel, clause by
    clause, with exact cone data
========================================================================
[PASS]  5. [B] (Z-i) the massless set is FINITE and exactly the 8 BZ corner points: E = 2 sqrt(sum sin^2 p_mu) = 0 iff every sin p_mu = 0 iff p_mu in {0, pi} (sympy solveset on [0, 2pi)) => |Z(h)| = 2^3 = 8; eigensolver kernel dims (8, 8, 8) at L = 4, 8, 12, L-CONSTANT; symbol-grid zero count at L = 128 is 8
[PASS]  6. [B] (Z-ii) the cone is EXACT and the same at every corner: sin^2(c + q) = sin^2 q for c in {0, pi} (sympy), so E(p_j + q) = 2 sqrt(sum sin^2 q_mu) identically at all 8 corners; series E^2/4 = |q|^2 - (1/3) sum q_mu^4 + O(q^6) (sympy) => the cone term is exactly |2 I q|: V_j = 2 I_3 for every corner branch
[PASS]  7. [B] (Z-ii) quantitative cone data (V, C_j, r_j) = (2I, 2/3, 1): | |E(p_j+q)| - |2Iq| | <= (2/3)|q|^3 <= (2/3)|q|^2 for |q| <= 1 -- chain: sin^2 x <= x^2; sin x >= x - x^3/6 >= 0 on [0,1] (scan min 0.0e+00 >= 0); sum q^4 <= |q|^4 (exact: difference = 2 sum_(mu<nu) q_mu^2 q_nu^2); sqrt(a) - sqrt(b) = (a-b)/(sqrt a + sqrt b); measured worst deviation ratio 0.3333 <= 2/3
[PASS]  8. [B] (Z-iii) V_j = 2I is invertible and isotropic: det V = 8 != 0, sigma_min = 2; measured directional speeds at corners (0,0,0) and (pi,pi,pi) along axis/face-diagonal/body-diagonal/skew = 2.000000 (spread 2.2e-13) -- hypothesis (Z) holds for the K1 kernel with explicit data
[PASS]  9. [B] cone weights, both declared normalizations: unit hopping |det V_j| = 8 per corner branch, sum |det V|^-1 = 8 x 1/8 = 1 per site (= 8 species per 2^3 cell, speed 2); central-difference h/2: V_j = I_3, |det V_j| = 1, sum |det V|^-1 = 8 per cell (speed 1) -- tied by the exact lambda^3 covariance det(lambda V)^-1 = lambda^-3 det(V)^-1; the convention-invariant datum is the count 8
[PASS] 10. [B] definition match (textual): the (Z) certified above is FSB-K's own hypothesis -- the FSB note's defining text ('Hypothesis (Z) (point-like linear-cone zero set)', zero set 'is finite, and for each' branch an 'invertible real `3x3` matrix' V with the 'C_j |q|^2' bound) is exactly what checks 5-8 instantiate as (V, C_j, r_j) = (2I, 2/3, 1); only the DEFINITION text is consumed -- no theorem content, no grade
RESIDUAL (declared-open): finite-L sampling is wrap-convention data: the PBC kernel realizes the 8 corner zeros iff 4 | L (certified at L = 4, 8, 12); the (Z) statement itself is about the Bloch band family on the Brillouin torus, exact at all volumes by the symbolic identity of check 2 (boundary B-Z-L)
RESIDUAL (declared-open): two normalizations are declared (unit-hopping h and central-difference h/2); all cone data is stated in both and tied by exact scale covariance; neither is claimed canonical (boundary B-Z-N)

========================================================================
[C] the companion negative fact: the K0 kernel VIOLATES (Z)
    (both clauses, exactly)
========================================================================
[PASS] 11. [C] (Z-i) FAILS for K0: zero-mode counts (20, 68, 140) at L = 4, 8, 12 = the lattice trace of the codim-1 symbol surface sum_mu cos p_mu = 0, growth exponent 1.78 -- extensive, not finite, not L-constant
[PASS] 12. [C] (Z-i) fails EXACTLY: p(t) = (pi/2 + t, pi/2 - t, pi/2) is a one-parameter zero LINE of the K0 symbol for ALL t (sympy: cos(pi/2+t) + cos(pi/2-t) + cos(pi/2) = 0 identically) -- the zero set is uncountable in every neighborhood of (pi/2, pi/2, pi/2); no finite zero set exists
[PASS] 13. [C] (Z-ii) fails: along the zero-line direction u the cone inequality |E(p0+tu)| >= |Vu| t - C t^2 forces |Vu| <= C t -> 0, i.e. V u = 0: ANY candidate cone matrix is singular; measured tangent speed 3.7e-10 (= 0 exactly by the check-12 identity), normal speed 3.4641 = 2 sqrt(3) -- a maximally degenerate non-cone
[PASS] 14. [C] discipline (textual, on this note's own file): the K0 violation is a computed companion fact for the downstream consumer -- this note 'performs no selection', carries 'no thermal content', and declares status authority 'independent audit lane only'; both branches pass through the same machinery with the same tolerances
RESIDUAL (declared-open): the K0 violation certificate is companion content for the named downstream composer; which kernel is realized (the P-FLUX bit) is neither assumed nor decided here (boundary B-Z-S)

========================================================================
[D] falsification legs: the certificate machinery is
    quantitative and branch-sensitive, not vacuous
========================================================================
[PASS] 15. [D] weighted witness K1(c=1/2) (off the two-class surface -- anisotropic amplitude -- but inside FSB-K's realized class): zero set still 8 points (counts 8, 8 at L = 4, 8), detector V = diag(2.0000, 2.0000, 1.0000), det = 4: (Z) still HOLDS but with weight sum 8/4 = 2 != 1 -- the machinery tracks cone data quantitatively, it is not a rubber stamp
[PASS] 16. [D] broken-cone witness K1(c=0): the detector reports V = diag(2.0000, 2.0000, 0.0e+00) SINGULAR (axis-3 speed 0), and the zero set goes extended (16, 32 = 4L at L = 4, 8) -- singular-V detection works on a perturbed kernel
[PASS] 17. [D] quadratic comparator (scalar NN + on-site -6, off-surface): POINT-LIKE zero set (1, 1, 1) yet all directional speeds < 1e-5 => V = 0 singular -- the two (Z) clauses are detected independently (point-likeness alone does not pass)
[PASS] 18. [D] non-vacuity of the decision: the (Z) machinery over {K1, K1(c=1/2), K0, K1(c=0), comparator} returns {pass, pass, fail, fail, fail} from computed zero counts and cone speeds ONLY, through one code path -- the flux certificates of check 1 are never read by the decision; no flux label, branch label, count-3, or species input enters it
RESIDUAL (declared-open): the falsification witnesses K1(c=1/2), K1(c=0), and the comparator are declared OFF the licensed two-class surface (anisotropic amplitude / on-site sector); they exercise the machinery, they are not surface members (boundary B-Z-W)

TOTAL: PASS=18 FAIL=0
VERDICT: the flux-(-1) Kawamoto-Smit realized kernel satisfies hypothesis (Z) of FSB-K EXACTLY: massless set
         = the 8 BZ corner points (L-constant, eigensolver-certified at L = 4, 8, 12; exact by the
         all-volume symbolic Bloch identity), one exact isotropic cone V = 2I at every corner (V = I in the
         central-difference normalization), explicit (V, C, r) = (2I, 2/3, 1), cone-weight sum = 1 per site
         = 8 species per 2^3 cell. The flux-(+1) kernel VIOLATES both clauses of (Z): extensive zero set
         20/68/140 with an EXACT zero line, and every candidate cone matrix singular along it. The machinery
         is quantitative and branch-sensitive (falsification legs); no selection is performed and no
         thermal content is consumed: this row only certifies kernel geometry for the named downstream
         composer.
```

Exit code 0 iff `FAIL=0`.

## 10. Honest status

```yaml
claim_type_author_hint: positive_theorem
claim_scope: "On the Z^3 NN one-particle hopping surface (axiom adjacency + retained Fock bridge), the flux-(-1) Kawamoto-Smit realized kernel satisfies hypothesis (Z) of FSB-K exactly: massless set = the 8 BZ corner points {0,pi}^3 (kernel dims 8,8,8 at L=4,8,12; all-volume by the exact symbolic Bloch identity H(kappa)^2 = 4 sum cos^2(kappa/2) I_8); every corner branch carries the same exact isotropic cone V = 2I (V = I in the central-difference normalization h/2) with explicit data (V, C, r) = (2I, 2/3, 1) proven by an elementary inequality chain; det V = 8 != 0; cone-weight sum = 1 per site = 8 species per 2^3 cell (= 8 per cell at speed 1), tied across normalizations by exact lambda^3 covariance. Companion negative fact: the flux-(+1) kernel violates (Z) in both clauses (zero counts 20/68/140 at L=4/8/12; an EXACT zero line p(t) = (pi/2+t, pi/2-t, pi/2); every candidate cone matrix singular along it, tangent speed exactly 0, normal speed 2 sqrt(3)). Falsification: the machinery detects V = diag(2,2,1) on a weighted kernel (passes with weight sum 2), singular V on a broken-cone kernel and on a quadratic point-zero comparator -- quantitative and branch-sensitive. Bounded by: PBC corner sampling iff 4|L (wrap convention); declared dual normalization; (Z) consumed as definition text only; no selection, no thermal content."
upstream_dependencies:
  - minimal_axioms
  - tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25
admitted_context_inputs: []
source_sets_audit_outcome: false
```

This note decides no branch fact: both licensed kernels pass through
the same machinery and are separated only by their computed zero-set
geometry. The flux bit `φ` is neither assumed nor derived.
