# Higgs Wilson-form candidate: fitted diagnostic and finite search

**Date:** 2026-05-10; scope correction 2026-10-21
**Type:** open_gate
**Status:** physical Higgs derivation open; supplied arithmetic and finite search only.
**Primary runner:** [companion](../scripts/cl3_higgs_mass_wilson_chain_2026_05_10_higgsH1.py)

The historical candidate was selected with PDG mass exposure. PDG125.25GeV
informed the choice of the factor `sqrt(1-2 alpha_s)`; it is not an independent
post-construction validation. Coefficient2 is uncomputed here. No one-loop
multiplicity or QCD self-energy derivation is supplied.

The supplied model is

```
P=.5934, M=1.221e19 GeV, alpha_bare=1/(4 pi), u=P^(1/4),
alpha_LM=alpha_bare/u, alpha_s=alpha_bare/u²,
v=M (7/8)^(1/4) alpha_LM^16,
m_curv=v/(2u), candidate=m_curv sqrt(1-2 alpha_s).
```

The plaquette, bare normalization, hierarchy readout and strong-coupling
identification are supplied premises, not consequences established by this
probe. M is the chosen scale conversion. The curvature symbol replaces the
old `m_H_tree` label: no pole-mass identification follows from this arithmetic.
See the [historical input inventory](COMPLETE_PREDICTION_CHAIN_2026_04_15.md)
and [curvature source](HIGGS_MASS_FROM_AXIOM_NOTE.md); their physical bridges
are not certified by this diagnostic.

Evaluation gives v246.3029905252253, curvature140.31458100936328 and fitted
candidate124.98181088142584GeV. Agreement with the exposed target is a fit
diagnostic. The original0.1%,0.05%,0.3% search bands remain descriptive
thresholds, not retention criteria or uncertainty estimates.

The actual finite search evaluates58968 tuples in
`a=-4..8, b=-4..4, c=-4..4, d=-3..3, N=13..20` for

```
M (7/8)^(a/4) 2^(-b) 3^(-d) u^c alpha_LM^N.
```

There are seven matches below0.1%. The minimum in this box occurs at
`(a,b,c,d,N)=(6,-3,3,2,16)`, value125.26734859018732GeV,
relative error0.00013851169810239465. This directly contradicts the old
no-match/0.29%-minimum narrative. It establishes neither a physical law nor
an exhaustive search of all integer exponents. The search does not implement
a formal exclusion of every algebraic representation containing8/9; it simply
uses the printed factors. Any physical prohibition of a color readout needs
its own derivation.

The runner checks finite identities, preserves the finite search and prints
historical sister-form comparisons. It no longer counts literal-True
firewalls or verdict text as evidence. Physical coefficients, matching,
uncertainties, pole conversion and any preferred expression remain open;
failure of one fitted form cannot prove that RGE is the unique repair route.

Original note and runner, including contradictory declarations and check
accounting, are recoverable at
`f24d17d97d372df977476e4a69674577f31af575` with their same paths.
No historical log or failed check is rewritten. Run the companion directly
for current bounded arithmetic; this does not replay the old claimed proof.
