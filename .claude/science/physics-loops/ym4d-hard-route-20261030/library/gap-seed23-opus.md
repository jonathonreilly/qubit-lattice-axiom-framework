# The glue half from slabs? Tree gauges give the seed below beta_W = 1/3 (FINISH row 835), by Claude Opus 5.5 (max effort), author

- Clone: `/Users/jonreilly/ym4d-lead/clone`, commit `83f6ffafe92a18e8d6d415b47453e830424e4160`
  (`git pull --ff-only`: "Already up to date").
- Lane directory D = `.claude/science/physics-loops/ym4d-hard-route-20261030`. Line numbers below are at this commit.
- Read in full: `D/library/gap-vmf-lip.md` (609 lines), `D/library/gap-vmf-lip-check-opus.md` (153),
  `D/library/gap-arealaw-opus.md` (586), `D/library/gap-arealaw-check-astra.md` (470),
  `D/library/gap-crux-fp.md` (502). Read in part: `D/library/gap-crux-restate.md` lines 1-294
  (Sections 1, 3.4: Lemmas A, K, X, E, E', Theorem S); `D/library/gap-mid-max.md` lines 217-306
  (Identity FL, Lemma M, Proposition MIX, Lemma DC and Lemma INF in total-variation form, Theorem DOB);
  `D/library/gap-seed-shape.md` lines 1-182 (lead note, Theorem SH, thresholds, Theorem D-shape);
  `D/library/gap-novelty-opus.md` lines 1-140 and a keyword search of the rest; `D/library/gap-es1-opus.md`
  lines 1-75 (the vacuum-energy defect Delta); `D/FINISH.md` row 835.
- No repository file was edited. One GUIDE run (Section 6.4), under 300 MB, a few seconds; it decides nothing.
- Marks. PROVED: proved here by me, every step written. READ: read in the named source (path, line).
  ARGUED: an argument is given, not to proof standard. GUIDE: a run or a heuristic; it decides nothing.
  OPEN: not settled.
- Credits. Theorem V, Corollary V1, Lemma DC and Lemma INF in chord form, R-a with (AS-bg), Theorem DOB in
  chord form: Codex gpt-6-astra (`gap-vmf-lip.md`, row 785), checked line by line by Claude Opus 5.5
  (row 790). The layer model, Identity L, Proposition TW, the statement (AS-bg) and the block count
  12 beta/(1 - 6 beta): Claude Fable 5.2 (`gap-crux-fp.md`, row 712). Lemma S, Lemma SC, Lemma R, Theorem A:
  Claude Opus 5.5 (`gap-arealaw-opus.md`, row 825), checked by Codex gpt-6-astra (row 828). Identity FL,
  Lemma M, Proposition MIX, Theorem DOB (total-variation form): Claude Fable 5.2 (`gap-mid-max.md`,
  row 708), checked by Claude Opus 5.5 (row 709). Theorems S, D (row 697) and SH, D-shape (row 705):
  Claude Fable 5.2; Lemma E', Corollary S3': Codex gpt-6-astra (row 699). The comparison method is
  Dobrushin's. The slab idea is due to B. Durhuus and J. Frohlich (1980), as stated by Cao, Nissim and
  Sheffield (READ through `gap-arealaw-opus.md` lines 97-160). The axial (temporal) gauge is classical
  (attribution from memory, not read); Lemma G below proves the form used, so no recalled fact enters a
  proof. Forest gauges for this problem are claimed by D. Bhattacharjee, U. Bhattacharya and co-authors
  (unrefereed; READ through `gap-novelty-opus.md` lines 16-30 and 351-358: "a field of straight lines
  fixes one link in every plaquette", twelve partners, beta_W < 1/3, free-boundary limits and an
  infinite-volume transfer matrix); their proofs and their line field were not read.

## 1. Answer in brief

1. **The key question.** A background-uniform slab bound does not give (17) by itself. With time
   transverse, the slabs are the layers of time links. Given the spatial links they are independent
   layer models (Lemma S), and Lemma SC controls each one uniformly. But (17) is a response across
   a/2 slabs, and it runs through the spatial links between them. Any scheme that combines Lemma SC's
   slab responses with single-link chord bounds has exactly the threshold of the single-link matrix
   of the same measure (Proposition NG, PROVED): 2/9 for the ungauged measure. So the slab bounds
   give no gain. This is the precise failure point of the "slab-wise comparison" in its literal form.
2. **What the slab structure does give.** Gauge invariance turns every time slab but one into the
   identity (Lemma G, the temporal gauge). The remaining slab can sit at the cut, inside the set D of
   Lemma M, where nothing is needed. Dobrushin's comparison needs its condition only off D
   (Lemma DC', PROVED). Then every interior spatial link has 14 neighbours, not 18, and (17) holds
   with q = 7 beta/2: the seed and the gap for **beta < 2/7** (Theorem T, PROVED).
3. **One step further: a 4D line field.** A period-2 field of straight lines in all four directions
   puts exactly one fixed link in every plaquette of Z^4 (Lemma LF, PROVED by a 24-case hand check;
   found by a GUIDE search). On the periodic torus, cut each line once: the time lines at the time
   cut, the spatial lines at one seam plane per direction. Put the seams into D too. Every link off D
   then has exactly 12 neighbours. This gives (17) with q = 3 beta, the full seed (both halves) and
   a volume-uniform gap on periodic cubes, in all flux sectors, for **0 < beta < 1/3** (Theorem F,
   PROVED, given the checked inputs). Example: beta = 1/4, a = 282 gives m(L^3) >= 1/4700 for
   L >= 18048. The vacuum-energy defect obeys the same bound (Corollary F2).
4. **The ceiling of this method.** In every tree gauge the average number of free partners of a free
   link is at least 12 (Lemma AVG, PROVED). So single-link chord Dobrushin with the uniform constant
   1/4 cannot pass beta = 1/3 in any tree gauge, with or without slabs. No forest on a torus has
   exactly one fixed link in every plaquette of two consecutive slices (Proposition NP, PROVED), so
   defects are needed; Theorem F puts them all in D.
5. **Beyond 1/3.** The flux half holds up to 2/3 ((AS-bg), READ). The glue half S_0, hence the seed,
   is **OPEN for 1/3 <= beta < 2/3**. What is missing is a contraction of the gauge-fixed 4D measure
   better than 12 partners with constant 1/4 each: a block or field-dependent estimate, not a slab
   statement.

## 2. Definitions used (READ)

- **Seed, thermal sum.** `S(t;B) = sum_{i>=1} (lambda_i/lambda_0)^t` for the transfer operator of
  the periodic box B (`gap-vmf-lip.md` lines 426-434). It contains every excited state, all electric
  flux sectors included. The seed is `S(a;(2a)^3) < 1/1650` (lines 451-458).
- **The two halves (Identity FL).** `P_0 = (1/8) sum_k C^k` projects on zero electric flux;
  `1 + S_0 = Tr(T^t P_0)/lambda_0^t` (glue half); `U = (1/8) sum_{k != 0} (1 - Z[k]/Z)` (flux half);
  `0 <= S_0 <= S`, `0 <= U <= S/(1+S)`, `1 + S = (1 + S_0)/(1 - U)` (`gap-mid-max.md` lines 219-223;
  `gap-vmf-lip.md` lines 538-548). A bound on the full S bounds both halves.
- **D-shape.** `Phi_B(a;beta) = 2F(a,B) - F(2a,B) = 12 a|B| int_0^beta (abar_{2a,B}(s) - abar_{a,B}(s)) ds`
  and `S(a;B) <= e^{Phi_B} - 1` (`gap-seed-shape.md` lines 165-176; `gap-vmf-lip.md` lines 506-520).
  Here `abar_{t,B}(s)` is the mean of `1 - x_p` over plaquettes, `x_p = (1/2) tr U_p`, and the weight
  is `exp(-s sum_p (1 - x_p))` against Haar probability.
- **Theorem SH arithmetic.** If `S(a;(2a)^3) < 1/1650`, then `m(L^3;beta) >= 3/(50a)` for every
  integer `L >= 64a` (`gap-vmf-lip.md` lines 549-582, checked in row 790 Section 6). Smaller cubes
  have positive gaps by (TM).
- **Lemma M (cut).** `mu~` = the first-half marginal of the torus (2a,B), times mod a. Its one-link
  kernels are the Gibbs kernels of (a,B) off D = {space links at times 0, a-1} U {time links from
  a-1} (`gap-mid-max.md` lines 258-264; `gap-vmf-lip.md` lines 468-474).
- **Corollary V1.** `d_Lip(mu_F, mu_F') <= |F - F'|/4` for the laws `mu_F ~ e^{F.h} sigma(dh)` on S^3
  in the chord metric, for all F, F' (`gap-vmf-lip.md` lines 209-220).
- **Lemma DC (chord form)** (`gap-vmf-lip.md` lines 222-313) and **Lemma INF** (lines 315-347):
  layer model `C_xy <= beta/4`, row sum `3 beta/2`; 4D measure `C_lk <= s/4`, row sum `9 s/2`.
- **Lemma S and Lemma SC** (`gap-arealaw-opus.md` lines 186-248; check row 828 HOLDS): given all
  non-vertical edges, the vertical slabs are independent layer laws; a layer law with row sum
  `q = 3 beta/2 < 1` has `|mu^xi(h_x) - mu(h_x)| <= 2 G_xy <= 2 q^{d(x,y)}/(1 - q)`, uniformly in the
  background.
- **Vacuum-energy defect.** `Delta(c,d) = a (2 e(a,c,d) - e(2a,c,d))`, `e(A) = log lambda_0(A)`
  (`gap-es1-opus.md` line 40); `e(A) = lim_t F(t,A)/t` (`gap-crux-restate.md` line 178, Lemma K (a)).

## 3. The key question: does (17) follow from a slab-wise comparison?

Take the time direction as the vertical direction nu of Lemma S. The slabs are the time-link layers
k = 0, ..., t-1. H is the sigma-algebra of all spatial links. Given H, slab k is the layer law
`mu_k` on B with faces (U(k), U(k+1)) (Lemma S (iii), READ `gap-arealaw-opus.md` lines 197-209); its
partition function is `I(U(k), U(k+1))` (READ `gap-crux-fp.md` lines 371-375).

**Lemma HR (the whole difference sits in the spatial links; PROVED).** Let f be a bounded function of
the links of (a,B) whose time links lie in slabs 1, ..., a-2 only. Put `F_f(H) = E[f | H]`, computed
with the product of the layer laws of those slabs. Then
`mu_{a,B}(f) = mu_{a,B}(F_f)` and `mu~(f) = mu~(F_f)`, with the same function F_f.

Proof. For `mu_{a,B}` this is Lemma S (iii). For `mu~`: in the torus (2a,B), given all spatial links,
the slabs are independent and slab k has a law that depends only on its faces (Lemma S (iii) on the
long torus). For 1 <= k <= a-2 both faces lie in the first half. So the conditional law of these slabs
given the first-half spatial links and all other first-half links is still the product of the same
layer laws. Integrate. QED

So `mu_{a,B}(f) - mu~(f) = (mu_{a,B} - mu~)(F_f)` restricted to the spatial-link marginals. Lemma SC
says only that F_f depends on far spatial links with weights `q^d`, `q = 3 beta/2`. It says nothing about
the two spatial-link marginals. Those are periodic and open chains of slices with the effective
interaction `-beta V(U(k)) + log I(U(k), U(k+1))`. Comparing them across a/2 steps is the 4D mixing
problem. This is exactly where the slab route has to stop being slab-wise.

**Proposition NG (slab blocks give no gain; PROVED).** Let Lambda = H u V be finite, C >= 0 a matrix on
Lambda, and V = V_1 u ... u V_m with `C_{V_k V_l} = 0` for k != l and `rho(C_VV) < 1`. Put
`G = sum_n C_VV^n` and `M = C_HH + C_HV G C_VH` (the influence matrix on H after each slab is updated
exactly and its response is bounded by the Neumann series, as in Lemma SC). If `rho(C) >= 1`, then
`rho(M) >= 1`, and no weights w > 0 on H give `M w <= alpha w` with alpha < 1.

Proof. Perron-Frobenius gives x >= 0, x != 0, with `C x = rho x`, rho = rho(C) >= 1. The V rows read
`(rho I - C_VV) x_V = C_VH x_H`. Since rho >= 1 > rho(C_VV),
`(rho I - C_VV)^{-1} = sum_n rho^{-n-1} C_VV^n <= G` entry by entry, so `x_V <= G C_VH x_H`. The H rows
then give `rho x_H = C_HH x_H + C_HV x_V <= M x_H`. If x_H = 0, the V rows force x_V = 0; so x_H != 0.
From `M^n x_H >= rho^n x_H` with x_H >= 0 nonzero, `rho(M) >= rho >= 1`. Finally, `M w <= alpha w` with
w > 0 gives `M^n w <= alpha^n w`, hence `rho(M) <= alpha`. QED

**Application (PROVED).** Ungauged 4D measure at coupling s, sides at least 3. Lemma INF (13) gives
`C <= (s/4) A`, A the adjacency of "share a plaquette", which is 18-regular; so `rho((s/4)A) = 9s/2`
with the constant eigenvector. Slab independence is `C_{V_k V_l} = 0`. Hence no scheme of this kind
closes at s >= 2/9, for any vertical direction. Explicitly: a non-vertical link has 14 non-vertical and
4 vertical partners, a vertical link 12 and 6. The constant vector is an eigenvector of M with
eigenvalue `7s/2 + 3s^2/(1 - 3s/2)`, which is below 1 iff `9s^2/4 - 5s + 1 > 0`, that is s < 2/9 (roots
2/9 and 2). In the total-variation normalization (constant s per partner) the same computation gives
1/18; this is the exact form of the rough count 12 beta/(1 - 6 beta) of `gap-crux-fp.md` line 406.

**Answer to the key question.** In its literal form, no: neither (17) nor the vacuum-energy defect
follows from background-uniform slab bounds beyond the single-link range of the same measure.
Lemma HR names the object that must be compared (the spatial-link marginals), and Proposition NG shows
that slab blocks with Lemma SC's bounds never beat the Perron root of the single-link matrix. The time
slabs help in a different way: they can be removed. That is Section 4.

## 4. Three tools: tree gauges, comparison off D, the cut in a gauge

**Lemma G (tree gauge; PROVED).** Let E be the links of a torus and F a subset of E without cycles.
Let `rho(U) = prod_p exp(-s(1 - x_p))` and let f be bounded, measurable and gauge invariant. Then
`int f rho dU = int (f rho)(1_F, V) dV`, where `(1_F, V)` puts 1 on every link of F and V on E \ F,
and dV is Haar probability on `SU(2)^{E \ F}`. So the gauge-fixed law
`mu_F(dV) = rho(1_F, V) dV / Z` has the same Z and the same expectation of every gauge-invariant f.

Proof. Gauge action: `(U^g)_l = g_x^{-1} U_l g_y` for l from x to y. In each tree of F fix a root r and
set g_r = 1. Walking away from the root, a link l of F between a known site and a new site determines
g at the new site uniquely so that `(U^g)_l = 1` (g_y = U_l^{-1} g_x if l runs from x to y, g_y = U_l g_x
if it runs from y to x). So g = g(U_F) depends on the links of F only, and `U^{g(U)}` is 1 on F.
For fixed U_F the map `U_{E\F} -> V := (U^{g(U)})_{E\F}` is a product of left and right translations,
so it keeps Haar measure. By Fubini, (U_F, V) is Haar distributed on `SU(2)^F x SU(2)^{E\F}`.
Gauge invariance gives `(f rho)(U) = (f rho)(U^{g(U)}) = (f rho)(1_F, V)`. Integrate. QED

*The temporal gauge.* F = all time links from times 0, ..., t-2 is a forest (one path per spatial
site). In slab language: every time slab but the last is set to the identity, and the last slab
carries the layer model `I(U(t-1), U(0))` with the Polyakov variables as its spins. This is how the
time-transverse slab structure is used below: not bounded, removed.

**Lemma DC' (Dobrushin's comparison with the condition only off D; PROVED).** Let Lambda be finite,
`Omega = (S^3)^Lambda`, D a subset of Lambda. For i not in D let `gamma_i(. | w)` be measurable kernels
depending on w off i, with `C_ij` as in (8) of `gap-vmf-lip.md` (line 228) for j != i, and
`max_{i not in D} sum_{j in Lambda} C_ij <= alpha < 1` (the sum includes j in D; rows of D are not
used). Let mu_1, mu_2 be laws on Omega such that gamma_i is a version of the conditional law at i of
both, for every i not in D. Let f have finite seminorms delta_i(f) (line 240) with delta_j(f) = 0 for
j in D. Then

    |mu_1(f) - mu_2(f)| <= 2 sum_{i not in D} delta_i(f) sum_{j in D} [(I - C~)^{-1} C_{.D}]_{ij}
                        <= 2 Delta(f) alpha^d / (1 - alpha),                               (DC')

where C~ is C on (Lambda \ D)^2, `C_{.D}` its block (Lambda \ D) x D, and d is the distance from the
support of f to D in the graph that joins i, j when C_ij + C_ji > 0.

Proof. If Lambda \ D is empty, f is constant. Otherwise let N' = |Lambda \ D|, Gamma_i as in
`gap-vmf-lip.md` line 255, and `P = (1/N') sum_{i not in D} Gamma_i`. By (9) there (line 263), for
j not in D: `delta_j(Pg) <= (1 - 1/N') delta_j(g) + (1/N') sum_{i not in D} C_ij delta_i(g)`, and for
j in D: `delta_j(Pg) <= delta_j(g) + (1/N') sum_{i not in D} C_ij delta_i(g)`. Write delta' for the
vector off D. Then `delta'(Pg) <= R'^T delta'(g)` with `R' = (1 - 1/N') I + C~/N'`, whose row sums are
at most `q' = 1 - (1 - alpha)/N' < 1`. So `Delta'(P^t f) <= q'^t Delta'(f)`, and
`|P^{t+1} f - P^t f| <= (2/N') Delta'(P^t f)` (each Gamma_i moves g by at most osc_i(g) <= 2 delta_i(g)).
Hence P^t f converges uniformly to some h with delta_i(h) = 0 off D: h depends on w_D only. Each
mu_k is invariant under every Gamma_i, i not in D, so `mu_k(f) = mu_k(P^t f) = mu_k(h)`. Thus
`|mu_1(f) - mu_2(f)| <= osc(h) <= 2 sum_{j in D} delta_j(h)` (chord diameter 2, one coordinate at a
time). Summing the D-inequality over t, with delta_j(f) = 0 on D and
`(1/N') sum_t R'^t = (I - C~)^{-1}` (since I - R' = (I - C~)/N'), gives
`delta_j(h) <= sum_k delta_k(f) [(I - C~)^{-1} C_{.D}]_{kj}`. This is the first inequality. A nonzero
entry `(C~^n C_{.D})_{kj}` needs a path of length n + 1 >= d, and `sum_{j in D} (C~^n C_{.D})_{kj} <=
alpha^{n+1}`; sum over n >= d - 1. QED

Lemma DC of `gap-vmf-lip.md` is the case where the condition also holds on D. The gain is that D may
contain sites with large influence sums.

**The cut in a gauge.** Let a >= 3, B with sides at least 3, n = (a,B), n' = (2a,B), and Lambda_0,
D_cut = {space links at times 0, a-1} U {time links from a-1} as in Lemma M. Let F be a forest on n
and F' a forest on n'. Assume (C1): a set D containing D_cut is given such that, under the reduction
of times mod a, F' restricted to Lambda_0 and F agree on every link outside D. Let mu_1 = mu_{n,F}
and let mu_2 be the image of the Lambda_0-marginal of mu_{n',F'}, both read as laws on
`Omega_F = SU(2)^{E(n) \ F}`; the coordinates of Omega_F that are fixed in F' (they lie in D) are set
to 1 under mu_2.

**Lemma MG (PROVED).** (a) For every free link l of F not in D, mu_1 and mu_2 have the same conditional
law at l: the law `mu_{F_l}` on S^3 with `F_l = s sum_{p ni l} W_p`, where W_p is the unit quaternion
staple of p computed with the links of F equal to 1. (b) Every free partner k of l (a free link sharing a
plaquette with l) has influence `C_lk <= s/4`; every other link has `C_lk = 0`. With sides at least 3,
two distinct links share at most one plaquette, so the row sum at l is at most (s/4) times the number
of free partners.
(c) For every plaquette p of n whose links lie off D, and which does not cross the cut,
`mu_{a,B}(x_p) = mu_1(x_p)` and `mu_{2a,B}(x_p) = mu_2(x_p)`, with x_p evaluated with F-links equal to 1.

Proof. (a) The density of mu_{n,F} is `rho(1_F, V)`; as a function of U_l it is
`exp(s sum_{p ni l} x_p)` up to factors free of U_l, and `x_p = <U_l, W_p>` after the cyclic and
inverse identities of `gap-arealaw-opus.md` lines 63-69 (READ). For mu_2: l is not in D_cut, so its six
plaquettes lie in Lambda_0 without wrapping (`gap-mid-max.md` line 262, READ). Under mu_{n',F'} the
conditional law of l given all other free links is the same vMF law with staples from these plaquettes,
computed with F'-links equal to 1; by (C1) and since these plaquettes contain no link of D on which F
and F' differ, the staples equal those of (a). This law depends on Lambda_0 coordinates only, so it is
also the conditional law under the marginal. (b) Changing one free partner k of l changes one staple by
exactly `|U_k - U_k'|` (unit quaternion multiplication is an isometry); Corollary V1 gives `s/4`.
(c) Lemma G on each torus, and the marginal for n'. QED

## 5. The seed beyond 2/9

### 5.1 Theorem T: the temporal gauge (time transverse to the slabs), beta < 2/7

**Theorem T (PROVED, given Corollary V1, Lemma M, D-shape (a), (d) and Theorem SH, all READ and
checked in rows 707, 709, 790).** Let 0 < beta < 2/7, q = 7 beta/2, a >= 3, j = floor(a/2), and B a
periodic box with sides at least 3. For 0 <= s <= beta:

    |abar_{2a,B}(s) - abar_{a,B}(s)| <= 6 q^{j-1}/(1 - q),                                   (17T)
    0 <= Phi_B(a;beta) <= 72 a|B| beta q^{j-1}/(1 - q).                                      (18T)

If `576 a^4 beta q^{j-1}/(1 - q) <= 3/5000`, then `S(a;(2a)^3;beta) < 1/1650` and
`m(L^3;beta) >= 3/(50a)` for every integer L >= 64a.

Proof. F = time links from 0..a-2 on n, F' = time links from 0..2a-2 on n', D = D_cut. (C1) holds:
both are the time links from 0..a-2 inside Lambda_0, and the time links from a-1 lie in D. The free
links off D are the space links at times 1..a-2. Such a link U(k)_b lies in four space plaquettes
(12 distinct space partners in slice k) and in two time plaquettes, whose time links are fixed; their
only free partners are U(k-1)_b and U(k+1)_b. So it has 14 free partners, and Lemma MG (b) gives row
sums at most `14 s/4 = 7s/2 <= q` off D. Let P be the 3|B| space plaquettes at time j and the 3|B| time
plaquettes of the slab [j-1, j]. A space plaquette has 4 free links (Delta(x_p) <= 4); a time plaquette
has 2 (`x_p = <U(j-1)_b, U(j)_b>`, Delta <= 2). Every influence edge joins space links whose times differ
by at most 1, and D cuts the time circle at 0 and a-1; so the distance from P to D is at least
`min(j - 1, a - 1 - j) = j - 1`. Lemma DC' with mu_1, mu_2 of Lemma MG gives
`|mu_1(x_p) - mu_2(x_p)| <= 2 Delta(x_p) q^{j-1}/(1 - q)`. By translation invariance of the two
ungauged torus measures (`gap-mid-max.md` line 272, READ) and Lemma MG (c), abar_{t,B} is the mean over P
of `1 - x_p` under mu_1 (t = a) or mu_2 (t = 2a). Half of P has bound 8, half has 4: (17T). (For a = 3,
j - 1 = 0 and P touches D; then (17T) is trivial, since `|abar_{2a,B} - abar_{a,B}| <= 2 < 6/(1 - q)`.) Then
D-shape (d) with (17T) uniform in s <= beta gives (18T), as in `gap-vmf-lip.md` lines 509-516. For
B = (2a)^3, |B| = 8a^3 and 72 x 8 = 576; the rest is the arithmetic of `gap-vmf-lip.md` lines 522-582
(checked in row 790, Section 6), which uses only `S(a;(2a)^3) < 1/1650`. QED

The interior of the temporal gauge is a 4D system of space links with 12 partners in their slice and
1 in each neighbouring slice. The time slabs are gone except at the cut. Lemma SC is not used: the one
remaining slab is inside D.

### 5.2 Lemma LF: a 4D field of lines with one fixed link per plaquette

For x in Z^4 let `p = x mod 2 = (p0, p1, p2, p3)`. Define d(x) in {0,1,2,3} by

    d = 0 iff p1 = p2 = p3;   d = 1 iff p0 = p2 != p3;   d = 2 iff p0 = p3 != p1;   d = 3 iff p0 = p1 != p2.

Let `L = {(x, x + e_{d(x)}) : x in Z^4}`.

**Lemma LF (PROVED).** (a) d is well defined: the four conditions partition {0,1}^4. (b)
`d(x + e_{d(x)}) = d(x)`, so L is a disjoint union of straight lines, one through each site.
(c) Every plaquette of Z^4 contains exactly one link of L.

Proof. (a) Each condition holds on 4 parity classes (16 in all), and no two hold at once: d = 0 and
d = 1 would need p2 = p3 and p2 != p3; (0,2): p1 = p3 and p3 != p1; (0,3): p1 = p2 and p1 != p2;
(1,2): p0 = p2, p0 = p3, p2 != p3; (1,3): p0 = p2, p0 = p1, p1 != p2; (2,3): p0 = p3 != p1 and p0 = p1.
(b) The condition for d = mu does not involve p_mu. Each site is the lower end of exactly one L-link and
the upper end of exactly one (x - e_{d(x)} has the same d). (c) Let the plaquette lie in the plane
(mu, nu) at x, and let {rho, sigma} be the other two directions. Its links are (x, x+e_mu),
(x+e_nu, x+e_nu+e_mu), (x, x+e_nu), (x+e_mu, x+e_mu+e_nu); they lie in L iff, respectively, d(x) = mu,
d(x + e_nu) = mu, d(x) = nu, d(x + e_mu) = nu. The set S_mu of allowed values of the three parities
other than p_mu is an antipodal pair in {0,1}^3 (S_0 = {000, 111} in (p1,p2,p3); S_1 = {001, 110} in
(p0,p2,p3); S_2 = {010, 101} in (p0,p1,p3); S_3 = {001, 110} in (p0,p1,p2)). So the first two indicators
add up to N_mu = 1 if (p_rho, p_sigma) lies in the projection of S_mu to the coordinates (rho, sigma), and
0 otherwise; this projection is one of the two antipodal pairs {00, 11} ("equal") or {01, 10}
("different"). The same holds for the last two indicators with S_nu. So the count is 1 for every x iff
S_mu and S_nu have projections of opposite type on (rho, sigma). Write E_mu(rho, sigma) = 1 if the
elements of S_mu have p_rho = p_sigma. From the definitions: E_0(1,2) = E_0(1,3) = E_0(2,3) = 1;
E_1(0,2) = 1, E_1(0,3) = E_1(2,3) = 0; E_2(0,3) = 1, E_2(0,1) = E_2(1,3) = 0; E_3(0,1) = 1,
E_3(0,2) = E_3(1,2) = 0. The six required inequalities hold:
(0,1): E_0(2,3) = 1 != 0 = E_1(2,3); (0,2): E_0(1,3) = 1 != 0 = E_2(1,3); (0,3): E_0(1,2) = 1 != 0 =
E_3(1,2); (1,2): E_1(0,3) = 0 != 1 = E_2(0,3); (1,3): E_1(0,2) = 1 != 0 = E_3(0,2); (2,3): E_2(0,1) =
0 != 1 = E_3(0,1). QED

GUIDE: the field was found by a backtracking search over period-2 parent functions
(`scratchpad/lane835/guide/forest_search.py`, first solution printed); the proof above does not use it.

### 5.3 Theorem F: the seed and the gap for 0 < beta < 1/3

**Construction on the torus.** Let all sides of n = (a,B) be even, a >= 4, b_i >= max(4, a). L is
well defined on the torus (it depends on parities). Each line is a cycle there: a time line has length
a, a line of direction i has length b_i. Let K_time = the L-links from time a-1 to time 0, K_i = the
L-links of direction i from x_i = b_i - 1 to x_i = 0 (the seam of direction i), and
`F = L \ (K_time u K_1 u K_2 u K_3)`. Each cycle loses exactly one link, so F is a disjoint union of
paths: a forest. Let D = D_cut u {all links of plaquettes that contain a link of K_1 u K_2 u K_3}.
On n' = (2a,B) define F' the same way with K'_time = the L-links from time 2a-1 to 0 and the same seams.

**Theorem F (PROVED, given Corollary V1, Lemma M, D-shape (a), (d) and Theorem SH, all READ and checked;
and Lemmas G, DC', MG, LF above).** Let 0 < beta < 1/3, q = 3 beta, a >= 4 even, j = a/2, and B with
all sides even and at least max(4, a). For 0 <= s <= beta:

    |abar_{2a,B}(s) - abar_{a,B}(s)| <= 6 q^{j-1}/(1 - q),                                   (17F)
    0 <= Phi_B(a;beta) <= 72 a|B| beta q^{j-1}/(1 - q).                                      (18F)

If
    576 a^4 beta q^{a/2 - 1}/(1 - q) <= 3/5000,                                              (19F)
then `S(a;(2a)^3;beta) < 1/1650`; with Identity FL both halves obey `S_0 < 1/1650` and
`U < 1/1651`; and `m(L^3;beta) >= 3/(50a)` for every integer L >= 64a, on the whole transfer-matrix
space, all electric-flux sectors included. Every cube with side at least 3 has a positive gap by (TM).
For every 0 < beta < 1/3 such an even a exists.

Proof. (C1): inside Lambda_0, F' and F (reduced mod a; the pattern has period 2 and a is even) differ
only on K_time, the time links from a-1, which lie in D_cut. Free links off D: a link l not in D lies in
no plaquette containing a seam link (by the definition of D) and in no plaquette of the slab [a-1, a]
(those contain only links of D_cut). So every plaquette through l has exactly the L-links of the
pattern, that is exactly one fixed link (Lemma LF (c)), and l has 2 free partners in each of its six
plaquettes: 12 in all. Lemma MG (b) gives row sums at most `12 s/4 = 3s <= q` off D.

Distance. Give each link the midpoint of its two ends. Two links of one plaquette have midpoints whose
coordinates differ by at most 1 each (circularly). Choose P = one plaquette of each of the six
orientations, with base point x* = (j, b_1/2 - 1, b_2/2 - 1, b_3/2 - 1) for the three space orientations
and (j - 1, b_1/2 - 1, b_2/2 - 1, b_3/2 - 1) for the three time orientations. The links of P have time
midpoints in [j-1, j] and x_i-midpoints in [b_i/2 - 1, b_i/2]. The links of D_cut are exactly the links
with time midpoint in {a-1, a-1/2, 0}; a path cannot cross that band without landing in it, so it needs
at least `min(j - 1, a - 1 - j) = j - 1` steps to reach D_cut. The links of the seam part of D lie in
plaquettes of planes (i, nu) at x_i = b_i - 1, so their x_i-midpoints lie in [b_i - 1, b_i]; reaching
them takes at least `b_i/2 - 1 >= j - 1` steps. So d >= j - 1.

Each plaquette of P has exactly one fixed link, hence 3 free links, Delta(x_p) <= 3, and Lemma DC' gives
`|mu_1(x_p) - mu_2(x_p)| <= 6 q^{j-1}/(1 - q)`. By translation invariance of the ungauged torus measures,
`abar_{t,B}(s) = (1/6) sum_{p in P} mu_{t,B}(1 - x_p)`; with Lemma MG (c) this gives (17F). (18F) and the
seed and gap statements follow exactly as in Theorem T (here |B| = 8a^3, 72 x 8 = 576, and
3/4997 < 1/1650). Identity FL gives `S_0 <= S` and `U <= S/(1 + S)`. Existence: a^4 q^{a/2} tends to 0
along even a. QED

**Example (PROVED by hand).** beta = 1/4, a = 282 (even), B = (564)^3. Then q = 3/4, a/2 - 1 = 140,
and `(3/4)^5 = 243/1024 < 1/4`, so `(3/4)^140 < 2^{-56}`. The left side of (19F) is
`576 x 282^4 x (3/4)^140 < 576 x 288^4 x 2^{-56} = 2^6 3^2 x 2^20 3^8 x 2^{-56} = 3^10/2^30`, and
`3^10 x 5000 = 295 245 000 < 3 x 2^30 = 3 221 225 472`. So the seed holds at beta = 1/4 and
`m(L^3; 1/4) >= 3/(50 x 282) = 1/4700` for every L >= 18048. (beta = 1/4 is above 2/9; it is below
2/7, so Theorem T also covers it, with a larger a.)

**Corollary F2 (the vacuum-energy defect; PROVED).** For 0 < beta < 1/3, a >= 4 even and even c, d >= a:
`0 <= Delta(c,d) = a (2 e(a,c,d) - e(2a,c,d)) <= 72 a^2 c d beta q^{a/2 - 1}/(1 - q)`. Hence
`delta = 4 Delta(a,a) + 2 Delta(2a,a) + Delta(2a,2a) <= 864 a^4 beta q^{a/2-1}/(1 - q)`.
Proof. Z is symmetric in its four sides (READ `gap-crux-fp.md` line 38), so
`F(t,a,c,d) = F(a,(t,c,d))`, the torus of time a over the box (t,c,d). With Lemma K (a),
`2e(a,c,d) - e(2a,c,d) = lim_t Phi_{(t,c,d)}(a)/t` along even t >= a. (18F) with B = (t,c,d) bounds
`Phi_{(t,c,d)}(a)/t` by `72 a c d beta q^{a/2-1}/(1 - q)` for every such t. Delta >= 0 is Lemma K (b)
(READ `gap-crux-restate.md` line 178). The sum: 4a^2 + 2(2a)(a) + (2a)^2 = 12 a^2. QED
The same holds for beta < 2/7 by Theorem T, with q = 7beta/2 and floor(a/2) - 1, for all c, d >= 3.

**GUIDE check of the construction.** `scratchpad/lane835/guide/forest_check.py` builds F and D on the
tori (4,8,8,8), (6,6,6,6), (8,8,8,8): F has no cycle; no plaquette without a seam or cut link is
imperfect; every free link off D has exactly 12 free partners (2034, 1320, 5670 links); the breadth-first
distance from P to D is 1, 2, 3 = j - 1. It decides nothing; the proofs above are by hand.

## 6. Where the method stops

### 6.1 Lemma AVG: 1/3 is the ceiling of single-link chord Dobrushin in every tree gauge (PROVED)

Let F be a forest on a 4-torus with N sites and sides at least 3. For a free link l let deg(l) be the
number of free links sharing a plaquette with l. Then the mean of deg over free links exceeds 12.

Proof. With n_p free links in plaquette p and f_p = 4 - n_p fixed ones,
`sum_l deg(l) = sum_p n_p (n_p - 1) = sum_p (4 - f_p)(3 - f_p) >= sum_p (12 - 6 f_p)`
(the values 12, 6, 2, 0, 0 at f = 0..4 lie on or above the line 12 - 6f). There are 6N plaquettes and
each link lies in 6, so `sum_p f_p = 6|F|`; hence `sum_l deg(l) >= 72N - 36|F|`. There are 4N - |F| free
links, and |F| <= N - 1. The ratio `36 (2N - |F|)/(4N - |F|)` decreases in |F|, so the mean is at least
`36 (N + 1)/(3N + 1) > 12`. QED

Consequence (PROVED). Let A be the symmetric free-partner matrix and D any set of links. The Rayleigh
quotient with the indicator of the free links off D gives
`rho(A restricted off D) >= 12 (1 - |D|/N)` (remove at most 18 partners per link of D, twice, and use
4N - |F| >= 3N). By Proposition NG's last step, no weighted row-sum condition with the uniform constant
s/4 per partner holds off D once `3s (1 - |D|/N) >= 1`. In the seed geometry |D|/N is of order 1/a. So
in the limit of large seeds no argument of this family (any tree gauge, any D, any slab blocking with
Neumann bounds) passes beta = 1/3. Theorem F reaches this ceiling: off D every free link has exactly 12
partners. This agrees with the Hexagon claim "no single-link Kantorovich argument in a forest gauge
reaches 1/3" (READ `gap-novelty-opus.md` line 355; their proof not read).

### 6.2 Proposition NP: no forest is perfect across two slices of a torus (PROVED)

Let F be a forest on a 4-torus with sides at least 3, and t a time. Then some plaquette of slice t, of
slice t + 1, or of the slab between them does not contain exactly one link of F. (By symmetry the same
holds for every direction.)

Proof. Suppose all of them contain exactly one. Let E_t = F-links in slice t, and tau = the sites x with
the time link (x, t -> t+1) in F. (i) Each space link lies in 4 space plaquettes of its slice, and the
slice has 3|B| of them: |E_t| = |E_{t+1}| = 3|B|/4. (ii) The time plaquettes of the slab are indexed by
the 3|B| space bonds; a time link from t lies in 6 of them, a space link of slice t or t+1 in one:
`6|tau| + |E_t| + |E_{t+1}| = 3|B|`, so |tau| = |B|/4. (iii) If x is in tau, each of the six time
plaquettes at x already contains the time link at x, so no space link at x in slice t is in F: x is an
isolated vertex of the forest E_t. (iv) E_t is a forest on |B| vertices with 3|B|/4 edges, so it has
exactly |B|/4 components. By (iii) the |B|/4 vertices of tau are |B|/4 of them, so every component is a
single vertex of tau, and E_t is empty. This contradicts |E_t| = 3|B|/4. QED

So the line field of Lemma LF cannot be cut into a forest without defects in every slab of thickness two.
Theorem F places all the defects in D: the cut slab and the three seams.

### 6.3 The flux half up to 2/3 (PROVED from READ statements)

On every torus (t, (2a)^3) with t >= 3 and 0 < beta < 2/3, q' = 3beta/2:
`U <= 24 a^2 beta q'^{a-1}/(1 - q')`.
Proof. Identity L gives `Z[k]/Z = E[I(u, c^k v)/I(u, v)]` (READ `gap-crux-fp.md` line 379), so
`0 <= 1 - Z[k]/Z <= sup |log(I(u, c^k v)/I(u, v))|`. A k with r flips is a product of r one-flip ratios
in other backgrounds (Proposition TW, Step 6, READ line 400); (14) of `gap-vmf-lip.md` (line 359,
uniform in the background) bounds each by `(4 beta/(1 - q')) 4a^2 q'^{a-1}`. The seven k carry 12 flips:
`U <= (12/8) 16 a^2 beta q'^{a-1}/(1 - q')`. QED

### 6.4 What is open for 1/3 <= beta < 2/3

- The glue half S_0, hence the seed (Identity FL: `S <= (S_0 + U)/(1 - U)`), is **OPEN** there. Given
  6.3, a bound `S_0 < 1/1650 - O(U)` would suffice; no such bound is proved.
- By Lemma HR, what is needed is a comparison of the spatial-link marginals of the tori (a,B) and (2a,B)
  across a/2 slices, that is (17) itself. By Proposition NG and Lemma AVG it cannot come from slab
  blocks, nor from any tree gauge with the uniform single-link constant 1/4. It needs either a
  per-partner constant below 1/4 on average (the field-dependent a(|F|) of Theorem V is 1/4 at F = 0,
  and F = 0 is reachable, so a uniform gain needs more than the sup), or a multi-link block estimate
  (the Hexagon plaquette blocks claim 0.345 to 0.348, READ `gap-novelty-opus.md` lines 356-358;
  unrefereed, not checked), or a non-Dobrushin input.
- A uniform slab hypothesis cannot pass the ordering point of the flat 3D O(4) layer model (GUIDE, about
  0.94; READ `gap-arealaw-opus.md` lines 485-489 with the check's correction, `gap-arealaw-check-astra.md`
  lines 376-386). So 2/3 is not a natural ceiling of the slab picture, but nothing here reaches it.

## 7. Scope, verification boundary, comparison, marks

**Scope.** Fixed lattice coupling, strong coupling only: 0 < beta_W < 1/3 for the seed and the gap.
Lane coupling = physics Wilson coupling beta_W = 4/g^2 (READ `gap-arealaw-opus.md` lines 59-61). The
gap is on periodic cubes, on the whole transfer-matrix space (all electric-flux sectors), with
m(L^3) >= 3/(50a) for L >= 64a and m > 0 for every cube with side >= 3. Seed boxes have a even, as the
line field has period 2; Theorem T has no parity condition but stops at 2/7. Gauge fixing is used only
to compute plaquette expectations; Z, (TM), Identity FL and Theorem SH concern the ungauged measure and
are used unchanged. Nothing here touches the middle range, the continuum, (PHYS-SEED) or SU(N), N >= 3
(Theorem V is a statement on S^3). The rate is poor: at beta = 1/4 the bound is 1/4700.

**Verification boundary.** Lemmas HR, NG, G, DC', MG, LF, AVG, Proposition NP, Theorems T and F,
Corollary F2, the 6.3 bound and the example are my author proofs; nothing in this note has had an
independent reading. The steps that most need one: Lemma DC' (the condition only off D, and the bound
on delta_j(h) for j in D); condition (C1) and Lemma MG (a) for the pair F, F' (which links are fixed in
one torus and free in the other); the distance count in Theorem F (midpoints, the cut band, the seams);
the six inequalities in Lemma LF (c); Proposition NP step (iv). The inputs Corollary V1, Lemma DC,
Lemma INF, Lemma M, D-shape, Identity FL, Identity L, (14), Theorem SH are READ and were checked in
rows 707, 709 and 790. Two GUIDE runs (Sections 5.2, 5.3) found and spot-checked the construction; they
are not part of any proof. Scripts: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/lane835/guide/`
(`forest_search.py`, `forest_check.py`; a third search, `forest_descend.py`, was stopped unfinished
and is superseded by Proposition NP).

**Comparison (bounded to the sources read by rows 819 and 825; no new literature search).**
- In the lane: Theorem DOB in chord form proved the seed for beta < 2/9 (`gap-vmf-lip.md` line 438).
  Theorem F moves it to 1/3, and the vacuum-energy defect with it.
- Bhattacharjee, Bhattacharya et al. (Hexagon v4/v7, unrefereed) claim a forest gauge with one fixed link
  per plaquette, twelve partners, beta_W < 1/3, for free-boundary limits and an infinite-volume transfer
  matrix with m >= -log(3 beta_W) (READ `gap-novelty-opus.md` lines 351-355). The range is **EQUAL**.
  The object differs: Theorem F is the finite periodic seed, all flux sectors, from checked lane inputs,
  with the defects of the periodic torus (forced by Proposition NP) placed in D. Its rate is much weaker.
  The idea of a forest gauge with twelve partners is theirs; I did not read their construction.
- Their plaquette-block claim reaches 0.345 to 0.348 (READ lines 356-358): Theorem F is **WEAKER**.
- Refereed sources named in rows 819 and 825 (SZZ 1/12; CNS 1/6, area law only): no gap claim at 1/3
  was found there; this is not an absence theorem.

**Marks.**

| Statement | Mark | Where |
|---|---|---|
| Definitions of S, S_0, U, Identity FL, D-shape, Theorem SH arithmetic, Lemma M, V1, DC, INF, S, SC | READ (paths, lines in Section 2) | 2 |
| Lemma HR: (17) is a comparison of the spatial-link marginals | PROVED | 3 |
| Proposition NG: slab blocks with Neumann bounds never beat rho of the single-link matrix | PROVED | 3 |
| Ungauged slab scheme closes iff s < 2/9 (TV form: 1/18) | PROVED | 3 |
| Literal slab-wise route to (17) or to Delta beyond 2/9 | FAILS (by NG and HR) | 3 |
| Lemma G (tree gauge) | PROVED | 4 |
| Lemma DC' (Dobrushin condition only off D) | PROVED | 4 |
| Lemma MG (the cut in a gauge) | PROVED | 4 |
| Theorem T: (17T), (18T), seed and gap for beta < 2/7 (temporal gauge) | PROVED given READ inputs | 5.1 |
| Lemma LF: period-2 line field, exactly one link per plaquette | PROVED (hand check); found by GUIDE | 5.2 |
| Theorem F: (17F), (18F), (19F), seed (both halves), gap on periodic cubes, beta < 1/3 | PROVED given READ inputs | 5.3 |
| Example beta = 1/4, a = 282, m >= 1/4700 for L >= 18048 | PROVED (hand arithmetic) | 5.3 |
| Corollary F2: vacuum-energy defect Delta(c,d) <= 72 a^2 cd beta q^{a/2-1}/(1-q) | PROVED | 5.3 |
| Construction checks on three small tori | GUIDE | 5.3 |
| Lemma AVG: mean free degree > 12 in every tree gauge; ceiling 1/3 of the method | PROVED | 6.1 |
| Proposition NP: no forest is perfect across two slices | PROVED | 6.2 |
| Flux half U <= 24 a^2 beta q'^{a-1}/(1-q'), beta < 2/3 | PROVED from READ (Identity L, (14)) | 6.3 |
| Glue half S_0 and the seed for 1/3 <= beta < 2/3 | OPEN | 6.4 |
| Uniform slab ceiling near 0.94 | GUIDE (READ as recalled numerics) | 6.4 |
| Independent reading of this note | OPEN (not done) | 7 |

RESULT: The literal slab-wise route fails (Lemma HR: (17) is a comparison of the spatial-link marginals; Proposition NG: slab blocks with Lemma SC's Neumann bounds never beat the single-link Perron root, so 2/9 ungauged), but slab independence with time transverse, used through gauge invariance, does move the seed: in the temporal gauge all time slabs but the cut slab are the identity and Dobrushin's comparison is needed only off the cut (Lemma DC'), giving (17) with q = 7beta/2 and the seed for beta < 2/7 (Theorem T); a period-2 line field with exactly one fixed link per plaquette (Lemma LF), cut at the time cut and at three seams that are put into D, gives |abar_{2a,B} - abar_{a,B}| <= 6(3beta)^{a/2-1}/(1-3beta), Phi_B(a) <= 72a|B|beta(3beta)^{a/2-1}/(1-3beta), hence S(a;(2a)^3) < 1/1650 (both halves, S_0 and U) whenever 576a^4 beta(3beta)^{a/2-1}/(1-3beta) <= 3/5000 (a even), and a volume-uniform gap m(L^3) >= 3/(50a) for L >= 64a on periodic cubes in all flux sectors for every 0 < beta_W < 1/3 (Theorem F; e.g. beta = 1/4, a = 282, m >= 1/4700), with the same bound for the vacuum-energy defect; PROVED by the author given the row-707/709/790-checked inputs, not independently read; 1/3 is the ceiling of every single-link uniform-constant tree-gauge argument (Lemma AVG; Proposition NP shows torus defects are unavoidable), the flux half holds to 2/3, and the glue half and the seed for 1/3 <= beta_W < 2/3 stay OPEN (range equal to the unrefereed forest-gauge claim, weaker than its plaquette-block claim 0.348).
