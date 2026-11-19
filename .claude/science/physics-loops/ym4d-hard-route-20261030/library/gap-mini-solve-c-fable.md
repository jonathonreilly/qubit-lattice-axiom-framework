lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T10:59Z

# gap-mini-solve-c-fable (queue row 1190)

Worker: Claude Fable 5.2, max effort, Mac mini worker 3, single session, no subagents.
Pinned commit: f7e5907e5 on `claude/ym4d-hard-route`. Started 2026-11-19T22:59Z.

The problem as the row states it: prove that four-dimensional SU(2) Yang-Mills theory has a
mass gap, in the sense of Jaffe and Witten.

Labels used below: PROVED (a written argument, checkable by hand, in this file or cited by
path), ARGUED (an argument with a named hole), GUIDE (heuristic or numeric; never a proof
step), OPEN (not established).

Status of this file: in progress. Sections are appended one step at a time.

## 0. Log of steps

- Step 0 (22:59Z): file created; reading FINISH.md, GOAL.md, `parts/gap.md`, `library/open-core.md`.
- Step 1 (23:05Z): orientation read finished (list below). Attack not yet chosen.

## 1. Orientation: what the record holds (read in this run; statements about the record)

Read in full: `GOAL.md`; `FINISH.md` L1-84 and L299-356; `parts/gap.md` L1-104 and L213-322
(formulation, methods 19-36, lead rules, route registry, test table, exact price);
`library/gap-council-synthesis.md`; `library/prior/gap-o4-pinned-cell-read-opus.md` L57-201
(the digest of OpenAI's pinned-cell stiffness iteration for the 2D O(4) model);
`library/gap-mini-free-fable.md` plan, steps 2 and 5. RESULT lines read: rows 720, 1011,
1013, 1016, 1018, 1161, 1174, 1179, 1180, and the briefs of rows 1181-1189.

What I take from it (each item is the record's statement, not mine):

1. The lane reduces the Jaffe-Witten gap clause to one lattice input plus the continuum
   datum: the one-cube physical neutral bound (N-phys) of row 1161 (Theorem BP of row 1179,
   unchecked at this pin; check row 1183 running). By row 1180's corollary, (N-phys) is a
   lattice gap for centre-neutral states at arbitrarily weak coupling with a lower bound of
   asymptotic-scaling type. The continuum datum (the T0 chain) is itself not proved
   (`FINISH.md` L11: "Existence is not proved").
2. The wall in plain words (`parts/gap.md` L33-35): a selective inequality at every scale
   between first passage and the seed size; selective means false for a massless factor.
3. Constraints a route must meet (row 1181 step 2, from `parts/gap.md`): it reads the group
   at order-one response; it cancels between supports before bounding (method 35); it reads
   the whole state space (Lemmas FAC, PT); it averages over the actual Wilson law, because
   every worst-case form is false (Theorem D2, Lemma SHEET, method 36, Theorem BH).
4. The one mechanism on file that crosses the band in a model of the same type is OpenAI's
   2D pinned-cell iteration: stiffness = direct cost minus current variance; a lower bound
   on the current variance comes from the bracket term of a non-abelian Ward identity, by
   Cauchy-Schwarz against a test functional; only an upper bound on stiffness is carried.
   Its direct port to 4D SU(2) fails in the class of all pins (rows 1011, 1016: Propositions
   B, B', Theorem BH), because pure gauge theory has no rigid non-abelian symmetry on the
   link variables (Lemma CEN+) and a lab-frame twist has a mass-form cost (Lemma WN,
   Lemma 5.1a of row 1181).
5. Three earlier Fable seats and row 1181, starting from their own fields, each found the
   lane's map again. So a fresh start from a standard field is expected to add nothing.

- Step 2 (23:50Z): first pass at choosing an attack; eleven candidates checked against the
  record before any work (rule 0a). All eleven are on file. Table in Section 2.

## 2. First pass: candidates I generated, checked against the record (statements about the record)

How I chose candidates: I asked what a proof of the fixed-coupling lattice gap at weak coupling
must contain, starting from the one mechanism on file that crosses a band of this type (item 4 of
Section 1), and from the standard fields. Before any work I grepped `library/`, `library/prior/`,
`parts/gap.md` and the FINISH rows for each. The right column is what the record already holds.

| # | Candidate (my wording) | On file as | Verdict |
|---|---|---|---|
| 1 | Stiffness of the abelian Schrodinger functional, gain from the bracket term | rows 1011, 1013, 1016, 1018 (Propositions A, W, B, B', Theorem BH, Lemma FLOW) | found again; blocked at frames |
| 2 | A rigid non-abelian group on the link variables in temporal gauge (the time-independent gauge group) | row 1016, Identities QL1, HAM1: the response is the family of Polyakov-loop correlators, blind | found again |
| 3 | Diffeomorphism or shape twists (anisotropy, stress-tensor response) | routes RB, BR-2, rows 934, 960-965, 1066-1115 | found again |
| 4 | The continuous path from the periodic to the twisted torus through a thin non-central vortex | C2 of row 1013, Lemma WN (cost of order one per plaquette, an area-order barrier) | found again |
| 5 | Continuity in beta with an a priori bound on d log m / d beta (Feynman-Hellmann, Gronwall) | item 46 and G8 of row 859, (NOCRIT-HF); row 878 F5 | found again |
| 6 | Pinned flat plane: the links leaving it are a two-dimensional O(4) model with one-sided twists | Lemma EMB of row 1011 (after Durhuus and Froehlich); gives only charged decay, weaker than the trivial perimeter bound | found again |
| 7 | Correlation inequalities in Hopf coordinates (Dunlop and Newman; Ginibre) | row 1076 L206 (one line); row 1181 5.1 (eight monomials); the sign pattern of the eight monomials cannot be removed by phase shifts (my check, Section 2.1) | found again, with one small addition |
| 8 | Griffiths II for products of elementary plaquettes | (EP), false: Theorem EP-NO of row 754 (checked, row 756), by the projective plane S_0 of row 737 | found again |
| 9 | The neutral premise as a thermodynamic statement (pressure, Casimir energy of one short direction, equation of state) | route RB, row 934, Proposition VIR, row 1181 step 5 | found again |
| 10 | The neutral excited sum as a chi-square quantity (sum of squared canonical correlations of two time slices; mean chi-square distance of the ground-state chain from a typical start) | 46 gap files use chi-square, 39 Hilbert-Schmidt, 24 mutual information; the exact wording "typical start" not searched further | a restatement; no new handle |
| 11 | A class of plaquette coupling fields in [0, beta], closed under removing plaquettes, with free boundaries (no pins) | Lemma SHEET (unbounded fields), Identity MIX, rows 995-997; a free-boundary scale induction is not a theorem schema (Section 2.2) | found again in part; my remark 2.2 is ARGUED |

### 2.1 The eight monomials: the sign pattern is not removable (PROVED; small)

Write a link as U = [[z, w], [-conj(w), conj(z)]] with z = r e^(i phi), w = rho e^(i psi),
r^2 + rho^2 = 1. Then (1/2) tr(U_1 U_2 U_3^* U_4^*) is the real part of the sum over index
paths (1, a, b, c, 1), a, b, c in {1, 2}, of the products of entries. The eight terms are:

1. (1,1,1): + r_1 r_2 r_3 r_4 cos(phi_1 + phi_2 - phi_3 - phi_4)
2. (1,1,2): - r_1 r_2 rho_3 rho_4 cos(phi_1 + phi_2 + psi_3 - psi_4)
3. (1,2,1): + r_1 rho_2 rho_3 r_4 cos(phi_1 + psi_2 - psi_3 - phi_4)
4. (1,2,2): + r_1 rho_2 r_3 rho_4 cos(phi_1 + psi_2 + phi_3 - psi_4)
5. (2,1,1): - rho_1 rho_2 r_3 r_4 cos(psi_1 - psi_2 - phi_3 - phi_4)
6. (2,1,2): + rho_1 rho_2 rho_3 rho_4 cos(psi_1 - psi_2 + psi_3 - psi_4)
7. (2,2,1): + rho_1 r_2 rho_3 r_4 cos(psi_1 - phi_2 - psi_3 - phi_4)
8. (2,2,2): + rho_1 r_2 r_3 rho_4 cos(psi_1 - phi_2 + phi_3 - psi_4)

Claim: no constant shifts phi_l -> phi_l + e_l, psi_l -> psi_l + c_l make all eight coefficients
non-negative, even on one plaquette. Proof: positivity of terms 3 and 4 needs
e_1 + c_2 - c_3 - e_4 = 0 and e_1 + c_2 + e_3 - c_4 = 0 (mod 2 pi); subtracting,
c_4 - c_3 = e_3 + e_4. Term 2 needs e_1 + e_2 + c_3 - c_4 = pi, so e_1 + e_2 - e_3 - e_4 = pi.
Term 1 needs e_1 + e_2 - e_3 - e_4 = 0. Contradiction. QED

So in these coordinates the plaquette trace is not a positive-definite function on the torus of
phases, after any translation. Ginibre's method for abelian groups does not apply to the phases
given the moduli. This is the exact form of the one-line remark at row 1076 L206. It agrees with
row 1181 5.1, which lists the monomials without the signs.

### 2.2 Why a free-boundary induction over coupling fields is not a theorem schema (ARGUED)

Removing every plaquette that holds a link of a closed wall of links makes inside and outside
independent, so the class of coupling fields in [0, beta] is closed under an exact decoupling with
no pins. A finite-size criterion in that class would read: "if all normalized covariances at
distance d are below eps for every field of the class with free boundaries, then they are smaller
at 2d". This form is false in general lattice models: near a first-order point with a free
boundary that prefers one phase, a box of side below a crossover size d* sees one phase, a box
far above d* sees the other, and a box near d* sees a mixture. So smallness at one scale does
not pass to the next without a worst case over boundary data, and for Wilson SU(2) the worst
case over pins is false at large coupling (Theorem BH, method 36, Theorem D2). I state no
theorem. The remark only says why I do not attack candidate 11.

