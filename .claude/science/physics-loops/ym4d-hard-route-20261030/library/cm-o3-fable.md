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
