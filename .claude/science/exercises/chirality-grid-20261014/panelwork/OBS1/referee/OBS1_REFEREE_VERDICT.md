# OBS-1 independent referee verdict

## VERDICT: CONFIRMED WITH CORRECTIONS

The exact-symmetry core of R2 and the rate arithmetic of R3 survive.  The R1
loop numbers also reproduce, but `FLAV-NEAR` is established only for the
registered diagonal-`E_g`, vector-like-U(1), bilinear-proxy completion.  It is
not yet a result for the full X2/Standard-Model theory, and the complete
five-component traceless-strain reading remains open because `T2g` was not
computed.

## 1. R2: exact symmetry

**Finding: the microscopic X2 terms shown in the packet are U(1)_X invariant.**

- The charge table in `scripts/sizes.py:127-134` is correct:
  `X=(1,1,-3,-3,1,5)` on `(Q,u^c,d^c,L,e^c,nu^c)`.  Thus
  `16 = 10_1 + bar(5)_-3 + 1_5` under
  `Spin(10) -> SU(5) x U(1)_X`.  This is precisely the centralizer U(1) of
  SU(5), so U(1)_X does commute with the stated SU(5) subgroup.  Sign-reversing
  all X charges would only change convention.
- The filtered field transforms covariantly because the scalar filter is the
  identity on the 16 (`X2_COMBO_REPORT.md:55-68`) and, after gauging, every
  `G_SM` link commutes with X.  Consequently filtering does not spoil X.
- For the potentially dangerous quartic, the bilinear `B^a` is a Spin(10)
  vector.  Under `SU(5) x U(1)_X`, the vector is
  `10_v = 5_-2 + bar(5)_+2`.  The invariant contraction in
  `B^a B^a + h.c.` pairs the `+2` and `-2` components; `B^{a dagger}B^a` is
  neutral term by term.  Thus the statement "Spin(10) singlet" in
  `REPORT.md:89-93` is sufficient, but the charge pairing should have been
  written explicitly because this was the load-bearing step.
- The walker, strain deformation and leakage generated from those vertices
  act on spacetime/corner data and do not insert an X-charged spurion.  They
  therefore preserve X.

**Electroweak breaking:** with the standard Higgs doublet
`Y(H)=+1/2`, `B-L(H)=0`, hence `X(H)=-2`.  All four Dirac Yukawa classes are
X-neutral.  The Higgs vev breaks X and gauged Y separately, but annihilates
`X+4Y=5(B-L)`, so the physical unbroken global symmetry is U(1)_(B-L), modulo
the gauged hypercharge transformation.  This validates `REPORT.md:95`, not an
assertion that the bare X generator itself leaves the vev invariant.

**Anomalies and the lattice correction:** an independent exact calculation
gives zero for `X^3`, gravitational-X, `Y^2 X`, `Y X^2`, `SU(3)^2 X`, and
`SU(2)^2 X` for one 16.  But `REPORT.md:94` has the logic backwards if read by
itself: anomaly freedom does not force an arbitrary lattice regulator to keep
X.  Here the valid finite-cutoff argument is instead the manifest microscopic
commutator `[H_X2,Q_X]=0`; anomaly cancellation then says that integrating out
fields does not obstruct its Ward identity.  This conclusion still requires
the symmetric, unbroken mirror vacuum that the packet itself leaves open as
`L_X2` (`X2_COMBO_REPORT.md:169-188`) and states as condition c2
(`REPORT.md:101-105`).

Subject to that condition and to the standard B-L-neutral Higgs/Yukawa
completion, `nu^c nu^c` is the minimal named breaking operator and exact B-L
forbids Majorana masses, ordinary neutrinoless double beta decay and
neutron-antineutron oscillation.  Thus R2 is correct as a conditional theorem,
not as an unconditional established phase of X2.

## 2. R1: loop, lemmas and clock mapping

**Numerics confirmed.**  A fresh one-process `N=40`, `m0=0.1`, `Delta=0.5`
run used 83 MB RSS and returned

```
L0 = 0.0820790
(L'_x,L'_y,L'_z) = (-0.00767855,-0.00868787,-0.01696959)
||L' traceless|| = 0.00720946
K_on-site = 0.00150340
```

These interpolate the saved `N=32,48,64` values in
`scripts/r1_leak.out:9-24,41-48` and `scripts/r1_loop.out:55-81`.  A centered
finite difference in the mass-symbol coefficient and a halved strain step
gave `0.0072882`, only 1.1% above the worker's forward-difference value.  The
Ward residual and `N=48 -> 64` convergence claims are also borne out by those
outputs.

**Staggered-reflection lemma confirmed at its stated narrow scope.**  With
only an on-site mass, `k_a -> pi-k_a` leaves the sine walker and the diagonal
SF flow invariant and maps a hw1 corner to the origin.  Cubic symmetry at the
origin forbids a scalar linear coupling to traceless strain.  This explains
the numerical zero at `Delta=0` (`scripts/r1_loop.out:1-18,37-54,82-99`).  It
does not apply once the non-onsite mirror proxy is present; the nonzero
`Delta=0.5` result is consistent with that limitation.

**Circulant lemma confirmed as a symmetry lemma, with a scope correction.**
For a nondegenerate T-invariant mass sector, cyclic/cubic covariance maps
`dM_a` into `dM_{a+1}` and a T eigenstate has equal diagonal expectation on
the orbit, so an `E_g` traceless diagonal strain has zero first-order shift.
The numerical zero in `scripts/sizes.out:1-3` is therefore expected.  It does
not make the CKM-broken down sector strain-blind, and the runner evaluates only
diagonal `E_g` response (`scripts/sizes.py:16-40`).

**Clock arithmetic confirmed under the packet's estimator.**  An independent
frequency-domain transfer-function integration, rather than the worker's
time-domain covariance matrix, gives the same four LS slopes to the printed
precision: `1.5024, 3.4218, 2.6255, 4.2741 e-15 /yr`; the corresponding
low-frequency rms derivatives are `2.8119, 5.0172, 3.9068, 5.7034 e-15 /yr`.
Thus the multiplication that produces the branch table in
`scripts/sizes.out:10-42` is correct, as is the `3.6e-17/yr` one-sigma clock
number used in `REPORT.md:47-60`.

**Correction to the reading.**  The branch figures `A = 80-360`,
`B = 0.12-2.5`, and `B' = 2-93` are correct outputs of the specified `E_g`
proxy and chosen mass-matrix decompositions.  But the report calls them lower
bounds and explicitly says `T2g` was not computed (`REPORT.md:49,63-72`).
Because the stochastic gravitational-wave field has all five traceless-tensor
components and the CKM-broken sector has no symmetry setting its `T2g`
coefficient to zero, an `E_g` lower bound lying below 10 does not prove that
the full rate lies below 10.  The honest fixed reading is therefore:

- `FLAV-NEAR` for the registered diagonal-`E_g` U(1)/proxy completion;
- `OPEN` for the full first-order X2/SM strain response until `T2g`, chiral
  non-Abelian vertices and the actual mirror self-energy are computed.

The matter-sector Lorentz-violation part is likewise not a result: the only
flavour-pattern residual is explicitly labelled "suggested, not computed" in
`REPORT.md:74-78`.

## 3. R3: proton-decay formula and floor

The two-body formula in `REPORT.md:120-131` is correctly normalized when
`W0` is the full three-quark-to-pion form factor.  Recomputing the unit
conversion from `tau > 2.4e34 yr` gives
`|C| < 2.63e-32 ... 9.85e-32 GeV^-2`, hence a unit-coefficient scale
`3.19e15 ... 6.17e15 GeV`, exactly as in `scripts/sizes.out:67-71`.
Multiplying the strict end by `sqrt(c_eff=10)` gives
`1/a > 1.95e16 GeV`, so the stated rounded worst-case floor `2e16 GeV` and
the Planck-scale lifetime margin `1.5e11` are correct.

Two corrections are required:

1. The factor 4800 is a representative point (`W0=0.13 GeV^2`, `A_R=1`),
   not the packet-wide correction.  Across the stated `W0=0.10-0.15` and
   `A_R=1-2.5` ranges, the naive `m_p^5/Lambda^4` rate overstates the rate by
   about `5.8e2` to `8.1e3`.
2. The floor is conditional on the assumed leakage envelope
   `c_eff <= 10`.  X2 supplies the allowed channels, but the nonperturbative
   coefficient was not derived: the link estimate and filter-offset estimate
   are labelled suggested in `X2_COMBO_REPORT.md:152-159`, and
   `scripts/sizes.py:169-175` installs the envelope.  Therefore
   `PDK-SAFE-AT-PLANCK` is robust for the stated O(1)-to-10 coefficient
   completion, not an unconditional bound from X2 alone.

## 4. Scope of the observational sheet

- **U(1) stand-in:** it checks the lattice momentum/strain machinery and
  orders of magnitude, but omits chiral electroweak couplings, non-Abelian
  vertices, representation factors and operator mixing (`REPORT.md:63-68`).
- **Bilinear mirror proxy:** `Delta f_NN` is not X2's filtered Spin(10)
  quartic or a derived self-energy of its symmetric-gapped phase.  It can be
  used as a regulator model, but its coefficient and even its pole structure
  are completion data.  The strain-dependent subtraction of the `m0=0`
  additive mass in `scripts/r1_loop.py:79-86` is also a renormalization
  prescription, not an X2 theorem.
- **SF transplant:** the diagonal flow and the identification
  `|s|=|h_GW|` are imported bridge assumptions (`PREREG.md:20-24,32-34`).
  Off-diagonal strain is absent.  Consequently the sheet is a useful
  conditional sensitivity estimate, not yet a prediction of the native X2
  law.

## Strongest correct statement

For the X2 Hamiltonian actually written, every microscopic term preserves the
Spin(10)-centralizer U(1)_X, including the all-legs-filtered 10-channel
quartic; standard B-L-neutral electroweak breaking leaves the gauge-equivalent
continuous U(1)_(B-L), so a symmetric mirror phase predicts no Majorana mass,
no ordinary 0nu-beta-beta and no neutron-antineutron oscillation.  Independently
rerun one-loop proxy coefficients and clock arithmetic support an `E_g`
flavour-strain sensitivity of `0.12-2.5` clock bounds in the chosen circulant
branch, while the standard proton-decay formula gives a worst assumed
`c_eff<=10` floor near `2e16 GeV`; neither numerical statement is yet a native
X2 theorem because the full `T2g` response, the chiral non-Abelian theory, the
quartic mirror self-energy and the leakage coefficient remain uncomputed.
