# Theta Assembly Paired-Shift Law From Fixed Grading

**Date:** 2026-07-02
**Primary runner:** `scripts/theta_assembly_paired_shift_fixed_grading_mckean_singer_2026_07_02.py`

## Claim

> This is an exact finite-dimensional narrow theorem: L1 fixed-grading McKean-Singer rigidity, L2 twisted-mass determinant identity, and L3 the paired-shift law follow on finite staggered surfaces with unitary links and fixed state-independent grading. The corollaries are C1 balanced collapse and C2 supplier reduction: on the balanced surface the transfer integer is zero, while any nontrivial transfer is pushed to the same supplier class named by (P1'-sharpened). The scope is the fixed state-independent grading on finite staggered surfaces with unitary links; this note supplies the invariant bookkeeping on the fixed-grading surface; it does not supply either side's physical value.

## Context

The Tier-A row `strong_cp_theta_zero_note` has a minimum decomposition into a gauge-side winding account and a mass-side orientation-determinant readout. The in-flight bridge `THETA_BAR_ASSEMBLY_INTERFACE_BRIDGE_2026-07-01` (PR #4768) names the residual wall `W_anomaly_covariant_assembly` and quotes the paired shift law `theta_gauge -> theta_gauge - n alpha; arg det M -> arg det M + n alpha`.

"Derived" here means the finite fixed-grading algebra proves the bookkeeping law and the value n = 2 tr(eps) on this surface. "Supplied" would mean importing the physical value of theta_gauge, the physical value of arg det M, or a nontrivial background-dependent assembly transfer. This note does the first task only.

## Setup

The surface is a finite lattice with one-component staggered fermion field and unitary U(1) links. The staggered operator is

```text
D_U(x, x +/- mu) = +/- (1/2) eta_mu(x) U_{+/- mu}(x)
eta_mu(x) = (-1)^{x_1 + ... + x_{mu-1}}
U_{-mu}(x) = conj(U_mu(x - mu)).
```

With periodic even side lengths, every hop flips the site grading
`eps(x) = (-1)^{x_1 + ... + x_d}`. Therefore `{eps, D} = 0` exactly. For unitary links the forward and backward entries are conjugate with the opposite sign, so `D^dag = -D` exactly.

## L1 Fixed-Grading McKean-Singer Rigidity

For any finite anti-Hermitian D with Hermitian involution eps, `{eps, D} = 0`, and `eps^2 = I`, define `A_t[U] = Tr(eps * exp(t D^2))`. Since `D^2 = -D^dag D <= 0`, the statement is:

A_t[U] = tr(eps|_{ker D[U]}) = tr(eps) for every t > 0 and every unitary link configuration U

Proof. The identities eps Hermitian and `{eps, D} = 0` give `{eps, D^dag} = 0`, hence `[eps, D^dag D] = 0`. In the eps eigenbasis, `eps = diag(I_{n+}, -I_{n-})`, anticommutation and anti-Hermiticity force

```text
D = [[0, B],[-B^dag, 0]]
```

so `-D^2 = D^dag D = diag(B B^dag, B^dag B)`. The nonzero spectra of `B B^dag` and `B^dag B` coincide with multiplicity. Therefore

```text
A_t = Tr exp(-t B B^dag) - Tr exp(-t B^dag B)
    = dim ker B^dag - dim ker B
    = (n+ - rank B) - (n- - rank B)
    = n+ - n-
    = tr(eps).
```

Also `ker D = ker B^dag (+) ker B`, so `tr(eps|_{ker D}) = tr(eps)`.

Rigidity reading: with a fixed, state- and background-independent grading, the heat-kernel index carries no background information. It is pinned to the surface integer `tr(eps)`.

## L2 Twisted-Mass Determinant Identity

For any finite matrix D, anti-Hermiticity not required, with `{eps, D} = 0`, `eps^2 = I`, and any complex alpha and m:

det(D + m e^{2 i alpha eps}) = e^{2 i alpha tr(eps)} det(D + m I)

Proof. From `eps D = -D eps`, termwise expansion gives `e^{i alpha eps} D = D e^{-i alpha eps}`. Hence

```text
e^{i alpha eps} D e^{i alpha eps} = D
e^{i alpha eps} (m I) e^{i alpha eps} = m e^{2 i alpha eps}.
```

Taking determinants of `e^{i alpha eps} (D + m I) e^{i alpha eps} = D + m e^{2 i alpha eps}` gives the result, because each exponential factor contributes determinant `e^{i alpha tr(eps)}`.

## L3 Paired-Shift Law

For the finite Grassmann integral `Z = det(D + m I)`, rotate the fields by `psi -> e^{i alpha eps} psi` and `psibar -> psibar e^{i alpha eps}`. The kinetic bilinear is invariant by the L2 conjugation identity. The mass bilinear becomes `m psibar e^{2 i alpha eps} psi`. The measure contributes `det(e^{i alpha eps})^{-2} = e^{-2 i alpha tr(eps)}`.

Thus the measure deposits phase shift `-2 alpha tr(eps)` while the mass determinant's argument shifts by `+2 alpha tr(eps)`, and `Z` is invariant. This derives the paired shift law `theta_gauge -> theta_gauge - n alpha; arg det M -> arg det M + n alpha` with n = 2 tr(eps). On this surface the measure deposit and the mass-determinant shift are one exact identity, not two admissions.

## C1 Balanced Collapse

On the framework's staggered even-torus surface, the eps sublattices are equal. Therefore `tr(eps) = 0` and `n = 0`. The paired-shift law holds with zero transfer: assembly bookkeeping is exact and trivial there.

The square-block no-go is the audited surface instance. Its `A_t == 0` result is precisely L1's balanced case, and its scope is "exact route-pruning no-go on the standard staggered epsilon-index residual; not a retained 3+1 closure theorem".

## C2 Supplier Reduction

By L1, `tr(eps)` is a background-independent integer for any fixed grading, and it is zero on the balanced surface. Hence a nonzero or background/sector-dependent assembly transfer cannot come from this fixed grading. It requires the (P1'-sharpened) supplier class named in the GW-not-necessary note:

- an operator-dependent grading, such as Ginsparg-Wilson/overlap eps(D);
- a flavored/taste-singlet flow, such as Adams;
- an eta/K^1 family flow;
- an unbalanced or `chi != 0` complex.

The theta lane's `W_anomaly_covariant_assembly` residual and the ABJ lane's (P1'-sharpened) residual name the same supplier class; the next path this opens is building that supplier once and serving both lanes, with prose adjacency to `THETA_4D_CARRIER_FLUX_COHOMOLOGY` (PR #4811), where the exact F-cup-F sector reduction is being carried separately.

## Synthetic Toy

This section is synthetic and is not a framework background. Take a random complex `3 x 2` block B, set

```text
D_toy = [[0, B],[-B^dag, 0]]
eps_toy = diag(1,1,1,-1,-1).
```

Then `tr(eps_toy) = 1`, so L1 gives `A_t = 1` for all t and L2 gives determinant ratio `e^{2 i alpha}`. The two shift factors are individually nontrivial and cancel exactly. The square-block no-go runner's rectangular synthetic control is prior art for this escape-hatch demonstration.

## Runner And Gate Table

Run:

```bash
python3 scripts/theta_assembly_paired_shift_fixed_grading_mckean_singer_2026_07_02.py
```

Observed:

| Gate | Quantity | Tolerance | Measured | Result |
|---|---|---:|---:|---|
| G0[B2Q(0)] | uniform plaquette phase and total flux | phase<1.0e-12; total<1.0e-10 | phase_resid=0.00000000000000000e+00; total_resid=0.00000000000000000e+00 | PASS |
| G0[B2Q(1)] | uniform plaquette phase and total flux | phase<1.0e-12; total<1.0e-10 | phase_resid=2.77555756156289135e-16; total_resid=0.00000000000000000e+00 | PASS |
| G0[B2Q(-1)] | uniform plaquette phase and total flux | phase<1.0e-12; total<1.0e-10 | phase_resid=2.77555756156289135e-16; total_resid=0.00000000000000000e+00 | PASS |
| G0[B2Q(2)] | uniform plaquette phase and total flux | phase<1.0e-12; total<1.0e-10 | phase_resid=5.11787526652090422e-16; total_resid=0.00000000000000000e+00 | PASS |
| G0[B2Q(-2)] | uniform plaquette phase and total flux | phase<1.0e-12; total<1.0e-10 | phase_resid=5.11787526652090422e-16; total_resid=0.00000000000000000e+00 | PASS |
| G1[B4free] | max anticommutator entry and anti-Hermitian entry | each<1.0e-14 | anticom=0.00000000000000000e+00; antiherm=0.00000000000000000e+00 | PASS |
| G1[B4rand] | max anticommutator entry and anti-Hermitian entry | each<1.0e-14 | anticom=0.00000000000000000e+00; antiherm=0.00000000000000000e+00 | PASS |
| G1[B2Q(0)] | max anticommutator entry and anti-Hermitian entry | each<1.0e-14 | anticom=0.00000000000000000e+00; antiherm=0.00000000000000000e+00 | PASS |
| G1[B2Q(1)] | max anticommutator entry and anti-Hermitian entry | each<1.0e-14 | anticom=0.00000000000000000e+00; antiherm=0.00000000000000000e+00 | PASS |
| G1[B2Q(-1)] | max anticommutator entry and anti-Hermitian entry | each<1.0e-14 | anticom=0.00000000000000000e+00; antiherm=0.00000000000000000e+00 | PASS |
| G1[B2Q(2)] | max anticommutator entry and anti-Hermitian entry | each<1.0e-14 | anticom=0.00000000000000000e+00; antiherm=0.00000000000000000e+00 | PASS |
| G1[B2Q(-2)] | max anticommutator entry and anti-Hermitian entry | each<1.0e-14 | anticom=0.00000000000000000e+00; antiherm=0.00000000000000000e+00 | PASS |
| G1[Btoy] | max anticommutator entry and anti-Hermitian entry | each<1.0e-14 | anticom=0.00000000000000000e+00; antiherm=0.00000000000000000e+00 | PASS |
| G2[B4free] | max abs(A_t - tr(eps)) over t=0.3,1.0,3.0 | <1.0e-10 | t=0.3:resid=2.44249065417534439e-15; t=1.0:resid=3.83026943495679006e-15; t=3.0:resid=1.39489114703295058e-14; max=1.39489114703295058e-14 | PASS |
| G2[B4rand] | max abs(A_t - tr(eps)) over t=0.3,1.0,3.0 | <1.0e-10 | t=0.3:resid=2.44249065417534439e-14; t=1.0:resid=2.43971509661378150e-14; t=3.0:resid=2.49305784350006832e-14; max=2.49305784350006832e-14 | PASS |
| G2[B2Q(0)] | max abs(A_t - tr(eps)) over t=0.3,1.0,3.0 | <1.0e-10 | t=0.3:resid=1.99840144432528177e-15; t=1.0:resid=1.11022302462515654e-15; t=3.0:resid=4.99600361081320443e-16; max=1.99840144432528177e-15 | PASS |
| G2[B2Q(1)] | max abs(A_t - tr(eps)) over t=0.3,1.0,3.0 | <1.0e-10 | t=0.3:resid=8.21565038222615840e-15; t=1.0:resid=7.29971638691040425e-15; t=3.0:resid=7.68829444552920904e-15; max=8.21565038222615840e-15 | PASS |
| G2[B2Q(-1)] | max abs(A_t - tr(eps)) over t=0.3,1.0,3.0 | <1.0e-10 | t=0.3:resid=8.21565038222615840e-15; t=1.0:resid=7.29971638691040425e-15; t=3.0:resid=7.68829444552920904e-15; max=8.21565038222615840e-15 | PASS |
| G2[B2Q(2)] | max abs(A_t - tr(eps)) over t=0.3,1.0,3.0 | <1.0e-10 | t=0.3:resid=1.52655665885959024e-15; t=1.0:resid=1.94289029309402395e-15; t=3.0:resid=2.80331313717852026e-15; max=2.80331313717852026e-15 | PASS |
| G2[B2Q(-2)] | max abs(A_t - tr(eps)) over t=0.3,1.0,3.0 | <1.0e-10 | t=0.3:resid=1.52655665885959024e-15; t=1.0:resid=1.94289029309402395e-15; t=3.0:resid=2.80331313717852026e-15; max=2.80331313717852026e-15 | PASS |
| G2[Btoy] | max abs(A_t - tr(eps)) over t=0.3,1.0,3.0 | <1.0e-10 | t=0.3:resid=4.44089209850062616e-16; t=1.0:resid=1.11022302462515654e-16; t=3.0:resid=0.00000000000000000e+00; max=4.44089209850062616e-16 | PASS |
| G2b[B2Q(0)] | Q-blind A_1 residual; sigma_min diagnostic | A_1<1.0e-10; sigma no gate | A1_resid=1.11022302462515654e-15; sigma_min=2.21301005575440376e-17 | PASS |
| G2b[B2Q(1)] | Q-blind A_1 residual; sigma_min diagnostic | A_1<1.0e-10; sigma no gate | A1_resid=7.29971638691040425e-15; sigma_min=4.41783507936554958e-17 | PASS |
| G2b[B2Q(-1)] | Q-blind A_1 residual; sigma_min diagnostic | A_1<1.0e-10; sigma no gate | A1_resid=7.29971638691040425e-15; sigma_min=4.41783507936554958e-17 | PASS |
| G2b[B2Q(2)] | Q-blind A_1 residual; sigma_min diagnostic | A_1<1.0e-10; sigma no gate | A1_resid=1.94289029309402395e-15; sigma_min=5.86239662106997310e-17 | PASS |
| G2b[B2Q(-2)] | Q-blind A_1 residual; sigma_min diagnostic | A_1<1.0e-10; sigma no gate | A1_resid=1.94289029309402395e-15; sigma_min=5.86239662106997310e-17 | PASS |
| G3[B4free,alpha=0.3,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=1.42108547152020037e-14; phase_resid=2.91393646794427307e-15 | PASS |
| G3[B4free,alpha=0.3,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=1.42108547152020037e-14; phase_resid=1.66976458451096373e-15 | PASS |
| G3[B4free,alpha=0.7,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=7.10542735760100186e-15; phase_resid=5.36620025422423109e-16 | PASS |
| G3[B4free,alpha=0.7,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=2.84217094304040074e-14; phase_resid=2.32071456886134650e-15 | PASS |
| G3[B4free,alpha=pi/3,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=3.55271367880050093e-14; phase_resid=1.18459386534184373e-16 | PASS |
| G3[B4free,alpha=pi/3,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=1.42108547152020037e-14; phase_resid=1.24802310199208968e-15 | PASS |
| G3[B4rand,alpha=0.3,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=3.90798504668055102e-14; phase_resid=1.81172247717811585e-14 | PASS |
| G3[B4rand,alpha=0.3,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=7.10542735760100186e-15; phase_resid=5.12657471082411504e-15 | PASS |
| G3[B4rand,alpha=0.7,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=8.88178419700125232e-15; phase_resid=8.00241963095440696e-15 | PASS |
| G3[B4rand,alpha=0.7,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=1.42108547152020037e-14; phase_resid=1.84605264881274186e-15 | PASS |
| G3[B4rand,alpha=pi/3,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=3.55271367880050093e-15; phase_resid=9.48269007025751048e-15 | PASS |
| G3[B4rand,alpha=pi/3,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=1.42108547152020037e-14; phase_resid=3.44794363427710040e-15 | PASS |
| G3[B2Q(1),alpha=0.3,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=0.00000000000000000e+00; phase_resid=7.64682840691782119e-16 | PASS |
| G3[B2Q(1),alpha=0.3,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=4.44089209850062616e-16; phase_resid=3.54658581424633528e-16 | PASS |
| G3[B2Q(1),alpha=0.7,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=0.00000000000000000e+00; phase_resid=5.74635737428243914e-16 | PASS |
| G3[B2Q(1),alpha=0.7,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=1.33226762955018785e-15; phase_resid=7.19896908384460678e-16 | PASS |
| G3[B2Q(1),alpha=pi/3,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=1.77635683940025046e-15; phase_resid=4.03368667388874770e-16 | PASS |
| G3[B2Q(1),alpha=pi/3,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=2.66453525910037570e-15; phase_resid=9.20582855313245169e-16 | PASS |
| G3[Btoy,alpha=0.3,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=2.22044604925031308e-16; phase_resid=1.11022302462515654e-16 | PASS |
| G3[Btoy,alpha=0.3,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=0.00000000000000000e+00; phase_resid=1.11022302462515654e-16 | PASS |
| G3[Btoy,alpha=0.7,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=4.44089209850062616e-16; phase_resid=2.61845576667213508e-16 | PASS |
| G3[Btoy,alpha=0.7,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=0.00000000000000000e+00; phase_resid=1.57009245868377517e-16 | PASS |
| G3[Btoy,alpha=pi/3,m=0.1] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=2.22044604925031308e-16; phase_resid=1.11022302462515654e-16 | PASS |
| G3[Btoy,alpha=pi/3,m=0.5] | slogdet logabs equality and determinant phase identity | log<1.0e-09; phase<1.0e-10 | log_resid=0.00000000000000000e+00; phase_resid=1.24126707662363656e-16 | PASS |
| G4[B4free,alpha=0.3,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=2.91393646794427307e-15 | PASS |
| G4[B4free,alpha=0.3,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=1.66976458451096373e-15 | PASS |
| G4[B4free,alpha=0.7,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=5.36620025422423109e-16 | PASS |
| G4[B4free,alpha=0.7,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=2.32071456886134650e-15 | PASS |
| G4[B4free,alpha=pi/3,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=1.18459386534184373e-16 | PASS |
| G4[B4free,alpha=pi/3,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=1.24802310199208968e-15 | PASS |
| G4[B4rand,alpha=0.3,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=1.81172247717811585e-14 | PASS |
| G4[B4rand,alpha=0.3,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=5.12657471082411504e-15 | PASS |
| G4[B4rand,alpha=0.7,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=8.00241963095440696e-15 | PASS |
| G4[B4rand,alpha=0.7,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=1.84605264881274186e-15 | PASS |
| G4[B4rand,alpha=pi/3,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=9.48269007025751048e-15 | PASS |
| G4[B4rand,alpha=pi/3,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=3.44794363427710040e-15 | PASS |
| G4[B2Q(1),alpha=0.3,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=7.64682840691782119e-16 | PASS |
| G4[B2Q(1),alpha=0.3,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=3.54658581424633528e-16 | PASS |
| G4[B2Q(1),alpha=0.7,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=5.74635737428243914e-16 | PASS |
| G4[B2Q(1),alpha=0.7,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=7.19896908384460678e-16 | PASS |
| G4[B2Q(1),alpha=pi/3,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=4.03368667388874770e-16 | PASS |
| G4[B2Q(1),alpha=pi/3,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=9.20582855313245169e-16 | PASS |
| G4[Btoy,alpha=0.3,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=5.96037985002822259e-17 | PASS |
| G4[Btoy,alpha=0.3,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=8.75380130025642529e-17 | PASS |
| G4[Btoy,alpha=0.7,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=2.45551874705944676e-16 | PASS |
| G4[Btoy,alpha=0.7,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=1.73784038490735611e-16 | PASS |
| G4[Btoy,alpha=pi/3,m=0.1] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=1.15880045472754345e-16 | PASS |
| G4[Btoy,alpha=pi/3,m=0.5] | measure deposit times mass-det shift | <1.0e-10 | invariance_resid=2.24512894665323291e-16 | PASS |
| G4[Btoy,alpha=0.7,m=0.5,nontriviality] | abs(mass-det shift - 1) | >1.0e-01 | nontriviality=1.28843537447538181e+00 | PASS |
| G5a[B2rand,wrong-eps] | broken-premise anticommutator magnitude | >1.0e-01 | anticom=1.00000000000000022e+00 | PASS |
| G5a[B2rand,wrong-eps] | wrong-grading determinant identity rejector | >1.0e-03 | phase_resid=1.94381779301609520e-01 | PASS |
| G5b[B2rand,Dpert] | broken-anticommutation heat-index t-dependence | >1.0e-06 | abs(A0.3-A3.0)=1.79895233830061563e-01 | PASS |
| G6[Btoy,wrong-n] | reject tr(eps)+1 determinant phase | >1.0e-03 | phase_resid=1.28843537447538203e+00 | PASS |
| G6[B2Q(1),wrong-Q-as-n] | reject pretending n is set by Q | >1.0e-03 | phase_resid=1.28843537447538270e+00 | PASS |
| G7[Btoy,A_t] | toy A_t exactness over t=0.3,1.0,3.0 | <1.0e-10 | max_resid=4.44089209850062616e-16 | PASS |
| G7[Btoy,det] | toy determinant ratio exactness over G3 grid | <1.0e-10 | max_resid=2.61845576667213508e-16 | PASS |

Diagnostic line: `A_1(eps') = 8.64590992243524648e-03` for the wrong-grading B2rand check. Final runner line: `TOTAL: PASS=82 FAIL=0`.

## Boundary / Honest Auditor Read

This note does NOT supply theta_gauge's physical value or arg det M's physical value. It does NOT derive the continuum ABJ anomaly. It does NOT close `W_anomaly_covariant_assembly` in the nontrivial direction. It derives the fixed-grading bookkeeping exactly and locates nontrivial transfer in the (P1'-sharpened) supplier class.

The in-flight or unaudited names `THETA_BAR_ASSEMBLY_INTERFACE_BRIDGE_2026-07-01`, `THETA_4D_CARRIER_FLUX_COHOMOLOGY`, `ABJ_ANOMALY_FRAMEWORK_INTERNAL_U1_JACOBIAN_NARROW_NOTE_2026-05-27`, and `STRONG_CP_JOINT_BRIDGE_FAILS_HOLOMORPHIC_RESIDUAL_2026-06-04` are context, not premises. The J4 zero-index diagnostic of `ABJ_ANOMALY_FRAMEWORK_INTERNAL_U1_JACOBIAN_NARROW_NOTE_2026-05-27` is an L1 instance: a fixed balanced grading reports `tr(eps) = 0`, not a gauge-sector integer. `STRONG_CP_JOINT_BRIDGE_FAILS_HOLOMORPHIC_RESIDUAL_2026-06-04` previously checked paired-shift invariance numerically in one model; this note derives the law.

## Deps

- [ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md](ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md) - supplies the balanced square-block surface instance; ledger effective_status: retained_no_go.
- [ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md](ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md) - supplies the (P1'-sharpened) supplier-class framing; ledger effective_status: retained_bounded.
- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) - supplies the minimal axiom boundary for treating this as fixed finite-dimensional bookkeeping rather than a physical-value import.
