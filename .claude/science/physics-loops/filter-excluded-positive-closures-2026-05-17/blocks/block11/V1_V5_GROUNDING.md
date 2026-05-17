# Block 11 V1-V5 Grounding

**Date:** 2026-05-17
**Block:** u0-plaquette-quartic-derivation

## V1 — Independent of blocks 08, 10

Three distinct exponents/maps in the tadpole-improvement chain:

| Block | What is derived | Object type |
|-------|-----------------|-------------|
| 08 | `n_link = 2` (exponent on `u_0` in `alpha_s(v) = alpha_bare / u_0^{n_link}`) | exponent on u_0 in coupling map |
| 10 | The map `M: alpha_bare → alpha_bare / u_0^2` itself | coupling-rescaling map |
| 11 | `1/4` (exponent on `<P>` in `u_0 = <P>^{1/4}`) | exponent on <P> in plaquette map |

These are not equivalent under any algebraic relabeling:

- The exponent `n_link = 2` lives on the coupling-space side
  (`alpha_bare ↦ alpha_s(v)` direction).
- The exponent `1/4` lives on the plaquette-space side
  (`<P> ↦ u_0` direction).
- The map `M` is the composition of two coupling-space rescalings.

The numbers `2` and `1/4` arise from different counting principles:
`2` from vertex insertions (one per gauge link in the
vacuum-polarization channel), and `1/4` from loop length (four links
per elementary plaquette). The two counts are independent: a triangular
plaquette would give exponent `1/3` for `u_0 vs <P>` while still
having `n_link = 2` for the vertex count.

## V2 — A_min only

Two named inputs in the derivation:

- **(P1)** "Elementary plaquette is the ordered product of four
  gauge-link variables." This is the **geometric incidence statement**
  on a cubic lattice: each elementary square face has exactly four
  bordering edges. It is local cubic-lattice geometry; no field-theory
  axioms beyond the lattice structure are consumed.

- **(P2)** Tree-level mean-field unit-normalization principle (named
  external admission, Lepage-Mackenzie 1993).

No other axioms enter. The proof is two algebraic steps:
factorization-by-scalar (a property of matrix multiplication) and
unique positive fourth root (an arithmetic fact on `R^+`).

## V3 — No fitted u_0, no PDG

The runner verifies:

- All algebraic steps over abstract sympy positive-real symbols.
- The numerical scan in Part 9 uses 10 test points across multiple
  orders of magnitude (0.01 to 100.0), explicitly NOT consuming any of
  them as load-bearing imports. The value 0.5934 appears as one test
  point only because it overlaps with the canonical
  beta = 6 SU(3) lattice regime; the runner explicitly flags it as
  "test value, not load-bearing."
- No specific gauge group (works for any `N ≥ 1` abstract).
- No fitted selectors, no comparison to observed `u_0`.

## V4 — Not a relabeling of an already-landed cycle

Searched repo for prior derivations of the `1/4` exponent specifically:

```bash
$ grep -lE "u_0.*=.*<P>\^\(?1/4\)?" docs/ | head -5
docs/ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md
docs/U0_SU2_BIVECTOR_IRREP_ANALYTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md
```

Inspection of both:

- The 2026-05-10 vertex-power note treats `u_0 = P^(1/4)` as a
  parametrized algebraic substitution `(T6)` with abstract positive
  `P`. The exponent `1/4` is taken as the convention; it is not
  derived.
- The 2026-05-17 SU(2) bivector note explicitly admits the
  `u_0 = <(1/N) Re Tr U_p>^{1/4}` form as **named external admission
  `(X3)`**, citing Lepage-Mackenzie 1993. The `1/4` exponent itself is
  not derived.

The current block 11 closes the previously-convention-only `1/4`
exponent by deriving it from `(P1) + (P2)`. This is a genuine
structural derivation, not a relabeling.

## V5 — Honest bounded scope

- Author tier: `bounded_theorem` (not `retained`).
- The principle `(P2)` itself remains a named external admission.
- The numerical `<P>` evaluation remains in a separate bounded chain.
- The downstream `alpha_s(M_Z)` lane retains its own bounded scope
  statement in `ALPHA_S_DERIVED_NOTE`.

The closure adds the `1/4` exponent as a structurally-derived quantity
(not a convention), reducing the set of unaudited external admissions
in the tadpole chain by one. It does not promote any retained-tier
authority; it does not close the full chain.

## Done

All five V-checks pass. Proceed to build phase.
