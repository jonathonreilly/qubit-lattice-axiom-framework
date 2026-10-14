# X1 PREREG — test DI-Z8 ("disentangled inflow" in the smallest dimension where it needs interactions)

Written 2026-10-14 ~14:24Z, BEFORE any script was written or run. Readings below are fixed.

## What is being tested, and what it can and cannot decide

X1's construction (COMBO_REPORT §2) is: take an inflow slab whose bulk is a free invertible
fermion state with an on-site symmetry G; if a G-symmetric locality-preserving unitary V
("symmetric disentangler") maps the bulk to a product state, then cutting V at depth w gives
a far wall that is gapped exactly, with the near-wall chiral content intact and G still
on-site, so gauge links can be shared across layers (F4-A geometry, F4-L3(a) made harmless).
X1 claims (Lemma E) that this is equivalent to far-wall symmetric gapping (P_V <=> P_bdry),
that V is necessarily non-Gaussian, and that the far wall it builds carries the forced
Green's-function zero of F4-L2.

The target class (4+1D bulk, 16 Weyl, Spin(10) or Z4^X) is far beyond exact diagonalisation.
The smallest bulk where (a) the free classification is nontrivial, (b) interactions trivialise
it, and (c) everything is exactly computable is the 1+1D BDI Majorana chain (T^2 = +1),
Fidkowski–Kitaev Z -> Z8: nu = 8 chains = 16 Majoranas per site ("16-fold Majorana" site).
**This test therefore cannot decide P_V in 4+1D.** It is an instrument / logic test of the X1
lemma chain in the one dimension where every step is checkable. A PASS does not move the wall;
a FAIL kills or forces repair of a stated X1 lemma.

## Model (fixed)

- Per site j: nu T-even Majoranas gamma_{j,a} and nu T-odd Majoranas gamma'_{j,a}; T antiunitary, T^2 = +1.
- Kitaev fixed-point bond (j, j+1): h_B = -sum_a i gamma'_{j,a} gamma_{j+1,a} (same sign for all a, so winding nu).
- T-symmetric "end" Hamiltonians: random real combinations of all degree-4 and degree-8 monomials
  of one Majorana type (degree 2 is T-forbidden for a single type; checked, not assumed).

## Sub-tests and pre-registered PASS criteria

**T1 (the Z8 gate for P_bdry).** For n = 2, 4, ..., 16 T-odd Majoranas alone, build the induced
antiunitary T_n on the 2^{n/2}-dim Clifford module. Record (i) whether T_n preserves fermion parity,
(ii) T_n^2 on each parity sector. Also draw 20 random T-symmetric even Hamiltonians for each n
and record the ground-state degeneracy (tolerance 1e-9).
PASS iff: n = 0 mod 8 -> parity preserved, T^2 = +1, and >= 18/20 draws have a unique ground
state; n = 4 mod 8 -> parity preserved, T^2 = -1, every draw >= 2-fold; n = 2, 6 mod 8 ->
parity swapped, every draw >= 2-fold.

**T2 (explicit symmetric disentangler for nu = 8, and its non-Gaussianity).** On one bond
(16 Majoranas, 256-dim): |B> = ground state of h_B (Gaussian); |P> = |E'(gamma')> (x) |E(gamma)>
from random T-symmetric quartic+octic end Hamiltonians (parity matched to |B>). Build U_b as a
real Givens rotation in span{|B>, |P>}.
PASS iff: U_b commutes with T (||U_T conj(U_b) U_T^-1 - U_b|| < 1e-10), with total parity (< 1e-10),
is unitary (< 1e-10), and |<P|U_b|B>| > 1 - 1e-10; AND the one-site Majorana covariance of |E'>,
M'_ab = <i gamma'_a gamma'_b>, has max |M'| < 1e-10 (so |E'> is maximally non-Gaussian and no
Gaussian unitary — in particular no T-symmetric free circuit — can produce |P> from |B>).
Repeat for 5 independent random draws; all 5 must pass.

**T3 (the cut gives an exactly solvable far-wall SMG with a forced zero).** Reduce
O = U_b h_B U_b^dag to the far-end gamma' factor by the partial expectation in |E(gamma)>.
PASS iff: (i) the reduced H_far is T-symmetric, parity-even, has a unique ground state equal to
|E'> (overlap > 1 - 1e-10) with gap > 1e-3; (ii) its quadratic (bilinear-mass) component is zero
(Frobenius norm of the projection onto i gamma'_a gamma'_b < 1e-10); (iii) the far-end elementary
Green's function G_ab(i w) of the 8 gamma' satisfies max|G(i w)| < 10 w for w = 1e-2, 1e-4, 1e-6
(a zero at w = 0, linear), while a T-breaking control (H_far + 0.3 i gamma'_1 gamma'_2) gives
max|G(i 1e-6)| > 1e-2 (the instrument sees a nonzero G(0) when T is broken); (iv) the free
near-end control (8 dangling gamma, H = 0 on them) has a pole: max|G(i w)| > 1/(10 w).

## Readings (fixed)

- **CHAIN-CONSISTENT (PASS):** T1, T2, T3 all pass. Reading: in the only exactly checkable
  dimension, (a) P_V <=> P_bdry <=> nu = 0 mod 8 (Lemma E both directions); (b) the
  disentangler is necessarily interacting; (c) the disentangler-built far wall is, by
  construction, a symmetric mass generation term with no bilinear and a forced Green's-function
  zero (F4-L2 analogue). Says nothing about 4+1D existence.
- **CHAIN-BROKEN (FAIL):** any criterion fails. The failing lemma is named and X1's report is
  repaired or the lemma withdrawn.
- **INSTRUMENT-FAIL:** the T-breaking control in T3(iii) or the pole control in T3(iv) fails;
  then T3's zero reading is void.

Resources: one Python process, numpy dense <= 256x256 (and 2^8-dim for n = 16), OMP_NUM_THREADS=2,
expected < 100 MB, < 5 min.
