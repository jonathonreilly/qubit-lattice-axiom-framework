# EW kappa_EW: conditional color algebra and an unsupplied readout weight

**Date:** 2026-06-08
**Type:** bounded_theorem
**Status:** source repair; no retained-status or physical matching verdict.
**Scope:** finite matrix identities and nonidentifiability from supplied channel data alone. The historical filename does not assert universal Monte Carlo impossibility.

**Primary runner:** [frontier_ew_kappa_self_energy_object_pin.py](../scripts/frontier_ew_kappa_self_energy_object_pin.py), expected PASS=20 FAIL=0. Historical text is recoverable at Git revision `f24d17d97d372df977476e4a69674577f31af575` under this note's path.

## 1. Supplied mathematical object

For an arbitrary complex `N x N` matrix `M`, with Hermitian traceless generators normalized by `Tr(t_A t_B)=delta_AB/2`, set

```text
T = Tr(M M^dag), S = |Tr M|^2/N,
C = 2 sum_A |Tr(M t_A)|^2, T = S+C.
```

This is the Hilbert–Schmidt orthogonal decomposition into scalar and traceless matrices. It does not say `C/T=8/9` for a fixed matrix: `M=I` has `C=0`. For independently Haar-averaged transformations at distinct endpoints, `M -> U M V^dag`, the second-moment identity gives `<S>=T/N^2`, `<C>=(1-1/N^2)T`. Thus `<C>/<T>=8/9` for `N=3` and nonzero norm. This fraction is independent of dressing or beta under those averaging hypotheses. Same-site conjugation, gauge fixing, fixed matrices and physical vertex kernels are not covered. No topological identification with a genus expansion follows from this dimension ratio alone.

For an invertible massive staggered operator satisfying `D_m^dag=eps D_m eps`, its inverse obeys `G^dag=eps G eps`. Consequently, for a block `M=G(x,y)`,

```text
Tr[G(x,y)G(y,x)] = p_xy Tr(M M^dag) = p_xy(S+C),
p_xy=eps(x)eps(y).
```

The raw reversed-block trace can be negative at opposite parity. `T` is its nonnegative sign-adjusted color factor. The runner checks the reflection on one finite random-SU(3) background, including all site pairs; this is numerical support for the algebraic implication, not an ensemble or continuum calculation.

## 2. Conditional internal-color factorization, not a physical object pin

If the kernel is supplied to be `(Q tensor M)(Q tensor p_xy M^dag)`, its trace is exactly `p_xy Tr(Q^2)(S+C)`. A traceless `Q` need not remove the scalar-color contribution: `Q=T_3`, `M=I_3` gives `Tr(Q^2)=1/2`, `S=3`, `C=0`.

This unadorned bilocal matrix trace has **not** been identified here with the full point-split EW-current self-energy. A point-split current carries gauge links, displaced endpoints, vertex factors and Wick signs; their contraction and continuum matching must be supplied and checked separately. Color-blindness alone does not erase them. The runner's tensor-product calculation verifies only the explicitly supplied kernel above.

## 3. Readout nonidentifiability on the stated data surface

Supply data `{S,C,T=S+C}` with no equation relating a parameter `kappa` to those data, and define a family of formal readouts `Pi_kappa=C+kappa S`. The same data admit `Pi_0=C` and `Pi_1=T`. More precise measurement of those same data does not add the absent equation. This is a bounded identifiability statement about an externally supplied parameter, not a theorem that all Monte Carlo methods or all possible matched observables fail to determine a physical coupling.

A scalar rescaling `M -> zM` multiplies both channels by `|z|^2` and does not select `kappa`. Traceless projection removes `S`; identity readout retains it. These are mathematical operations. Neither their status as physically admissible renormalization schemes nor their applicability to a gauge-invariant EW self-energy has been proved here. An additional matching condition or a new observable with specified parameter dependence may determine or constrain a physical coefficient.

With the further supplied parametrization `F=8/9` and `K(kappa)=1/[F+kappa(1-F)]`, one obtains `K(0)=9/8` and `K(1)=1`. For real coupling rescalings take a positive denominator. If both `g_1` and `g_2` are multiplied by the same `sqrt(K)`, their ratio and `g_1^2/(g_1^2+g_2^2)` are unchanged. This conditional cancellation does not derive either coupling or the physical readout. No pole-mass or experimental accuracy comparison is made.

## 4. Dependencies and historical context

The displayed results use finite matrix algebra, the stated epsilon-hermiticity hypothesis and independent endpoint Haar averaging. They do not require an inherited physical no-go as a premise. Earlier discussions are context, not proof of physical admissibility:

- [EW current Fierz channel decomposition](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md): channel notation and projection distinction.
- [EW matching-rule open gate](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md): historical matching question.
- [Traceless-generator selector note](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md): historical generator argument.
- [RCONN note](RCONN_DERIVED_NOTE.md): historical Monte Carlo interpretation.
- `SUPPLIED_MATRIX_HILBERT_SCHMIDT_HAAR_IDENTITIES_NOTE_2026-10-24.md`: the
  separately landed positive owner of the Hilbert–Schmidt, endpoint-Haar,
  epsilon-reflection, tensor-product and parameterized identities of §§1–3.
  The narrowed nonidentifiability statement here is not a premise of that note.

This repair does not reconfirm the retained labels or all claims of those notes. The runner uses NumPy and SymPy, with fixed seeded numerical examples, and reads no repository note or experimental input.

## 5. Negative-claim discipline and limits

The only negative result is the elementary nonidentifiability under §3's explicit absence of a parameter-data equation. It is not a physical no-go certification.

- **N1 routes examined:** full norm measurement determines `T`; channel measurement determines `S,C`; tracelessness of the internal generator fails to eliminate scalar color by the `Q=T_3,M=I` counterexample; large-N dimension counting supplies a size ratio, not a readout equation; scalar renormalization rescales both channels. The first two share the same data-only wall and are not independent physical exclusions.
- **N2 wall independence:** there is one wall, the missing readout relation, not five independent obstructions.
- **N3 hidden assumptions:** endpoint averaging, epsilon-hermiticity and the supplied tensor-product kernel are explicit. Physical current identification is not assumed established.
- **N4 residual:** the unresolved quantity is a matched physical readout, beyond the formal `Pi_kappa` family.
- **N5 rhetoric and resolution:** per_element means finite matrix identities; per_block means the supplied color/internal blocks; per_site means the finite numerical epsilon-hermiticity example only; per_mode has no physical mode-selection result; lattice_wide has no continuum matching result. None is a physical bridge certificate.
- **N6 partial closure:** a specified matching relation could close the question; no exhaustive claim about all registered primitives is made.
- **N7 steelman:** a physical renormalization condition or parameter-dependent observable can constrain a coefficient. That route remains open, not excluded by this note.
- **N8 earlier-cycle lesson:** algebraic fractions and Monte Carlo agreement with those fractions do not by themselves establish a physical readout. The earlier object-pin and universal-MC wording is withdrawn here.

No independent retained no-go gate result is claimed. The open work is the actual point-split contraction, gauge-invariant observable construction, renormalization conditions and continuum matching, including proof of any proposed scheme's admissibility.

## 6. Verification and safe claim

Run `python3 scripts/frontier_ew_kappa_self_energy_object_pin.py`. The exact algebra and finite numerical diagnostics support the supplied identities and conditional cancellation. Finite examples do not prove universal physical statements.

Safe claim: the supplied channel data alone do not fix an independently introduced readout parameter. Unsafe claims include “the physical EW self-energy is pinned,” “both readouts are admissible physical schemes,” “no lattice measurement can decide kappa,” and “the 9/8 matching rule is derived.”
