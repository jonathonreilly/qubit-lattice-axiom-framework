# Post-Record Selector/Tangent Readout Weight Prototype

**Date:** 2026-06-06
**Updated:** 2026-07-12
**Type:** bounded_theorem / explicitly accepted finite-packet arithmetic
**Claim type:** bounded_theorem
**Status:** proposed_retained exact finite-packet theorem; independent audit is
required before effective status changes;
audit_required_before_effective_retained=true; bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.py`](../scripts/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.txt)
**Diagnostic inventory helper (not a theorem dependency):**
`scripts/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.py`
with cache
`logs/runner-cache/frontier_post_record_measure_weight_normalization_subdivision_2026_06_06.txt`

## Result

This block proves exact finite readout/tangent-weight arithmetic for one
explicitly accepted packet:

```text
explicitly accepted finite carrier, weights, and maps
  + explicitly accepted symmetric positive-definite metric/Hessian
  => exact normalized push-forward weights and positive quadratic form
```

The result is a theorem about the accepted mathematical packet, not a
derivation of that packet from Record. The live
`selector_tangent_readout_weight` ledger bucket is printed only as a diagnostic
snapshot. Its cardinality is not a theorem premise and cannot make this
arithmetic pass or fail.

## Explicit supplied-packet bridge theorem

### Accepted local premises

For this theorem only, the supplied packet is explicitly accepted as local
mathematical hypotheses, not as framework primitives, chain-satisfying physics
premises, or physical authority:

1. The supplied packet carrier is
   \(C = \{c_0, \ldots, c_{15}\}\), with raw rational weight
   \(u(c_i)=1\) for every \(i\).
2. The supplied endpoint map is
   \(e(c_i)=\texttt{endpoint_lo}\) for \(0\leq i<4\), and
   \(e(c_i)=\texttt{endpoint_hi}\) otherwise.
3. The supplied readout map is
   \(r(c_0)=\texttt{ground}\) and
   \(r(c_i)=\texttt{excited}\) for \(1\leq i<16\).
4. The supplied tangent metric/Hessian and tangent vector are
   \[
   G=\begin{pmatrix}3&1\\1&2\end{pmatrix},
   \qquad v=\begin{pmatrix}1\\1/2\end{pmatrix}.
   \]

No value in this list is inferred from a ledger row, an observed target, a
fit, or the Record axiom. These are the complete non-derived inputs to the
claim scope.

### Theorem

Let \(C\) be a nonempty finite carrier with supplied weights
\(u(c)\in\mathbb Q_{\geq0}\) and \(U=\sum_{c\in C}u(c)>0\). For any supplied
map \(f:C\to Y\), define

\[
p_f(y)=\frac{\sum_{c:f(c)=y}u(c)}{U}.
\]

Then every \(p_f(y)\) is nonnegative and
\(\sum_{y\in f(C)}p_f(y)=1\). If a supplied symmetric matrix
\(G=\bigl(\begin{smallmatrix}a&b\\b&d\end{smallmatrix}\bigr)\) satisfies
\(a>0\) and \(\det G>0\), then \(x^T Gx>0\) for every nonzero
\(x\in\mathbb Q^2\).

For the supplied packet above, the theorem gives exactly

\[
(p_e(\texttt{endpoint_lo}),p_e(\texttt{endpoint_hi}))=(1/4,3/4),
\]
\[
(p_r(\texttt{ground}),p_r(\texttt{excited}))=(1/16,15/16),
\]
\[
\det G=5>0,\qquad v^T Gv=9/2.
\]

### Proof

Nonnegativity follows from \(u(c)\geq0\). Because the nonempty fibers
\(f^{-1}(y)\) partition \(C\), summing their numerators gives \(U\), so the
normalized push-forward sums to one. For the quadratic form,

\[
x^T Gx
=a\left(x_1+\frac{b}{a}x_2\right)^2
+\frac{\det G}{a}x_2^2.
\]

Both coefficients are positive; the two squares can vanish simultaneously
only when \(x=0\). Thus \(G\) is positive definite. Direct finite sums on the
two supplied maps give \(4/16,12/16\) and \(1/16,15/16\); direct rational
arithmetic gives \(\det G=3\cdot2-1=5\) and \(v^TGv=9/2\). This closes the
finite readout/tangent weight arithmetic inside the explicitly accepted packet.

## 2026-06-18 Record-axiom non-supply repair

The current Record axiom
([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)) is an approved
axiom-premise node for fixed records and finite scalar readout additivity. It
explicitly does not supply context selection, measurement basis selection,
Born weights, probability rules, source/action or physical-observable
identification, a tangent metric, or a Hessian.

The theorem above neither needs nor asserts such a derivation: packet
provenance is excluded from its claim scope. Consequently, its exact
finite-packet conclusion can be reviewed independently of the still-open
physical supplier problem. It remains not selector/tangent/readout authority.

## 2026-07-12 missing-bridge closure

The audit blocker asks for a retained bridge deriving or explicitly accepting
the selector/tangent/readout carrier, readout weights, and positive tangent
metric/Hessian, or else for the row to remain scoped as supplied-support only.

This repair takes the explicit-acceptance route. The carrier, raw weights, two
maps, metric/Hessian, and test vector are enumerated above and accepted as
local mathematical hypotheses of the bounded theorem. They are supplied finite packet data.
The proof derives every claimed output from exactly those inputs.
This acceptance does not register them as framework primitives. The theorem
does not derive selector/readout/tangent authority from Record or make a claim
about the packet's physical origin. Record-derived selector/readout/tangent authority remains open.

## Meaning

The theorem certifies finite tangent/readout weights, positive supplied
quadratic form, and exact projection/readout normalization for its accepted
packet. It cannot certify
that the readout is the selected physical selector, that a missing endpoint is
chosen, or that Record derives the selector, metric, readout map, Born law, or
physical measure.

## Boundaries

- Does not edit `docs/audit/data`.
- Does not apply or predict audit verdicts.
- Does not promote any row.
- Does not derive a selector, tangent metric, Hessian, projection map, readout
  primitive, source law, or Born law from Record.
- Does not derive a readout context, central-sector decomposition, fixed
  `K`/CPT structure, weighting rule, normalization authority, probability law,
  measurement dynamics, tangent metric, or Hessian from the Record axiom.
- Does not select or force a generation/Koide dial location.
- Does not derive production dynamics, a kernel, Hamiltonian, instrument,
  clock/rate, or physical arrow.

## Runner certificate

The runner constructs the complete accepted packet, checks that its carrier,
weights, maps, and symmetric positive-definite metric/Hessian satisfy the
theorem contract, and then recomputes the exact rational outputs. It also
prints the current live diagnostic row count without treating that count as a
premise, verifies stable semantic source anchors, preserves the audit-ledger
hash. Its final uppercase fields are informational scope declarations, not
self-verifying tests of absent physical derivations or audit actions.

Run:

```text
python3 scripts/frontier_post_record_selector_tangent_readout_weight_prototype_2026_06_06.py
```

## Audit dependency repair links

The prior conditional review named
`POST_RECORD_MEASURE_WEIGHT_NORMALIZATION_SUBDIVISION_2026-06-06.md` as a
diagnostic inventory surface. It is deliberately not a Markdown dependency
because it supplies no premise used by the exact finite-packet proof.
