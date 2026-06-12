# Gauge-Vacuum Plaquette Trivial-Slice Eigen-Identity Lemma

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Claim boundary:** finite-packet identity for the matrix-element
multi-word tensor-transfer trivial slice at `beta = 6`, `NMAX = 4`,
`MODE_MAX = 80`, with the composed source readout using the existing
source-sector `NMAX = 7`, `MODE_MAX = 200` machinery. This note does not
compute the physical 3D unmarked spatial Wilson environment, the untruncated
tensor-transfer Perron state, an `L_perp` limit, a full rim-boundary
`eta_beta^env` evaluation, an analytic plaquette value, or a canonical
repinning.

**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Primary runner:** [`scripts/gauge_vacuum_plaquette_trivial_slice_eigen_identity_lemma_2026_06_12.py`](../scripts/gauge_vacuum_plaquette_trivial_slice_eigen_identity_lemma_2026_06_12.py)
**Runner cache:** [`logs/runner-cache/gauge_vacuum_plaquette_trivial_slice_eigen_identity_lemma_2026_06_12.txt`](../logs/runner-cache/gauge_vacuum_plaquette_trivial_slice_eigen_identity_lemma_2026_06_12.txt)

## Scope

This note proves a finite-packet identity for the multi-word tensor-transfer
operator used in the ladder runner. It explains why the derived
all-trivial-except-word0 slice of the `k`-word Perron vector is
word-count-stationary after normalization.

One-hop authorities:

- [GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md)
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md)
- [GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md](GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md)
- [GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md](GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md)
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_MULTIWORD_PERRON_LADDER_BOUNDED_NOTE_2026-06-11.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_MULTIWORD_PERRON_LADDER_BOUNDED_NOTE_2026-06-11.md)
- [GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md](GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_PERRON_DERIVED_RHO_COMPOSED_READOUT_BOUNDED_NOTE_2026-06-11.md)
- [GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)

No new literature values, axioms, external citations, or comparator numbers
are imported here. The proof uses only the finite packet ingredients already
constructed in the landed ladder runner:
[`scripts/gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11.py`](../scripts/gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11.py).

## Index Form Of The Multi-Word Transfer

Let `I` be the finite dominant-weight box. For `a in I`, write:

- `D_a` for the normalized single-link Wilson coefficient used by `diag`;
- `d_a` for the SU(3) representation dimension;
- `M_ab` for the one-word fusion sum `nf + nfb`;
- `e = (0,0)`, `f = (1,0)`, and `fb = (0,1)`.

For a `k`-word row label `x = (x_1, ..., x_k)` and column label
`y = (y_1, ..., y_k)`, define `D_x = product_j D_(x_j)`. The runner's
matrix-element branch is the symmetric sandwich

```text
T_k = D_k M_k D_mid M_k^T D_k,
M_k = M tensor ... tensor M.
```

Before the adjacent bond is applied, the middle label is
`mu = (mu_1, ..., mu_k)`. The factor `diag` contributes
`product_j D_(mu_j)`. The matrix-element adjacent bond contributes

```text
product_(j=1 to k-1) delta_(mu_j, mu_(j+1)) / d_(mu_j).
```

Therefore `D_mid(mu)` vanishes unless all middle labels are equal. On the
surviving diagonal middle state `(mu, ..., mu)`,

```text
D_mid(mu, ..., mu) = D_mu^k / d_mu^(k-1).
```

Thus the full matrix element is

```text
T_k[x,y]
  = D_x D_y sum_(mu in I)
      (D_mu^k / d_mu^(k-1))
      product_(j=1 to k) M_(x_j,mu) M_(y_j,mu).              (1)
```

This is the load-bearing collapse: the adjacent-word bond turns the middle
sum from an `I^k` sum into a single shared-label sum over `I`.

## The Slice Equation

Let `psi_k` be a positive Perron vector for `T_k` with eigenvalue `theta_k`.
Define the raw trivial slice

```text
S_k(a) = psi_k(a, e, ..., e).
```

Apply `(1)` to the row `(a,e,...,e)`. All dependence on off-slice entries of
`psi_k` is contained in the channel functional

```text
H_k(mu)
  = sum_y D_y product_(j=1 to k) M_(y_j,mu) psi_k(y).
```

The restricted eigen-equation is

```text
theta_k S_k(a)
  = D_a D_e^(k-1) sum_(mu in I)
      (D_mu^k / d_mu^(k-1))
      M_(a,mu) M_(e,mu)^(k-1) H_k(mu).                       (2)
```

The finite SU(3) recurrence used by `M` has

```text
M_(e,mu) = 1  for mu in {f, fb},
M_(e,mu) = 0  otherwise.                                     (3)
```

So the whole slice equation factors through the two channels `f` and `fb`:

```text
theta_k S_k(a)
  = D_a D_e^(k-1) [
      (D_f^k / d_f^(k-1)) M_(a,f) H_k(f)
    + (D_fb^k / d_fb^(k-1)) M_(a,fb) H_k(fb)
    ].                                                       (4)
```

The finite packet is conjugation-symmetric:

```text
D_f = D_fb,  d_f = d_fb,
```

and `T_k` commutes with simultaneous conjugation of every word. Under the
verified positive swap-even Perron branch, equivalently under the explicit
hypothesis `H_k(f) = H_k(fb)`, equation `(4)` becomes

```text
theta_k S_k(a)
  = C_k D_a [M_(a,f) + M_(a,fb)]                              (5)
```

for one scalar `C_k` that may depend on `k`, `theta_k`, and the full Perron
vector.

This is the structural feature that closes the slice after normalization.
The slice of a Perron vector does not generally satisfy a closed equation;
here the off-slice dependence has collapsed to one common scalar. Dividing
`(5)` by the same equation at `a = e` cancels `C_k` and `theta_k`:

```text
rho_k(a)
  := S_k(a) / S_k(e)
   = D_a [M_(a,f) + M_(a,fb)]
     / (D_e [M_(e,f) + M_(e,fb)]).                            (6)
```

Equation `(6)` is independent of `k`. Equivalently, the normalized trivial
slice is the fixed point of the `k`-independent slice map whose right-hand
side is `(6)`.

On the finite `NMAX=4, MODE_MAX=80` packet, `D_e = 1` and
`M_(e,f) + M_(e,fb) = 2`, so

```text
rho_k(a) = D_a [M_(a,f) + M_(a,fb)] / 2.                       (7)
```

The support is exactly

```text
{(0,0), (1,0), (0,1), (1,1), (2,0), (0,2)}.
```

The displayed components include

```text
rho_k(1,0) = 0.211265869825
rho_k(1,1) = 0.162259799480
```

for every `k >= 2` covered by this finite-packet construction.

## Verification

The runner verifies the algebraic steps, not just the final readout.

Key checks:

- `D_mid` has nonzero support only on all-equal middle labels, with value
  `D_mu^k / d_mu^(k-1)`.
- The trivial row of `M` sees exactly `f` and `fb`.
- The restricted eigen-equation `(4)` reproduces the direct two-word and
  three-word Perron slices.
- The channel functionals satisfy `H_k(f) = H_k(fb)` on the positive
  swap-even Perron branch.
- The measured two/three raw slice proportionality is reproduced:
  common scalar `0.025986536153`, spread `1.388e-16`.
- The full three-word vector is not rank-one across `(word0 word1 | word2)`:
  second/top singular ratio `0.024190312518`.
- The `k=4` prediction is checked with the 25 by 25 finite-rank reduction of
  the same operator rather than by building the 390625-dimensional vector.

The finite-rank reduction follows directly from `(1)`:

```text
T_k = A_k C_k A_k^T,
C_k(mu,mu) = D_mu^k / d_mu^(k-1),
G = M^T diag(D^2) M,
nonzero spectrum from C_k^(1/2) G^(entrywise k) C_k^(1/2).
```

It reproduces the direct `k=2` and `k=3` eigenvalues and slices, then gives
the `k=4` slice

```text
rho_4(1,0) = 0.211265869825
rho_4(1,1) = 0.162259799480
```

and the stationary composed source readout

```text
P = 0.429196712321.
```

## Falsification Control

The unperturbed character-level branch in the ladder script is not a useful
falsifier for this particular trivial-slice identity. It removes the
`1/d_mu` factor but keeps the same-label delta and conjugation symmetry; since
the surviving channels are still exactly `f` and `fb` with equal packet data,
the normalized slice remains `(6)`.

The runner therefore uses a positive conjugation-asymmetric character-level
perturbation as the control. It keeps the same-label middle support but weights
the shared label by `2 + p + 2q`. That breaks the equality of the two surviving
channels. The normalized two/three slices then differ by `4.061e-02`, and the
raw slice-ratio spread is `4.854e-01`. This control is not a theorem input; it
only verifies that the proof depends on the two-channel conjugation symmetry.

## Named Residuals

- finite dominant-weight box only;
- finite Bessel mode support only;
- no full physical 3D unmarked spatial Wilson environment computation;
- no all-weight or untruncated convergence proof;
- no `L_perp` limit;
- no evaluated full rim-boundary `eta_beta^env`;
- no analytic `P(6)`;
- no canonical repinning.

## Runner

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_trivial_slice_eigen_identity_lemma_2026_06_12.py
```

Expected tail:

```text
TOTAL: PASS=21, FAIL=0
```

Cache refresh command:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); from runner_cache import execute_runner, write_cache, runner_timeout_for; rp='scripts/gauge_vacuum_plaquette_trivial_slice_eigen_identity_lemma_2026_06_12.py'; res=execute_runner(rp, runner_timeout_for(rp)); print(write_cache(rp, res))"
```
