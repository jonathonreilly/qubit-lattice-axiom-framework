# OC gate: line-by-line check of library/oc.md (CA-I 4.13:lem-own-constant)

Checker: Claude (fresh session), 2026-11-05. One honest reading, not a hostile one. Notes appended as the check proceeds.

## Running notes

- Target read: CA-I L45203-45234. Statement: seeds (small pairs, real-background pairs printed in CMP109 SS3-5, CMP116 SS1-2) satisfy (l1) at own alpha_0' with single bound c LM B alpha_0'; "this property is reproduced by one step". Route: "to be derived together with the thin-cube gradient bound of this chapter".
- 4.9:cor-printed-pairs (L36806-36906) states the same seed content, conditional on B_12 >= 2B_3 and the hypotheses of 4.9:prop-real-backgrounds (a) (two ceilings on eps_0, floors S,M >= 4R_1M_1, torus side >= 3S). Its "reproduction" is the seed statement re-read at level k+1.
- 4.9:prop-real-backgrounds (a) proof (L36640-36699) uses only: CMP98 Prop 2 (averaging), Balaban CMP102b Thm 1 (9) (4.9:thm-minimal-orbit, L35144-35199), 4.9:lem-restriction-monotone, 4.9:lem-level-change. No use of 4.13:lem-own-constant there.
- Lattice convention (L35049-35117): one fine lattice, pp = translation by one fine step; so A_j = mu A_k on the same bonds. lem-level-change (L35500-35539) gives |A| scale mu, difference scale mu^2. OC (15) matches.
- Thm minimal-orbit needs M' <= M(eps_1) (non-strict); OC asks m_* < M(eps_1), stronger, harmless.
- Thin-cube lemma (L37902-38107): clause (ii) = prop-real-backgrounds + cor-printed-pairs; B_12 := max{4C_gl B, 2B_3, 14dL^2B_1, B_12^Sigma1}, chosen before M (L37914-37919). Its proof does not cite 4.13:lem-own-constant. Literal label occurs only at its declaration (grep over CA-I/II/III).
- Consumers read: prop-small-pairs (L34058-34100, L34194-34208) needs (l1) at alpha_0' for U_j at its own level with "eps_0 sufficiently small" and 2B_3 alpha_0' <= alpha_0; tower-clause-b (L33095-33110) is the (l1) reading, and B^109 "may be enlarged as needed". prop-class-reproduction (e) (L34241-34304). prop-clause-zero (a') (L56419-56437) is broader (widened form for all pairs plus reproduction).
- CMP109 OCR p.262 (1.12): |A|, |grad^xi A| < O(1) LM B alpha_0 on cubes of size O(1)LM, B "sufficiently large". Matches (2) of OC.
- SHA-256 of ca_I.tex and ca_III.tex match OC's table.

## Line-by-line findings

First failing step: none.

1. Statement (check 1). OC's Result is the lemma's two parts: seeds at their own alpha_0' with bound c LM B alpha_0' on every closed cube in the domain of side <= cLM; and reproduction by one step with one B = B_12 fixed before M. The standing conditions (3)-(7) are made explicit. They are the hypotheses of cor-printed-pairs / thin-cube lemma ((C-1), floors, (T_low)^S), all early floors, ceilings after M, or a volume floor. The consumer prop-small-pairs itself says "eps_0 sufficiently small". So the scope matches the statement as the account uses it.
2. Scope note, not a failure. The lower-level radius alpha_0' = mu eps_0 (16) is the account's one-power assignment (cor-printed-pairs L36824-36826). The curvature of U_k read at level j is mu^2 eps_0; at that constant the |A| member would generally fail, since |A| scales by one power of mu. "Printed membership" must be read as the account reads it. The direct consumer prop-small-pairs uses U_j at its own level, alpha_0' = eps_0, so nothing breaks.
3. Enclosing cube (10)-(12). m_* = r ceil((s+2M_1)/(2r)) < s/2 + M_1 + r <= s/2 + 2r (M_1 <= r) <= S (S >= 4r) <= r a_1/(2 eps_0) = M(eps_1) by (6). Grid extension is valid: 2m_* >= s + 2M_1 and 2m_* is a multiple of M_1. Enlargement side 2m_* + 4r < s + 4r + 4r <= 3S, strictly below the torus side, so it embeds. Trivial nest: B^k(Lambda_k) = T and the next layer is empty, so both layer conditions hold. Correct. OC asks m_* < M(eps_1); the theorem (L35190) needs only M' <= M(eps_1). Stronger, harmless.
4. Strict gauge bound (13). < B_3 m_* eps_1 = 2B_3 m_* eps_0 < 2B_3(s/2+2r) eps_0 <= 2B_3 S eps_0 <= S B eps_0 by (4). The chain is strict at the first step. Restriction to Q keeps bd Q and pp Q inside bd Q^a and pp Q^a. Correct; identical to CA-I L36651-36699.
5. Two powers (15). One fine lattice; pp means a one-step translate (L35049-35117). xi_k = mu xi_j, A_j = mu A_k; xi_j^{-1}|Delta A_j| = mu xi_k^{-1} * mu |Delta A_k|, so mu^2 <= mu. Correct; it is lem-level-change (L35500-35539).
6. Factor order. (9): U'_W U_W e^{iZ} = U'_W (U_W e^{iZ} U_W^{-1}) U_W = (U'_W e^{i Ad Z}) U_W, bondwise. Correct; it matches <5b>(b). The real gauge change (U^v)^{u v^{-1}} = U^{(u v^{-1}) v} = U^u holds under the left action (U^a)^c = U^{ca}. Far product e^{iA}U'U = e^{iA''}U matches CA-I L33871-33874.
7. Identity (17). cL(M/L)(LB) mu a = cLMB mu a = S B mu a. Exact; matches L34119-34138 and L36142-36152.
8. One B before M. (4) B = B_12 >= 2B_3 is an entry of the max at L37914-37919, chosen before M. The same B is used for the seeds at k and k+1 and in transport. Correct.
9. Volume (7). T_m has side 2L^m and spacing L^{-K} (H1), so side_j = 2L^{m+K-j} >= 2L^m. H5 gives L^m >= L^{11} M R, with R >= 1 by its definition (L667). The floor 2L^{10} >= 3c then gives >= 3S. c is a fixed absolute number (L4426-4432), so this is a legitimate Stage-1 floor. Correct. This also discharges the account's (T_low)^S from H5, which the account only lists as a hypothesis.
10. Running comparison (18). Uses lem-radii-ratio, alpha_{0,i}/alpha_{0,i'} <= (1+beta_0) sqrt(1+n). The hand bound sqrt(1+n) <= sqrt2 L^{n-1} is right. The constant is beta, as at locus <7> (L35987-35992), not beta_s; <7> is the locus the table row cites. The far-source running form <3> (beta_s) is not in OC's table. It is a CMP119-radius standing condition outside the seed content, so this is not a gap in the lemma.
11. Amplitude bound. g(log g^{-2})^q = t^q e^{-t/2} <= (2q)! 2^{2q} t^{-q}, from e^{t/2} >= (t/2)^{2q}/(2q)!. The right side decreases in t, so the bound is uniform for g_i <= gamma. Correct.
12. Use of mu (check 4). The near-product representative (Landau copy over U = 1, mu (3.1)) is used within mu's Lemma-4-window scope. So are the amplitude order alpha_1, alpha_0, alpha_3, alpha_2 (mu section 8, step 3) and the left action (mu section 2 item 4 / section 6). One wording overreach, not load-bearing: section 4.2 says "The actual minimizer is that orbit, with the representative convention fixed by mu where needed". The global U_k(V) on the torus is identified with Balaban's minimal orbit by CMP109's notation (CA-I L36687-36688), not by mu, whose result concerns CMP109 Lemma 4 windows. The clause is invariant under real gauge changes, so no representative is needed. Suggested rewording: "U_k(V) is, by CMP109's notation, a configuration in the minimal orbit; no representative choice is needed."
13. Minor. (6) adds eps_0 < c_98 for CMP98 Prop 2. The account's proof uses that proposition without naming the ceiling. It is an extra ceiling in the allowed direction.

## Question 2: is the label stale, and is there circularity?

Section 4.9 contains the mechanism. cor-printed-pairs (L36806-36906) states the lemma's seed content verbatim (same bound, same alpha_0' list, reproduction at k+1). It is conditional on B_12 >= 2B_3 and the hypotheses of prop-real-backgrounds (a). thin-cube lemma clauses (ii)-(iii) (L38040-38070) fix those hypotheses in a valid order of choice. The seed chain rests on CMP102b Thm 1 (9), CMP98 Prop 2, and the elementary 4.9 lemmas (restriction, level change, gauge invariance, identity field). None of these uses 4.13:lem-own-constant, membership in U^Sigma1, or the inductive hypothesis. The one inductive coupling is lem-radii-ratio, which needs the slope bound of clause (0) at (j, k+1). It enters only at the transport loci <7> and <8>, never the seeds. It is the ordinary joint induction: the slope bound is available once g_{k+1} is defined, before step k+1. It is not a cycle within a step. So the "Proof outstanding" label (L45204, L166622-166623; CA-III L111213-111214) is stale in substance: the earlier proof exists, and OC discharges its conditional hypotheses by (3)-(7).

## Verdict

Proved as stated and used, in the account's setting and order of constants, with the standing smallness and volume conditions (3)-(7) made explicit. Scope notes: alpha_0' at lower levels is the account's one-power radius mu eps_0. Transport loci of the CMP119/122 branches (<3> running, <8>, <9>, <13>) are not covered and are not needed for the lemma. One wording fix is suggested in finding 12.

Checked line by line by Claude (fresh session).
