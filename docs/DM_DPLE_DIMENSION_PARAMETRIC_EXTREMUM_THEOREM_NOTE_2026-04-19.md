# Critical points of log absolute determinant on Hermitian pencils

**Type:** bounded_theorem
**Date:** 2026-04-19; mathematical correction 2026-10-21.
**Status:** conditional matrix-analysis support; no physical selector or audit promotion.
**Primary runner:** `scripts/frontier_dm_dple_theorem.py`.
The stable filename records the original DPLE identity. The previous argument and execution counts are recoverable at f24d17d97d372df977476e4a69674577f31af575.

## 1. Setup and corrected classification

Let H0,H1 be Hermitian d by d matrices, H0 invertible, and p(t)=det(H0+t H1). The polynomial is real and nonzero, with degree n<=d (not necessarily d; H1 may be singular or zero). On the open nonsingular set define W(t)=log|p(t)|. Jacobi's identity gives

```text
W' = p'/p = Tr(H^-1 H1),
W'' = p''/p - (p'/p)^2.
```

At a critical point t*, require p(t*)!=0 and p'(t*)=0. Its one-dimensional Morse index is zero precisely when **p''(t*)/p(t*)>0**. Testing p''>0 alone classifies a minimum of p, not W. On a negative-determinant component a W minimum is a p maximum. A zero of p is outside W's domain, including a repeated zero where p' also vanishes. Degenerate points W''=0 are not Morse minima.

For an exact counterexample set x=t-1/2 and

```text
B(t) = [[x,1],[1,-x]],
p(t) = -(x^2+1),
p'(1/2)=0, p''(1/2)=-2, W''(1/2)=2.
```

This is a genuine d=2 W minimum, with H0 invertible and negative determinant throughout. Thus d=2 is neither vacuous nor excluded from the at-most-one-minimum case. The former runner missed this minimum.

## 2. Bound, with a proof for W rather than p

A nonconstant real degree-n polynomial has at most floor(n/2) nondegenerate local minima of log|p| on its whole nonsingular real domain, hence on (0,1). In particular the bound is floor(d/2) for this pencil. For constant nonzero p there are no Morse critical points.

Proof: let k be the number of distinct complex roots of p and r the number of distinct real roots. Cancel common factors in p'/p. Its numerator has degree k-1: logarithmic differentiation gives a sum of simple fractions m_j/(t-z_j), with positive integer multiplicities m_j and leading behavior n/t. There are therefore at most k-1 real zeros counted with multiplicity.

On the real axis W' is negative near minus infinity and positive near plus infinity. At each of its r real poles it changes from negative to positive, since the residue is positive. Let M and X count its zero crossings from negative to positive and positive to negative, respectively; zeros with no sign change do not contribute. Following signs along the real line gives M-X+r=1. Thus 2M+r-1=M+X<=k-1, so M<=(k-r)/2<=floor(n/2). Every nondegenerate W minimum is one of the M upward crossings. This also covers repeated roots and degenerate critical points without counting them as Morse minima. QED.

This is an upper bound, not an existence or selection principle. Both d=2 and d=3 have at most one such minimum. Any existence predicate is Boolean at every dimension; calling it a binary selector does not privilege d=3.

The bound can reach two at d=4. Let B_a(t)=[[t-a,1/8],[1/8,-(t-a)]] and H=B_(1/4) direct-sum B_(3/4). With x=t-1/2,

```text
p=x^4-(3/32)x^2+25/4096 > 0,
p'=x(4x^2-3/16).
```

The points t=1/2 +/- sqrt(3)/8 are nondegenerate W minima in (0,1); t=1/2 is a maximum. The runner verifies the determinants and curvatures exactly. This example does not establish anything about physical carrier dimension.

## 3. Cubic chart predicate, separately from the bound

For c3!=0, put Delta=c2^2-3 c1 c3. There are two distinct real stationary points iff Delta>0; Delta=0 is a degenerate stationary point. At

```text
t_plus=(-c2+sqrt(Delta))/(3c3), p''(t_plus)=+2sqrt(Delta),
t_minus=(-c2-sqrt(Delta))/(3c3), p''(t_minus)=-2sqrt(Delta).
```

The plus branch is the p minimum, but is the smaller root only if c3<0. The W minimum additionally requires p positive on the plus branch or p negative on the minus branch. If c3=0, use the actual lower-degree derivative; no cubic division is valid.

The legacy positive F4 predicate can be stated explicitly as existence of t in (0,1) with p'=0, p''>0 and p>0, optionally with c0>0 as an additional baseline condition. It equals a **positive-determinant W minimum** predicate. It is not equivalent to every W minimum. A count bound does not force F4 to hold, select a physical path, or select an endpoint.

The runner evaluates the four supplied decimal basin fixtures from the original chart, reports determinants/critical points separately and compares direct derivative-root classification with the cubic formula. These are finite chart diagnostics, not exact certification of rounded basin coordinates or a derivation of their physical relevance. No former expected basin table or PASS count is imposed.

## 4. Sign, inertia and path boundaries

Equal determinant signs do not imply equal Sylvester inertia: diag(1,1,1) and diag(1,-1,-1) both have positive determinant. Nor does positivity at one critical point establish nonsingularity along an entire path. For example H(t)=(t-9/10) direct-sum [[t-3/10,1/10],[1/10,-(t-3/10)]] has p=(9/10-t)[(t-3/10)^2+1/100]. It has p(0)>0 and a positive p-minimum at t=1/2-sqrt(33)/30, but crosses det=0 at t=9/10 before the endpoint.

The observable W is unchanged by p -> -p. For odd d the pencil transformation H -> -H implements that sign flip, though it need not preserve a chosen baseline, chamber or physical model. It therefore cannot by itself determine a physical determinant sign. This does not prohibit an additional supplied dynamics or sector identification from breaking that ambiguity. See [the scoped sign-blindness companion](DM_DPLE_ABCC_NO_GO_NOTE_2026-04-19.md).

A continuous nonsingular path preserves full inertia. Nonsingularity is an additional premise, not a consequence of continuity. The [P3 path note](DM_NEUTRINO_SOURCE_SURFACE_P3_SYLVESTER_LINEAR_PATH_SIGNATURE_THEOREM_NOTE_2026-04-18.md) concerns a specified path and endpoint; identifying that endpoint as physical remains separate. The current [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) does not supply the chart or selector used here.

## 5. Reproduction and limits

Run `python3 scripts/frontier_dm_dple_theorem.py`. Exact symbolic fixtures test domain exclusion, degree drop, both determinant signs, cubic branch order, d=2 nonvacuity and d=4 multiplicity. Numerical Hermitian sweeps and the supplied basin diagnostics test implementation consistency; they are not proofs of quantified bounds. The proof above supplies the bound. No source-side PMNS closure, observational exclusion, global path certificate or audit grade follows from a successful runner.

## Audit dependency repair links

This preserves the existing source relationship without assigning status:

- [P3 specified-path source](DM_NEUTRINO_SOURCE_SURFACE_P3_SYLVESTER_LINEAR_PATH_SIGNATURE_THEOREM_NOTE_2026-04-18.md).
- Downstream context: `SCALAR_SELECTOR_CYCLE1_SCIENCE_REVIEW_NOTE_2026-04-19.md` and `SCALAR_SELECTOR_SYNTHESIS_NOTE_2026-04-19.md`.
