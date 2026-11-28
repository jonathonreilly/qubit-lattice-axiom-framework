lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-24T09:32Z

# CM-O3 (CM-OLD-TERMS): old-term reads against the random-walk supplier

Queue row 1444, `cm-o3-fable`. Started 2026-11-23T21:32Z (date -u). Pinned at commit b0c2eeda4. Research-stage working state; no status.

Credit: T. Balaban (CMP 122b, the old-term remark at p. 375, and the random-walk expansions); E. Sussman and
L. Alpoge, with Claude and Codex as authors of their text (the complete account CA-II, statement
5.10:rem-old-terms-beside at lines 59542-59551 and supplier 5.2:lem-random-walk-bounds); earlier lane work
`library/cm-claude.md`, `gates/cm-gate.md`, digest `library/prior/cm-o3.md`.

## 0. Plan (written before reading)

1. Read `library/prior/cm-o3.md` in full; then `gates/cm-gate.md` and `library/cm-claude.md` at the cited lines.
2. Read the account at CA-II 59542-59551 and the supplier 5.2:lem-random-walk-bounds, clause (b3).
3. Enumerate the actual old-term reads D_old. For each: admitted Z containing Z_0', membership in the supplier
   domain, assigned companion. Either prove for the full class or exhibit a legal read outside the domain.
4. Mark every step proved, sketched or guessed. End with the next two rows.

## Status log

- 2026-11-23T21:32Z: file created; nothing proved yet.
- 2026-11-23T21:32Z: read prior/cm-o3.md, gates/cm-gate.md (full), cm-claude.md L20-50 and L190-223, CA-II 59536-59622, 2175-2275, 8915-9000, 4150-4182, 4312-4328 (CA-I, CA-II fetched to /tmp/cm-o3-fable-sa at the pinned upstream commit). Next: Balaban CMP 122b (1.51)-(1.65) and p. 375.

## 1. What the old-terms sentence reads (source reading; no proof yet)

Sources read at 2026-11-23T21:33Z: CMP 122b OCR `~/ym4d-papers/cmp122b.txt` L690-1074 (journal pp. 368-375);
CA-II 59539-59618 (remark and proposition), 2181-2271 ((b3)), 8922-9000 (lemma and its explanation), 4168-4177,
4321-4324, 48580-48602; CA-I 32686-32700, 34962-34970.

1.1 **The composed read (Balaban, CMP 122b pp. 373-375).** An old term E(X, U'_k) with X meeting Z is evaluated at the
"extended function" U^0_k. This function is a three-fold composition of local background representations:
- (1.61): on Y_1 (smallest domain of D_k containing X and the components of Z meeting X), determining set
  B'_k(Y_1), gauge factor u_k (explicit formula (106) of CMP 102, analytic in H'_k on one block), response H'_k;
- (1.62): on Y_2 = Y_1 u Y_2', determining set B_1(Y_2) = B(Y_2) u B_1, response H_B, from the expansion (1.57);
- (1.63)-(1.64): on Y_3 = Y_2 u Y_3', determining set B_k(Y_3) = B(Y_3) u B_k, response H_k, from (1.58).
Each response is localised by "the localization expansion ... with the set sigma_0 of cubes disjoint with
Lambda", resummed in the form (6.10) of CMP 109; the final domain is Y_4 = Y_1 u Y_2' u Y_3' u Y_4'.
The variables (U, J) enter H_k "in the usual way". The printed claim (1.65) is: U^0_k is analytic on
U~^c_k(Y_4, a~_0, a~_1) with values in U~''^c_k(Y_1, a~_0, a~_1), the space of CMP 122a (1.64)-(1.69) at n = N.
The old-terms sentence then says this value space lies in the analyticity domain of each old term.

1.2 **What the account adds.** CA-II 59566-59568: "The same step also uses the independence from M of the kernel
constants and of the decay rate of the random walk. This is not a printed sentence; it is Proposition
5.10:prop-m-freeness". CA-I 32697-32700 and 34962-34970 say the sentence "concerns the spaces of CMP 122b, not the
space U^c_j" of CMP 109, and is not a consequence of the account's inclusion corollary 4.8.

1.3 **First observation (to be tested in Section 2).** The operators inside U^0_k are the background responses
H'_k, H_B, H_k with decoupling parameters s(Y). They are built from Green's functions of the type G_k, G''_k
(CMP 99b (3.148)-(3.153), named at CMP 122b p. 370), not from the fluctuation covariance. The supplier (b3) lists
only A, C_{Lambda*}, C_{Lambda*}^{1/2}, C_I. So the question "is D_old in the domain of (b3) and which companion is
assigned" splits in two: (i) does the old-term composition read the root C^{1/2} at all; (ii) which supplier covers
the s-families of H. Status: reading, nothing proved.

1.4 **The fluctuation variable of the step has no root (source reading, 2026-11-23T21:35Z).** CMP 122b (1.1)-(1.2), pp. 356-357
(OCR L60-80): in the operation R the variable in Lambda is V' = exp(i g_k B') with the axial gauge factor
delta_{G_0}(B') and a characteristic function chi({|B'| < ...}); (1.49), p. 369: "chi ... int dB sigma(g_k B)
delta_{T_0}(B) chi' exp[...]". No Gaussian normalisation and no change of variable B = C^{1/2} B'' is made in this
step. So C_{Lambda*}^{1/2} does not occur in (1.50)-(1.65). [reading; the page images were not re-rendered here]

1.5 **The expansions used are those of CMP 116 Section 1.** CMP 122b cites "(6.9) [I]", "(6.10) [I]",
"(6.24)-(6.29) [I]" (pp. 372-374). The printed CMP 109 ends with Section 5 (OCR `cmp109.txt` L2214-2600), and
CMP 119 p. 277 (OCR L1650-1655) writes the same displays as "(6.9) [I]" and "(1.6.10)". So old Section 6 is the
printed CMP 116 Section 1, and (6.9), (6.10) are CMP 116 (1.9), (1.10): the localisation expansion in the
decoupling parameters s of the response functions. The account reads CMP 116 the same way: CA-II 21970-21973,
"Balaban proves the same property for the operators H, G, H_0 of [CMP 116, Section 1, after (1.9)] as functions of
the decoupling parameters". [reading; CMP 116 itself is not on this machine, so the renumbering is inferred from
three consistent citations, not seen]

1.6 **Earlier lane on the same composition (rule 0a match).** `library/ch-r2.md` (FINISH row 415, CH4-AUX; also
`ch-r1.md`, `ch-bridge.md`, `ph.md`, `prior/ch.md`) treats the three links (1.61)-(1.63) from the page images.
Its (2a): every link output is a localised constrained minimiser for one fixed determining system; the switches
enter only through H_k(sigma) in the data on the boundary layer. Its premise (P1): H_k(sigma) is holomorphic on the
switch polydisc with |eta H_k(sigma)| <= C_H e^{16 kappa_1} |xi|, resting on (K10), "the CMP 99b
covariance-inverse walk hypothesis" (repo chain PI, GW, GW1). That lane's open items are regularity memberships
(P4'), CH3-REG, final membership (d), outer room R_*. It does not state which supplier family the reads use
relative to (b3); that is this row's question.

1.7 **The account's own dictionary agrees (read 2026-11-23T21:35Z).** CA-II 47976-48160 (`5.6:def-localization-links`) and
48414-48419: "Sections 6 and 7 of [I] are Sections 1 and 2 of CMP 116, and an equation cited in CMP 122b as (6.n) [I]
or (7.n) [I] is equation (1.n) or (2.n) of CMP 116". So 1.5 is the account's reading too, not only an inference.
The account writes the composed read as three links i = 2, 3, 4 with link functions H^(2) (in (1.61), with u_k),
H^(3) = H_B, H^(4) = H_k of (1.64), each localised by one expansion "in the form CMP 116 (1.10)" with the set
sigma_0^(i) of cubes disjoint with Lambda, parameters sigma^(i) = (s(Delta)) on a finite set V_i. Its per-link
reading (`5.6:def-link-readings`, CA-II 48236-48275) is a HYPOTHESIS: sigma^(i) enters "through operators with
generalised random walk expansions, into which the parameters are introduced as in CMP 116 Section 1 and which obey
the walk bound CMP 116 (1.11), and through contraction fixed points"; ||H^(i)(sigma; xi, psi)|| <= C e^{16 kappa_1}
||xi|| under delta_1 M >= kappa_1, "uniformly in the background psi". The route text CA-II 46168-46216 (proof
outstanding) says the same: on |sigma(Delta)| = e^{kappa_1} "the interpolated operators of the random-walk and
localisation expansions keep their exponential decay. There they are bounded by e^{16 kappa_1} [CMP 116 (1.7),
(1.11)]".

1.8 **The spaces of the read have local real parts (read 2026-11-23T21:37Z).** CMP 109 p. 262 (OCR L686-720): the space
U^c_j(X, a_0, a_1) consists of (U, J) "defined at bonds of X" with U = U'U_0, U_0 G-valued, regular on X by
(1.11)-(1.12) (a gauge on each cube of size O(1)LM inside X); condition (iv) builds the tower "considering X as
Omega_0". CMP 122a p. 190 (OCR L784-790): the stage space U^(n)c_k(X, a_0, a_1) "is the set of configurations
(U, J) defined on X, such that U = U'U, U has values in the group G", with towers U_{p,X}(M'(U)) =
U(B_p(X) u {Gamma^l}, M'(U)) built on X. So every element of the source space U~^c_k(Y_4, .) and of the value space
U~''^c_k(Y_1, .) of (1.65) has a real part given on Y_4 (on Y_1) only. Y_1 contains the components of the
large-field region Z that meet X (CMP 122b p. 373). This is the class that `cm-claude.md` O2 / registry
CM-LOCAL-REAL describes: local real part, cells whose hull is not inside Omega_{k+1}.

1.9 **Balaban's supplier for the link functions is not Theorem 3.15.** CMP 99b (OCR L1520-1535, L1946-1953,
L2336): Theorem 3.10 is the walk expansion (3.107)-(3.108) of the propagator G; Theorem 3.12 gives "Theorem 3.10
... for the operators H, H_1" under the regularity conditions (3.35), (3.36), with a common rate delta_0, "a
positive, absolute constant depending on d and L only"; Theorem 3.15 is the separate statement for the covariance
C^(k)(Lambda), "for M alpha_0 sufficiently small". CMP 119 p. 277 (OCR L1648-1651): the localisation expansions
(6.9) [I] use "Theorems 3.7-3.10 [13] in their full generality" for a sequence {Omega_j}. The supplier (b3) =
`5.2:lem-random-walk-bounds` is headed "[CMP 99b, Theorem 3.15]" and lists the four operators A, C_Lambda,
C_Lambda^{1/2}, C_I (CA-II 8922-8926).

## 2. Result: the identification (written 2026-11-23T21:39Z)

Notation. D_old is the old-term read of the row: for a first-part term t = E(X; .) with X meeting Z and a piece
index (Y_2', Y_3', Y_4'), the map (sigma, d) -> t(R(sigma; d)), R = E_2(sigma^(2); E_3(sigma^(3); E_4(sigma^(4); d))),
as in `5.6:def-localization-links` (CA-II 47976-48145) and `5.6:thm-link-holomorphy` (CA-II 49117). At sigma = 1
and summed over pieces it is Balaban's E(X, U^0_k) of CMP 122b p. 375. "(b3)" is CA-II 2181-2271 with
`5.2:lem-random-walk-bounds` (CA-II 8922). Each item says proved, sketched or guessed. "Proved" here means: follows
from the quoted definitions and printed text; one reading by one model, not checked by another.

**Proposition 2.1 (operator inventory of D_old). Proved (from the definitions).** The constituents of R are:
(a) three switched link functions H^(2)(sigma^(2)), H^(3)(sigma^(3)) = H_B, H^(4)(sigma^(4)) = H_k of (1.64);
(b) the gauge factor u_k, an explicit blockwise analytic function of H^(2) (CMP 122b p. 373; CMP 102 (106));
(c) three localised constrained minimisers U(B(Y_i) u B_*, .) for the fixed determining systems B_k(Y_1) (printed
B''_k(Y_1), see `ch-r2.md` (2d)), B_1(Y_2), B_k(Y_3);
(d) block averages M(.) and restrictions.
The switches enter only through (a). *Argument.* This is clause (d)-(f) of `5.6:def-localization-links` (CA-II
48058-48128) and CMP 122b (1.61)-(1.64) as quoted in Section 1.1; `ch-r2.md` (2a) reads the same from the page
images. The definition lists no other operator.

**Proposition 2.2 (no member of the (b3) family is read; the assigned companion is not read). Proved at the level
of the printed construction; sketched for "no hidden use".** No constituent of R is one of A, C_{Lambda*},
C_{Lambda*}^{1/2}, C_I, and none is a function of them. *Argument.* (i) The four operators of (b3) are defined at
the rim datum of the small-field step: A = C* Delta_k C on l^2(X; g), C_Lambda = A_{Lambda Lambda}^{-1} "Balaban's
covariance C^(k)(Lambda_{k+1})", C_Lambda^{1/2}(sigma) "the operator of CMP 116 (2.7)" (CA-II 8922-8926,
8946-8948). CMP 116 (2.n) is Section 7 of [I]; the links use only (6.n) [I] = CMP 116 (1.n) (CA-II 48417-48419;
`5.6:thm-link-holomorphy` hypothesis (d) reads only "the floor delta_1 M >= kappa_1"). (ii) The step R_k has no
Gaussian fluctuation integral: its variable is B on Lambda with an axial-gauge delta function and characteristic
functions (Section 1.4), so there is no covariance and no root to substitute. (iii) A search of CA-II 46131-48700
(the whole link chapter) for root, companion, random-walk and M-freeness finds four lines (46177, 46730, 48256,
48410), all about the walk bound for the link functions. *What is only sketched:* that the "transformations and
estimates of Sects. 3-5 [I]" applied in the first operation (link 1, CMP 122b (1.59)-(1.60)) use no covariance. I
read CMP 109 Sections 4-5 only in part (OCR L2090-2560: polarisation tensor, generic small B). Link 1 is "not among
the three links" of the composed read (CA-II 48043-48044), so the row's D_old does not depend on this.

**Proposition 2.3 (the supplier of D_old). Proved as an identification; the supplier itself is conditional.**
The family that D_old reads is the switched response family of the response chart: clause (K10) of
`4.5:thm-chart-existence` = `4.5:prf-chart-walk-localisation` (CA-I 15265-15300), primitive operators
G_0, G', R, P, (Q'G'^2Q'*)^{-1}, q_0, G^J_pi, q_J, G~^J, G^J_1, (Q G^J_1 Q*)^{-1}, each walk term multiplied by
prod s(Delta) by the rule of CMP 116 after (1.7). In Balaban's papers this is CMP 99b Theorems 3.10 and 3.12 (H,
H_1; rate delta_0 depending on d and L only) with CMP 116 (1.7)-(1.11), not Theorem 3.15. (The rule for the
factors s(Delta) and the walk-wise bound (1.7), (1.11) are common to both suppliers; (b3) also cites them. What
differs is the operator: the covariance (3.158) and its root (2.7) there, the response operators here.) (K10) has one hypothesis:
the walk expansion of the constrained covariance inverse q_0 = (Q G_0 Q*)^{-1}, "printed without proof in [CMP 99b,
after Theorem 3.9]" (CA-I 15268-15272). The account's per-link reading (`5.6:def-link-readings`) keeps the
application of this family at each link as a hypothesis (Section 1.7). In this repository the same supplier is
premise (P1) of `ch-r2.md` (L145) with lanes PI, GW, GW1, B99-W. *Consequence.* The "admitted Z containing Z_0'"
of the row has no object in D_old: Z_0, Z_0', sigma_0 of CMP 116 p. 13 belong to the cluster expansion of the
small-field fluctuation integral (Section 2 of CMP 116). The analogue in D_old is the piece index: the link
domains Y_i', each component in D_k, containing a component of Lambda and meeting the layer Y_{i-1} \ Y_{i-1}^0,
with the cube sets sigma_0^(i) disjoint with Lambda (CA-II 48058-48090).

**Proposition 2.4 (the domain class of D_old; the class O2 is read). Proved (from the printed definitions).**
The source domain of D_old is U~^c_k(Y_4, a~_0, a~_1) and the value space is U~''^c_k(Y_1, a~_0, a~_1). Every
element of either space is a pair (U, J) defined on Y_4 (on Y_1) only, with U = U'U_0 and U_0 G-valued and regular
on that domain only; its towers are built from the domain as Omega_0 (Section 1.8). Y_1 contains every component
of the large-field region Z that meets X, so Y_1 is not inside Omega_{k+1}. Hence D_old reads data of the class
that `cm-claude.md` O2 (registry CM-LOCAL-REAL) describes. It reads them through the response family of 2.3, not
through the root. The chart class S of that family is itself local: (S1) asks U = e^{i eta a} U_r with U_r
G-valued and a gauge on each cube of the class (CA-I 12945-12967), and it contains every pair satisfying (i)-(iii)
of CMP 109 on X under the ceilings c_12 L M B^109 a_0 <= a_0^S, a_1 <= a_1^S, gamma_0 <= a_gamma (CA-I
13000-13017). The first ceiling reads M and bounds alpha_0 from above; alpha_0 is a Stage-7 letter, after M (CA-I
1590-1627), so the order of choice admits it. *Not proved here:* that the stage spaces of CMP 122a (1.64)-(1.69),
whose conditions on the crucial domain Omega''_{k_0+1} \ Omega_{k_0+1} carry powers of L_0, lie in S. That is the
block-level comparison (P4') of `ch-r2.md` and the membership hypothesis (b) of `5.6:thm-link-holomorphy`; it is
owned by CH.

**Corollary 2.5 (what the old-terms step reads of M). Proved from 2.1-2.3 and the account's order of choice.**
The only condition on M that D_old reads is the floor delta_1 M >= kappa_1, with delta_1 the rate after CMP 116
(1.11) (CA-II 48150-48154; hypothesis (d) of `5.6:thm-link-holomorphy`; route text 46175-46179). In the account's
order delta_1 stands before M_1: Stage 5 imposes delta_1 M_1 >= c kappa_1 as a floor on M_1 (CA-I 1498-1504), and
Stage 6 lists delta_1 M >= kappa_1 as its own floor (CA-I 1541-1542), apart from the three floors that read mu_0
and delta_W (CA-I 1545-1550). So D_old does not read (B_W, delta_W) or mu_0, and the corrected clause (*') of
`cm-claude.md` (the root bound at rate min(mu_0, delta_W)) is never evaluated in this step. The sentence CA-II
59566-59568 ("The same step also uses the independence from M of the kernel constants and of the decay rate of the
random walk ... it is Proposition 5.10:prop-m-freeness") has no object in the link construction: the terms
"conditional fluctuation operator" and "companion kernel" occur in CA-I and CA-II only inside the two statements of
that proposition (grep: CA-I 2242-2247, CA-II 59582-59607). What the step does need, uniformly in M, is the bound
of the link reading "uniformly in the background psi" (CA-II 48259-48275) at backgrounds of the local class of
2.4. That is M-freeness of the (K10) constants on S, a clause of CH, not of CM. *Guessed, not proved:* that the
account's authors meant exactly this by the sentence at 59566.

**Answer to the row's alternative.** The row asks: prove membership and companion identification for the full
class, or exhibit a legal read outside the supplier's domain or family. Result: every actual read is outside the
FAMILY of (b3) (2.1-2.2), and its data are of the local class O2 (2.4). This is not a counterexample to any
estimate: it shows the requested match has no object. In the row's words the reads are "unmatched" to (b3), and
they are matched to a different supplier, (K10) on S, whose application at the links is the open lemma CH
(`open-core.md` L540 and L551 "reached-link holomorphy"; `open-registry.md` L17 CH and L23 CH4-AUX; `ch-r2.md` Result).

## 3. What this changes, and what it does not

- **CM-O3 / CM-OLD-TERMS (registry L183, t0-tree L311).** The task "place old-term local reads in the supplier's
  analytic class and assigned companion family" can be closed as an identification: the class is named (2.4), the
  family is named (2.3), and it is not the companion family. The remaining analytic content is CH's. Proposed
  registry wording for the lead: "identified (cm-o3-fable 2.1-2.5, unchecked): reads are the three CMP 122b links;
  family = (K10) on S; no root read; analytic content merged into CH".
- **The gate's objection to the CM merger (`gates/cm-gate.md` L11, L30-34).** The gate found that rows 2 and 7 of
  the consumer table identify the consumer class with (b3)'s class without proof. For row 7 (old terms) the answer
  is now: the consumer reads no companion, so no identification with (b3) is needed there. Row 2 ((A2), CA-I
  2325-2345) is an abstract hypothesis "at the local density data actually used"; this note shows the old-terms
  site is not such a use for the companion clause. I did not re-run the search for other local-data uses;
  `cm-claude.md` Section 2 did (its table rows 1-8), and the gate did not dispute its inventory, only the two
  identifications. So the merger "CM = the cited leaf `5.2:lem-random-walk-bounds` plus Lemma R" now rests on one
  unchecked reading (this note) instead of an open identification.
- **CM-LOCAL-REAL (registry L182).** Its class is read at the old-terms site, but by the response family. A root
  bound on that class has no consumer found. Proposed wording: "class is read by CH's links through S (cm-o3-fable
  2.4); no companion read found there".
- **Not changed.** CH and its premises ((P1) with the q_0 walk hypothesis, (P4'), CH3-REG, final membership (d),
  outer room R_*) stay open. The old-terms containment itself (value space inside each old term's domain,
  hypothesis (e)(i), CA-II 48585-48598) stays "printed without proof". B99-W's leaf stays cited. Nothing here was
  checked by another model.
- **Failed or unfinished in this row.** (1) CMP 116 is not on this machine; the renumbering and the content of
  (1.7)-(1.11), (2.7), p. 13 are taken from the account's quotations and from CMP 119, 122b citations. (2) I did
  not prove stage space inside S (2.4, last paragraph). (3) I did not construct a datum of U~^c_k(Y_4) that fails
  the domain of (b3); with the family already different this would add nothing a consumer reads.

## 4. Next two rows and their decisive outcomes

1. **`cm-o3-check` (other provider, one line-by-line check of Section 2).** Read CMP 122b pp. 356-357, 369-375 from
   the page images and CMP 116 Sections 1-2 from a copy (fetch one; it is missing in ~/ym4d-papers). Decisive
   outcome: either "first failing step none", then the lead merges CM-O3 into CH and K1 = CM reduces to the cited
   leaf `5.2:lem-random-walk-bounds` with Lemma R; or one printed line where a link, the first operation, or the
   resummation reads C^(k)(s) or its root, which is then the exact datum O3 asked for.
2. **`ch-stage-in-S` (proof row, CH owner).** Statement: for every admitted history and every piece, the stage
   spaces U~^c_k(Y_4, a~_0, a~_1) and the reached link backgrounds lie in the chart class S (CA-I 12945-13017) with
   radii fixed before M, the M-reading ceiling falling on alpha_0 only. It is `ch-r2.md` (P4') extended to all
   three links. Decisive outcome: a proof gives the link readings their domain, so (K10) supplies D_old with
   M-free constants and Corollary 2.5 becomes unconditional on the class; or a stage-space clause on the crucial
   domain Omega''_{k_0+1} \ Omega_{k_0+1} whose constant exceeds a_0^S for every admitted alpha_0, which would be a
   legal datum outside the supplier's domain and a real obstruction to the old-terms sentence.

## 5. Closing record

- Finished 2026-11-23T21:40Z (date -u). No numeric run, no lock taken, no subagent, no commit. Only this file was written.
- Kind of result: identification of a step the account cites as printed (which class and family Balaban's
  old-terms sentence reads); no statement of Sussman and Alpoge or of Balaban is corrected. One observation on
  their text is recorded, not claimed as an error: the attribution at CA-II 59566-59568 names objects that the
  link construction does not contain (Corollary 2.5).
- Who checked what: written by Claude (Fable 5.2, medium effort), not checked by the other model. Sources read
  from OCR text, not from page images; `ch-r2.md` read the same pages of CMP 122b from images and agrees on 2.1.
- Rule 0a matches cited: `ch-r2.md`, `ch-r1.md`, `ch-bridge.md`, `ph.md`, `prior/ch.md` (the links);
  `cm-claude.md` O2, O3 and `gates/cm-gate.md` Section 1 (the question); `open-core.md` CH; registry CH, CH4-AUX,
  CM-OLD-TERMS, CM-LOCAL-REAL; t0-tree CM-O3 (K1). No file found that states 2.2 or 2.5 (grep of library, gates and
  FINISH for "old-terms-beside", "(1.65)", "CM-O3").

RESULT: CM-O3 identified, not matched to (b3). Proved from the printed definitions (one reading, unchecked): the old-term read of CA-II 59542-59551 is the three-link composition of CMP 122b (1.61)-(1.63); it reads only the switched response family ((K10) of 4.5:thm-chart-existence; CMP 99b Thm 3.10/3.12 with CMP 116 Section 1), no member of the (b3) family and no root companion; its data have local real parts on Y_4 containing large-field components (the class of CM-LOCAL-REAL); the only M-condition it reads is delta_1 M >= kappa_1, so (*') and mu_0 are never evaluated there. Open: the analytic content, which is CH (stage spaces inside the chart class S, link readings with the q_0 walk hypothesis, final membership, the old-terms containment itself); a cross-provider check of this reading against CMP 116, which is not on this machine.
