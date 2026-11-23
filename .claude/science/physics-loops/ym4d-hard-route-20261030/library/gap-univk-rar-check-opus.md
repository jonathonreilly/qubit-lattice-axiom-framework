lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-23T16:03Z

# Check 1419: cross-provider check of row 1413 (`library/gap-univk-rar-astra62.md`)

Checker: Claude Opus 5.5 (high), Mac mini worker 1, branch `claude/ym4d-hard-route` at 9628cb76f. Started 2026-11-23T04:03Z (date -u).
Object: row 1413 (gpt-6.2-astra max), file `library/gap-univk-rar-astra62.md` (151 lines).
Sources: Sussman-Alpoge account (authors Ethan Sussman and Levent Alpoge, text with Claude and Codex), part III at
`~/ym4d-papers/sa-ca`, `YM4_1400.tex` at `~/ym4d-papers/sa1400`; lane files cited by row 1413.

## 0. Plan and status log

Plan: (A) read row 1413 in full; (B) the disjoint split old / young-common-unaligned; (C) native age estimate (1):
H_c(a), CA-III 34470-34528 marked polynomial and Schwarz bound, labelwise check, outstanding hypotheses (III 34033-34040);
(D) relative estimate (2), range (3), simpler sufficient range, log-series step; (E) tile model (4)-(7): partition,
mixed chessboard inequality, masses (5), root (6), lower bound (7), "every printed hypothesis holds"; (F) consequence for
the per-edge bound of check 1405; (G) verdict table, at most ten defects, RESULT.

- 2026-11-23T04:03Z: file created; reading row 1413.
- (clock not read; between 04:03Z and 2026-11-23T04:10Z): read row 1413 in full (151 lines) and CA-III 34425-34538 (Corollary 9.2:cor-old-age-smallness and proof).

## 1. Sources re-read (anchors by `grep -n` / `sed -n` on the local files)

- CA-III 11928-11955: labels H^c, first index, "common" = first index >= 1, "aligned" = first index > n_c and
  varpi(h) <= varpi_0 = 1/80, (9.1:eq-centre-normalisation-b) H_al and a(X) = k - j(X). L11949-11955: "a label of first
  index at most n_c **that is alive at the stop** has a live component of age at least k - n_c"; labels of B not of A have
  first index 0 (the proof at 17836-17838 says B's private finest level is -1, age k+1; a native wording mismatch, harmless
  for the age bound since both are >= k - n_c).
- CA-III 17800-17856: Lemma (unpaired labels), (9.1:eq-unpaired-labels-1/2): the low-first-index labels of both runs
  cost 4 q_a^(k-n_c) A <= C_nc rho^(n-w); proof uses m_a(h) >= 1 for j(h) <= n_c at a = k - n_c.
- CA-III 34429-34538: Corollary 9.2:cor-old-age-smallness, antecedents (A) (history-wise majorant, Proposition
  9.2:prop-modulus-majorant marked outstanding), (B) (|Z~| <= e^(E_+ N^4) on the dial domain with the per-history
  quantity e e^(-2(1+beta_0)^(-1) p_0(g_K')) times comparison factors), (C) disc lemma; conclusion
  |Z~_(>=a)| <= 2 q^a e^(E_+ N^4); proof: dial mu on T_(K',>=a)(X) at every live component, |mu| < q^(-a), polynomial,
  per-history slack q^(a'-a+1) <= q, Schwarz at 1.
- CA-III 32062-32103: Definition 9.2:def-histories-ages: lineage Z_n nonempty exactly for j <= n <= k (eq-histories-ages-a),
  j(h) = min{n >= 1 : Z_n nonempty}, a(h) = k - j(h), anc(h) = {(n, Z): j(h) <= n <= k, Z in comp(Z_n)}.
- CA-III 34033-34070 Theorem 9.2:thm-geometric-forgetting (hypothesis (A) = Proposition 9.2:prop-modulus-majorant, "proof
  outstanding"; index at L75849 and L111261 also lists the theorem itself as "proof outstanding"); proof Steps 2-4
  L34140-34183: E^[C_0](h) = E^[C](h) exp(-c_a sum_anc sqrt(d) M^d R_n^(d+1) |Z|) (eq-geometric-forgetting-3, C = C_0 + c_a),
  x_h = D I E^[C] <= exp(-2 p_0(g_(k-a))) (eq-..-4), and only then the coarse floor y_h <= q^(a+1) (eq-..-5, from
  #anc >= a+1 and each term >= 1, Lemma 9.2:lem-live-levels (b), (c)).
- (clock not read; between 04:03Z and 2026-11-23T04:10Z): sources for (1) read.

## 2. The disjoint split (row 1413 L41)

Claim: for 1 <= a <= k - n_c the complement of G (aligned labels with no live component of age >= a) is the disjoint
union O_a ⊔ U_y, O_a = labels with a live component of age >= a, U_y = common unaligned labels of first index > n_c
outside O_a.

Check. Complement of G = (unaligned) ∪ (aligned with an old component). Unaligned = (first index <= n_c) ∪ (first
index > n_c and varpi > 1/80). Labels of first index <= n_c have a live component of age >= k - n_c >= a (III 11951-11955,
17827-17838; B's private labels have first index 0 or -1, age >= k), so they lie in O_a; aligned labels with an old
component lie in O_a by definition; the rest of the unaligned labels have first index > n_c >= k_* >= 1, are therefore
common, and lie in U_y. Disjointness is by the clause "outside O_a". **HOLDS.**

Remark (wording, not a defect). The native sentence carries "that is alive at the stop". A label of first index <= n_c
none of whose regions survives would fall in neither class. The account's removal clause (III 13832, 14137: "healed
components ... leave the label") means the first index is read on the surviving regions, so a label with a first index
has a live component; the qualifier is then automatic. Row 1413 inherits the same reading as the native Lemma on
unpaired labels (III 17836-17842), which drops the qualifier in the same way. Also note the native text says B-only labels
have first index 0 (L11953) while the proof says -1 (L17836); either gives age >= k - n_c.

Second point (also holds): the split needs a <= k - n_c, i.e. a_0 <= k - n_c, which check 1397 proved eventually
(`gap-univk-log-check-astra62.md`, the paragraph "Choice of a_0 HOLDS eventually", from III 17883-17909).

## 3. The native age estimate (1) (row 1413 L43-62)

Re-derivation. In d = 4 the native surplus of a history is y_h = q^(sum_anc 2 M^4 R_n^5 |Z|) (III eq-geometric-forgetting-3
with sqrt(d) M^d R_n^(d+1) = 2 M^4 R_n^5). By Lemma 9.2:lem-live-levels (a)-(b) (III 32918-32940) every live level
j(h) <= n <= k carries at least one ancestor cell, and |Z| >= 1 counts cells. So for a history of age a' >= a,
sum_anc 2M^4 R_n^5 |Z| >= 2M^4 sum_(n=k-a')^k R_n^5 >= [H_c(a) + 1] + 2M^4 (a' - a) >= H_c(a) + 1 + (a' - a),
using R_n >= 1 and 2M^4 >= 1. With |mu| < q^(-H_c(a)): |mu| y_h <= q^(a'-a+1) <= q, and x_h <= exp(-2 p_0(g_(k-a')))
<= exp(-2(1+beta_0)^(-1) p_0(g_k)) (eq-..-4 and Step 5). So each dialled history stays inside the quantity
(eq-old-age-smallness-2) that antecedent (B) uses, exactly as in the native proof with q^(-a) replaced by q^(-H_c(a)).
f(mu) = Z~(mu) - Z~(0) is a polynomial (finitely many live components), |f| <= 2 A_c on the disc of radius
rho = q^(-H_c(a)) >= q^(-1) >= 2, f(0) = 0, f(1) = whole old sum; Schwarz gives |f(1)| <= 2 A_c q^(H_c(a)). **(1) HOLDS**
under the corollary's antecedents, with H_c(a) >= 2M^4(a+1) - 1 (R >= 1).

Precision that row 1413 states only in passing (L58 "the exact split ... CA-III 34118-34185"): (1) uses the
**proof-level** history-wise form sup_h [x_h y_h] of the geometric-forgetting theorem, not its statement
(eq-geometric-forgetting-a), which keeps only the floor q^(a+1). A later proof of the outstanding pieces that delivers
only the printed statement would give back the native q^a, not q^(H_c(a)). The antecedent should be written as
"(A_y): the history-wise majorant with the per-history surplus y_h formed inside (B)".

Direct labelwise check (L62). The native moduli form is III (9.1:eq-aligned-terms-3), L17461-17468:
sum_h |mu|^(m_a(h)) ||tau_h|| <= A^sharp for |mu| <= q_a^(-a), a sum of total variations, proved by the same "unused
factor pays |mu|" step (third step, L17501-17509). With the surplus y_h it extends to real r < q_a^(-H_c(a)), and then
sum_(m_a >= 1) ||tau_h|| <= A/r directly; the test r^(1 - m_a(h)) of row 1413 is a harmless detour (the bound is on moduli,
no test is needed). Letting r rise to the radius gives A q_a^(H_c(a)) without the factor 2. **HOLDS.** Note (9.1:eq-aligned
-terms-3) is printed for H_al; the extension to all labels of H^c is the one the native Lemma on unpaired labels already
makes (L17838-17847, "in the form in which (9.1:eq-aligned-terms-a) bounds the total variations of the individual terms").

Outstanding hypotheses under (1), from the account's own lists (III L75846-75849 and L111258-111261, re-printed):
(i) Proposition 9.2:prop-modulus-majorant (history-wise modulus majorant), proof outstanding (named in Theorem (A),
L34036, and in Corollary (A), (B), L34445, L34465); (ii) "the nesting clause of the majorant hypothesis used in the proof
of Theorem 9.2:thm-geometric-forgetting", proof outstanding; and, for the full comparison, (iii) Proposition
9.1:prop-blind-site-expansions for labels with a live second-class strip (III 17945-17947, hypothesis (e)). Row 1413
names (i) and (iii) but not (ii). **Defect D-a (minor, citation):** the nesting clause (ii) is a separate outstanding item
in the account's list and is an input of (1) through the theorem's proof; it should be listed.
- (clock not read; between 04:03Z and 2026-11-23T04:10Z): Section 3 written.

## 4. The relative estimate (2), the range (3), the simpler range and the log-series step (row 1413 L64-82)

Sources re-read: III 17640-17672 (Lemma 9.1:lem-ramp-comparison, H^m_nc = common, not aligned, first index > n_c) and
its proof L17756-17784: moves (m2), (m4) multiply the H^m_nc terms by mu, |mu| <= (4 C_chi^sharp theta_chi^k)^(-1), and
the disc estimate gives sum_(H^m_nc) ||tau_h^m|| <= 4 C_chi^sharp theta_chi^k M^m (the separate estimate; the combined
form (9.1:eq-ramp-comparison-1) carries C_test with 80 C_chi N_w^4); III 21068-21079: A = e^(E_+^sharp N_w^4),
B = e^(C^w_low N_w^4); III 53485-53490 hypothesis (b): P_0, Q_0 >= 1/B at each run's real centre; III 18115-18120:
A^sharp carries e^(E_+^(sharp sharp) N_w^4); III 53901-53904: Pi_n <= C n^(-(kappa_0-4)/2) (log n)^(c_3); III 17941-17942:
index condition theta_chi <= rho.

(2). Z~^c - Z_G^c = sum_(O_a0) tau_h^c(V_w) + sum_(U_y) tau_h^c(V_w) by Section 2. The first sum is bounded by (1);
U_y is a subset of H^c_nc, so the second is at most sum_(H^c_nc) ||tau_h^c|| <= 4 C^sharp theta^k M^c. Divide by
|Z~^c| >= B^(-1). Every constant (2 A_c B, 4 C^sharp M^c B) is e^(O(V)) with g, w, L fixed, so one pair (C_0', Gamma)
serves both runs and both tori. **(2) HOLDS** (no mixed interpolation, no positivity used, as row 1413 says).

(3). If Gamma V <= min{|log q_a| H_c(a_0), k |log theta_chi|} - D with D = (1/2) log(1/eps), each of e^(Gamma V) q_a^(H_c)
and e^(Gamma V) theta^k is at most e^(-D) = sqrt(eps); the right side of (2) is at most 2 C_0' sqrt(eps), below 1/2
eventually; |Log(1 - z)| <= sum |z|^n / n <= |z|/(1 - |z|) <= 2|z| for |z| <= 1/2. So |log(Z_G/Z~)| <= 4 C_0' sqrt(eps).
**HOLDS.** This is stronger than the extensive form C V (q_a^(a_0) + delta) asked by check 1397 (no factor V), on the range.
Positivity: if Z~^c is real (it is >= 1/B > 0 at the real centre) and Z_G^c is real, Z_G/Z~ lies in the real interval
[1/2, 3/2]: **HOLDS.**

Simpler range Gamma V_large <= D. H_c(a_0) >= 2M^4(a_0 + 1) - 1 >= 2 a_0 + 1, so q_a^(H_c(a_0)) <= q_a (q_a^(a_0))^2 <= eps,
i.e. |log q_a| H_c(a_0) >= 2D; theta_chi^k <= rho^k <= eps gives k |log theta_chi| >= 2D. Then each member of the min minus
D is >= D >= Gamma V_large >= Gamma V on both tori. Only R >= 1 is used, so it holds on B's own lengths. **HOLDS.**
Envelope example: at fixed w, rho^k is exponentially small and Pi_n <= C n^(-p) (log n)^(c_3) with p = (kappa_0 - 4)/2,
so D >= (p/2) log n - (c_3/2) log log n - O(1) and V_large <= [p/(2 Gamma) - eta] log n is covered eventually. **HOLDS**
(needs kappa_0 > 4; the later "kappa_0 > 8" of L124 is a different statement, V sqrt(eps) -> 0 at V of order n, and is
consistent with this one).

Young unaligned class alone: e^(Gamma V) theta^k <= rho^(k/2) <= sqrt(eps) when Gamma V <= k log(sqrt(rho)/theta_chi) (> 0
since theta_chi <= rho < 1). **HOLDS.** The after-cut variant assumes an extensive floor e^(-D_o V) on Z_(not O)/Z~; it is
stated as an assumption, not proved. **HOLDS as a conditional.**

Size of the range (a fact the reader should keep): the volume range of (3) is logarithmic in the cutoff index n at
fixed stop depth, V_large = O(log n), while the native tori of the account have V = N_w^4 = (2 L^(m_0 + w))^4, fixed in n
for fixed (m_0, w). So for each fixed geometry the range is met for all large n; it is NOT met by a family with V of
order k, which is exactly the family of the tile model (Section 5). The two halves of row 1413 are consistent.
- (clock not read; between 04:03Z and 2026-11-23T04:10Z): Section 4 written.

## 5. The positive tile model (4)-(7) (row 1413 L84-126)

Sources re-read for the printed bounds the model must meet: III (9.1:eq-aligned-terms-3) L17461-17468 (moduli form,
|mu|^(m_a(h)), |mu| <= q_a^(-a)); III L17756-17774 and Y 130310-130322 (the common unaligned labels born above n_c are
multiplied by ONE mu per label, "The sum for this class is linear in mu", radius (4 C_chi^sharp theta_chi^k)^(-1));
III L17640-17672 (combined C_test form); III L21068-21079 (A, B); the definition of varpi via slot thresholds near
III L17680-17692 (not used by the model, which sets the flag).

Partition and masses (5). Labels = subsets S of the V tiles; w(empty) = 1, w(S) = d_k b^|S|. Sum over nonempty S of
b^|S| = (1+b)^V - 1, so Z~ = 1 + d_k((1+b)^V - 1) = 1 - d_k + d_k(1+b)^V and Z_G = 1. **HOLDS.** Recursion check
U_(v+1) = (1+b) U_v + d_k b, U_0 = 0, gives U_v = d_k((1+b)^v - 1): (1+b) d_k((1+b)^v - 1) + d_k b = d_k((1+b)^(v+1) - 1).
**HOLDS** (an independent derivation of (5)).

Printed bounds, item by item (d_k = d_0 theta^k, 0 < d_0 <= min{1, 4 C^sharp}, log(1+2b) below the upper density):
- upper: Z~ <= (1+b)^V <= e^(E_+ V) since d_k <= 1; lower: Z~ >= Z_G = 1 >= e^(-C_low V). HOLDS.
- unaligned move disc: for |mu| <= (4 C^sharp theta^k)^(-1), |mu| d_k <= d_0/(4C^sharp) <= 1, so
  1 + |mu| d_k((1+b)^V - 1) <= (1+b)^V; the separate estimate d_k((1+b)^V - 1) <= 4 C^sharp theta^k (1+b)^V. HOLDS.
  Combined form: C_test >= 18 e C^sharp theta^(-1) >= 4 C^sharp, so it holds too.
- age forms: every component has age 0, so m_a = 0 for a >= 1 and every old sum is 0; at a = 0 the radius is 1 and the
  moduli sum is Z~. Low-index (unpaired) labels: none. HOLDS. The "doubling" remark (2b per occupied cell) only covers a
  factor 2 per component; HOLDS.
- per-cell large-field suppression: the stop-level coupling is the fixed g, so the native per-cell factor at level k is a
  fixed number; b may be taken below it before k and V are chosen. HOLDS (row 1413's sentence "a fixed extra charge per
  occupied terminal cell can likewise be paid by reducing b").
- both runs equal, both ramps constant, aligned part = empty label only: recent, test and shell costs vanish. HOLDS.
So every printed inequality that row 1413 lists holds in the model. The only freedom used is the one the account leaves:
the unaligned class is priced by one degree-one multiplier per label (III L17762-17774, Y 130315-130318), not per
component or per tile. That is the precise reason the model works.

Mixed chessboard inequality. nu = [(1 - d_k) delta_empty + d_k (1+b)^V Bern(p)^(x V)] / Z~, p = b/(1+b) (check:
d_k(1+b)^V p^|S| (1-p)^(V-|S|) = d_k b^|S|, and at S empty the two parts add to 1). For nonnegative tile functions f_t,
each component i of the mixture is a product law, so nu_i(prod_t f_t) = prod_t a_(i,t) with a_(i,t) = nu_i(f_t) one-site,
and nu_i(prod_s theta_s f_t) = a_(i,t)^V. Hölder with V exponents over the two-point mixing law pi:
sum_i pi_i prod_t a_(i,t) <= prod_t (sum_i pi_i a_(i,t)^V)^(1/V). **HOLDS** (also for indicators and tile-dependent f_t).
PART (Z_G/Z~ = nu(S empty)) and TILE (bad set = union of the reflected occupation events) hold by construction.

Root (6): nu(S = all)^(1/V) = (d_k b^V / Z~)^(1/V) = [b/(1+b)] (1 + (1 - d_k)/(d_k (1+b)^V))^(-1/V). **HOLDS.**
Rate (7): |log(Z_G/Z~)| = log Z~ >= log(d_k (1+b)^V) = V log(1+b) - k|log theta| - |log d_0|. **HOLDS.**
Geometric family: V_small = first (2 L^(m_0+w))^4 >= 2(k|log theta| + |log d_0|)/log(1+b); then V_small and L^4 V_small
are Theta(k), (7) >= (1/2) log(1+b) per site on both, and (6) -> b/(1+b) (since d_k(1+b)^V >= (1+b)^(V/2) -> infinity).
**HOLDS.** With kappa_0 > 8, V sqrt(eps) ~ n^(1 - p/2) (log n)^(c_3/2) -> 0 (p = (kappa_0-4)/2 > 2) and V theta^k -> 0:
**HOLDS**; so a floor stated in eps (V sqrt(eps) <= 1/2) does not restore the inference, while the sum of the disseminated
roots, V b/(1+b), diverges. **HOLDS.**

Marked polynomial 1 + mu U_V with zero -1/U_V -> 0: HOLDS (a zero-free interpolation in mu would need input beyond the
printed disc).

Two precisions (not defects):
(P1) The model's runs are identical, so the quantity the carry needs, log(Z~^B/Z~^A), is exactly 0 while (RAR) fails.
The model refutes the implication "printed bounds => (RAR)", and also shows (RAR) is not necessary for the carry; it
says nothing against the carry itself. Row 1413 says this ("The failed conclusion in (7) is RAR", L126).
(P2) The model depends on the terminal definition of "aligned" (III 11939-11946, with varpi <= 1/80). The account also
glosses "aligned" by first index alone (III 53462-53464; and III 26427 uses j >= k_* for nested sequences). Under the
index-only reading the class U_y is empty, every nonempty S of the model is aligned, and the model is no longer a
model of the printed bounds. The ramp lemma (III 17640-17642, H^m_nc) and Y 130310-130322 charge U_y explicitly, so
the terminal definition is the operative one and row 1413's reading is right; the account is internally inconsistent
on this word, and row 1413 records that (L134).

Verdict on the decisive question: **the tile model does show that the printed bounds are insufficient for uniform (RAR)**
(no r_K = o(1) follows on unrestricted sides). HOLDS.
- 2026-11-23T04:10Z (date -u): Section 5 written.

## 6. "What a chessboard proof would have to count" and the alignment readings (row 1413 L128-134)

Theorem C and PART / TILE / PROD are row 1395's (`gap-univk-log.md` L128-149, checked by 1397 at
`gap-univk-log-check-astra62.md` L34-38).
- Incidence count. If every contributing history of the all-tiles event has m_a0(h) >= N/J, the moduli form at real
  r < q_a^(-H_c(a_0)) gives sum ||tau|| <= A r^(-N/J), so the disseminated probability is <= C e^(Gamma V) q_a^(H_c N/J),
  and with V = vN the N-th root is <= max(1, C) e^(Gamma v) q_a^(H_c/J). **HOLDS.** "J <= 2M^4 suffices for the
  rate q_a^(a_0)": 2M^4(a_0+1) - 1 >= J a_0 when J <= 2M^4. **HOLDS.** Distinct live components at the stop have disjoint
  lineages (regions only grow until healed, III 11951; a component at level n lies in one component at n+1), so the
  per-component factors multiply, as the native corollary already uses; the caution "count each paid cell once" is right.
- Reflecting two-point mixture (mass s = sqrt(eps)/2 on all-occupied, 1 - s on all-empty): -log(1 - s) <= 2s and the
  root is s^(1/N) -> 1; it satisfies (CB) by the Hölder argument of Section 5. **HOLDS**: the root test is strictly
  stronger than (RAR).
- Outline anchors re-read in a scratch copy (`YM4_sketch_500.tex` at 31a47c543775, fetched by raw URL): O 23350-23358 does
  keep the mark c_a-bar = 2 c_a M^4 per live level in the two-term age bound; O 23250-23265 is Theorem 4.13 under D3;
  O 5288-5308 says "Higher mixed bounds require an appropriate majorant for the history event on which all marked uses
  occur; they do not acquire a product of rarity factors from holomorphy alone". **HOLD.** CA-II 106171-106192,
  106818-106846, 127294-127323 and Y 130128-130136, 130251-130270: **not re-read** (not load-bearing for any verdict here).
- Alignment readings III 26424-26438 (nested sequences, j >= k_*), 53460-53467 (index-only gloss), 11939-11949 (terminal,
  with varpi): **HOLD** as quoted; see (P2) of Section 5.

**Defect D-c (credit, minor).** The same outline paragraph (O 23350-23358, cases (1)-(3)) already states the
volume-floor form of the reserve argument: on a torus with ell > ell_V(g) "the torus satisfies the same bound at those
levels at which c_a-bar (K' - k + 1) >= B(x_K') |T^(K')|", i.e. the summed per-level mark pays the e^(B V) volume factor
only on a volume range, and uniformity in the side is left to Lemma 4.15 (tiles, windows, triggers). Row 1413's range (3)
is the two-cutoff, stop-mass analogue of that case (3); the file credits O 23350-23358 for the mark but not for this
structure. The result is still correct; the credit should say "the volume-range form is the outline's case (3)".

## 7. Consequence for the per-edge bound of check 1405 (row 1413 L136-144)

Check 1405 (`gap-univk-pos2-check-astra62.md` L40-44) adds |log(Z~^m / F^m)| <= C V r_K for each run m, with F^m = Z_G^m on
identical good labels. Row 1413's (2)-(3) give |log(Z~^m/Z_G^m)| <= 4 C_0' sqrt(eps) for m = A, B on each torus in the range,
so the term 2 C V r_K may be replaced by 8 C_0' sqrt(eps) (a fortiori O(V sqrt(eps))). **HOLDS** under (3) at both runs and
both tori of each edge used. "On unrestricted volumes the printed estimates allow (7) even when the other three costs
vanish": the tile model has B_rec = d_test = s^m = 0. **HOLDS.** The remark on Theorem T* (floors at each edge, no seed from
a volume window) is a correct reading.

**Defect D-f (summary wording, moderate).** Row 1413's FINISH RESULT says "the alignment condition varpi(h) at most 1/80
on young common labels is the unpriced piece". The old class is equally unpriced on unrestricted sides. Check 1397's
private-label example survives the stronger reserve (1): give run B one private label of age k and mass e^(V b) - 1,
b <= E_+/2 fixed. The moduli form at the improved radius needs 1 + q_a^(-H_c(k)) (e^(V b) - 1) <= e^(E_+ V), which holds
once V >= 2 |log q_a| H_c(k)/E_+ + O(1); then |log(Z_G/Z~)| = V b on that torus, so no r_K = o(1) follows for the old
class either, on volumes of order H_c(k) (of order k when the R_i are bounded). Row 1413's own text lists the old-charge
matching as its second next row (L151), so the file is consistent; only the one-line summary misleads.
- 2026-11-23T04:12Z (date -u): Sections 6-7 written.

## 8. Verdict

**Row 1413: HOLDS AFTER CORRECTION.** No mathematical line fails. Every display (1)-(7), the split, the Schwarz step, the
labelwise check, the log-series step, both ranges, the chessboard check of the mixture, the root (6), the rate (7) on the
geometric family and the consequence for check 1405 were re-derived by hand from the account's lines (Sections 2-7). The
corrections are in the hypotheses named and in the one-line summary.

Decisive outcomes.
1. **The conditional volume-range rate holds**: on each run and each torus with Gamma V <= min{|log q_a| H_c(a_0),
   k |log theta_chi|} - D, in particular Gamma V_large <= D = (1/2) log(1/e_w), |log(Z_G^c/Z~^c)| <= 4 C_0' sqrt(e_w),
   conditional on the antecedents of Corollary 9.2:cor-old-age-smallness **in the proof-level form** (A_y) (see D-b), the
   two outstanding items (i), (ii) of Section 3, hypothesis (e) of III 17945-17947 for second-class strips, the ramp
   lemma's inputs (III 17643-17654) and the endpoint bounds A, B. For fixed (m_0, w) the range holds for all large n; it is
   not uniform in the side.
2. **The tile model shows that the printed bounds are insufficient for uniform (RAR)**: all printed inequalities hold, the
   log cost per site is >= (1/2) log(1+b) on both tori with V of order k, and no r_K = o(1) follows. The mechanism is that
   the unaligned class is priced by one degree-one multiplier per label (III 17762-17774, Y 130315-130318). The model has
   identical runs, so it says nothing against the carry itself (P1); it depends on the terminal definition of "aligned"
   (P2), which is the operative one.

Defects, ranked by what each breaks (at most ten):

| # | Line of row 1413 | Defect | What it breaks |
|---|---|---|---|
| D-b | L43-58, L80 | (1) uses the per-history surplus y_h of the PROOF of Theorem 9.2:thm-geometric-forgetting (III 34140-34183), not its statement (eq-geometric-forgetting-a), which keeps only q^(a+1). Name it as a hypothesis (A_y). | The whole positive result: with the statement alone the old labels cost e^(Gamma V) q_a^(a_0) >= e^(Gamma V) q_a sqrt(eps), and the range (3) shrinks to nothing (row 1413 L80 last sentence concedes this for the coarse multiplier). |
| D-f | FINISH RESULT of row 1413 | "the alignment condition ... is the unpriced piece" omits the old class, which is equally unpriced on unrestricted sides: check 1397's private-label example survives (1) on V >= 2|log q_a| H_c(k)/E_+ (Section 7). | Direction of the next rows if read from the summary; the file's own L150-151 lists both. |
| D-a | L60, L35 | The account's second outstanding item "the nesting clause of the majorant hypothesis used in the proof of Theorem 9.2:thm-geometric-forgetting" (III 75848-75849, 111260-111261) is not listed among the hypotheses of (1). | Completeness of the conditional statement only. |
| D-c | L39 | The volume-floor form of the reserve argument is the outline's own case (3) (O 23350-23358); credited only for the mark. | Credit only. |
| D-e | L62 | The moduli form is bounded by A^sharp (III 17467), not A_c = e^(E_+^sharp V). | Nothing (absorbed in C_0' e^(Gamma V)). |
| D-d | L41 | The native qualifier "alive at the stop" (III 11952, 17829) is dropped; automatic by the removal clause (III 13832, 14137). Inherited from the account's own Lemma on unpaired labels. | Nothing. |

Not re-read (not load-bearing for any verdict): CA-II 106171-106192, 106818-106846, 127294-127323; Y 130128-130136,
130251-130270; III 12081-12097, 31730-31805; the repository-search table at L5-12 of row 1413.
No numeric run was needed (hand checks only); no new statement is claimed here beyond the corrections, and the D-f example
is check 1397's example re-scaled.

Process: checker Claude Opus 5.5 (high), a different provider from the author (gpt-6.2-astra max); the derivations above
are a separate hand derivation from the account's lines, not a re-run of the author's text. Sources: Ethan Sussman and
Levent Alpoge's account (part III local, `YM4_1400.tex` local, outline fetched by raw URL at 31a47c543775 into
/tmp/chk1419_src), with Claude and Codex as authors of their text.
- 2026-11-23T04:12Z (date -u): Section 8 and RESULT written; check finished.

RESULT: Check 1419 of row 1413 — HOLDS AFTER CORRECTION, no line fails. The conditional volume-range rate holds
(|log(Z_G/Z~)| <= 4 C_0' sqrt(e_w) on both runs and tori when Gamma V_large <= (1/2) log(1/e_w)), but only under the
proof-level history-wise surplus of the geometric-forgetting theorem (D-b), plus the account's outstanding modulus
majorant and its nesting clause (D-a). The tile model is right: the printed bounds do not imply uniform (RAR), because the
unaligned class has one degree-one multiplier per label. Correction D-f: the old class is equally unpriced on unrestricted
sides, not only the alignment condition. Open: Wilson (RAR) on all sides, both for old labels and for young common
unaligned labels.
