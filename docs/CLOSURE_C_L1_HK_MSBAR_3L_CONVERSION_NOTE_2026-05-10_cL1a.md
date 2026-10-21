# Closure C-L1a: conditional finite-coupling conversion through three loops

**Date:** 2026-05-10; source correction 2026-10-21.
**Claim type:** conditional algebraic theorem, with an open physical matching bridge.
**Status authority:** independent audit lane only. This source correction does not
promote a claim or add a framework premise.
**Primary runner:** [cl3_closure_c_l1a_2026_05_10_cL1a.py](../scripts/cl3_closure_c_l1a_2026_05_10_cL1a.py).

## 1. Exact formal statement and hypotheses

Suppose two dimensionless couplings describe the same theory in compatible
mass-independent schemes and have a scale-independent analytic finite map
with unit leading coefficient. Write the **explicit** directed map as

```
g_B = g_A + a g_A^3 + b g_A^5 + c g_A^7 + O(g_A^9),
beta_A(g) = -b0 g^3 - b1 g^5 - b2A g^7 + O(g^9).
```

The chain rule beta_B(g_B)=f'(g_A) beta_A(g_A) gives

```
b0B = b0,  b1B = b1,
b2B = b2A - 2 a b1 + (2 b - 3 a^2) b0.                 (1)
```

Indeed the g_A^7 coefficient on the chain-rule side is
`-b2A - 3 a b1 - 5 b b0`; on the beta_B side it is
`-b2B - 5 a b1 - (3b+3a^2)b0`. Equating them proves (1).
The coefficient c cancels from this order because it first affects g^9.
The runner checks coefficient identities with indeterminates, not selected
numerical points or a formula followed by its own rearrangement.

Explicit scale dependence in f contributes a separate partial derivative;
(1) does not apply to arbitrary log-dependent matching expressions at a
varying scale. Existence of the two physical schemes and matching map is a
hypothesis, not a consequence of finite polynomial algebra.

## 2. AFP convention and directed composition

Alles, Feo and Panagopoulos use an **implicit** bare coupling relation
at fixed matching scale:

```
g_W = g_MS (1 + z1 g_W^2 + z2 g_W^4 + ...).
```

Solving perturbatively gives the explicit maps

```
MS -> W: a=z1, b=z2+2z1^2,
W -> MS: a=-z1, b=z1^2-z2.
```

Only with this substitution does (1) become AFP's expression
`b2W=b2MS-2 z1 b1+(z1^2+2z2)b0`. Using this expression for
an explicit map with b=z2 was the convention error in the former note.
The discrepancy is `4 z1^2 b0`, nonzero in general.

For explicit A->B coefficients (a,b) and B->C coefficients (u,v),
substitution gives A->C `(a+u,b+v+3au)`. The inverse is
`(-a,3a^2-b)`. Applying (1) in two steps agrees identically with
applying it once to the composite. This establishes a conditional
factorization through Wilson when both maps exist; it does not establish
an HK-to-Wilson physical matching map.

Primary convention source: [AFP, hep-lat/9609025, Section II](https://arxiv.org/html/hep-lat/9609025v1),
*The three-loop beta function in SU(N) lattice gauge theories*, Nuclear
Physics B 491 (1997), 498–512. The earlier B502325 bibliographic entry was
incorrect. No additional literature claim is needed for the algebra above.

## 3. Supplied scalar examples and their limits

The runner evaluates the supplied QCD coefficient polynomials with
`CA=3, CF=4/3, TF=1/2, Nf=6`, obtaining stripped coefficients
`b0=7, b1=26, b2MS=-65/2`. They are inputs/examples, not a derivation of
QCD or its identification with the repository substrate. In the convention
`beta(g)=-b0*g^3-b1*g^5-b2*g^7`, the usual stripped coefficients carry
powers of `1/(16*pi^2)` respectively. One must keep this normalization
and Nf consistent on both sides of a conversion.

Separately, the supplied single-plaquette function
`P(s)=1-exp(-4s/3)` has Taylor coefficients `4/3,-8/9,32/81`.
**The coefficient 32/81 is not established as b2HK.** A one-variable
plaquette expectation alone does not specify the scale derivative of a
renormalized coupling, the multi-plaquette perturbation theory, or its
continuum matching. The former identification and its mixed Nf6/pure-gauge
comparison are withdrawn. Even the pure-gauge beta coefficient remains
open here. The historical [C-iso source](C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md)
is context for the supplied function, not certified physical input here.

For an explicitly supplied pure-gauge SU3 Wilson example the runner uses
`P1=.15493339`, `P2=.024013181`, and the rounded Wilson b2 polynomial
`(N/(16*pi^2))^3*(-366.2+1433.8/N^2-2143/N^4)`.
These constants are load-bearing imports for that example. It computes
z1 from the supplied AFP formula and **back-solves** z2 from b2W.
Substitution back is an arithmetic round-trip, not independent two-loop
matching or a literature validation. The existing relative `1e-10`
round-trip threshold and `1%` rounded Lambda-scaling comparator are
preserved. The latter uses the same imported b2W and is not an independent
measurement. The [T1 child](CLOSURE_T1_Z10_Z20_BZ_INTEGRALS_NOTE_2026-05-10_t1z10z20.md)
provides a separately scoped numerical/model diagnostic.

## 4. Open bridge and downstream impact

To apply (1) physically to HK and MSbar requires a defined renormalized HK
coupling, its beta function, a common continuum theory and normalization,
and actual matching coefficients. This note supplies none of their missing
perturbative integrals. It does not establish that only two missing scalar
integrals suffice to construct those objects, that the literature lacks
such integrals, or that symmetry and a plaquette formula prove universality.

Within an already supplied single-coupling analytic map, only a and b enter
the three-loop transformation. This formal parameter count is narrower
than closing the physical matching problem. No Lane1 prediction, alpha_s
value, physical Cl(3)/Z3 identification, upstream theorem, or audit status
is independently certified here. Prior claims of a new universal result,
complete scheme construction, hidden-parameter exclusion, and a derived
pure-gauge b2HK are withdrawn.

## 5. Reproduction

```
python3 scripts/cl3_closure_c_l1a_2026_05_10_cL1a.py
```

The runner reads no repository files or audit metadata. It imports SymPy
for exact polynomial checks and standard-library math. It reports formal
identities and supplied numerical arithmetic separately, and prints the
physical nonverification explicitly. The original all-green output is
not evidence for the withdrawn claims; failures exit nonzero.
