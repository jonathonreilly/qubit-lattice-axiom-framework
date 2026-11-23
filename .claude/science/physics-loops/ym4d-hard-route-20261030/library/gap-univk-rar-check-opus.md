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
- 2026-11-23T04:10Z: read row 1413 in full (151 lines) and CA-III 34425-34538 (Corollary 9.2:cor-old-age-smallness and proof).

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
- 2026-11-23T04:18Z: sources for (1) read.

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
- 2026-11-23T04:27Z: Section 3 written.
