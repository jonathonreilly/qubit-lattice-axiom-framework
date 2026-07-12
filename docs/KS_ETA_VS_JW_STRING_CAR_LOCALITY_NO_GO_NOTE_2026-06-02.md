# KS Eta Versus Jordan-Wigner String CAR Locality No-Go

**Date:** 2026-06-02
**Claim type:** no_go
**Runner:** `scripts/ks_eta_vs_jw_string_car_locality.py`

This note tests a narrow algebraic route: whether matter-attachment locality
plus the Kogut-Susskind staggered construction forces cross-site CAR
anticommutation. The answer is no. The staggered `eta_mu(x)` signs are
Dirac/taste c-number link coefficients. The Jordan-Wigner string is the
operator-valued statistics object. They are orthogonal.

The framework baseline is
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): Lattice supplies
`Z^3`, Qubit supplies the one-qubit local algebra, and Record is irrelevant to
this statistics question. The tested route does not add a new primitive or
statistics rule.

## Result

On a `2 x 2 x 2` `Z^3` qubit patch, the runner builds the same staggered
hopping coefficients in two realizations:

- hard-core boson ladders `b_x = sigma_+^(x)`, which are single-site,
  nilpotent, single-occupancy operators and commute across sites;
- Jordan-Wigner dressed operators `c_x = S_x sigma_+^(x)`, which satisfy CAR
  because of the string `S_x = product_{y < x} sigma_3^(y)`.

Both realizations carry the same Kogut-Susskind `eta_mu(x)` link signs. The
decisive counterfactuals are:

```text
keep eta, drop the string  -> CAR fails
drop eta, keep the string  -> CAR holds
```

In the displayed finite operator construction, the staggered eta signs neither
supply nor are needed for CAR. Locality also does not supply the string in the
displayed ungraded Pauli-tensor
representation: the maximally endpoint-local ladder has no string, while every
Jordan-Wigner order on the patch has a nearest-neighbor link with a
non-endpoint tail.

## Scope

This is not a no-go against fermions on `Z^3`. The Jordan-Wigner frame exists.
The claim is that the tested locality-plus-KS route does not force it over
the hard-core-boson frame. A future graded-locality/braiding rule or
lattice-native statistics derivation remains open and would need explicit owner
approval or an independent derivation. Fermion-parity superselection may
accompany that structure, but parity alone is shared by both frames and does
not select their cross-site braiding.

## No-Go Discipline Gate

This gate applies to the route above: deriving cross-site CAR from the
staggered eta signs plus locality.

### N1 - Alternative Route Enumeration

| Route | Marker | What it attempts | Result |
| --- | --- | --- | --- |
| Eta-as-statistics | `ATTEMPTED` | Treat `eta_mu(x)` as the CAR sign. | C5 counterfactuals show CAR rides the string, not eta. |
| Locality-generates-string | `ATTEMPTED` | Require matter operators to be local and infer the string. | C2 exhibits endpoint-local hard-core ladders without CAR. |
| Single-valuedness | `ATTEMPTED` | Use single-valued fields to select the graded frame. | Both finite frames are single-valued. |
| Per-site nilpotency | `ATTEMPTED` | Upgrade `b_x^2=0` to cross-site anticommutation. | C3 has nilpotency without cross-site CAR. |
| Same-algebra route | `ATTEMPTED` | Use the shared ungraded matrix algebra to claim CAR is forced. | C6 finds the same full ungraded algebra in both frames. |
| Order-choice route | `ATTEMPTED` | Choose a total order that removes all strings on nearest-neighbor links. | C7 enumerates all patch orderings and leaves a nontrivial tail. |
| Parity-involution route | `ATTEMPTED` | Use the global parity involution to select the fermion frame. | C4 verifies that the same parity anticommutes with bare hard-core ladders and JW fermions, so parity does not select their braiding. |

### N2 - Wall Independence

The collapsed wall is the graded statistics selector. Eta signs supply
Dirac/taste structure; a separate string or graded-locality principle supplies
statistics.

### N3 - Hidden-Wall Scan

The trigger scan classifies each potentially load-bearing phrase:

- "framework baseline" links the current axiom memo;
- "canonical lexicographic order" is a non-load-bearing convenience because C7
  enumerates all patch orderings;
- "canonical KS pattern" is the explicitly defined finite sign table;
- "standard finite linear algebra" is mathematical infrastructure;
- "canonically supply" states the negative conclusion rather than assuming a
  uniqueness premise.

"Locality" means support in the tested ungraded tensor representation. "Eta"
means a c-number coefficient in the hopping term. No graded locality,
superselection rule, or physical total-order selection is hidden in those
words.

### N4 - Residual Matching

The residual is cross-site CAR selection. It is not the per-site nilpotency
residual, the staggered Dirac/taste residual, or the existence of a compatible
fermion representation. No prior no-go or campaign is used as the scientific
witness. The retained rows listed in N6 and N8 are partial-path context; the
runner's two finite realizations are the residual-matched witness.

### N5 - Rhetoric Audit

The negative statement is route-local: KS eta plus ungraded tensor locality
does not force CAR. Its tested resolutions are:

| Resolution | Exact tested surface |
| --- | --- |
| per mode | not tested and not claimed |
| per site | all eight HCB and JW ladders: nilpotency, single-site HCB support, and shared parity oddness |
| per distinct-site pair | all 28 pairs: HCB commutation and JW CAR |
| per geometric link | all 12 links: HCB endpoint support and exact JW ordered-interval support |
| per finite block | three-site full ungraded algebra and eight-site cube bandwidth |
| lattice-wide | outside the finite-patch theorem domain |

### N6 - Partial-Closure Path Scan

Current partial paths are:

- raw tensor locality, `retained_bounded`, supplies ungraded support control;
- the parity involution, `retained`, supplies a grading operator but no braiding;
- the Cl(4)-to-CAR equivalence, `retained`, derives CAR after Clifford relations
  are supplied;
- Cl(3) complexification, `retained`, supplies abstract algebraic structure;
- the Pfaffian determinant-power theorem, `retained`, treats a supplied
  Grassmann carrier;
- approved primitives supply no odd-operator braiding or statistics selector.

An owner-approved graded-locality/braiding primitive or a lattice-native
statistics theorem could resolve the residual. Graded locality is substantive
statistics structure, not a naming convention. Parity superselection alone
cannot resolve the residual because both tested frames carry the same parity
action.

### N7 - Steelman

A hostile reviewer can argue that physical locality should be graded locality
rather than ungraded tensor locality. That would supply CAR directly, but it is
an added odd-operator braiding rule; it is not derived from the eta
coefficients. The retained
`fermion_parity_pauli_tensor_involution_narrow_theorem_note_2026-05-10`
supplies the best ingredient, the involution `F`; it does not supply
odd-operator braiding.

### N8 - Cross-Cycle Echo

Current-ledger context checked on 2026-07-12, without adding dependency edges:

- `lieb_robinson_equal_time_tensor_locality_narrow_theorem_note_2026-05-10`
  is `retained_bounded` for raw ungraded tensor locality;
- `fermion_parity_pauli_tensor_involution_narrow_theorem_note_2026-05-10`
  is `retained` for the parity involution, without a braiding selector;
- `area_law_majorana_car_fock_equivalence_narrow_theorem_note_2026-05-09`
  is `retained` after Clifford/CAR relations are supplied;
- `cl3_complexification_split_narrow_theorem_note_2026-05-10` is `retained`
  for abstract algebraic structure;
- `acphilambda_fermionic_realification_pfaffian_power_identity_narrow_theorem_note_2026-07-12`
  is `retained` for determinant-power identities on a supplied Grassmann
  carrier.
- `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25`
  is `unaudited` context; its statistics wall has not been retired and is not
  cited as retained support.

The Cl(4) result derives CAR from supplied Clifford relations; parity supplies
grading algebra without braiding; raw tensor locality distinguishes the
ungraded representation. None converts eta plus ungraded locality into CAR.
The unaudited staggered-Dirac row echoes the same wall but contributes no
retained authority here.

**Gate result:** pass for the narrow eta-versus-string route.

## Validation

The runner checks 35 exact finite-matrix facts:

- eta signs are c-number Kawamoto-Smit phases;
- hard-core boson and Jordan-Wigner hopping use the same eta coefficients;
- all hard-core link terms are endpoint-local while exactly `8/12` Jordan-Wigner
  link terms carry non-endpoint string support in the displayed ordering;
- hard-core boson ladders are nilpotent and local but not CAR;
- Jordan-Wigner dressing gives CAR;
- eta and the string pass the two counterfactual tests above;
- on a three-site subpatch, both frames generate the same ungraded matrix
  algebra;
- the patch order has a nontrivial nearest-neighbor string tail.
