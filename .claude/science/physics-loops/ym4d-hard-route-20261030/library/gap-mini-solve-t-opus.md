lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T18:04Z

# gap-mini-solve-t-opus: four-dimensional SU(2) Yang-Mills mass gap

Queue row 1229 of `FINISH.md`. Started 2026-11-20T06:04Z on the Mac mini Claude worker 3, at commit ca359c011 of branch `claude/ym4d-hard-route`.

Labels: PROVED (a complete written argument here or in a cited, checked source), ARGUED (an argument with a named gap), GUIDE (heuristic or numeric), OPEN.

## Step 0. Reading (in progress)

Reading FINISH.md (rules, efficiency, RESULT lines of the gap rows), `parts/gap.md`, `library/prior/gap-onebound-read-sol.md`, `library/open-core.md`.

Sources read (06:04Z-06:40Z): `GOAL.md`; `FINISH.md` L1-84, L299-356 and the RESULT lines of rows 916-917, 924-925,
1007, 1009-1011, 1014, 1016, 1020, 1025, 1029, 1139-1140, 1179-1180, 1183, 1188, 1193, 1200, 1212-1232;
`parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` (row 1218) in full; `library/gap-mini-solve-r-fable.md`
(row 1225) in full.

What the record says (cited, not re-derived):

- The Jaffe-Witten gap clause on the account's tr F^2 sector follows from one open lattice estimate, (N-phys), beside
  the account's premises (row 1179 Theorem BP, check 1183; row 1225 Theorem E-N, same provider, check row 1232 queued).
  (N-phys): one physical side L and j_0 such that for every cutoff j >= j_0 some integer u_j with 3 <= u_j <= n_j/K
  has Tr_{H_+} U_j^{u_j} - 1 <= 1/2 on the periodic spatial cube of side n_j = L/a_j (K = 512).
- (N-phys) holds iff every fine coupling has a finite one-cube seed size nu(beta_j) with limsup a_j nu(beta_j) finite
  (row 1180). Modulo (UNIV-K) the crux is the lattice gap of SU(2) Wilson at one fixed coupling with seed side of
  order exp(c beta_0) (row 1225, ARGUED). (UNIV-K) is open and unowned since row 925; it lives in the account's
  ultraviolet steps (MAPCONV, VAC-ID, DENS-K, CLASS) and needs no infrared input.
- Row 1225's table: every structure valid at all couplings on file stops at a cited failure (positivity and
  association; positive duals; coupling integrals; loop and sector identities; curvature and Gribov geometry; the
  bracket stiffness step of the 2D O(N) proofs).
- The 2D O(N) proofs (rows 1007, 1009, 1010) cross the band by a uniform-in-coupling stiffness iteration whose gain is
  the Lie bracket; in 2D O(4) the bracket gives only the charged half, and the rotation-invariant half comes from
  positivity (row 1193, ARGUED). The 4D port fails at: no global non-abelian twist in a gauge theory (Lemma CEN,
  CEN+, rows 1011, 1016); pin suprema lose colour coherence (Propositions B, B'); the fourth-order commutator cost on
  a 3D slice is too large (Lemma PC, PC-c, rows 1188, 1193); the 4D positivity step fails (rows 1084, 1213).
- Row 1218's published inputs do not shorten the path (rows 1219, 1220).

Step 0 done 06:40Z.

Also read for Step 1: `library/prior/gap-2don-proofs-read-opus.md` L120-176 (row 1007: the OpenAI 2D O(n) proof,
step by step, and its 4D analogue table); RESULT lines of rows 957, 968, 1032, 1049-1050, 1053 (grep only);
`library/gap-mini-solve-q-fable.md` headings (row 1224, running on worker 1: A's slab route and a kill test of A's
hypothesis (M); not repeated here). Row 1228 (worker 2) has no file at this pin.

## Step 1. How to attack it (judgement; 06:40Z-07:05Z)

### 1.1 The crux in one statement (cited)

Modulo (UNIV-K), (N-phys) is a lattice gap of SU(2) Wilson at one fixed weak coupling beta_0, with an explicit
finite seed size (rows 916-917 (ONE-K), 1180, 1225 Section 4). This is the exact 4D analogue of the step that crosses
the band in OpenAI's 2D O(3) continuum paper: Proposition 8.1 (a) applies the lossy mixing bound of Proposition 2.1 (ii)
at the bare coupling of one reference cutoff, and the renormalisation group only carries it to finer cutoffs (row 1010).
So the crux is: a 4D analogue of OpenAI's Proposition 2.1, a uniform-in-coupling mechanism that gives a finite
mixing length at one fixed weak coupling. A non-sharp length is enough for this step.

### 1.2 What the 2D mechanism uses, and the 4D status of each input

The 2D proofs have two halves (row 1007 B(2), row 1193):

- Charged half: a continuous non-abelian global symmetry with a boundary twist exp(tc); a change of variables on the
  bulk spins turns the abelian-looking twist dF into the commutator twist B = (1/2)[F_x, F_y] + O(F^3); the
  fourth-order inequality (OpenAI Proposition 2.2) and a coherent sum over log N frequency shells give twist cost at
  most C_beta/log N (Proposition 3.1).
- Rotation-invariant half: positivity (conditional abelian ferromagnets, Ginibre, association) and the coupling
  integral (row 1193, ARGUED).

4D pure SU(2), status on file:

| Input | 4D status | Where |
|---|---|---|
| Rigid continuous non-abelian group acting on gauge-invariant data, whose localisation is not a symmetry | none on the lattice: link-wise maps keeping plaquette traces are gauge times a closed Z_2 field | Lemma CEN+, row 1016, HOLDS in check 1020 |
| The same in the continuum through space-time rotations | an elastic SO(4) twist has no dimensionless stiffness | row 1053 (wall-vectors) |
| A twist felt only through pinned boundary data | the commutator family lives on a 3D layer, cost at least lambda^2 eta^2 N | Lemma PC, PC-c, rows 1188, 1193 |
| 1-form symmetry as the twist group | Z_2, discrete and abelian | row 1007 B(5); row 1017 |
| Positivity for the neutral half | fails | Lemma FKG-NO (row 1213); Lemma HF (row 1188); row 1084 |
| Orbit-space curvature (selective: Ric(S^3) > 0, flat for U(1)) | killed at typical fields by the Hessian | row 957 GUIDE: horizontal Hessian 8-11 against Ric = 2 at beta 2.3-2.6; row 968 Proposition ANG, obstruction (LOC-COV) is itself a gap statement |

Two additions of mine, to close the one loophole the table leaves (configuration-dependent symmetries, Lemma MC of
row 1016) and to name the common cause.

**Lemma LS: WITHDRAWN at 07:12Z (written at 07:05Z; vacuous as stated).** The version written here claimed that
conditional symmetries such as the staple rotations of Lemma MC (row 1016) give a twisted ratio
W(t) = E_mu[exp(S(U) - S(T_t U))] identically 1. That identity holds for EVERY Haar-preserving bijection T_t, symmetry
or not (change variables V = T_t U), so it says nothing. Also its proof assumed, without saying so, that the flow on
an A-link reads the other A-links not at all (two simultaneous maps that each preserve one factor need not preserve
the product). The right notion, as in OpenAI's (2.1) (row 1007 B(2) step 1): a twist is a background connection
inserted into EACH interaction term, and that is defined only for a group that preserves each term. For link maps
that group is gauge times a closed Z_2 field (Lemma CEN+, row 1016, HOLDS in check 1020). Staple rotations preserve
only the sum of the six plaquette terms at a link, so they cannot be inserted as a twist at all.

Consequence (ARGUED; it is the lane's corrected filter of row 1016, "rigid group + charged pins + response on the
gauge-invariant algebra", which I only restate): a stiffness needs a rigid group that preserves each interaction
term and whose localised action is NOT a symmetry. In 2D that group is SO(n) acting on site spins. In 4D pure SU(2) the rigid groups acting on links are gauge (localised: still a symmetry, W = 1), the centre
(discrete), the hypercubic group (finite), and, in the continuum only, SO(4) (no dimensionless stiffness, row 1053;
and it is shared with the free photon, so any bracket gain built from it alone would also apply to compact U(1) at
weak coupling, whose photon is massless by Guth and by Frohlich-Spencer, RECALLED). So the charged-half mechanism of
the 2D proofs has no 4D carrier, and the neutral half, where (N-phys) lives, has lost its positivity.

### 1.3 Decision

I see no structure, on file or new, that holds at every coupling, is selective, and gives a bound. Every route I
could name in this step is a row of the table above or of row 1225's table. Row 1225 reached the same judgement
an hour ago and started no attack. A second decline adds nothing, so in Step 2 I attack the one object in the table
that is selective AND uniform in volume, the orbit-space curvature, at the point where the record says it fails:
the gluon-spin part of the Hessian at typical fields. The question is whether that negative part is a coherent
obstruction or an artefact of the pointwise (worst-direction) form. Kind: (K-one), one scale, the Wilson law at one
coupling. Moves: the curvature row of row 1225's table (partly selective; failure "magnetic energy not convex",
row 1032 B8; method 31). Success would give a uniform Poincare constant for some dynamics at one coupling; failure
pins the obstruction to a named estimate.

Step 1 done 07:05Z.

## Step 2. The curvature row at the spin term: dropped at the first test (07:12Z-07:35Z)

The plan of 1.3 was to ask whether the negative part of the Hessian at typical fields (the gluon-spin term
F_(mu nu)[dA_mu, dA_nu], the same term that drives asymptotic freedom) is a coherent obstruction or an artefact of the
worst-direction form. The answer does not need a computation.

**Claim A (ARGUED; inputs RECALLED or unchecked, named).** No bound of the form Ric + Hess S >= kappa on SU(2)^E,
with kappa > 0 independent of volume AND of the coupling along the trajectory, can hold. Reason: Bakry-Emery
(RECALLED) would give a volume-uniform gap kappa for the single-link Langevin dynamics. A reversible local dynamics
with a volume-uniform gap has equilibrium correlations that decay at a rate bounded below in lattice units
(RECALLED, for finite-range Gibbs measures on a compact product space; I did not write the proof). Then the
correlation length stays bounded in lattice units as beta -> infinity, so the physical mass is at least c/a_j ->
infinity, and the continuum limit is trivial on the complement of the vacuum, against NT1 (GOAL.md). The same holds
for any bounded-block dynamics: B's Theorem 66 (row 1218, unchecked) with n_k fixed and ell = n_k a_k -> 0 gives the
continuum gap at least 16 varpi/(625 e^2 n_k a_k) -> infinity. So the pointwise failure at weak coupling (row 957
GUIDE) is forced, not an artefact. A curvature bound can only work at one coupling where the correlation length is
of order one, or in a multiscale form.

**At one coupling (the window).** Row 957's GUIDE measured the Hessian term at 8-11 against Ric = 2 at beta 2.3-2.6.
A block form at the window needs bounds on conditional laws of blocks where the strong-coupling parameter is far
from small. Hand arithmetic (displayed series, GUIDE orientation only): with S = beta sum_p (1 - (1/2) tr U_p), the
fundamental character ratio is u(beta) = I_2(beta)/I_1(beta).
- beta = 2.3: I_1 = 1.15 + 0.760438 + 0.167613 + 0.018472 + 0.001221 + 0.000054 = 2.097798;
  I_2 = 0.66125 + 0.291501 + 0.048189 + 0.004249 + 0.000234 + 0.000009 = 1.005432; u = 0.4793.
- beta = 2.6: I_1 = 1.3 + 1.0985 + 0.3094 + 0.04358 + 0.003682 + 0.000207 = 2.7554;
  I_2 = 0.845 + 0.4760 + 0.10056 + 0.01133 + 0.000798 = 1.4337; u = 0.520.
The hand-proved fixed-spacing SU(2) gap reaches beta_W <= 9/25 (row 1218, A's Theorem 9.5), that is beta <= 0.18 in
this normalisation, where u is about beta/4 = 0.045. The window needs u near 0.5, an order of magnitude further, past
any convergent expansion I know. Under GOAL.md's rule (no computed certificate) a block bound there has no hand route.

**Multiscale forms.** On file and closed: row 968 (Polchinski flow; the obstruction (LOC-COV) is itself a gap
statement; (TILT-COV-sup) is a supremum over tilts, false by Theorem D2, `parts/gap.md` L29) and row 957 (Piazza-Shen;
Proposition EQ moves the problem to the skeleton law).

So the curvature row of row 1225's table is closed as an attack route in every form I can state: uniform forms prove
too much (Claim A), the window form needs a computed certificate, and the multiscale forms end at a gap statement or
a false supremum. No attack started. Step 2 done 07:35Z.
