---
claim_id: two_qubit_site_cubic_covariant_stabilizer_rules_three_dimensional_defect_motion_writes_a_local_record_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Supplied reading as in the one-qubit companion note, with two qubits per site of Z^3: a spin qubit with the full soldered action and a flavour qubit that is either fixed (trivial action) or also soldered (full action). Rules are signed sets of two-qubit Pauli strings on the seven-site star, closed under the proper cubic group O; their translates generate an abelian stabilizer group without -1. Exact (exhaustive enumeration of all 16^7 - 1 star strings, exact GF(2) algebra, and for two rules Ext^3 computed over GF(2) with Singular): call an operator record-free if it commutes with every single-site Pauli that commutes with all generators but is not in the group (a free local variable). Then no record-free operator moves a nontrivial charge along three independent lattice vectors. Consequently every rule without a free local variable has no defect mobile in three dimensions. Such defects do exist when free local variables are present: for the rule 'spin Chamon (x) flavour X on the six neighbours', the charge module is GF(2)[x,y,z]/((x+1)^2, (y+1)^2, (z+1)^2), eight charge types that move by any even translation, and every such move flips a conserved flavour variable. Not claimed: the spin-unsoldered two-qubit cases, non-Pauli or frustrated rules, larger supports, blocks, any dynamics, coherence or physical identification."
upstream_dependencies:
  - one_qubit_cubic_covariant_nearest_neighbour_stabilizer_rules_have_no_three_dimensionally_mobile_defect_bounded_theorem_note_2026-10-17
  - minimal_axioms
runner: scripts/two_qubit_site_cubic_covariant_stabilizer_rules_three_dimensional_motion_writes_a_record_2026_10_17.py
---

# Two qubits per site: a defect moves in three dimensions only by writing a local record

**Date:** 2026-10-17
**Type:** bounded_theorem
**Status:** bounded support, unaudited. The statements are exact within the
supplied stabilizer reading of Admissibility. Nothing is adopted.

## Question

The one-qubit companion note found that, with spin soldered, the only
nearest-neighbour Pauli rule is Chamon's, and its defects cannot move in
three dimensions. For free ticks, a second qubit per site removed the
corresponding freeze. Does a second qubit also free the defects?

## Result

1. **Classification (exact).** The spin qubit is soldered. Every string
   that commutes with all translates of all its rotated images falls into
   one of a few maximal commuting families.

   | flavour qubit | strings | orbits | maximal commuting families |
   |---|---|---|---|
   | fixed | 775 | 127 | three families of 39 orbits: spin part Chamon C or identity, every flavour factor one label P; six triples {C, K, C K}, with K a flavour cluster string |
   | soldered | 16387 | 858 | one family of 855 orbits using only the Bell labels {II, XX, YY, ZZ}; {spin Chamon, flavour Chamon, B}; and {E, B} |

   In the soldered-flavour row, B = XX(+-x) YY(+-y) ZZ(+-z) and
   E = YZ(+-x) ZX(+-y) XY(+-z), together with its partner ZY XZ YX; E E' = B.
2. **Theorem (exact).** Call a single-site Pauli a *free local variable*
   if it commutes with every generator but is not in the group. Call an
   operator *record-free* if it commutes with every free local variable.
   - **(a)** In every rule, no record-free operator translates a
     nontrivial charge along three independent lattice vectors.
   - **(b)** Hence a rule without free local variables has no defect mobile
     in three dimensions; in such a rule every operator is record-free.
3. **Existence (exact).** Take the rule "spin Chamon (x) flavour X on the six
   neighbours" (one generator per site).
   - Its charge ideal is ((x+1)^2, (y+1)^2, (z+1)^2) over GF(2).
   - There are eight charge types, labelled by position modulo 2. Each moves
     by any even translation, so it is mobile in three dimensions.
   - Spin-only operators cannot move a charge at all. A move by (2, 0, 0)
     must flip flavour X at some site, a conserved free local variable.
     The motion is therefore recorded in the flavour qubits. On L^3 tori the
     code dimension grows like L^3 (log2 = 72, 224 and 520 at L = 4, 6, 8),
     one free flavour variable per site.

## Proof of (a)

Each family is handled by a separate case.

- **Flavour fixed, one-label families.**
  - Every flavour factor is I or P, so P on the flavour qubit of one site
    commutes with all generators.
  - If P is in the group, multiplying by it strips the flavour factors.
    The rule becomes Chamon on the spin times a pinned flavour, whose
    charges are Chamon's.
  - If P is not in the group, it is a free local variable. A record-free
    operator then has flavour factors I or P, so it acts on generators only
    through its spin part.
  - Spin parts of generators are C or I. So the syndrome of a spin
    operator is the Chamon syndrome s, placed on every C-type generator
    and 0 elsewhere.
  - Suppose (x^{t_k} + 1) e lies in that image for three independent t_k.
    Then e vanishes on the I-type components, because R is a domain, and is
    equal to some f on all C-type components. Also (x^{t_k} + 1) f lies in
    the Chamon ideal for all k.
  - The Chamon ideal is the intersection of four curve primes. x^t + 1 lies
    in the prime of body diagonal d exactly when t is orthogonal to d, and
    no d is orthogonal to three independent t_k. So f lies in the Chamon
    ideal, and e is the syndrome of a spin operator: e is trivial.
- **Flavour fixed, triples {C, K, C K}.** Every sub-rule is ⟨C⟩, ⟨K⟩, ⟨C K⟩
   or ⟨C, K⟩.
   - In ⟨C⟩ the flavour qubits are free, so record-free operators are
     spin-only and the charges are Chamon's.
   - In ⟨K⟩ and in ⟨C K⟩, a single-site flavour Pauli creates each defect
     alone, so there is no nontrivial charge.
   - ⟨C, K⟩ has Chamon's charges plus trivial ones.
- **Flavour soldered, Bell family.**
  - O permutes XX, YY and ZZ transitively, and the group is O-invariant. So
    either all three single-site Bell labels are in the group, or none is.
  - If all are, the rule is a product of Bell pairs with no charges.
  - If none is, all three are free local variables. Record-free operators
    then commute with XX and ZZ at every site. The commutant of {XX, ZZ} is
    the Bell alphabet itself, so these operators commute with every
    generator and create or move nothing.
- **Flavour soldered, {C_s, C_f, B} and {E, B}.**
  - The sub-rules are ⟨C_s⟩ or ⟨C_f⟩, where the other qubit is free and the
    charges are Chamon's for record-free operators; ⟨B⟩, which is in the
    Bell family; ⟨C_s, C_f⟩, a sum of two Chamon codes; and ⟨E, E'⟩, which
    contains B.
  - For ⟨E, E'⟩ and ⟨E, E', B⟩, Singular computes the charge module
    N / im(σ) over GF(2), with N the syndromes allowed by the generator
    relations, and Ext^3(C, R). Its support has no point off the coordinate
    planes.
  - A charge mobile along three independent vectors would generate a
    finite-length submodule, hence a point in that support. So there is
    none.

∎

## How this bears on an emergent electron (interpretation, not a claim)

The second qubit does free the defects, but only in a specific way. Every
three-dimensional move flips a conserved single-site variable, so the
defect's path is written into the neighbourhood as it goes.

Such a particle leaves which-path information behind. One would therefore
not expect it to show the coherent, interfering propagation of an electron,
although this note does not compute coherence. It sits oddly with the
owner's information-compression picture: the defect becomes mobile by
storing more local information, not less. Within this class, a defect that
moves coherently in three dimensions needs a rule with no free local
variables, and then it does not move at all.

## Premises

- **Axioms used.** Lattice, and Qubit read as two qubits per site. Two
  qubits per site is the parked M_4(C) fork, which is a declared
  enlargement and not the Qubit axiom's M_2(C).
- **Supplied model.** The hard-support stabilizer reading of Admissibility,
  as in the companion note.
- **Declared choices.**
  - The spin qubit is soldered by the full action. The axis action has the
    same label action up to sign, and the theorem's statements concern
    subsets, so they still hold.
  - The flavour qubit is fixed (trivial; the sign twist has the same labels)
    or soldered (full; the axis action has the same labels).
  - Pauli conditions, star support.

## Relation to prior work

- Chamon's model and its fracton structure are standard. See the companion
  note for references.
- Fracton mobility gained by creating or absorbing other excitations is a
  known theme. Examples: Pretko, PRB 96, 024051 (2017); Prem, Haah and
  Nandkishore, PRB 95, 155133 (2017); and gauging and duality constructions
  with fracton matter.
- **New here, within the stated class.**
  - The exhaustive classification for two qubits per site with soldered
    spin.
  - The exact statement that three-dimensional motion requires flipping a
    conserved local variable.
  - The explicit decorated rule with eight even-step-mobile charge types.

## No-Go Discipline Gate

- **N1 — routes around the claim.**
  - Spin-unsoldered two-qubit sites are not classified here (253,215
    candidate strings).
  - Also outside: non-Pauli commuting projectors, frustrated or energetic
    rules, larger supports, block rules, and dynamics that would make the
    free variables themselves move.
- **N2/N3 — scope.** One statement, about record-free operators, for one
  model class.
- **N4 — inputs.**
  - The enumeration is exhaustive over 16^7 strings.
  - Commutation is checked against every overlapping translate of every
    rotated image.
  - The E-family step uses Singular over GF(2). This is exact arithmetic in
    the natural field, not a modular shortcut. The runner runs it when
    Singular is available; the scripts and outputs are in the loop pack.
- **N5 — wording.** "Writes a record" means the motion operator anticommutes
  with a free local variable. It is not a statement about the Record axiom's
  formation process, which this note does not model.
- **N6/N7 — strongest objection.** Free local variables may simply signal
  an incomplete rule. Adding constraints removes them, and then the defects
  stop moving. That is the content of (b).
- **N8 — earlier claims.** This extends the companion note; nothing is
  withdrawn.

## Independent check

A fresh-context agent (same model family) wrote its own code without reading
these scripts. It used a C brute force over 16^7 strings and its own orbit,
clique, Singular and torus code.
- It confirmed the flavour-fixed classification, the theorem, and the example,
  including the code dimensions and that flavour X is the only free local
  variable.
- It refuted the author's first statement of the flavour-soldered
  classification. That statement had missed the E orbit, which the runner
  now checks.
- It checked 658 rules exactly with its own Ext^3 test: every subset of the
  small families, all 117 single-orbit rules of the one-label families plus
  random subsets, and 125 Bell rules.
  - Three-dimensional mobility appeared only in the six rules "C (x)
    (flavour P on the neighbours)", with or without P at the centre. All six
    have a free local variable.
  - None of the 321 rules without a free local variable has a
    three-dimensionally mobile charge.
- Its sign handling was unsigned, so the "no -1 in the group" condition was
  not independently tested.

Files: `.claude/science/physics-loops/toe-campaign-20261017/c2_two_qubit_site/independent_check/`.

## Verification

```bash
SINGULAR_BIN=/path/to/Singular python3 scripts/two_qubit_site_cubic_covariant_stabilizer_rules_three_dimensional_motion_writes_a_record_2026_10_17.py
```

Expected, with Singular: `TOTAL: PASS=17 FAIL=0` (about ten minutes, mostly
the two 16^7 enumerations). Without Singular the two E-family checks are
reported as skipped: `PASS=15`.

## Load-bearing sources

- [One-qubit companion](ONE_QUBIT_CUBIC_COVARIANT_NEAREST_NEIGHBOUR_STABILIZER_RULES_HAVE_NO_THREE_DIMENSIONALLY_MOBILE_DEFECT_BOUNDED_THEOREM_NOTE_2026-10-17.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Two-qubit free tick](TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md)
