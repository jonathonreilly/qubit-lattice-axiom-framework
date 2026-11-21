lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T23:35Z

# gap-mini-seed-fable (queue row 1363): Mini Fable on the neutral seed

Pinned at commit 767a6b4e5 of claude/ym4d-hard-route. Started 2026-11-21T11:35Z (date -u). Nothing in this file is checked.

## Status log

- 2026-11-21T11:35Z (date -u): file opened; reading the queue row, GOAL.md and the FINISH.md rule sections.

- 11:36Z (date -u): read GOAL.md, FINISH.md L1-90 and L299-358 (rules), the queue row, the RESULT lines of rows 1340-1362, gap-phys-seed.md L296-326 (Theorems ZD, ZD-c, the two lead notes), row 1356 Sections 1-3 (Lemma M1, Corollary M2), row 1353 Sections 2 and 6 ((N-phys), Corollary BT2, (M-neutral)).
- 11:53Z (date -u): read `parts/gap.md` L1-104, the RESULT lines of rows 1318-1339; ran two registry greps (72 terms; counts in Section 1.2). Section 1 written.
- 12:06Z (date -u): literature probe (arXiv API, three queries, newest first): no record that proves a lattice SU(2) gap at a coupling of order one; every listed paper with a lane entry is already read (Section 2.4). Sections 2 and 3 written.

## 1. Inputs, repo search, and the statement in plain terms (written 11:53Z, `date -u`)

### 1.1 The statement

Notation of row 1356, Section 2 (`library/gap-mini-mneutral-fable.md` L78-84): n^3 is the spatial box, T the Wilson
transfer operator on gauge-invariant functions of one time slice, P_0 the mean of the eight centre translations,
lambda_0 the vacuum eigenvalue, x_a = lambda_a/lambda_0 the relative neutral eigenvalues, s(u) = sum over a >= 1 of
x_a^u, Z_+(t) = Tr(P_0 T^t) = lambda_0^t (1 + s(t)).

- (M-neutral), row 1353 6.3: there are an admissible physical side L and, for all late j, an integer w_j <= n_j/1024,
  a unit vector phi_j and c_j > 0 with Hilbert-Schmidt norm(P_0 T_j^(w_j)/c_j - |phi_j><phi_j|) <= 2/5.
- By Lemma M1 and Corollary M2 of row 1356 (check 1359: hold) this is s_j(2 w_j) <= 4/21, that is
  lambda_0^(2w) >= (21/25) Z_+(2w).
- (N-phys), row 1342 L93-94: s_j(u_j; n_j^3) <= 1/2 with 3 <= u_j <= n_j/512, 4 | n_j, n_j >= 2^70.
- Coupling range: beta_0 <= beta_j <= B_0 log(L/a_j) (lead note after Theorem ZD-c, `library/gap-phys-seed.md` L322).
- Consumer: rows 1161, 1179, 1342 with checks 1162, 1183, 1349 (the Jaffe-Witten gap clause from (N-phys)).

### 1.2 Repo search (rule 0a, "Repo first")

`library/open-core.md`: `/usr/bin/grep -n -i -E "neutral|N-phys|M-neutral|mass gap|rank-one"` returns no line, as rows
1353 and 1356 found. The statement is owned by the gap lane: rows 895, 920 ((GLUE-FP)_sigma), 1161, 1180, 1184, 1342,
1353, 1354, 1356, 1358, 1360 and their checks. Row 1364 (`gap-mini-seed2-fable`) runs the same brief in parallel on
worker 2; I did not read it.

Before choosing an attack I counted lane files (`library/gap-*.md`, `library/prior/gap-*.md`, `parts/gap.md`) that
contain each of 72 terms, one term per mechanism I considered. All mechanisms with a known name are on file:
log-Sobolev 92 files, Bakry 115, chessboard 113, Tomboulis 116, Villain 174, Seiler 194, Chatterjee 109, anisotrop 108,
string tension 87, small-volume 63, van Baal 57, Dobrushin-Shlosman 51, finite-size criterion 40, orbit space 39,
hypercontract 42, 1-form 32, Elitzur 31, trace anomaly 23, O'Neill 22, Koller 21, step scaling 21, Feynman-Hellmann 18,
interaction measure 16, Goldstone 12, Hagedorn 7, femto 5, tensor network 5, Karabali 4. Terms with 0 or 1 files:
"heat kernel action" 0, "cutoff phenomenon" 0, "warm start" 0, "Nash inequality" 0, "ultracontract" 1, "finitary" 1,
"entropy density" 1, "Lipschitz in beta" 1. So a new list of mechanisms is not a contribution (the lesson of rows
1188-1259), and this row does not write one.

Cross-branch search (main and the open YM4D pull requests): not repeated. Rows 1351 and 1353 record it for the same
statement on 2026-11-21 with no proof of the neutral seed found.

### 1.3 What the statement says in physical terms (GUIDE; arithmetic only, no claim)

For a theory whose lightest neutral state has mass m and a one-particle band of the usual form, in a box of side
n = r u at time u (lattice units), s(u) is about r^3 (u m/(2 pi))^(3/2) e^(-u m). At the least aspect ratio that
(N-phys) allows, r = 512, the bound s(u) <= 1/2 needs u m - (3/2) log(u m) >= 16.65, that is u m about 21.5 and a
box of side about 1.1 x 10^4/m. In thermal words: at the temperature T = m/21.5 the neutral pressure obeys
p/T^4 <= log(3/2)/512^3 = 3.0 x 10^(-9), against pi^2/15 = 0.66 for three free colours. So the statement is true for
any massive theory with a normal count, it is false by eight orders of magnitude for free gluons, and it sits at a
size 10^4 times the correlation length. Row 931 has the same reading for the periodic seed (`gap-direction-max.md`
L186-232, "(ANOM)").

## 2. How best to attack it (written 12:06Z, `date -u`; ARGUED unless a proof is cited)

### 2.1 The three legs, and where the statement lives

1. Ultraviolet leg. The account carries the late bare data to first-passage data. On file this leg ends at an
   effective lattice theory with an inverse coupling above 5 and no upper value (check 1331, quoted in row 1332,
   Lemma N). At that coupling the correlation length is far above one lattice unit of the effective theory. So the
   ultraviolet leg does not reach a regime where an expansion around a product measure converges.
2. Infrared leg. The engine (Theorem S, Theorem ZD-c; row 1161 for the neutral form) carries a seed at one physical
   size to every larger size. By 1.3 the neutral seed sits at a size near 10^4 correlation lengths.
3. The band between them. This is a statement about one lattice theory at a coupling of order one, robust under
   the small non-local corrections that the ultraviolet leg leaves. It is the lattice mass gap problem at
   intermediate coupling, with a count. No row has a method for it, and I found none (Section 3).

### 2.2 The two halves, each in its weakest form on file

(M-neutral) is equivalent, for one box, to two statements that carry no small number (Theorem ZD (D) and Theorem
ZD-c, `library/gap-phys-seed.md` L296-320, row 720; neutral forms: Lemma G5 of row 895, `library/gap-glue-max.md`
L188, and the split (a)/(b) of row 1180, `library/gap-mini-neutral-fable.md` L112). In the words of this row:

- (G) the gap half: the neutral gap of the cube, in units of the inverse side, is unbounded along the sizes
  ((Z-UNB)). Compact U(1) at weak coupling fails it. The stratified model ST_q of row 1342 has it.
- (C) the count half: a crude bound on the number of thermal states, by any constant, at one fixed aspect ratio
  ((BDD-Delta)). Compact U(1) has it. ST_q fails it.

Section 3.1 restates the step from (G) and (C) to (M-neutral) with the constants of this row.

### 2.3 What kinds of proof are possible

- (i) A hand proof needs an inequality that is exact at the vacuum (row 1356, Section 3, item 2: the two bounds
  together may lose the factor 25/21 on a lattice of at least 2^211 sites). The exact tools on file are reflection
  positivity and convexity of the masses. They give signs, not sizes. So a hand proof of either half must be a
  SIGN statement: a monotone quantity along the scale, started at first passage, where asymptotic freedom gives
  the sign. The sign statements on file are (MONO-Delta) (`gap-phys-seed.md` L355), (CAS) (row 708), (DRIFT)_c
  (`gap-ymcons-opus.md` L425), (MON') (`gap-brainstorm-max.md` L655-659), and the thermal form (ANOM)/(RATE)
  (`gap-direction-max.md` L104, L147, L212).
- (ii) A block step at order-one coupling into an end class (rows 1340-1362). Open; each landing on file needs
  the seeds of its cells.
- (iii) A computation that is a formal proof. Row 1326 (check 1331) sized every finite form on file: none is both
  finite and sufficient, because each sufficient form has the quantifier "every late cutoff", and the one carry
  that would remove it (Theorem T of row 1332, hypotheses A1-A3) contains the band as its hypothesis A2.

### 2.4 Literature probe (2026-11-21; arXiv API, queries "Yang-Mills" with "mass gap", lattice gauge "area law",
"Yang-Mills" "confinement" "rigorous"; sorted by submission date)

No record newer than those on file supplies a gap or an area law for SU(2) at a coupling of order one. Listed and
already in the lane: Cao, Nissim and Sheffield, arXiv:2509.04688 (strong coupling); Nissim, arXiv:2605.16162
(SO(3), strong coupling); Nair, arXiv:2608.10133 (three dimensions, not a proof); Faizal and Shabir,
arXiv:2606.19362 (read by rows 825 and later). Not in the lane and not read here: Bao, arXiv:2608.02452; Zhou,
Reed and Hayes, arXiv:2605.02156 (a survey). The probe is a title search, so it proves nothing about papers it
did not list.

### 2.5 Choice of attack

Kinds (ii) and (iii) are owned by rows 1326-1362, and three rows of this model on (ii) today (1353, 1356, 1360)
each ended at a statement on file. So I attack kind (i): I ask of each half whether some sign statement for it has
a SOFT proof, one that uses only positivity of the transfer operators, the hypercubic symmetry and the
first-passage start. A soft proof would be a closure with no computation. A soft statement that fails in a named
model tells the lane which property a proof must add. Section 3 does this for five statements. The comparison
models are those of the lane: compact U(1) (and the path to it through the fixed-length adjoint Higgs model,
item A16 of `gap-compact-rigidity-max.md` L94), ST_q, the ordered Ising model.

## 3. The attack: sign statements for the two halves (written 12:06Z, `date -u`)

Notation. Z(n_1, n_2, n_3; t) is the periodic Wilson partition function. For each direction there is a transfer
operator, positive, self-adjoint and trace class, with Z = Tr T^(period) ((TM); rows 667, 671, 731). S(u) is the
full excited thermal sum of the box, S(u) = Z(u)/lambda_0^u - 1, and s(u) <= S(u), because s keeps the neutral
states only and all terms are positive. E_0 = -log lambda_0 is the vacuum energy of the box, and
P(u) := log(1 + S(u)) is the thermal free energy (times -1).

### 3.1 Lemma GC (gap and a crude count at one box give (M-neutral); PROVED, two lines; on file in substance)

Let the neutral relative eigenvalues of one box obey x_a <= e^(-mu) for a >= 1, and let log(1 + s(u')) <= K at one
time u'. Then for every integer w with 2w >= u':

    s(2w) <= s(u') e^(-mu (2w - u')) <= (e^K - 1) e^(-mu (2w - u')).

So s(2w) <= 4/21 as soon as mu (2w - u') >= K + log(21/4). Proof: x_a^(2w) = x_a^(u') x_a^(2w - u'). QED

In physical units: let the box have side L, neutral gap m, and count log(1 + s) <= K at the time u' = L/2048.
Then (M-neutral) holds at 2w = L/512 if m L (1/512 - 1/2048) >= K + 1.66, that is m L >= 683 (K + 1.66). The count
K may be any number that does not grow along the late cutoffs; it only moves the size. This is Lemma G5 of row 895
and Theorem ZD (D) of row 720 in the notation of (M-neutral); I claim nothing new in it.

### 3.2 What positivity alone gives for the count (PROVED; on file as Lemma A and (ES-1))

(a) For a positive trace-class operator, Tr T^(2k) <= (Tr T^k)^2. So doubling one period gives
Z(.., 2n, ..) <= Z(.., n, ..)^2 (Lemma A, `library/gap-es1-astra.md` L37). Letting the time go to infinity:
E_0(2n, n_2, n_3) >= 2 E_0(n, n_2, n_3). The vacuum energy is superadditive under doubling a period.

(b) Hence, for a cube and one time u:

    P(u; (2n)^3) <= 8 P(u; n^3) + u C(n),      C(n) := E_0((2n)^3) - 8 E_0(n^3) >= 0.

Proof: log Z((2n)^3; u) <= 8 log Z(n^3; u) by (a) three times, and P = log Z + u E_0. QED

(c) Reading. The thermal free energy is subadditive in the volume only up to the Casimir term u C(n), which has
the wrong sign for a bound: positivity bounds C(n) from below (by zero), and a crude count needs it from above,
C(n) <= c/n. That upper bound is the statement (ES-1) of rows 748-753, which row 753 found is not bounded by
even thermal sums (`gap-es1-astra.md`). First failing step: an upper bound for the doubling Casimir defect.

(d) The same in the symmetric geometry: with f(L) := log Z(L^4)/L^4, positivity gives f(2L) <= f(L), and
f(L) - f(infinity) = sum over k >= 0 of [f(2^k L) - f(2^(k+1) L)], a sum of non-negative terms. (BDD-Delta) says
that the k = 0 term is at most D_0/(16 L^4). Positivity gives the sign of each term and no rate. The crude count
is therefore not a soft statement: ST_q satisfies every inequality of this subsection and has
f(L) - f(2L) of the order L^(-3).

### 3.3 The count from the gap and an ultraviolet count (fails by arithmetic)

A count is available at short times from the lattice itself, or from the ultraviolet leg at the first-passage
scale u_0: log(1 + s(u_0; L^3)) <= c (L/u_0)^3 (a Stefan-Boltzmann bound, c of order one). Lemma GC then needs
m (2w - u_0) >= c (L/u_0)^3 with L >= 1024 w. Since u_0 < 2w this forces m (2w) >= c 512^3 (2w/u_0)^3, so
(2w)^2 <= m u_0^3/(c 512^3) < u_0^2 when m u_0 < 1: no solution. The count must be taken at a time comparable to
2w, where it is an infrared statement. So the gap and ultraviolet data do not give the count. This agrees with
row 1259 (Lemma CD: the count is a low-temperature thermal bound) and with Lemma UVC of row 1356.

### 3.4 The thermal sign (the count half as a monotone)

With P(u) for a box of fixed aspect ratio, the crude count at every scale follows from the ultraviolet start and
the sign statement

    (A)   P(2u; (2n)^3) <= P(u; n^3)   for all sizes above the first-passage size,

which says that the pressure in units of T^4 does not grow towards the infrared. In the continuum it is
"energy density at least three times the pressure". It is the thermal sibling of (MONO-Delta) and it is
(ANOM)/(RATE) of row 931. Tests: free fields satisfy (A) with equality; a massive theory satisfies it; compact
U(1) satisfies it (GUIDE: scale invariance), so (A) is not the selective half. Soft proof: none. The inequality
compares two partition functions on a torus and on its dilated copy, and positivity of the transfer operators
relates only tori with a common period lattice (3.2 (a)). A class proof is excluded for a second reason (RECALLED
from the literature, not checked here): the coefficient of T^4 in the pressure is not monotone along
renormalization flows in general (the O(N) vector model in three dimensions between its critical point and its
Goldstone phase is the standard example). So (A) needs a property of the pure gauge theory. First failing step:
the same as (MONO-Delta), "open in the middle" (`gap-phys-seed.md` L388).

### 3.5 The gap half as a monotone

Let z(L) = L m(L) for the neutral gap of the cube. Two sign statements:

- (MONO-z): m(2L) >= m(L)/2. "Doubling the box at most halves the gap." Free massless fields satisfy it with
  equality, massive theories satisfy it, and the small-volume Wilson theory satisfies it (z of the order
  g(L)^(2/3), growing by asymptotic freedom; Luscher's small-volume expansion, RECALLED). It fails where the
  larger box has a tunnelling mode that the smaller lacks (two coexisting phases). It gives z bounded below by
  its first-passage value, which is not (Z-UNB).
- Strict growth: z(2L) >= (1 + eta) z(L) while z is below the engine threshold of Corollary Z4. This is
  (Z-UNB) with a rate. In the ultraviolet it is asymptotic freedom (d z/d log L = kappa z^4 at leading order,
  from z = c g^(2/3) and the one-loop flow; arithmetic). It is (MON') of row 859 and (DRIFT) of row 975 in the
  gap variable, and the entry "No infrared fixed point" of `gap-measured-vectors-max.md` L433.

Soft proof: none for either. A lower bound for the gap of the larger box from the smaller one is not a
consequence of positivity (the same remark as in 3.4: the two boxes have no common transfer operator), and
(MONO-z) is false at a first-order point of a positive, local, reflection-positive model. First failing step:
any lower bound for m(2L) in terms of data of the box L.

