lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T10:06Z

# gap-mini-neutral2-fable: second independent attack on (N-phys) (FINISH row 1184)

Working file of a Mac mini worker session, pinned at commit 654e32080 of branch claude/ym4d-hard-route. Research-stage
working state: it grants no status and is not a public claim. Every statement below carries one of the marks PROVED,
ARGUED, GUIDE, OPEN. Nothing here is computer-assisted.

## 0. Status log (times by `date -u` in the same command that writes the line)

- 2026-11-19T22:06Z start. Plan: (1) read the queue row, FINISH rule sections, GOAL.md; (2) read the exact statement of (N-phys)
  (row 1161, `library/gap-solve9-astra62.md` L146-148, restated in `library/gap-mini-branch-fable.md` L304-310) and its
  consumer; (3) read `library/gap-council-synthesis.md`, `parts/gap.md`, and the RESULT lines of rows 1143-1182;
  (4) write the statement and what a proof / a counterexample would have to be (Section 1); (5) attack, one route per
  response, appending each result here before thinking further; (6) only after my own attack is written, read
  `library/gap-mini-neutral-fable.md` (row 1180) and compare. Not read so far: row 1180's file.
- 22:17Z read: FINISH rule sections (L52-73, L299-350), GOAL.md, row 1184, `gap-council-synthesis.md` (full),
  `parts/gap.md` (L1-104 formulation, methods 19-36, lead rules; L186-207 obligations of rows 1127-1175; L213-322
  route registry, test table, price), RESULT lines of rows 1143-1183 (1143-1175 through `parts/gap.md`, 1176-1183 from
  FINISH), `gap-solve9-astra62.md` L1-160 (row 1161), `gap-mini-branch-fable.md` L1-400 (row 1179),
  `gap-phys-seed.md` L60-68 and L309-324 (trajectory, the set P, Theorem ZD-c). Not read: row 1180's file.
- 22:32Z Section 2 written: ten routes derived blind, each then found on file by `grep` (matches named there).
- 22:41Z Section 3 written (obstruction per route; Lemmas N1, N2; Remark N3).
- 22:45Z row 1180's file read for the first time: a header and a plan, no mathematics. Sections 4, 5 and a first
  RESULT line written.
- between 22:45Z and 22:48Z (not timed by `date -u`): correction after reading `gap-glue-max.md` L106, L312 and `gap-glue2-opus.md` L79: (N-phys) has the form of
  (GLUE-FP) of rows 895 and 920 (order-one margin, aspect 24); my first reading called that form new. Fixed in the
  reading of Section 2, in Section 5 item 1 and in the RESULT line.
- 22:48Z re-read of every PROVED item ((E1)-(E5), Lemmas N1, N2) and of every line anchor (each taken from `grep -n` or
  from a numbered print). One wording change: the gloss on Corollary Z4 in 3.2 is marked ARGUED.

## Repo search (lane folder, then other branches; lane part last run 22:51Z)

- `library/open-core.md` and `library/open-registry.md`: no entry for (N-phys), (GLUE-FP) or a neutral bound
  (`grep -n -i -E "N-phys|GLUE|neutral"`; the hits are items of the ultraviolet chain).
- FINISH rows that name (N-phys), (GLUE-FP) or (GLUE-STEP): 895, 896, 912, 913, 920, 1124, 1125, 1179, 1183 and this
  row; row 1180 names the same bound in words. By the queue row, the overlap stop does not apply to (N-phys) itself.
  It does apply to the open lemmas each route ends at ((SEAM), (VIR-log), (NOCRIT), (A), (AC'-lat), (BETA)_C, the
  trichotomy branch): each has an owner row, so none is attacked again here; Section 3.2 names them.
- Lane files: every route of Section 2 was searched with `grep` in `library/gap-*.md`, `library/prior/gap-*.md` and
  `parts/gap.md` after it was derived; the matches are in the last column of that table.
- Other branches (run 22:52Z, after the result was written): bare, blob-less, depth-1 fetch into a scratch folder of
  origin/main (8b11ae2) and the heads of pull requests 10114 (f76f6c6), 10133 (89faef2), 10134 (1e70c72), 10141
  (a2f6a43), 10144 (1f20846), 10149 (7fc6b1a). Scope: the 137 files whose path holds "mass-gap", "MASS_GAP" or a name
  `gap-*.md`. Patterns: "GLUE-FP", "N-phys", "one-cube", "neutral upper bound", "neutral excited", "even seed",
  "glue half". Hits: six files, all on main under `research/mass-gap/library/` (landed copies of lane files:
  `gap-crux-fp.md`, `gap-flux-exercise.md`, `gap-phys-seed.md`, `gap-skeleton-max-b.md`, two `prior/` notes), for
  "one-cube", "even seed" and "glue half" only. No hit for "GLUE-FP" or "N-phys" outside this branch, and no hit on
  any pull-request head. So no other branch holds a proof or an attack of the neutral bound.
- Not searched: files outside those 137 paths, and the Sussman-Alpoge repository (row 1161 cites their text: the
  account leaves the gap outside its theorem).

## 1. The statement, and what it says (written before any attack)

### 1.1 Statement

Notation of row 1161 (`gap-solve9-astra62.md`). Periodic spatial cube n^3, 4 | n, Wilson SU(2) at coupling beta.
F_0 is the symmetric positive transfer operator of the periodic cube on the gauge-invariant slice space, and
lambda_0 = norm(F_0). The centre flips C_1, C_2, C_3 (the sign of every i-link that crosses one plane x_i = const)
commute with F_0. The neutral sector is the joint +1 eigenspace. Put

    X(u) := Tr_neutral (F_0/lambda_0)^u = (1/8) sum over temporal twists e in (Z_2)^3 of Z_(0,e)(n^3 x u) / lambda_0^u,
    s(u) := X(u) - 1   (the neutral excited trace; row 1161 writes s(u) = X_(0,0)(u) - 1).

**(N-phys)** (row 1161 L146-148; row 1179 L304-309). Fix s_0 = 1/2, J = [1/2, 1], eps < 1/(8 x 5041), and
K = K(s_0, eps, J), the integer of row 1161's finite-aspect statement. There are a physical side L in
P = {2^i l_1} and j_0 such that for every cutoff j >= j_0 (spacing a_j, coupling beta_j, n_j = L/a_j, 4 | n_j) there
is an integer u_j with 3 <= u_j <= n_j/K and s(u_j; n_j^3) <= 1/2.

Consumer (rows 1161, 1179, 1065; under check in row 1183): (N-phys) gives the Pfaffian seed in both flux
alternatives, and so a cutoff-uniform gap on the centre-blind sector. I do not re-prove the consumer here.

### 1.2 Elementary exact facts (PROVED; each is a two-line argument)

Let 1 = mu_0 > mu_1 >= mu_2 >= ... > 0 be the eigenvalues of F_0/lambda_0 in the neutral sector (F_0 is positive
and trace class; the vacuum is simple and neutral by positivity of the kernel, row 1161 L17).

- (E1) s(u) = sum over i >= 1 of mu_i^u is non-increasing in u. So (N-phys) is the same as
  s(floor(n_j/K); n_j^3) <= 1/2 for every j >= j_0. Only the largest allowed time matters.
- (E2) Each level obeys mu_i^u <= s(u). So s(u) <= 1/2 at u <= n/K forces, with m := - log mu_1 the neutral gap of
  the cube in lattice units,  n m >= K log 2.   (NC1)
  The neutral gap of the cube, in units of its inverse side, is at least K log 2.
- (E3) Counting. The number N(E) of excited neutral levels with - log mu_i <= E obeys N(E) <= (1/2) exp(u E).  (NC2)
- (E4) Converse with a count. If n m >= z and a short-time bound s(t_0) <= S_0 holds at some t_0 < u, then
  s(u) <= S_0 exp(- m (u - t_0)) <= S_0 exp(- z (u - t_0)/n). (Each term: mu_i^u <= mu_i^(t_0) mu_1^(u - t_0).)
- (E5) Thermal form. log X(u) = log Z_neutral(n^3 x u) - u log lambda_0(n^3), and
  log lambda_0(n^3) = lim over v of (1/v) log Z(n^3 x v). So log X(u) is the free energy of the thermal torus minus
  the same volume of zero-temperature cylinder of the same cross-section.

### 1.3 Reading in physical units (ARGUED; guides the attack, proves nothing)

With T = 1/(u a) = K/L and V = L^3, (E5) says log X = p_neutral(T, L) V / T, the neutral pressure of the box. So
(N-phys) is:  p_neutral(T, L)/T^4 <= log(3/2)/K^3  at  T = K/L.
A free massless gas has p/T^4 = const > 0 at every T (photon: pi^2/45), so X = exp(c K^3) at every size: (N-phys)
fails at every size for a massless theory, and for SU(2) at a side below the confinement scale (rows 1143, 1153:
the short-period gluon gas). For a theory with gap m_phys and a particle gas, p V/T is about
(K^2 x/(2 pi))^(3/2) exp(-x) with x = m_phys L/K, so (N-phys) holds from about L = (K/m_phys)(3 log K + const) on.
By (NC1) it cannot hold below L = K log 2 / m_phys. So (N-phys) is a statement at a side of at least K log 2
correlation lengths. With any K of row 1161's size this is far outside every numeric test on this machine: no
GUIDE run of (N-phys) itself is possible, and none is made in this file.

### 1.4 What kind of statement it is (from the lane's test table, `parts/gap.md` L268-309)

(N-phys) is T_ev, uniformly in the cutoff, at one physical size (row 1179 Section 6 item 5). It is false for compact
U(1) at weak coupling, for the free photon, and for every product with a massless factor. A proof has to use the
non-abelian structure, a rate, the whole state space, and typical fields. Tools are of kind (K-one) or (K-flow).

## 2. Blind derivations and where they land (22:32Z; no new claim in this section)

Each line below was derived by hand in this session before the matching lane file was opened. The match was then
found with `grep` and is named. None of these is claimed as new. Every one stops at the same place: an order-one
statement about one physical scale beyond the last scale that perturbation theory controls ("the band").

| # | Blind derivation about (N-phys) | First failing step | On file |
|---|---|---|---|
| 1 | Pressure form: (N-phys) is p_neutral/T^4 <= log(3/2)/K^3 at T = K/L; a massless gas has a constant p/T^4 | nothing bounds the pressure from above below the scale of the gap | row 895 ("its content is thermodynamic", faces G1-G4, `gap-glue-max.md`); the floor: rows 975, 988 |
| 2 | Gap plus count: (E4) of 1.2 turns (N-phys) into "n m_ev >= c_K at one physical size" plus a cutoff-uniform short-time trace bound; (NC1) is the converse | the gap in units of 1/L has to pass a threshold above the massless value 2 pi | Lemma G5 of row 895 (`gap-glue-max.md` L188-196: (GAP_ev) and (COUNT)); Theorem ZD-c of row 720 (`gap-phys-seed.md` L311: (Z-UNB) and (BDD-Delta)) |
| 3 | Coupling integration: log X_beta(u) is the integral over [0, beta] of the thermal plaquette excess, because X = 1 at beta = 0 | needs the excess on the whole path; that is "no transition on the path" | Theorem D (f) of row 697 (`gap-crux-restate.md` L99); route RB; Proposition TR and (BETA)_C of row 895; (M5), (NOCRIT) |
| 4 | Rotated frame: log X(u; n^3) = n^3 u [F(n,n,u;inf) - F(n,n,n;inf)] + log(1 + s'(n; n^2 x u)), both terms >= 0 (F = free energy per site, decreasing in each side) | each term is again a neutral bound of the same strength; every exact inequality of the class points the same way | Lemma CS of row 895; shape comparison B3 (`gap-seed-shape.md`) |
| 5 | Mixing form: s(u) is the chi-square distance of the two-slice law from the product law, at slice distance u/2 | a volume-uniform minorization, or two-replica overlap bounds | Identity I1 of row 839 (`gap-compress-opus.md` L36); statement (A) of row 1132 and rows 1135, 1138; swap forms, rows 1118-1121; row 1161 (1)-(2) |
| 6 | Semi-classical window: on a thin torus with a centre twist the neutral gap is perturbative (of order pi/width) and vortices disorder the long plane; continue in the width | the continuation in the width crosses the band; the engine does not read a thin or twisted seed | Route T, (AC'-lat), rows 678-686 (`gap-ac-lat.md`); planar tension test of row 1177 |
| 7 | A model with the same ultraviolet data and no unique gapped vacuum: SU(2) at theta = pi (anomaly argument). So a proof must use positivity of the measure | belief-grade; it is outside the positive class and binds nothing | item 72 of row 838; C7 and N11 of row 1052 (`gap-wall-assumptions-opus.md` L168, L212) |
| 8 | Thermal count p/T^4 as a c-function; entropic monotones; the trace anomaly gives T d(p/T^4)/dT = (e - 3p)/T^4 | no monotone is proved, and a monotone alone gives no rate | F7 of row 1031 (`gap-afield-a-max.md` L342); rows 934, 1072 (MON statements, some FALSE) |
| 9 | Rigidity: if no size has the neutral bound, a rescaled limit is a gapless scale-covariant theory; exclude it | no rigidity theorem excludes an infrared-free abelian limit | rows 1017-1019, 1024 (Theorems CE, OM, CR, TRI) |
| 10 | Margin: X(u) < 2 at one time gives mu_1^u <= (1 + s_0)/2, so all later excited weights decay geometrically; this is all that row 1161's (4) uses of the premise. For the neutral part alone K = 80 is explicit: s(n/80) <= 1/2 gives s(n/2) <= (3/2)(3/4)^39 < 2.1e-5 | the seven (m, m) sectors need row 1161's compactness step, so K stays non-explicit for the Pfaffian seed | row 1161 (3)-(4), L48-63 |

Reading (corrected between 22:45Z and 22:48Z, after `grep -n -F "(GLUE-FP)"`). The order-one margin and the high aspect are not new with
row 1161. (GLUE-FP)_sigma of rows 895 and 920 (`gap-glue-max.md` L106, L312; `gap-glue2-opus.md` L79) reads: at one
physical pair of sizes with b >= 24 a, for every first-passage datum from some index on, S_ev(a; b^3) <= sigma, with
sigma = 1/10. That is (N-phys) with aspect 24 and margin 1/10 in place of aspect K and margin 1/2. The two are
members of one family, S_ev(n/K; n^3) <= sigma, and by Lemma N1 below the member (K, sigma) gives the member
(K', sigma^(K/K')) for every K' <= K on the same cube. What row 1161 added is the consumer: the neutral bound alone
gives the Pfaffian seed, where rows 895 and 920 had no consumer for an even seed ((EV-STEP) was open). In a theory
with a particle gas the seed at aspect 2 needs m_phys L of about 25, and (N-phys) with K = 80 needs about 1200
(GUIDE arithmetic with the gas formula of 1.3).

## 3. The routes, each with its obstruction (22:41Z)

(N-phys) is not proved here and no counterexample is built. Each route of Section 2 was followed to its first
failing step. This section gives, for each one, the exact statement where it stops and the statement that blocks it.
Statements proved in this file are marked PROVED; statements of other rows are cited with their standing there.

### 3.1 Two small statements about the form of (N-phys) (PROVED here)

**Lemma N1 (explicit aspect for the neutral part).** For integers 1 <= u <= v and every cube and coupling,
s(v) <= s(u)^(v/u). So s(u) <= 1/2 at some u <= n/32 gives s(n/2; n^3) <= 2^(-16) < 1/(8 x 5041).

Proof. s(v) = sum over i >= 1 of (mu_i^u)^(v/u), and sum a_i^p <= (sum a_i)^p for a_i >= 0 and p >= 1. With
u <= n/32 and v = n/2 the exponent is at least 16, and s(u) <= 1/2. 2^(-16) = 1.53e-5 and 1/(8 x 5041) = 2.48e-5. QED

Remark. Row 1161's bound (4) gives the same with the base (1 + s_0)/2. Lemma N1 is sharper in the sector (0, 0) only,
because there the top level is exactly 1 and is not in the sum. The seven sectors (m, m), m != 0, are not covered:
their top levels are not known a priori, and row 1161 handles them by its rank-and-slope argument and a compactness
step. So the integer K of (N-phys) stays non-explicit for the Pfaffian seed. For the even seed alone K = 32 is enough.

**Lemma N2 (two-sided size condition).** Let m_ev be the neutral gap of the cube n^3 in lattice units.
(a) (N-phys) at the cube forces n m_ev >= K log 2.
(b) Put u = floor(n/K). If s(t_0) <= S_0 at an integer t_0 < u, and m_ev (u - t_0) >= log(2 S_0), then s(u) <= 1/2.

Proof. (a) is (E2). (b) is (E4): mu_i^u <= mu_i^(t_0) mu_1^(u - t_0) for every i >= 1, so
s(u) <= s(t_0) exp(- m_ev (u - t_0)) <= S_0/(2 S_0). QED

Reading. (b) is Lemma G5 of row 895 at another aspect: a gap in units of the inverse side above a threshold, and a
count S_0 that may be any finite number uniform in the cutoff. (a) says that the first of the two is necessary.
So (N-phys) is the statement "the neutral gap of one physical cube, in units of its inverse side, passes a
threshold". With t_0 = u/2 the threshold lies between K log 2 and about 2K log(2 S_0). A free massless field has the
value 2 pi at every size (ARGUED: the lowest momentum).

**Remark N3 (quantifiers; ARGUED from the statements as written).** (i) A proof of (N-phys) would give it for every
K (take L larger). So the non-explicit K does no harm to a proof, and the natural target is: for every K there is L in
P with limsup over j of s(floor(n_j/K); n_j^3) <= 1/2. (ii) Proposition P'-ev of row 1179 is stated for "cutoffs for
which (SEED-any-phys) holds". So the gap clause needs (N-phys) only along the subsequence of cutoffs on which the
continuum datum is taken. This weakens "every j >= j_0" to "infinitely many j", if the T0 chain supplies the datum
along that subsequence. It does not change the difficulty.

### 3.2 Obstruction per route

| Route (Section 2) | Where it stops | The blocking statement | Standing |
|---|---|---|---|
| 1 pressure form | an upper bound on p_neutral/T^4 below the scale of the gap | every inequality that holds in the whole class (F1) is satisfied by Villain U(1) at beta >= 2^14, which has no neutral seed at any size; the free photon has s = exp(c K^3) - 1 at aspect K | test table, `parts/gap.md` L281-282 (THM given the published U(1) theorem; lane rows 786, 975, 988) |
| 2 gap plus count | n m_ev above a threshold at one physical size | Corollary Z4 of row 720 (`gap-phys-seed.md` L322): the gap in units of 1/L either stays below 256 D_0 + 29.64 at every size or grows for ever. ARGUED gloss: the lane has no statement at sizes below the seed size that separates the two branches (row 998 6b, `parts/gap.md` L44-46) | PROVED GIVEN Theorem ZD there; Lemma N2 here |
| 3 coupling integration | the thermal plaquette excess on the whole path [0, beta_j] | the path statement is false for positive-character weights with a first-order point: Proposition V (`gap-crux-fp.md` L356); for Wilson it is (NOCRIT), (VIR-log) of row 708 (`gap-mid-max.md` L172, L207), OPEN; and it needs the sharp rate (below) | on file |
| 4 rotated frame | a Casimir bound for the thin box and a rotated neutral trace | Lemma CS of row 895: the Casimir term is >= 0 and every exact inequality of the class points the same way | PROVED there; the row's check 896 keeps the elementary identities |
| 5 mixing | a minorization, or a two-replica overlap, uniform in the volume | (A) is strictly stronger than a uniform gap (link-refresh model, row 1135, checked by row 1138); independent-replica swaps pay a junction cost (Proposition J of check 1121). My own blind objection to (A) (a slice with ordered plaquettes cannot carry unit commutator noise) does not apply: row 1132 states (A) in Moser coordinates, where the slice law is Haar | on file |
| 6 thin twisted torus | the continuation in the width | Lemma G of row 678 (`gap-ac-lat.md` L51): the Gaussian model of the twist has decay rate at most 2 arcsinh(sin(pi/2n)), so the perturbative gap gives no rate uniform in the width; the engine reads no thin seed | proved by one author there |
| 7 theta = pi | - | a constraint, not a route: a proof must use positivity of the measure (C7 of row 1052) | BELIEF |
| 8 monotones | a sign for a scale derivative | (MONO-Delta) (`gap-phys-seed.md` L351) is false for the ordered Ising model (same file L371, a GUIDE run with the leading term by hand); MON-L-cov of row 1072 is false (check 1074); a sign alone gives no rate | on file |
| 9 rigidity | exclusion of a gapless scale-covariant limit | the third branch of the trichotomy of rows 1017, 1024 is not excluded by any statement on file | on file |
| 10 margin | - | not a route: Lemma N1 | PROVED here |

**The sharp-rate remark (ARGUED; it explains why route 3 cannot be closed by a crude bound).** Transport from strong
coupling at a fixed lattice box needs an upper bound on the rate at which a level falls: - d(log E_i)/d(beta) <= 1/B'.
By the Feynman-Hellmann identity of row 895 this is a bound on the plaquette excess of the state i over the vacuum,
in units of its energy. In the scaling region the true rate is 1/B with B = 11/(3 pi^2) (the one-loop coefficient,
a(beta) proportional to exp(- beta/B)). A bound with B' < B gives a lower bound on the mass in lattice units that
falls faster than the lattice spacing, so it gives nothing in the continuum limit. A bound that suffices has the
sharp constant up to an integrable error. So a transport proof contains asymptotic scaling of the gap itself. This
is the reading of (VIR-log) in row 708 ("a change of form, not of difficulty"), found again.

## 4. Comparison with row 1180 (22:45Z; read only after Sections 1-3 were written)

`library/gap-mini-neutral-fable.md` at this pin (commit 654e32080; its last commit there is 9bd75675d) holds a header,
a provenance note and a four-step plan. It holds no mathematical statement. So there is nothing to compare, and
nothing of row 1180 is used or checked here. Its plan (state the bound with every quantifier, grep, attack, record
the obstruction per route) is the same plan as this file's. If row 1180 reports a proof or a disproof of (N-phys),
it conflicts with nothing proved here, but it would have to pass Lemma N2 (a): the cube must have
n m_ev >= K log 2.

## 5. What this row adds, and what it does not

1. **(N-phys) is the crux lemma (GLUE-FP) of rows 895 and 920 with other constants (read from the files, lines
   in Section 2).** (GLUE-FP)_sigma is S_ev(a; b^3) <= 1/10 at b >= 24 a, at one physical size, for every late
   cutoff. (N-phys) is the same with aspect K and margin 1/2. By Lemma N1, (N-phys) with K >= 80 gives (GLUE-FP)
   with sigma = 1/10 on the same cube ((1/2)^(80/24) < 1/10), and (GLUE-FP) gives (N-phys) for every K <= 24. Rows
   895, 920 and 1125 attacked that statement ((GLUE-FP), (SEAM), (GLUE-STEP)) and stopped at an order-one bound on
   one physical scale. This row stops there too. The new fact of row 1161 is the consumer, not the statement.
2. **All ten blind routes are on file (Section 2).** None is new. For each one Section 3.2 names the blocking
   statement and its standing in the lane.
3. **Lemma N2** gives the necessary size: a cube with (N-phys) has neutral gap at least K log 2 in units of its
   inverse side. With any K of the size row 1161 needs this is far outside a numeric test here; no GUIDE run was
   made (memory was 60 percent free; no job was started and the numeric lock was not taken).
4. **Not done.** No proof of (N-phys). No counterexample. No new selective mechanism. The consumer (rows 1161, 1179,
   1065) was read, not re-proved. The Sussman-Alpoge repository was not searched in this row. The cross-branch search
   (section "Repo search") found no other attack of the neutral bound. No statement new to the lane is claimed
   beyond Lemmas N1 and N2, which are elementary (Lemma N2 is Lemma G5 of row 895 at another aspect).
5. **Evidence for the lead (the lead decides).** Four rows (895 and this one by Claude Fable, 920 by Claude Opus,
   1125 by gpt-6-astra) reach the same sentence on the neutral half. A further blind attack on (N-phys) by the Claude family
   is unlikely to differ. What is missing is unchanged: one inequality at order-one coupling that is false for a
   massless factor, or a step that carries asymptotic freedom across the band. The sharp-rate remark of 3.2 says
   that a transport proof in the coupling must contain asymptotic scaling of the gap with its exact rate.

Credits. Tadeusz Balaban (the renormalization group the lane's trajectory rests on). Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text (the transfer operator and trace identity GL8 that row 1161 uses; their
account leaves the gap outside its theorem, CA-I 2704-2712 as cited in row 1161). Sourav Chatterjee (the
weak-coupling free-energy method of rows 1143-1153). gpt-6.2-astra (rows 1143-1177, the chain and (N-phys) itself).
Earlier Claude rows 895 and 920 (the glue half), 720 (Theorem ZD-c), 708 ((VIR-log)), 839 (the chi-square form),
678 (the thin twisted torus), 1179 (Theorem BP).

RESULT: (N-phys) is NOT proved and NOT refuted; it stays OPEN. Claude Fable 5.2 max, Mac mini worker 1, author only, checked by no one. Ten independent routes were followed to their first failing step; every one is already on file (rows 678, 708, 720, 839, 895, 920, 1017, 1132-1135, 1161), and Section 3.2 names the blocking statement for each. PROVED here (elementary): Lemma N1, s(v) <= s(u)^(v/u), so (N-phys) with K = 32 already gives the even seed s(n/2; n^3) <= 2^(-16) (the (m, m) sectors still need row 1161's non-explicit K); Lemma N2, a cube with (N-phys) has neutral gap at least K log 2 in units of its inverse side, and a gap above about 2K log(2 S_0) with a finite short-time count S_0 gives (N-phys). Read from the files: (N-phys) is the crux lemma (GLUE-FP) of rows 895 and 920 (S_ev(a; b^3) <= 1/10 at b >= 24 a) with aspect K and margin 1/2; row 1161 added its consumer, not a new statement. ARGUED: a transport proof in the coupling needs the sharp asymptotic-scaling rate. Row 1180's file held no mathematics at this pin, so no comparison was possible. OPEN: (N-phys), the continuum datum, (BS), (W).
