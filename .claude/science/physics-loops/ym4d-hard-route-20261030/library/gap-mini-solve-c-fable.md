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

Status of this file: closed by the author at 2026-11-19T23:57Z. Checked by no one.

## 0. Log of steps

- Step 0 (22:59Z): file created; reading FINISH.md, GOAL.md, `parts/gap.md`, `library/open-core.md`.
- Step 1 (23:05Z): orientation read finished (list below). Attack not yet chosen.
- Step 2 (23:41Z): first pass at choosing an attack; eleven candidates checked against the
  record before any work (rule 0a). Table in Section 2.
- Step 3 (23:52Z): second pass, six more candidates. Two small exact statements written
  (3.1, 3.2). No attack opened on a statement already on file.
- Step 4 (23:55Z): third pass, fifteen more method words grepped (fourteen have files); read
  row 1141's RESULT (field-built frames) and the headings of Section 7.4 of row 1011. Verdict
  written (Section 4).
- Step 5 (23:57Z): own re-read of the file; three corrections (the slice distance in 3.2, the
  power count in 3.1, the counts in Section 4). Closed.

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

## 3. Second pass: six more candidates (statements about the record, then two exact statements)

| # | Candidate (my wording) | On file as | Verdict |
|---|---|---|---|
| 12 | A zero-free strip of Z in complex beta, then analytic continuation of exponential decay from small beta by a harmonic-measure bound | Route Z: rows 669-696, 988, 991 (Theorem Z of `gap-skeleton-max-b.md` L423, Theorem A, Proposition B, Lemma BC, the Schwarz form, the strip half-width 11/(6 pi) of `gap-skeleton-max.md` L116) | found again |
| 13 | A structural reason for a zero-free region: a Lee-Yang theorem with the plaquette couplings as the fields (3.1) | row 975, `gap-ymcons-opus.md` L359 (one recalled line: not of Lieb-Sokal type); items 7 and 40 of row 876, `gap-brainstorm2-max.md` L151 and L193 (Asano, for other polynomials) | not attacked on file as stated; fails in half-plane form (3.1) |
| 14 | A regularization chosen so that the gap is provable (fundamental or adjoint frozen Higgs at small hopping; a stochastic-matrix-form Hamiltonian with ground state the 3D Wilson measure; a five-dimensional construction) | Higgs bridge rows 905-923; Lemma AUX, Lemma HW of row 1016; Langevin and frustration-free files | found again in part; each stops outside the range of a convergent expansion or leaves the Yang-Mills class |
| 15 | Heat-kernel action as independent group Brownian motions on plaquettes, conditioned on the Bianchi identity; a linear flow in the coupling | Identity MIX and Remark POL of row 996 (heat flow in the coupling field); the intrinsic Brownian motion on connections with the curvature metric has a non-local density, so no reflection positivity (my reason, ARGUED) | no consumer |
| 16 | The time-independent gauge group as a rigid group: the Polyakov-loop effective weight is a positive-definite class function on SU(2)^(sites) | Identity HAM1 of row 1016; Borgs and Seiler (recalled). The response is a function of class angles only, so the twist is abelian | found again |
| 17 | Neutral gap from confinement (a bound of the neutral sum by flux-sector sums) | false in the class at a critical end point of a mixed action (the K7 row of the test table); Lemma FAC, council synthesis 2c | found again |

### 3.1 The couplings as fields for the plaquette traces (reading; one PROVED identity, one ARGUED remark)

Reading. With x_p = (1/2) tr U_p and nu the joint law of (x_p) under product Haar measure,
Z(b) = integral of exp(sum_p b_p x_p) d nu(x). So the coupling field b is the external field of a
"spin" system (x_p) whose whole interaction sits in the fixed measure nu (the Bianchi identity).
beta = 0 is the trivially mixing point. This is the frame of the Lee-Yang theorem and of the
Lebowitz-Penrose theorem that a ferromagnet in a non-zero field clusters exponentially (recalled,
not rebuilt). The question it suggests: is there a domain Omega containing the positive axis with
Z(b) non-zero whenever every b_p lies in Omega, by a structural (contraction-type) argument
instead of an expansion?

Identity (PROVED; the Laplace form of Identity CUBE of row 1016). For the six faces of one cube,

    Z_cube(b_1, ..., b_6) = prod_i (2 / b_i) * sum over d >= 1 of d^2 prod_(i=1..6) I_d(b_i).

Proof. exp(b x) = sum_j c_j(b) chi_j with c_j(b) = 2 d_j I_(d_j)(b) / b, d_j = 2j + 1 (the
character expansion of the Wilson weight). The six faces form a sphere with V = 8, E = 12. Each
link integral of two characters gives 1/d_j and forces equal spins; the index contractions
close into one loop at each vertex, which gives d_j per vertex; so the power is
d_j^(V - E) = d_j^(-4). So Z_cube = sum_d d^(-4) prod_i (2 d I_d(b_i) / b_i). Check:
as b -> 0, I_d(b) ~ (b/2)^d / d!, the term d = 1 gives 1. QED

Remark (ARGUED; GIVEN Theorem Z of Route Z as on file, which I did not re-read line by line,
and the account's law a(beta) = exp(-c_a beta (1 + o(1))), `gap-skeleton-max-b.md` L313). The
half-plane form, Z(b) non-zero whenever Re b_p > 0 for all p, cannot hold uniformly in the
volume for the lane's box families. Theorem Z turns a volume-uniform zero-free domain D into a
mass of at least kappa_0 omega(beta), omega the harmonic measure in D of the strong-coupling
anchor. For a half-plane (cut to a bounded domain) omega(beta) is of order 1/beta, since the
Green function of a half-plane at two points a << beta on the axis is about 2a/beta. A
polynomial lower bound on the mass contradicts the exponential law. The lane's strip result
(half-width at most 11/(6 pi)) says the same for strips; the half-plane case follows from it,
since a half-plane holds strips of every width. Published numerics are said to agree (Denbleyker, Du, Liu, Meurice and Zou
on Fisher zeros of SU(2) near beta = 2.2, at a distance from the real axis that I recall as of
order 0.1; recalled from memory, not read in this run, so the number is a gap, not a fact). So a structural zero-free domain can at most be a strip of
bounded width, and its width is set near beta = 2.2 by the distance of the Wilson axis from the
end point of the mixed-action transition line, a number and not a structure. I found no
contraction-type argument that yields a strip. Not attacked further.

### 3.2 The neutral premise as mixing from a typical start (PROVED; a restatement, no new handle)

Let F be the positive transfer operator on centre-flip invariant, gauge-invariant functions of the
spatial links of the cube, with simple top eigenvalue lambda_0 and eigenfunction Omega > 0. Let
P(A, dB) = Omega(B) F(A, B) dB / (lambda_0 Omega(A)), a Markov kernel reversible for
pi = Omega^2. Its u-step density against pi is k_u(A, B) = F^u(A, B) / (lambda_0^u Omega(A) Omega(B)).
Then, for even u,

    1 + s(u) = integral of k_u(A, A) pi(dA),     k_u(A, A) = 1 + chi^2( P^(u/2)(A, .) || pi ).

Proof. The first is Tr F^u / lambda_0^u. The second is k_u(A, A) = integral of k_(u/2)(A, B)^2 pi(dB),
by reversibility and the semigroup law. QED

So (N-phys) says: for some u at most n/512, the mean over a vacuum-typical start A of the
chi-square distance to the vacuum after u/2 steps is at most 1/2. It is an average over starts,
not a supremum. The same number s(u) is the sum of the squared canonical correlations between
two time slices at distance u/2 in the infinite-time measure (the canonical correlations at
distance t are the eigenvalue ratios to the power t). I record it because the worst-case forms are false (item 3 of Section 1)
and this form is exact; I found no tool that uses the average. Row 970 already works with typical
starts for flows (`gap-direction2-max.md` L266, L438).

## 4. Verdict

**The mass gap is NOT proved here, and nothing in the lane is disproved.** I opened no attack on
a statement that is already on file (rule 0a), and I found no statement that is not.

**What this row did.** It chose candidates from the target and from standard fields, 17 in all
(Sections 2 and 3), and checked each against the record before any work. Twelve are on file
with their first failing step (1-9, 12, 16, 17). Two are on file in part (11, 14). Two are
restatements with no consumer (10, 15). One (13, a Lee-Yang theorem in the coupling field)
has one recalled line on file; in half-plane form it fails GIVEN Theorem Z and the account
(3.1, ARGUED), and I have no structural argument for a strip. A third pass over fifteen more
method words (Chern-Simons and Kodama state, Nicolai map, abelian projection, Zwanziger,
spectral density, low-energy theorem, tensor networks, Wasserstein, supersymmetry, coupling
from the past, modular theory, Reeh-Schlieder, Hastings) found a file for each except "Witten
index", which gives no inequality (it counts vacua, it does not bound a gap). A count of a
word is not a count of an idea; I opened none of those files.

**Statements written here.**

| Statement | Mark | New? |
|---|---|---|
| 2.1 The eight monomials of the plaquette trace in Hopf-type coordinates carry signs + - + + - + + +, and no constant phase shift makes them all non-negative | PROVED | small addition to row 1076 L206 and row 1181 5.1 |
| 2.2 A free-boundary scale induction over coupling fields is not a theorem schema | ARGUED | a remark |
| 3.1 Z_cube = prod (2/b_i) sum_(d >= 1) d^2 prod I_d(b_i) | PROVED | the Laplace form of Identity CUBE (row 1016) |
| 3.1 No half-plane Lee-Yang theorem in the coupling field on the lane's box families | ARGUED, GIVEN Theorem Z and the account | a corollary of the strip result on file |
| 3.2 1 + s(u) = E_pi[k_u(A, A)], k_u(A, A) = 1 + chi^2(P^(u/2)(A, .) || pi) | PROVED | a restatement of (N-phys) |

None of these is selective, and none moves (N-phys), (W) or the gap.

**Where every candidate stopped (reading of the record together with my own passes; ARGUED).**

1. The two-dimensional engine carries one number, an upper bound on a stiffness, and it never
   needs a lower bound. That is possible because the twist is a rigid symmetry: the cost of a
   slow twist is a gradient form in every configuration, so no estimate on the field is needed
   to bound it.
2. In pure gauge theory every continuous twist with a small cost is small only relative to the
   field: its first-order cost is the covariant curl of the twist. A bound on that curl needs a
   bound on the roughness of the field at the same scale, which is a lower bound on the action
   (a stability estimate). So a one-number, one-sided induction does not close. Row 1141 proves
   the microscopic form of this: in a typical cell every adjoint field has covariant energy at
   least c/(1 + b + (log R)^(2/d)) times its squared norm.
3. With frames taken from blocked variables the defect per step is of the order of the squared
   coupling of that step times the stiffness, that is of order one, the same order as the
   one-loop gain. So the two must be computed together to one-loop accuracy. That is the
   block renormalization group itself, and at order-one coupling it has no small parameter.
4. The rigid groups that pure gauge theory does have (the time-independent gauge group; the
   centre; lattice translations and rotations) give abelian or discrete twists, or responses
   that every gauge theory has.
5. Soft routes to the neutral half (from confinement, from positivity, from analyticity in
   beta) each meet a model in the class where the conclusion fails (the end point of a
   mixed-action transition line, the projective plane S_0, Fisher zeros near beta = 2.2).

So the missing object is the one the record names: a selective inequality at order-one
response, on typical fields, with frames from blocked variables. I add no mechanism for it.

**For the lead.** Rows 1180, 1181 and 1184 (Fable, no method prescribed) each ended in the
lane's map, and so does this one. In this run 14 of 17 candidates were on file in full or in
part, 2 were restatements, and 1 fails as stated; 14 of 15 further method words have a file.
Row 1180's closing advice stands on this evidence: a further row whose task is a fresh choice
of route is not worth its cost. The file `library/open-core.md` has no line on the gap lane
(grep -i for "neutral", "N-phys", "mass gap", "Lee-Yang", "stiffness": 0 lines), so rule 0a
for gap rows rests on `parts/gap.md` and the FINISH rows only.

**Not done.** I did not read the Sussman-Alpoge repository in this run; I used what the lane
files quote from it. The lane's index of their outline lists the mass gap as their own open
requirement, not a result (`library/sa-index/chunk-01.md` L70, rows 594-599, "assumed"; L86,
rows 778-779, "named open"; `library/sa-index/chunk-04.md` L277, "a separate positive spectral
estimate for a mass gap"). So no step of the gap can be ported from their text. I did not read the primary texts of OpenAI's two-dimensional proofs; I
used the digest of row 1009 (credit: OpenAI for the mechanism; Claude Opus 5.5 for the
digest). No numeric run was made, so the numeric lock was not taken. No file other than this
one was edited. Checked by no one.

Credits. Balaban (renormalization group, ultraviolet trajectory); Sussman and Alpoge, with
Claude and Codex as authors of their text (the account, the positive transfer operator);
OpenAI (the two-dimensional O(4) and O(3) proofs); Ding, Huang and Yang; Durhuus and Froehlich
(the layer comparison); Lee and Yang, Lebowitz and Penrose, Lieb and Sokal, Ginibre, Dunlop and
Newman (the theorems recalled in 2.1 and 3.1); Denbleyker, Du, Liu, Meurice and Zou (Fisher
zeros, recalled); the lane rows cited in the tables, by row.

RESULT: Row 1190 (Claude Fable 5.2 max, Mac mini worker 3, 22:59Z-23:57Z; author only, checked by no one; no numeric run). The mass gap for four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved. 17 candidate attacks chosen from the target were checked against the record before any work: 12 are on file with their first failing step (stiffness with a bracket gain, the temporal-gauge rigid group, shape twists, the non-central vortex path, Feynman-Hellmann continuity, the pinned flat plane, Hopf-coordinate inequalities, (EP), the thermodynamic form, Route Z, Polyakov-loop positivity, gap from confinement); 2 are on file in part (coupling-field classes, other regularizations); 2 are restatements with no consumer (the chi-square form, the Brownian form); 1, a Lee-Yang theorem in the coupling field, fails in half-plane form GIVEN Theorem Z and the account (ARGUED). PROVED, small, not selective: the sign pattern + - + + - + + + of the eight plaquette monomials cannot be removed by phase shifts; Z_cube = prod(2/b_i) sum_d d^2 prod I_d(b_i); (N-phys) is a bound on the mean chi-square distance from a vacuum-typical start after u/2 steps, u at most n/512. ARGUED: a one-sided stiffness induction cannot close in pure gauge theory, because a small twist cost needs a roughness bound on the field. OPEN, unchanged: (N-phys), the continuum datum, (BS), (W), and a selective inequality at order-one response.
