# Graviton TT Spatial Spectral Tower on Round S³

**Claim type:** bounded_theorem (supplied conditional scope; no audit status change)

**Date:** 2026-04-24; scientific interpretation corrected 2026-10-21

**Status:** **proposed_retained structural-identity extension theorem** on `main`.

The dated status label above is not changed by this source repair. The
scientific content is the spatial spectrum and its ratios below, not a
particle-mass or Higuchi-stability theorem. Original text is recoverable at
Git base f24d17d97d372df977476e4a69674577f31af575.

**Script:** `scripts/frontier_graviton_spectral_tower.py`

## Operator and premises

On a round spatial S³ of radius R>0, let the TT tensor harmonics obey

```text
-D^k D_k Y_ij^(l) = lambda_l Y_ij^(l),
D^i Y_ij^(l)=0,  g^ij Y_ij^(l)=0,
lambda_l = [l(l+2)-2]/R²,       l=2,3,... .
```

The displayed convention is the rough (connection) Laplacian on TT tensors.
A Lichnerowicz operator includes additional curvature terms; its eigenvalues
must not be identified with this expression without specifying conventions.
The spectrum is a standard supplied geometric input here. This packet does
not derive roundness or physical selection of this background from the
framework axioms.

For orientation, the original upstream handles are
`GRAVITON_MASS_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`,
`S3_GENERAL_R_DERIVATION_NOTE.md`, and `S3_CAP_UNIQUENESS_NOTE.md`.
Their status and physical conclusions are not established by this calculation.

## T1: spatial wave-number and momentum scales

Define `q_l=sqrt(lambda_l)` and `p_l=hbar*q_l`. Then

```text
q_l² = [l(l+2)-2]/R²,
p_l² = hbar² [l(l+2)-2]/R².
```

These label spatial variation on a compact slice. They are not rest masses.
Multiplying by c gives the dimensional spectral energy scale
`E_l=c*p_l`; dividing p_l by c would only define a mass-equivalent unit,
not derive a physical mass parameter. No extra compact internal dimension or
4D massive-field equation is supplied here.

## T2: squared-ratio identities

```text
(p_l/p_k)² = lambda_l/lambda_k
          = [l(l+2)-2]/[k(k+2)-2] in Q.
```

The squared ratios, not generally the ratios themselves, are rational.
Examples relative to l=2 are 13/6, 11/3, 11/2 and 23/3 for l=3,4,5,6.
The adjacent eigenvalue numerator difference is 2l+3.

## T3: conditional curvature comparison, not a Higuchi test

If the comparison radius is additionally identified with the de Sitter
curvature radius ell, so that Lambda=3/ell² and R=ell, then

```text
lambda_l/(2 Lambda/3) = [l(l+2)-2]/2 >= 3,
```

with equality only at l=2. This follows because the numerator increases with
l. It compares inverse-length-squared quantities. The Higuchi bound concerns
the mass parameter of a massive spin-2 field on de Sitter, not spatial
wave-number eigenvalues, and is not tested by this inequality.

A massless linearized gravitational field already has nonzero spatial TT
harmonics: in global conformal de Sitter coordinates its amplitude obeys
`H''+2 tan(T) H'+[q_unit²+2]H=0`, where
`q_unit²=l(l+2)-2`. There is no Fierz-Pauli mass term. See
[Anninos, Ng and Strominger, Appendix A](https://arxiv.org/html/1106.1175).
This separates spatial momentum and curvature terms from a rest mass.

The global spatial radius is `a(t)=ell*cosh(ct/ell)`. On that physical slice,

```text
lambda_l(t)/(2 Lambda/3) = [l(l+2)-2] / [2 cosh²(ct/ell)].
```

It is not a time-independent lower bound of 3. The comparison R=ell applies
at the minimum-radius slice or on an auxiliary sphere, as explained in
[COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md](COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md).

## Numerical illustration and boundary

The runner retains the supplied R=c/H_0 pin for a dimensional illustration.
Its lowest `E_l=hbar*c*sqrt(lambda_l)` is about 3.52e-33 eV. These are spectral
energy scales, not inferred particle masses, detection predictions, or a
mass-limit comparison. Neither a cosmological value of R nor a physical
massive-graviton readout is derived. No new target or fit is introduced.

## Verification

```bash
python3 scripts/frontier_graviton_spectral_tower.py
```

The original 89 algebraic checks remain; their labels now state momentum
scales or conditional curvature comparisons. They do not certify the
geometric spectrum from a discretization or prove any physical mass mapping.
