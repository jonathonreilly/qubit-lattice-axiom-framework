# Closure T1 — Supplied Wilson integral and conditional coupling-map algebra

**Date:** 2026-05-10
**Claim type:** bounded_theorem — conditional formal identities and finite numerical diagnostic (SU(3), N_f=0)
**Sub-gate:** Lane 1 (alpha_s) --- L1 channel-weight admission sub-piece (a),
HK <-> MSbar 3-loop scheme conversion at SU(3) (children of PR #1059).
**Status authority:** independent audit lane only; effective status is
pipeline-derived. This note proposes a source theorem for review; it
does not claim retention of any new numerical content.
**Source-note proposal disclaimer:** this note is a source-note proposal;
audit verdict and downstream status are set only by the independent
audit lane. No new primitive proposed here is admitted as a framework
premise, and this note does not change the physical Cl(3) local
algebra / Z^3 spatial substrate baseline.

**Primary runner:** [`scripts/cl3_closure_t1_z10_z20_2026_05_10_t1z10z20.py`](../scripts/cl3_closure_t1_z10_z20_2026_05_10_t1z10z20.py)
**Parent note:** [`CLOSURE_C_L1_HK_MSBAR_3L_CONVERSION_NOTE_2026-05-10_cL1a.md`](CLOSURE_C_L1_HK_MSBAR_3L_CONVERSION_NOTE_2026-05-10_cL1a.md) (PR #1059)

## Scope and correction

This note estimates the tadpole integral of a **supplied four-dimensional
Wilson symbol** and checks formal coupling transformations. The physical
Cl(3)/Z^3 axioms do not select that symbol. It does not compute HK two-loop
matching constants. The earlier numerical HK-to-MS values mixed an implicit
AFP convention with an explicit map, including its direction, and are
withdrawn. The parent note is historical context, not authority overriding
the chain-rule calculation below.

## Wilson tadpole

For `D(p)=4 sum_mu sin²(p_mu/2)` in four dimensions,

`P1 = (2pi)^(-4) integral_[-pi,pi]^4 1/D(p) d^4p`.

Near zero `D(p) ~ |p|²`; the integrand is unbounded but integrable in four
dimensions, not a removable singularity. The runner uses shifted midpoint
meshes 24,32,40,48 and two-point Richardson extrapolation with power2. The
estimate is approximately 0.1549334402, agreeing with the supplied literature
comparator 0.15493339 to relative tolerance 1e-6. This is a numerical diagnostic,
not a rigorous remainder bound. Independently, Laplace separation gives
`P1 = integral_0^infinity [exp(-2t) I0(2t)]^4 dt`; one-dimensional quadrature
provides a distinct numerical check.

## Explicit map theorem and AFP convention

Define `beta_A(g)=-b0*g³-b1*g⁵-b2_A*g⁷+O(g⁹)` and the explicit map

`g_B = g_A + a*g_A³ + b*g_A⁵ + O(g_A⁷)`.

Then inversion, composition and the chain rule give

```
g_A = g_B - a*g_B³ + (3a²-b)*g_B⁵ + O(g_B⁷)
(a,b) followed by (d,e) = (a+d, b+e+3ad)
b2_B = b2_A - 2a*b1 + (2b-3a²)*b0.
```

The runner checks each identity as a polynomial series, including the inverse.
For the beta identity, expand `(dg_B/dg_A)*beta_A` in `g_B` using the inverse;
the coefficients of degrees3,5 remain `-b0,-b1`, and degree7 gives the formula.

[Allés, Feo and Panagopoulos, hep-lat/9609025](https://arxiv.org/abs/hep-lat/9609025),
Nucl. Phys. B491 (1997) 498–512, instead use the **implicit** relation at
zero matching logarithm

`g_W = g_MS * (1 + z1*g_W² + z2*g_W⁴ + ...)`.

Thus explicit MS-to-W has `(a,b)=(z1,z2+2z1²)`, while explicit W-to-MS has
`(a,b)=(-z1,z1²-z2)`. Substitution gives AFP's consistent identity

`b2_W = b2_MS - 2z1*b1 + (z1²+2z2)*b0`.

The `+z1²` term is correct in this implicit convention; it is incorrect if
one treats `z2` as the explicit degree5 coefficient. The earlier reference
hep-lat/9605013 was unrelated and is removed.

## Supplied numerical coefficients

At SU(3), Nf=0 the runner imports `P2=0.024013181` and uses

`z1 = N[1/(96pi²)+1/(16N²)-1/32-5P1/72-11P2/6]`.

With `q=N/(16pi²)`, it supplies `b0=11q/3`, `b1=34q²/3`,
`b2_MS=(2857/54)q³`, and the rounded literature expression
`b2_W=q³[-366.2+1433.8/N²-2143/N⁴]`. It backsolves `z2` using the
implicit identity. The roundtrip is an arithmetic consistency check, not an
independent derivation or validation of the supplied three-loop coefficient.
All coefficients use the same beta normalization and Nf=0.

## Conditional single-plaquette model

The supplied power series from the historical
[C-iso source](C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md) are

```
P_H(s) = 4s/3 - 8s²/9 + 32s³/81 + O(s⁴)
P_W(s) = 4s/3 - s²/9 + c3*s³/27 + O(s⁴).
```

They are treated as model inputs here, not independently certified lattice
expectations. Solving `P_W(s_W)=P_H(s_H)` gives

` s_W=s_H+alpha*s_H²+beta*s_H³`,
` alpha=-7/12`, `beta=(3/4)[32/81+2alpha/9-c3/27]`.

With the supplied identification `s=g²/2`, the explicit H-to-W map has
`a_HW=alpha/4`, `b_HW=beta/8-alpha²/32`. The runner checks the substitution
through cubic order in `s` and the coupling square root through degree6.
For a concrete illustration only it imports the fitted value `c3=-4.33`.
There is no supplied uncertainty bound on that fit and no proof that the
single-plaquette map dominates or equals full gauge-coupling matching.

Only after converting the AFP map to explicit W-to-MS can it be composed:

```
a_HM = a_HW-z1
b_HM = b_HW+(z1²-z2)-3*a_HW*z1.
```

These are conditional coefficients of the supplied composite model. Calling
them derived physical HK matching constants requires HK vertices, matching
integrals, and a bridge between the plaquette and gauge-coupling definitions.
Those obligations remain open. Pure-gauge data cannot supply Nf=6 matching;
the former mixed-normalization TVZ comparison and its unsupported dominance
language are withdrawn. No two-loop diagrams, fermion matching, physical
alpha_s prediction, or retained-status promotion follow from this runner.
