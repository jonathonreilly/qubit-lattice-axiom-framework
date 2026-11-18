# Council synthesis (FINISH row 1134)

Written by the lead, Claude Opus 5.5, on 2026-11-18. The lead read all six council files in full, as well as row 1127
(`library/gap-w-astra62.md`), which ran on the same question just before the council. A lens never synthesizes;
this file does. Every member file is research text, checked by no one. The lead's own judgements below are marked
ARGUED. Nothing here is a mass-gap claim.

Members, blind to one another, all from `library/gap-council-brief.md`:

| Row | Seat | Model | File | Lines |
|---|---|---|---|---|
| 1128 | constructive QFT, multiscale RG | Claude Fable 5.2 max | `gap-council-rg-fable.md` | 473 |
| 1129 | geometric analysis of gauge fields | Claude Fable 5.2 max | `gap-council-geom-fable.md` | 212 |
| 1130 | lattice gauge theory, confinement | Claude Fable 5.2 max | `gap-council-conf-fable.md` | 647 |
| 1131 | probability, Gibbs measures | gpt-6.2-astra max | `gap-council-prob-astra.md` | 146 |
| 1132 | operators, transfer matrices, Hamiltonian LGT | gpt-6.2-astra max | `gap-council-op-astra.md` | 106 |
| 1133 | combinatorics, random surfaces, loop equations | gpt-6.2-astra max | `gap-council-comb-astra.md` | 158 |

## 1. Correction to the brief

Rows 1131 (Section 5) and 1133 (Section 4) both flag a notation error in the brief, Section 2. The brief wrote
Phi_4(n) = 16 F(n^4) - F((2n)^4). In row 720, Phi_rho(n) = rho^4 F(n) - F(rho n). So the one-doubling defect is
Phi_2, and Phi_4 = 256 F(n) - F(4n) = 16 Phi_2(n) + Phi_2(2n). The (Z-SEED) line of the brief uses row 720's Phi_4.
The brief is corrected in place, with a note. No member's conclusion depends on the slip: 1131 routes its rectangle
through (PHYS-SEED), and 1133 uses Phi_2 throughout.

## 2. What the council agrees on

**2a. The three Fable seats found the lane's own map again.** All nine Fable attacks turned out to be on file:
- 1128: USF is rows 1009-1018, LAYER is BR-2 with rows 712, 825 and 839, THERMAL is RB with row 934.
- 1129: TWIST is rows 731, 783, 930, 1004, 1018 and 1025; HELIX is row 1032; FLOW-PIN, in law, is method 34.
- 1130: the duality ladder is row 878 Route E, the coupling integration is RB with row 800, the Higgs bridge is rows
  905-923.

Each seat started from its own field and stopped at the line the lane names (HOL = Lemma FR; (TW-line); V4 = the
locality statement of row 878). ARGUED by the lead: these are second derivations by the same model family, so they
are not independent checks of the lane's proofs. They do show that the standard tools of these three fields are
already on the map.

**2b. Expansions with positive or absolute weights are dead, three ways.** The three Codex seats near surfaces and
replicas, together with row 1127, each prove a volume-growth obstruction for one family:

| Row | Family ruled out | Proved bound |
|---|---|---|
| 1127 | groupings of plaquette supports, fine enough to see one crosscap event, then nonnegative or absolute group bounds on the twist deficit | negative mass of order exp(c n^4) against the full Wilson partition function, at every beta in [2.3, 2.6] |
| 1131 | two-replica plaquette erasure with the largest common summand (the Edwards-Sokal type double cover) | odd winding has probability tending to 1 along the fine trajectory, so bound (2) carries no information |
| 1133 | absolute sums over projected bare plaquette supports of the doubling defect | growth at least (log 2)/3 per unit side along beta_j, n_j to infinity |

Common lesson (ARGUED by the lead): a proof must cancel between different geometric supports, or between the two
covers, before it takes any bound. This is new as a theorem-grade statement about these families. The underlying
sign facts (the crosscap sign, Frobenius-Schur) are prior lane work (rows 737, 744, 878). The lead adds this as
method 35 in `parts/gap.md`.

**2c. Twist-only tools reach at most the flux half.** Seats 1129 and 1130 independently reach the reading of row
1025 Lemma FAC: a centre-twist tool reads one factor. So it can give the flux sectors and never the zero-flux
(glueball) sector, and at the seed size the zero-flux half is the binding one (1130 2, GUIDE). Seat 1129 adds the
scale: its Lemmas T1-T2 keep the twist ratio up only when every Casimir factor is below about 0.088 (GUIDE), so the
flux half does not separate from the glue half. Lead decision: no further row on a twist-only line without an
even-sector step. This is route RE's reopen condition.

## 3. What is new

| Item | Row | Grade | Use |
|---|---|---|---|
| Full-slice commutator extraction (A), with its consumer | 1132 | consumer PROVED, unchecked; (A) OPEN | the one new route; Section 4 |
| Signed mask derivative b_{j,n}(t) and contraction (B) | 1133 | identity PROVED; (B) OPEN; frozen groups violate it at an interior density (PROVED) | a new variable inside route RA; low priority |
| Relative winding identity d = log((1 - p_tw)/(1 - p_tr)) | 1131 | PROVED | names what a replica proof must bound: the relative winding probabilities |
| Proposition G1 (one-link gain = Ricci/12 + a group-blind shape part) and clause (OVERLAP) | 1128 | PROVED, unchecked | small; explains in RG terms why the 2D engine needs a symmetry orbit of pins |
| Twist-ratio guide numbers on 4^4 and 6^4, and the threshold r* = 0.199 of the ideal map | 1129 | GUIDE | the flux threshold comes early; no seed, because the Casimir factors were not measured |
| Hand counts for frozen Q_8 and 2T (736, 96; 5856, 96; even and odd ground spaces 52/40 and 124/120) | 1130 | PROVED by count | conclusion on file (rows 783, 878, 884, 930); the counts may be new |

## 4. The one new route: commutator extraction across a time slab (row 1132)

Statement (A), in plain words. Fix a physical time t. Across a slab of t/a time steps of the Wilson transfer
operator, find a part of the two-slice law, of probability at least p uniformly in the box and in the cutoff, on
which every spatial link of the output has been convolved with an independent Haar commutator
a b a^(-1) b^(-1).

Why it is worth a row (ARGUED by the lead):
- **Its consumer is proved, and it reaches every sector at once.** The commutator multiplier on spin j is
  (2j + 1)^(-2), so every nontrivial representation loses at least 3/4 of its norm on the extracted part. This
  gives a physical gap of at least -log(1 - 3p/4)/t on the full gauge-invariant space, flux and zero-flux sectors
  together, and so (Z-UNB). It is not a twist-only tool (2c), and it is not an expansion with absolute weights (2b).
- **It reads the group by construction.** For U(1) the commutator is the identity, so the margin is 0. For Q_8 and
  2T the nontrivial characters of the quotients C_2^2 and C_3 are fixed by every commutator, so the margin is 0 on
  them. A massless spectator factor is untouched by an SU(2)-only kick. Seat 1132 proves each of these lines.
- **Facts on file in row 1132:**
  - one electric step fails across growing boxes in the window (a Chebyshev argument on N disjoint plaquettes);
  - twelve electric steps pass with p = 1 for every box at beta at most 13/5, with the spatial weights switched off;
  - with the full Wilson slab, (A) holds at fixed box and cutoff after a number of steps that depends on the box;
  - a one-step sign obstruction at beta above 1/6 comes from the spatial multiplier.
- **Where it can die (ARGUED by the lead; this is the decisive question):** (A) asks for a joint minorization of a
  whole slice with p independent of the volume. The usual form of such a condition (a Doeblin bound) fails in every
  interacting model, because the extracted mass is a product over regions. Here the minorizing kernel may depend
  on the input, and only commutator noise has to be extracted, so the usual volume argument does not apply
  directly. But the interacting slab couples the output links through the spatial plaquettes. So a uniform p needs
  the effective one-link conditional law, after integration through the slab, to be fully commutator-deconvolvable
  link by link (as in the twelve-step electric case). Whether integration over a physical time can give that,
  uniformly in the volume, is open. If it cannot even at strong coupling, the route is dead. If it can at strong
  coupling but needs the gap itself in the window, (A) is the target in another form.
- **Free-energy side:** (A) gives (Z-UNB). (W) also needs (BDD-Delta). Row 1132 states this. ARGUED by the lead: a
  uniform physical gap on periodic cubes is likely to give (BDD-Delta) as well, since the periodic excess free
  energy has no boundary term. Not proved; the next row is to state it as a target, not assume it.

## 5. Rows to queue (the lead's choice)

1. **Row 1135, proof row, gpt-6.2-astra max (Mac mini): the decisive tests of (A).**
   - (i) Prove (A) with the full Wilson slab, spatial weights included, at small beta (an explicit beta_0, for
     example 1/48), uniformly in the box, at a fixed number of lattice steps; or show it fails there with p tending
     to 0 in the volume.
   - (ii) At fixed physical time in the window, bound the extractable p from above by a volume argument, and decide
     whether (A) is implied by a uniform gap with locality (target-equivalent) or is strictly weaker.
   - (iii) Locality of the Moser coordinates S, or a construction of the subdensity g that avoids them.
   - (iv) Whether a uniform gap gives (BDD-Delta) on periodic cubes.

   Stop at a proof, a counterexample, or a lemma that fails three ways.
2. **Row 1136, check, Claude Opus 5.5 max (laptop): line-by-line check of row 1132 Sections 2-3.** Cross-provider.
   It covers the consumer (Jensen, the multiplier 1/4, the norm bound), the sign-test equivalence, the one-step
   obstruction, the twelve-step pass, and the fixed-box bound with A_1, B_1. It runs in parallel with 1135, on the
   provider that did not write 1132.
3. **Row 1137, reading, gpt-6-luna high (Mac mini): literature on the new path.** Minorization and coupling by
   commutator or Haar noise on compact groups; positive deconvolution on SU(2); Doeblin and Dobrushin conditions
   uniform in the volume for lattice gauge transfer operators; random walks generated by commutators (Frobenius,
   Magee-Puder). Owner rule: a reading row on every new path.

Held:
- the checks of the three obstruction theorems (2b) and of 1133's (B), until 1135 reports;
- every Fable row, until the weekly reset (Fable is at 86%);
- a further twist-only row, by 2c.

## 6. RESULT

RESULT: Council of six (three Claude Fable 5.2 max seats, three gpt-6.2-astra max seats), synthesized by the lead.
No member passed the wall, and (W) is unchanged.
- The three Fable seats found the lane's map again, line for line.
- Three Codex seats and row 1127 prove volume-growth obstructions for expansions with positive or absolute weights,
  so a proof must cancel between supports before bounding (method 35).
- Two seats confirm that twist-only tools reach at most the flux half.
- One new route has a proved all-sector consumer and is selective by construction: full-slice commutator
  extraction across a time slab (row 1132, statement (A)). Its open question is whether p can be uniform in the
  volume at a fixed physical time.

Queued: proof row 1135 on (A), check 1136 of row 1132, reading 1137. The brief's Phi_4 notation is corrected.
