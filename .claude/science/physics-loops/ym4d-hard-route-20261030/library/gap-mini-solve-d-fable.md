lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T11:54Z

# gap-mini-solve-d-fable: the mass gap of four-dimensional SU(2) Yang-Mills (plain brief, fourth sibling)

Queue row 1193 of `FINISH.md`, pinned at commit 32c14c113. Worker: Claude Fable 5.2 (max), Mac mini worker 1.
Started 2026-11-19T23:54Z (`date -u`). This is research-stage working state. Nothing here is a public claim.

Labels used: PROVED (every step written here), ARGUED (argument written, a step is not fully written),
GUIDE (numeric or heuristic evidence, never a proof step), OPEN.

## Status log

- 23:54Z. File created. Read `GOAL.md`, the rule sections of `FINISH.md`, the row. Next: the sibling rows a, b, c
  (rows 1188-1190) and `parts/gap.md`, so that this row does not repeat them.
- 23:55Z. Read in full the three sibling files (rows 1188-1190: `gap-mini-solve-a-fable.md`, `-b-`, `-c-`). Their attacks: (a) pinned-slice
  Ward route, Lemma PC; (b) the doubly flat corner (route S2), Theorem A8, stops at (Sigma-unif) and at the first unfreezing;
  (c) seventeen candidates all on file, cube identity, chi-square restatement. I do not repeat these. Next: `parts/gap.md`.
- 00:25Z. Read `parts/gap.md` L1-104 and L223-322, the RESULT lines of rows 1178-1187, the digest of the two posted 2D O(N)
  proofs (`library/prior/gap-2don-proofs-read-opus.md` L44-126), statement (A) (`gap-council-op-astra.md` L14-52), the
  corner-twist candidates C1-C8 and their kill table (`gap-invent-selective-max.md` L96-200) with the cross-provider check
  items 11-18 (`gap-invent-selective-check-astra.md` L50-72). Section 1 written.

## 1. How best to attack it

### 1.1 The target as the record holds it (cited, not re-proved)

- The Jaffe-Witten gap clause is reduced to the continuum datum of the T0 chain (OPEN, `FINISH.md` L11) plus one lattice
  estimate, the one-cube physical neutral bound (N-phys) (row 1161, `gap-solve9-astra62.md` L146-148; consumer Theorem BP
  of row 1179; checks 1162, 1183). (N-phys) is a lattice gap for centre-neutral states at arbitrarily weak coupling with
  a rate of asymptotic-scaling type (rows 1180, 1184; check 1187).
- In one sentence (`parts/gap.md` L33-35, L311-322): one selective inequality is missing at every scale between first
  passage and the seed size; selective means false for a massless factor.
- The three sibling rows (1188, 1189, 1190) found this map again. Their own attacks: the pinned-slice Ward route (dead
  in d = 4 by Lemma PC of row 1188), the doubly flat corner (stops at (Sigma-unif) and does not descend, row 1189), a
  candidate screening (row 1190). I do not repeat them.

### 1.2 My screening (GUIDE; every line was checked against the record by grep before any work)

I asked from scratch what a proof needs, and searched `library/gap-*.md`, `library/prior/` and `parts/gap.md` for each
tool. Each has a match; the number is the count of lane files that name it.

| Candidate from first principles | Where it stops | On file |
|---|---|---|
| Zero-point closing of flat valleys (Simon's x^2 y^2, Luscher's toron Hamiltonian) as a volume-uniform operator inequality | it bounds H below, not E_1 - E_0; in a background field the spin term reverses the sign (the paramagnetic term that gives asymptotic freedom) | toron 40, quartic 29, `gap-skeleton-max.md` L76, `gap-paths-fable.md` L105 |
| Orbit-space geometry (Feynman, Singer, Karabali-Kim-Nair) | no consumer above beta about 1/8 | method 31; `gap-measured-vectors-max.md` L219 |
| Thin twisted torus, semiclassical gap, then continuity in the torus size | (AC') is the crux again | Route T, rows 678-695, 842 |
| The neutral premise as "no Casimir energy at aspect ratio K" (thermal form) | Proposition Delta: log(1 + s(a; n^3)) <= (n/a)^3 Delta(a^4); the seed again | `gap-ladder-max.md` 5.7; Casimir 115 |
| Concavity of a stiffness or of Delta in the logarithm of the size, as a carrier of asymptotic freedom | Delta >= 0 forces a change of convexity before the seed; no exact convexity known | (CVX), (CAS), (MONO-Delta); `parts/gap.md` L77 |
| Triangular (field-dependent, Haar-preserving) moves; frames read from the field | frames decohere; pointwise frustration by non-commuting plaquettes | C8 of row 1013; rows 1141, 1177, 1181 |
| Staple rotations (exact field-dependent symmetries special to SU(2)) | they preserve the action, so their Ward identities carry no coupling: void | Lemma MC, row 1016 |
| Loop equations with positivity | numerical; Theorem O | rows 754-767 |
| A corner-twist background with an exact non-abelian link-field invariance (my derivation of W(G^F) = W(G)) | found again: it is C1 of row 1013 | `gap-invent-selective-max.md` L101 |
| Commutator extraction (A) | a Doeblin factorization in Moser coordinates; no mechanism | rows 1132-1138 |

Verdict (GUIDE): a fourth screening finds no route off the map. I stop screening here.

### 1.3 What I take to be the exact obstruction (ARGUED; my wording of statements that are on file)

1. Power counting. A p-form transformation has a scale-invariant quadratic cost in dimension 2p + 2. Gauge functions
   (p = 0) are marginal on two-dimensional objects only: the 2D spin models, a 2D pinned plane (Lemma EMB of row 1011),
   the base of the corner model (row 1189). One-forms (p = 1) are marginal in d = 4, and the only exact one-form
   symmetry of Wilson SU(2) is the centre, which is discrete.
2. Every continuous move of the links has a pointwise mean cost that is a mass form, because no colour direction is
   covariantly constant on a field whose plaquettes do not commute (Proposition J and Lemma 5.1a of row 1181, Lemma FR
   of row 1011, row 1141 (2)). The physical stiffness is the difference of two such terms. A bound that drops the
   variance cannot see it.
3. Transitivity. In an O(N) spin model every boundary condition is a site-dependent symmetry twist of every other one.
   So a twist-stiffness bound controls every observable, the rotation-invariant ones included. In a gauge theory the
   boundary data modulo the exact symmetries is the gauge orbit of the boundary field, and no exact symmetry moves it.
   Every Haar-preserving change of variables gives a Schwinger-Dyson identity: the function exp(S o tau - S) - 1 has
   conditional mean zero given the links that tau does not move. Such identities exist in abundance and say nothing
   about the conditional law given gauge-invariant boundary data. This is the "neutral half".

Item 3 decides my choice. (N-phys) is a statement about the neutral half. The 2D proofs cross their band and, per the
record, also deliver mixing for all observables and a doubling criterion for partition functions. So the step to read
is not their twist bound (ported four times, each port dead) but **how they pass from the twist bound to the
rotation-invariant observables**. Section 2 reads that step in the lane's digest and asks for its gauge analogue.
