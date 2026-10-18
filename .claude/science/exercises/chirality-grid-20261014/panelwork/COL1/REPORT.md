# COL-1: can colour be carried by combinations of sites? (2026-10-14, 21:12–21:56Z)

**Provenance.** One Opus 5.5 agent, the same model family as the supervisor and panel. Not refereed. A background Opus agent checked the citations against abstracts. The harness blocked the worker from writing this file, so the supervisor saved it from the worker's final message, lightly condensed; all numbers and references are the worker's.

## Reading (fixed in advance)

- **COLOUR-SPREAD-OK** for qubits with many-body colour charges (class M).
- **COLOUR-BLOCK-FORCED** as the sub-reading for elementary quark fields with one fermion mode per site and quadratic charges (class Q).

## Plain words: Jon's question

**Q:** "Why does the site need to carry the colour — can't combinations of sites carry it?"

**A:** The site does not need to carry it. Combinations of sites can, with exact local colour gauge symmetry and with the same law at every site. There is an explicit, checked example on a line (Z¹) and on Z³, in which a quark's three colours sit on three different qubits.

Three things are forced. They are what the "≥ 16 modes per site" claim really comes down to:

1. **Each colour point needs its own private qubits.** If two colour points both act on a qubit, both can only read it, never change it (a theorem about commuting operators). So each point needs a private register of at least 3 states, which means at least 2 qubits. The example uses 3 qubits, one per colour.
2. **Colour points cannot all be "on" at once.** The law offers a colour point at every site. But one qubit per site cannot give every site its own private register simultaneously, so at most about 0.63 colour charges per site can be present together. The examples have 1 per 19 sites (line) and 1 per 35 sites (Z³). A small marker pattern in the qubits decides which sites are "on", so the colour lattice is itself a pattern.
3. **The counting cost moves rather than disappears.** It now applies per colour cell: 19 qubits per cell on the line and 35 on Z³, links included. In the linked example the cells line up like a crystal, so the vacuum picks one of 19 (or 35) offsets. The law keeps one-step translations, but this vacuum does not. The Z³ example ignores cubic rotations. Whether such a model behaves like QCD at long distances is unknown.

**Where the panelist was right.**
- One qubit cannot carry colour.
- For elementary quark fields (class Q), spreading colour, including staggered-style twisted shifts, does not lower the per-site count at all (proved).

**Where the panelist overreached.** "One qubit per site, read as blocks, cannot keep the axiom's one-step translation symmetry" is false as a statement about the law. What survives is weaker: in any one configuration, the active cells are disjoint blocks.

**Reading.** This is a concrete case of Jon's thought that "particles and forces are patterns of records": here even the lattice of colour points is a pattern.

## Class Q: elementary modes with quadratic charges (proved; checked in `col1_quadratic.out`)

The map t ↦ c†tc is an injective Lie-algebra homomorphism, so commuting quadratic generators are commuting single-particle su(3) representations on Cᴺ.

- **Q1.** N ≥ 3|I|, where I is the set of gauge points. The Majorana (BdG) form gives the same bound.
- **Q2.** Translations act freely on gauge-point labels, twisted or not, so |I| = kN with k ≥ 1. Then 3kN ≤ N is a contradiction.
- **Checks.**
  - Overlapping windows do not commute.
  - Blocks of 3 commute but are not translation-covariant.
  - Every covariant assignment s(x,i) = x + c(σ^{−x}i) puts 3 components on every site.
- **Precedent.**
  - Staggered fermions spread spin and taste, never colour (van den Doel–Smit; Golterman–Smit).
  - At finite spacing the shifts generate only a discrete subgroup (Golterman 2406.02906).
  - Gauging them gives Z₂ fields (Catterall–Pradhan 2405.03037).
  - Spread charges can fail to close (Chatterjee–Pace–Shao 2409.12220).

## Class M: what is forced (proved)

- **OWN (ownership lemma).** Take commuting algebras A on H₁⊗H₂ and B on H₂⊗H₃. Then H₂ splits as ⊕L_j⊗R_j, A ⊆ ⊕B(H₁⊗L_j)⊗1, and B ⊆ ⊕1⊗B(R_j⊗H₃). So a qubit both touch is read-only and classical for both.
  - Comparator: Bravyi–Vyalyi; Aharonov–Eldar, Lemma 3.3.
  - Checked: random SU(3) on 2–3 qubits always leaves a 4-dimensional commutant.
- **CAP (density cap).** 3^k ≤ 2^n, so the simultaneous colour density is at most 0.63 per site, and colour is hard-core at the grid scale.

## Construction on Z¹ (checked)

**(a) Matter only, cells free to float.**
- Each cell is 7 qubits, laid out `110 | one-hot r₁r₂r₃ | 0`.
- G_x^a = Π_x (T^a on the one-hot span) Π_x.
- Checked on the full 2^L Hilbert space for L = 14–20:
  - su(3) error 1e-16;
  - all cross-commutators 0;
  - T G_x T† = G_{x+1};
  - active cells never overlap;
  - at most ⌊L/7⌋ cells at once;
  - cells float (non-sublattice gap patterns occur).

**(b) With links and a Gauss law.**
- Each cell is 19 qubits:
  - a marker;
  - a quark (3);
  - an antiquark (3̄), with at most one of quark and antiquark present;
  - a link near-end colour (3̄ of SU(3)_z);
  - a link far-end colour (3 of SU(3)_{z+19});
  - guard zeros.
- The link is truncated to "no flux" plus one flux state (Kogut–Susskind).
- Π_x = V(x) ∧ V(x−19); the generator G_x covers the quark, antiquark, near end and incoming far end.
- K creates a quark–flux–antiquark state that is a singlet at both ends.
- **Exhaustive parse lemma** (exact over all overlapping offsets):
  - only consecutive cells can be on together;
  - projectors are blind to colour moves;
  - compatible cells share no acted-on qubit.
- **Lemma C:** these give commuting Gauss generators on the full Hilbert space.
- **Bit-level checks** (ring L = 38, constrained subspace, dimension 93,100):
  - su(3) error 4e-16;
  - cross-commutators 0;
  - translation covariance exact;
  - leakage 0;
  - [H, G] = 0;
  - T H T† = H.
- **Gauss-law physical space** at offset 0: dimension 4 (vacuum, two mesons, a flux loop), with spectrum −3.477, 0.6, 1.7, 5.177.

## Construction on Z³ (checked plus proved)

- Each cell is a 35-qubit rod along x: marker, quark, antiquark, and x/y/z link registers.
- Gauge point at every site; covariant under all three unit translations.
- Parse lemma over 692 displacements: only the 12 neighbouring-cell displacements are compatible.
- y-link algebra checked: su(3) error 4e-16, all commutators 0.
- **Cubic-rotation covariance is not satisfied.** An isotropic design is suggested, not built.

## Prices of the class-M route

| Price | Value |
|---|---|
| Private register per colour point | ≥ 3 states (≥ 2 qubits); cells of 19 qubits (Z¹) and 35 qubits (Z³) |
| Simultaneous colour density | ≤ 0.63 per site; hard-core at the grid scale |
| Cell positions | set by a classical marker pattern (a dynamical colour lattice) |
| Translations | exact for the law; the linked example's vacuum breaks Z → 19Z. A floating linked liquid needs geometry-changing moves, which are allowed at singlet cells; not built |
| Truncation | at most one quark or antiquark per point; links {1, (3̄,3)}; QCD universality open |
| SM content | the 16-mode count reappears per cell |

## Relation to other work

**Literature.**
- **Non-on-site gauging:** Seifnashri 2308.05151; Else–Nayak 1409.5436. The construction supplies the local commuting U_x(g) that these require.
- **Disentanglers:** Seifnashri–Shirley (finite groups, 1+1D) and Thorngren–Preskill–Fidkowski (U(1)) do not cover continuous non-abelian SU(3).
- **Quantum links and rishons:** Chandrasekharan–Wiese; Brower–Chandrasekharan–Wiese; Horn; Orland–Rohrlich; D-theory. Their link structure matches OWN.
- **Emergent and solved routes:** Levin–Wen; Wen; Hermele–Fisher–Balents. In the Gauss-law-solved multiplet basis (Ciavarella–Klco–Savage 2101.10227), colour becomes a vertex fusion rule, i.e. a neighbourhood admissibility rule.

**Repo (main).**
- `DYNAMICS_CLAUSE_NON_ABELIAN_GAUGE_LINKS_NEED_SEVERAL_QUBITS…_2026-09-24`: OWN explains why.
- `CL3_COLOR_AUTOMORPHISM_THEOREM.md:4` and `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`: the framework's own colour candidate (SU(3) on the 2³ taste cube's symmetric base) is already "combinations of sites". By Q1–Q2 it is an exact local gauge symmetry only as a 2-step block lattice or in class-M form; otherwise it is emergent (suggested).
- `COLOR_ARENA_BONDED_PAIR…_2026-07-06`: Sym²(C²) is a 3-state block on two qubits.
- The U(1) lane shares link qubits only because abelian generators are diagonal, which is the classical case of OWN.
- `A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS…_2026-09-03`: in the solved multiplet basis every basis state is a singlet. That is a different readout context, worth a note (suggested).

## Not shown

- A continuum limit or QCD dynamics; confinement; a translation-invariant ground state.
- Fermion statistics of the cells; cubic rotations; chirality; SU(2)×U(1).
- Floating linked cells.
- The linked construction was checked bit-level only on the constrained subspace; full-space coverage rests on Lemma C plus the parse checks.

## Deviations from PREREG

- The slice-algebra decomposition was replaced by the parse-lemma "no shared qubit" check.
- The Gauss-law check used 2 cells, not 3.
- One output header wrongly says "all 19 offsets"; that run covered offset 0 only.

## Memory: the 0.3 GB cap was broken three times

| Run | Peak | Duration |
|---|---|---|
| `col1_tokens_z1_full.py` at L = 20 | 0.76 GB | ~13 s |
| `col1_tokens_z1_links.py` | 1.61 GB | 87 s |
| `col1_z3.py` | 1.29 GB | 56 s |

Reruns within the cap reproduced every result.

## Files

`PREREG.md` and `scripts/`:
- `su3common.py`, `parse_lemma.py`
- `col1_quadratic`, `col1_ownership`
- `col1_tokens_z1_full` (plus the L18 cap check)
- `col1_tokens_z1_links` (plus the low-memory rerun)
- `col1_z3` (plus the low-memory rerun)
