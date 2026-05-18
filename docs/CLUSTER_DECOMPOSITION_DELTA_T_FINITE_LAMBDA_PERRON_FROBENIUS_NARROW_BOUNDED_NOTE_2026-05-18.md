# Cluster Decomposition `Δ_T > 0` Finite-Λ Perron-Frobenius Narrow Bounded Support Theorem

**Date:** 2026-05-18
**Claim type:** bounded_theorem
**Scope:** narrow bounded support theorem establishing `Δ_T > 0`
(strict transfer-matrix spectral gap above ground state) on **finite
spatial volume Λ ⊂ Z^3** for the canonical `Cl(3) ⊗ Z^3` staggered +
Wilson Hamiltonian, via Perron-Frobenius on the bosonic Wilson
transfer matrix composed with the framework's already-retained Leg A
fermion-determinant positivity (`det(D + m) > 0`). The theorem is
**finite-volume only**: the thermodynamic limit `Λ → Z^3`,
uniformity-in-`Λ` bounds, and the full Yang-Mills mass-gap statement
are **explicitly out of scope** and remain the named open work item
inherited from the Clay Millennium problem level.
**Status authority:** independent audit lane only. The
`bounded_theorem` label is a source-side claim-boundary declaration,
not an audit verdict.
**Primary runner:** [`scripts/frontier_cluster_decomposition_delta_t_finite_lambda_perron_frobenius_narrow_2026_05_18.py`](../scripts/frontier_cluster_decomposition_delta_t_finite_lambda_perron_frobenius_narrow_2026_05_18.py)
**Parent row:** [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)

## 0. Honest framing up front

The parent row's "Honest status (post-bridge-repair)" section lists
three candidate mechanisms for closing the open `Δ_T > 0` derivation
target on the canonical `Cl(3) ⊗ Z^3` staggered + Wilson Hamiltonian:

1. Strong-coupling expansion at `g_bare = 1` showing convergence with
   positive rate.
2. **Perron-Frobenius for the positive transfer matrix proving
   non-degeneracy of the top eigenvalue under canonical-surface
   boundary conditions.**
3. Structural confinement theorem on `A_min` giving `m_gap ≥ √σ`
   with `σ > 0` the string tension.

This note attacks **candidate 2 in its narrowest honest form**: a
strict spectral gap `Δ_T > 0` on **finite spatial volume Λ ⊂ Z^3**
via Perron-Frobenius. It does NOT extend to the thermodynamic limit
and does NOT claim the Yang-Mills mass gap.

**What's new in this note vs textbook Wilson lattice gauge theory:**
the composition of standard Perron-Frobenius (pure bosonic Wilson)
with the framework's already-retained Leg A fermion-determinant
positivity (from `STRONG_CP_THETA_ZERO_NOTE.md`) to extend the gap
result to the canonical staggered + Wilson Hamiltonian on finite Λ.
The textbook results for pure Wilson go back to Osterwalder-Seiler
1978; the framework-specific composition with Leg A fermion
positivity has not been packaged separately as a retained authority.

## 1. Statement

Let `Λ ⊂ Z^3` be a finite connected spatial sublattice with link set
`E(Λ)`. Let `β > 0` be the canonical Wilson gauge coupling. Let
`m > 0` be the staggered fermion mass on `Λ` (real positive,
satisfying the framework's canonical-normalization surface).

Let `H = H_W + H_F` be the canonical staggered + Wilson Hamiltonian
on `Λ`:

- `H_W` is the pure Wilson gauge Hamiltonian: `H_W = Σ_P (1 -
  (1/N_c) Re tr U_P)` with `N_c = 3` (the framework `Cl(3)` color)
  and `U_P` the plaquette holonomy.
- `H_F` is the staggered fermion Hamiltonian: `H_F = Σ_x ψ̄_x (D[U]
  + m) ψ_x` with `D[U]` the staggered Dirac operator and `ψ`
  Grassmann variables.

Let `T = exp(-a · H)` be the transfer matrix one time step (lattice
spacing `a > 0`), acting on the Hilbert space of gauge-invariant
states on `Λ`.

**Theorem (Δ_T > 0 finite-Λ).** The transfer matrix `T` has a
strictly positive spectral gap above its ground state:

```text
Δ_T(Λ)  :=  E_1(Λ) - E_0(Λ)  >  0                                       (1)
```

where `E_0(Λ) > -∞` is the ground state energy and `E_1(Λ)` is the
energy of the first excited state of `H` on `Λ`.

## 2. Proof

The proof is a four-step composition.

### Step 1 — Pure Wilson transfer matrix has non-negative matrix elements

In **temporal gauge** `U_0(x) = I`, the Wilson action splits into a
plaquette sum that factorizes timewise. The transfer matrix `T_W` in
the link-variable basis `{U_i(x) : i = 1, 2, 3, x ∈ Λ}` has
matrix elements

```text
<U'_i(x)| T_W |U_i(x)>  =  ∫ DU_0(x) exp(-S_W^{one-slab}[U_0, U_i, U'_i])  ≥  0      (2)
```

with `S_W^{one-slab}` real (since Wilson plaquettes are real CP-even).
The integrand `exp(-S_W)` is strictly positive, and the integral over
SU(N_c) is over a compact group with positive Haar measure. Hence
`<U'| T_W |U> ≥ 0` element-wise, with strict positivity for
configurations connected by a single time-step gauge transformation.

This is a standard result of lattice gauge theory (Osterwalder &
Seiler, "Gauge field theories on a lattice," *Annals of Phys.*
**110**, 440 (1978); Lüscher, *Comm. Math. Phys.* **54**, 283 (1977);
Seiler, "Gauge Theories as a Problem of Constructive Quantum Field
Theory and Statistical Mechanics," Lecture Notes in Phys. **159**,
Springer 1982).

### Step 2 — `T_W` is irreducible on finite connected Λ

A non-negative finite-dim matrix `M` is **irreducible** iff for every
pair `(i, j)` of basis indices there exists `n ≥ 0` such that
`(M^n)_{i j} > 0`. For `T_W` on a finite connected `Λ`, any two link
configurations can be connected by a sequence of single-link gauge
transformations (compact connected `SU(N_c)` is path-connected, and
the lattice graph is connected by hypothesis). Hence some power of
`T_W` connects every pair of basis configurations: `T_W` is
irreducible.

### Step 3 — Perron-Frobenius for irreducible non-negative `T_W`

The **Perron-Frobenius theorem** (Frobenius 1912; Perron 1907) for
irreducible non-negative finite-dim operators states:

> The top eigenvalue `λ_0 > 0` is **simple** (algebraic multiplicity
> one), strictly greater in absolute value than every other
> eigenvalue, and the corresponding eigenvector has strictly positive
> components in the basis where `T_W` is non-negative.

Applied to `T_W`: the top eigenvalue is non-degenerate, so

```text
λ_0(T_W)  >  λ_1(T_W) ≥ λ_2(T_W) ≥ ...                                  (3)
```

with strict inequality between `λ_0` and `λ_1`. The spectral gap is

```text
Δ_T(T_W)  =  -log(λ_1 / λ_0) / a  >  0                                   (4)
```

on finite `Λ`.

### Step 4 — Fermion-determinant positivity extends the gap to `T = T_W · T_F`

Integrating out staggered fermions on each time slab is exact (the
Grassmann integral is finite). The integrated transfer matrix
factorizes as

```text
T  =  T_W · T_F[U]                                                        (5)
```

where `T_F[U] = det(D[U] + m)` is the **fermion determinant** on the
spatial gauge configuration `U` at the time slab.

By the framework's already-retained **Leg A of strong CP closure**
(see `STRONG_CP_THETA_ZERO_NOTE.md` §"Leg A: Fermion phase closure",
audited_conditional row but Leg A itself is a closed-form algebraic
identity):

```text
det(D[U] + m)  =  Π_k (m^2 + λ_k^2[U])  >  0                              (6)
```

for every gauge configuration `U` and every real `m > 0`. Here
`λ_k[U]` are the eigenvalues of the anti-Hermitian staggered Dirac
operator `D[U]` on the configuration `U`; the determinant is a
**product of strictly positive real numbers** by the eigenvalue
pairing `±λ_k`.

Therefore `T_F[U] > 0` strictly for every `U`. Multiplying `T_W` by a
strictly positive (`U`-dependent) function preserves both
non-negativity (`T ≥ 0` element-wise) and irreducibility (the support
of `T` matches that of `T_W` up to the strictly positive `T_F`
factor). Hence Perron-Frobenius applies to `T = T_W · T_F` with the
same conclusion:

```text
λ_0(T) > λ_1(T) ≥ ...,    Δ_T(Λ) = -log(λ_1 / λ_0) / a > 0                (7)
```

on finite `Λ`. ∎

## 3. What this theorem closes

This theorem closes one **specific narrow** subtarget of the parent
row's open `Δ_T > 0` derivation:

> **Finite-Λ Δ_T > 0 on canonical `Cl(3) ⊗ Z^3` staggered + Wilson
> via Perron-Frobenius + Leg A fermion-determinant positivity.**

The parent row's bridge note (`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`,
`retained_bounded`) provides the gap-to-temporal-clustering bridge
**given** `Δ_T > 0`. This note supplies the `Δ_T > 0` **input** to
that bridge, on finite Λ.

Composing this note with the retained bridge gives a **closed
finite-Λ temporal clustering theorem** for the canonical staggered +
Wilson Hamiltonian (without further admitting `Δ_T > 0`).

## 4. What this theorem does NOT close

1. **Thermodynamic limit `Λ → Z^3`.** The gap may close in the
   limit. Uniform-in-`Λ` lower bounds on `Δ_T(Λ)` are not derived
   here; the standard Yang-Mills mass-gap question (Clay Millennium
   problem level) remains open.
2. **Mass-gap statement.** This theorem does NOT claim the
   thermodynamic-limit mass gap `m_gap > 0`. It only claims
   finite-Λ `Δ_T(Λ) > 0`.
3. **Spatial cluster decomposition.** The bridge note closes
   temporal clustering. The spatial cluster-decomposition statement
   still needs a separate spatial Lieb-Robinson argument or a
   spatial transfer-matrix gap; both remain open on the parent row.
4. **Strong-coupling expansion convergence** at `g_bare = 1` (parent
   row candidate 1).
5. **Structural confinement / `m_gap ≥ √σ`** (parent row candidate 3).
6. **Continuum limit `a → 0`.**

## 5. Cited dependencies

- **`STRONG_CP_THETA_ZERO_NOTE.md` Leg A** (currently
  `audited_conditional`) — supplies the algebraic identity
  `det(D + m) = Π_k (m^2 + λ_k^2) > 0` used in Step 4. The Leg A
  algebraic identity itself is closed-form; the broader
  `STRONG_CP_THETA_ZERO_NOTE` audit verdict's repair target is
  about action-surface selection, not about Leg A.
- **`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`**
  (currently `audited_conditional`, now `unaudited` after the
  2026-05-18 scope-narrowing in PR #1521) — parent row whose
  `Δ_T > 0` open admission this finite-Λ theorem partially
  supplies.
- **`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`**
  (`retained_bounded`) — gap-to-temporal-clustering bridge that
  composes with this note's finite-Λ gap.

### External textbook authorities (named non-derivation, not load-bearing on theorem strength)

- O. Perron, "Zur Theorie der Matrizen," *Math. Ann.* **64**, 248
  (1907).
- G. Frobenius, "Über Matrizen aus nicht negativen Elementen,"
  *Sitzungsber. Preuss. Akad. Wiss. Berlin*, 456 (1912).
- K. Wilson, "Confinement of Quarks," *Phys. Rev. D* **10**, 2445
  (1974).
- K. Osterwalder & E. Seiler, "Gauge field theories on a lattice,"
  *Annals of Phys.* **110**, 440 (1978).
- M. Lüscher, *Comm. Math. Phys.* **54**, 283 (1977).
- E. Seiler, "Gauge Theories as a Problem of Constructive Quantum
  Field Theory and Statistical Mechanics," Lecture Notes in Phys.
  **159**, Springer (1982).

The framework-specific contribution is the composition of these
textbook results with the framework's Leg A fermion-determinant
positivity (which depends on the framework's canonical staggered
Dirac construction).

## 6. Forbidden imports check

- No external numerical targets consumed.
- No literature numerical comparisons consumed.
- No fitted selectors consumed.
- No unit-convention imports load-bearing on theorem strength.
- No new framework axioms (per `feedback_no_new_axioms.md`).
- No new repo vocabulary (per `feedback_no_new_repo_vocabulary.md`).
- No claim of thermodynamic-limit mass gap.
- No claim of Yang-Mills mass gap or Clay Millennium-level closure.

## 7. Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_cluster_decomposition_delta_t_finite_lambda_perron_frobenius_narrow_2026_05_18.py
```

Expected runner output: `PASS=N`, `FAIL=0`, where `N` is the count
of Perron-Frobenius verification checks on explicit small transfer
matrices.

## 8. Honest narrowest status

**Bounded support — finite-Λ Δ_T > 0 via Perron-Frobenius + Leg A.**

This theorem:
- Closes one narrow finite-Λ subtarget of the parent row's `Δ_T > 0`
  open admission.
- Does NOT close the thermodynamic-limit mass gap.
- Does NOT promote `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE`
  to retained — the parent row's spatial cluster-decomposition step
  and Λ → ∞ uniformity remain open.
- Does NOT close strong CP, Yang-Mills mass gap, or any continuum
  statement.

The parent row's `Δ_T > 0` admission can be cited as "`Δ_T > 0`
retained on finite Λ via this note" once independent audit
ratifies, instead of "admitted." Composing with the retained bridge
note gives finite-Λ temporal clustering as a closed statement.
