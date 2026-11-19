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

Reading (ARGUED). The order-one margin and the high aspect of row 1161's form do not make the statement easier to
prove. By line 10 they trade the old threshold (1/5041 at aspect 2) for a box about K/2 times larger. In a theory
with a particle gas the old seed needs m_phys L of about 25 and (N-phys) with K = 80 needs about 1200
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
| 2 gap plus count | n m_ev above a threshold at one physical size | Corollary Z4 of row 720 (`gap-phys-seed.md` L322): the gap in units of 1/L either stays below 256 D_0 + 29.64 at every size or grows for ever; no statement at smaller sizes separates the two | PROVED GIVEN Theorem ZD there; Lemma N2 here |
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
