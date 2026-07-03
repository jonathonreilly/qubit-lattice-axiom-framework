# Theta Supplier: Flavored-Grading Spectral Flow Registers the Winding Integer on the 2D Staggered Surface

**Date:** 2026-07-02
**Primary runner:** `python3 scripts/theta_supplier_flavored_grading_spectral_flow_2026_07_02.py`
**Type:** bounded_theorem
**Claim type:** bounded_theorem (finite 2D flavored-grading spectral-flow registration theorem)
**Scope boundary:** Finite even-L 2D U(1) staggered surfaces and the tested flux/deformation family only; no 4D carrier, no SU(3) extension, no continuum limit, no physical theta value, and no record/readout-chain identification.
**Audit boundary:** Independent audit lane only. This note proposes a bounded theorem row; `audit_status` and `effective_status` remain pipeline/auditor-owned.

## Claim

> This is an exact finite-dimensional narrow theorem plus a machine-verified registration result on the 2D even-L periodic staggered surface with U(1) links. The flavored grading Gamma_f = i eta_2 (C_1 C_2 + C_2 C_1)/2 built from gauge-covariant symmetric shifts is Hermitian (the i prefactor is forced by eta_2 C_1 = -C_1 eta_2), commutes with the site parity eps, and has free-field symbol cos p_1 cos p_2 times the taste-singlet chirality with {Gamma_f, D} = 0 exactly at U = 1. The Hermitian family H(m) = eps D - m Gamma_f obeys the exact conjugation antisymmetry eps H(m) eps = -H(-m), so the spectral asymmetry flow(m) = N_neg(H(+m)) - N_neg(H(-m)) is an index-type functional. On uniform-flux backgrounds of total flux 2 pi Q the flow equals -2Q, plateau-constant in m, size-stable at L = 8 and L = 12, invariant under gauge transformation and under non-gauge link deformation preserving the total flux, while the identical flow slot returns 0 for the fixed grading eps and for the taste-nonsinglet dressing Gamma_w. This realizes, on the framework surface, the existence of a (P1'-sharpened)-class supplier: a state-independent gauge-covariant grading whose graded spectral functional is not background-blind and reproduces the winding integer. Scope: existence on the tested finite 2D family; the note supplies no 4D carrier, no SU(3) extension, no continuum limit, and neither side's physical theta value.

## Context

The Tier-A row `strong_cp_theta_zero_note` decomposes the target account into a gauge-side winding account and a mass-side orientation-determinant readout. This note feeds the gauge-side winding account. The in-flight bridge `THETA_BAR_ASSEMBLY_INTERFACE_BRIDGE_2026-07-01` names the residual wall `W_anomaly_covariant_assembly`.

The sibling fixed-grading reduction `THETA_ASSEMBLY_PAIRED_SHIFT_FIXED_GRADING_MCKEAN_SINGER_REDUCTION_NARROW_THEOREM_NOTE_2026-07-02` is in flight in PR #4841. Its rigidity lemma pins `Tr(eps exp(t D^2)) = tr(eps)` as background-blind, and its corollary pushes any nontrivial assembly transfer to a `(P1'-sharpened)-class` supplier. This note constructs exactly such a supplier on the same surface where the fixed grading is provably blind.

The dependency row `abj_residual_gw_not_necessary_narrow_theorem_note_2026-05-28` is represented by [ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md](ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md). Its `effective_status` is `retained_bounded`; its `claim_scope` is: "Audited only the bounded internal correction: on the free/flat staggered operator on Z_4 x Z_2^3, with an L=4 robustness check, the eps-gap identity and A[1,1]=0 show that the existing residual should target a chi != 0 or Q != 0 background, not treat absence of GW as the demonstrated internal obstruction." This note answers that instruction: it works on `Q != 0` backgrounds.

The dependency row `abj_epsilon_index_square_block_no_go_note_2026-05-30` is represented by [ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md](ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md). Its `effective_status` is `retained_no_go`; its `claim_scope` is: "The standard massless nearest-neighbor staggered site-parity epsilon heat-trace index A_t[U]=Tr(epsilon exp(-t D^dag D)) vanishes for all t>0 on equal-sublattice finite even periodic 4D hypercubic tori with arbitrary U(1) link phases; only that same-surface epsilon-index route to P1' is pruned." The flavored flow is not an epsilon heat-trace and lies outside the pruned scope.

The Record axiom boundary for the word "registers" is read against [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md). Here "registers" names the spectral functional's exact reproduction of the winding integer on this surface; no claim is made that this functional is a record in the sense of the Record axiom. Connecting the supplier to the record/readout chain is a named open path.

Derived here means the finite algebra in `L1` and `L2` plus the machine-verified registration in `L3` and its controls. Supplied would mean a physical theta value, a 4D SU(3) carrier, a continuum limit, or an identification of this functional with the record/readout chain. This note does the first task only.

## Setup

Work on the 2D periodic lattice `Z_L x Z_L`, with even `L`, one-component staggered field `chi(x)`, and U(1) links `U_mu(x)`. The staggered phases are

```text
eta_1(x) = 1
eta_2(x) = (-1)^{x_1}
eps(x) = (-1)^{x_1 + x_2}
```

The staggered operator is

```text
D = (1/2) sum_mu eta_mu(x)
      [ U_mu(x) delta_{x+mu} - U_mu^dag(x-mu) delta_{x-mu} ].
```

It is anti-Hermitian, and `{eps, D} = 0` because every nearest-neighbor hop flips `eps`.

The uniform-flux background of total flux `2 pi Q` uses

```text
phi = 2 pi Q / L^2
U_2(x_1, x_2) = exp(i phi x_1)
U_1(x_1, x_2) = 1                         if x_1 != L-1
U_1(L-1, x_2) = exp(-i phi L x_2)
```

The runner rechecks the total flux by summing principal plaquette angles and asserting

```text
sum_x angle(U_1(x) U_2(x+hat1) U_1(x+hat2)^dag U_2(x)^dag) = 2 pi Q.
```

Let `T_mu` be the gauge-covariant forward shift and

```text
C_mu = (T_mu + T_mu^dag)/2
S = (C_1 C_2 + C_2 C_1)/2
Gamma_f = i eta_2 (C_1 C_2 + C_2 C_1)/2
```

The taste-nonsinglet dressing used as a blind control is `Gamma_w = i (-1)^{x_2} S`.

## L1 Structure of the flavored grading

The site sign `eta_2` has the exact shift identities

```text
eta_2 C_1 = -C_1 eta_2
eta_2 C_2 =  C_2 eta_2
eta_2 S   = -S eta_2
```

Therefore

```text
(eta_2 S)^dag = S eta_2 = -eta_2 S,
```

so the prefactor `i` is forced and `Gamma_f` is Hermitian. Since `eps` anticommutes with each `C_mu`, it commutes with the two-link operator `S`, and

```text
[eps, Gamma_f] = 0.
```

Gauge covariance is built in: `T_mu` is covariant, `C_mu` is made from `T_mu` and `T_mu^dag`, and the site signs are fixed diagonal signs.

In the free field `U = 1`, the reduced-Brillouin-zone symbol of `Gamma_f` is `cos p_1 cos p_2` times the taste-singlet chirality `gamma_5 (x) 1`. On the full lattice the spectrum is exactly

```text
{ cos q_1 cos q_2 : q_i = 2 pi n_i / L }.
```

The runner verifies the `L = 8` maximum deviation as less than `1e-12`; the pre-spec measured value was `7.77e-16`.

The dressing discriminator is:

```text
L = 8, U = 1:
  ||{Gamma_f, D}||_F = 0.000000
  ||{Gamma_w, D}||_F = 5.656854 = 4 sqrt(2)
```

Thus only the `eta_2` dressing gives a free-field anticommuting Hermitian grading partner. In gauged backgrounds `||{Gamma_f, D}||_F` is nonzero and decreases with `L`; measured values are:

```text
L = 8:  Q = 0 -> 0.000000, Q = 1 -> 0.480, Q = 2 -> 0.956
L = 12: Q = 0 -> 0.000000, Q = 1 -> 0.321, Q = 2 -> 0.640
```

The flow result below does not require exact gauged anticommutation.

## L2 The registering functional

The operator `eps D` is Hermitian because `D^dag = -D` and `{eps, D} = 0`:

```text
(eps D)^dag = D^dag eps = -D eps = eps D.
```

Define

```text
H(m) = eps D - m Gamma_f.
```

The exact conjugation antisymmetry is

```text
eps H(m) eps = -H(-m).
```

The proof is two lines:

```text
eps (eps D) eps = D eps = -eps D
eps Gamma_f eps = Gamma_f
```

Hence `spec(H(m)) = -spec(H(-m))`, and the spectral asymmetry across `m = 0` is

```text
flow(m) = N_neg(H(+m)) - N_neg(H(-m)).
```

The runner computes `N_neg` from `np.linalg.eigvalsh` on the actual Hermitian matrices and rejects any case with an eigenvalue within `1e-10` of zero.

## L3 Registration: flow = -2Q

On the uniform-flux backgrounds above, the runner verifies `flow(m) = -2Q` for each `m in {0.1, 0.2, 0.3, 0.4, 0.5}`. The plateau table is:

| L | Q | flow values over the m-grid |
|---|---:|---|
| 8 | -2 | 4, 4, 4, 4, 4 |
| 8 | -1 | 2, 2, 2, 2, 2 |
| 8 | 0 | 0, 0, 0, 0, 0 |
| 8 | 1 | -2, -2, -2, -2, -2 |
| 8 | 2 | -4, -4, -4, -4, -4 |
| 12 | -2 | 4, 4, 4, 4, 4 |
| 12 | -1 | 2, 2, 2, 2, 2 |
| 12 | 0 | 0, 0, 0, 0, 0 |
| 12 | 1 | -2, -2, -2, -2, -2 |
| 12 | 2 | -4, -4, -4, -4, -4 |

This is plateau-constant in `m` and size-stable between `L = 8` and `L = 12` on the tested grid.

## C1 Blindness contrast

The identical flow slot is then reused with `G` replacing `Gamma_f`. With `G = eps`, the flow is zero for every `(L, Q, m)` in the `L in {8, 12}`, `Q in {-2, -1, 0, 1, 2}`, `m in {0.1, 0.2, 0.3, 0.4, 0.5}` grid.

With `G = Gamma_w`, the same flow machinery also returns zero on the same grid. These are blind controls: the same negative-eigenvalue counting that registers `-2Q` for `Gamma_f` returns `0` for `eps` and `Gamma_w`.

The inline heat-trace control also remains blind:

```text
|Tr(eps exp(t D^2))| < 1e-10
```

for `t in {0.5, 1.0}`, `Q in {0, 1, 2}`, at `L = 8`. This is the fixed-grading functional on the same backgrounds and is consistent with the sibling rigidity lemma. The flavored flow is not an epsilon heat-trace.

## C2 Robustness

Gauge covariance is checked by a random gauge transform with seed `7` at `L = 8`, `Q = 1`. The total flux remains `2 pi`, `flow(Gamma_f)` remains `-2` over the `m` grid, and `flow(eps)` remains `0`.

Non-gauge deformation is checked by multiplying every `U_1` and `U_2` by `exp(i * 0.05 * randn)` with `numpy default_rng` seed `11`, before any gauge transform. On the periodic surface each deformed link borders exactly two plaquettes with opposite orientation, so the deformation phases cancel in the total plaquette product. At amplitude `0.05` there is no branch wrap on the tested backgrounds, and the runner reasserts the summed plaquette angle as `2 pi Q`.

For `L = 8`, `Q in {1, 2}`, and `m in {0.05, 0.1, 0.2, 0.3, 0.4, 0.5}`, the deformed backgrounds keep

```text
flow(Gamma_f) = -2Q
flow(eps) = 0.
```

The reading is that the spectral flow depends only on the total flux on this tested surface, not on the particular flux distribution or gauge slice.

## C3 Rejector spectrum

The wrong candidate `Ge = i eps S` is not Hermitian. The runner enforces the discriminating gate

```text
||Ge - Ge^dag||_F > 1.
```

It therefore never enters the flow slot as a grading.

The undressed `S` is Hermitian, so it does enter the same flow slot. The runner wraps this computation in the zero-gap guard and reports the candidate as

```text
REJECTED (ambiguous zero mode / no quantized flow)
```

This is a pass of the rejection check: `S` must not report a clean constant `-2Q` plateau.

## Taste dictionary

On the free field, use the reduced-Brillouin-zone two-qubit representation with bit `1` the pi-shift in direction `1` and bit `2` the pi-shift in direction `2`:

```text
gamma_1 = Z_1
gamma_2 = X_1 Z_2
gamma_5 = Y_1 Z_2
xi_5-like = Z_1 Y_2
eps = X_1 X_2 = gamma_5 (x) xi_5
Gamma_f carries gamma_5 (x) 1
```

Thus `eps` is taste-ANTIsymmetric, which is the blindness mechanism, while `Gamma_f` is taste-SINGLET. Two tastes each carry continuum index `Q`; the taste-singlet counts both and gives `|flow| = 2|Q|`, while the taste-antisymmetric grading cancels them and gives `0`.

The plateau mechanism is that the `2|Q|` would-be zero modes are taste-split into `+/-lambda` pairs with `lambda < 0.01` at `L = 8`. `Gamma_f` takes the same sign on both tastes, so both crossings sit at `|m| = lambda`, and the asymmetry across `m = 0` is saturated for all `m > lambda`. That is why a one-sided `m` scan starting at `m = 0.01` sees nothing while the symmetric-window functional sees `-2Q`.

## What this does and does not supply

This note feeds the gauge-side winding account by giving a finite 2D staggered-surface supplier whose gauge-covariant flavored grading has a graded spectral functional reproducing the winding integer on the tested flux family.

It does not supply a physical theta value, no 4D carrier, no SU(3) extension, no continuum limit, and no identification of this functional with the record/readout chain. The next paths opened by this supplier are the 4D carrier on the glued flux sectors, the SU(3) extension, the scaling limit, and the record/readout identification checkpoint.

## Honest auditor read

The strongest skeptical reading is that this is an existence result on one finite 2D family with uniform-flux backgrounds and controlled deformations. The `-2Q` law is machine-verified here, not analytically derived here. The taste dictionary is a free-field dictionary. The gauged anticommutator is measured and observed to decrease with `L`; it is not bounded by a theorem in this note.
