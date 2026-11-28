lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T16:44Z

# gap-idab-opus: port of the two identification inputs of (DET)

Queue row 993 of `FINISH.md`, pinned at commit 0ee089f92. Next step (i) of
`library/gap-iloc-opus.md`. Sources: Balaban CMP 109 (1987) 249-301 and CMP 119
(1988) 243-285 (`~/ym4d-papers/`, OCR checked against the PDFs page by page);
CMP 102 (1985) 277-309 for (174). The papers are credited, not load-bearing:
each step used is rebuilt below in the repository's terms.

Marks: PROVED, ARGUED, OPEN, FAILS.

## Plan (at most eight steps)

1. Read the row's context: `library/gap-iloc-opus.md` (Lemma Z', Lemma LR,
   (ID-a), (ID-a'), (ID-b), (DET)), rows 989/990 and their outputs,
   `library/open-core.md` grep for overlaps. Record exact statements needed.
2. (ID-a') part 1: CMP 119 (3.28)-(3.33): what log z^(k)(c) is, which
   background it reads, locality radius, covariance under level-k cell
   translations.
3. (ID-a') part 2: the constants of (3.33): one number per cell/bond, torus
   independence; is E_0^(j) the same additive set function on both tori.
   Combine with Lemma Z' to settle (ID-a).
4. CMP 109 (0.10)-(0.12): is the block map a bond-by-bond local covariant rule
   (Lemma LR, Step 6b of the row).
5. (ID-b): CMP 109 (2.4)-(2.11) and CMP 102 (174): at U = 1, compare
   C^* Delta^(k) C with pr-lay (7) at P_0.
6. Rebuild of each used step in repository terms, with credits.
7. Verdict table and RESULT.

## State of attack

All steps done 08:00Z. Item complete; verdicts in Step 7. Checked by no one; no numeric run.

## Step log

### Step 1. Inputs and overlap check (04:55Z)

- **Overlap.** `grep -n "ID-a\|ID-b"` over `library/open-core.md`: no hit. In `FINISH.md`: rows 989, 990 (which name them open) and this row 993 only. In `library/`: only `gap-det-check-opus.md`, `gap-iloc-opus.md` (the rows that posed them). No other row attacks them. Proceeding.
- **(ID-a)** (row 989 L154, L200): at U = 1, every z^(k)(c) of CMP 119 (3.33) and every per-cell constant of its measure is one number per cell, the same on every torus for a common coupling sequence.
- **(ID-a')** (row 990 Lemma Z'): Balaban's log z^(k)(c) is a rule that (L) reads the background only on a bounded patch around c and otherwise depends only on (L, k, couplings of level k), and (E) is covariant under translations preserving the level-k cell lattice. Lemma Z' (row 990, PROVED as implication): (ID-a') gives (ID-a) for z^(k)(c).
- **(ID-b)** (row 989 L155, L201): (1c.1) at U = 1: Balaban's C^* Delta^(k) C at 1 equals pr-lay (7) at P_0.
- **pr-lay (6)-(7) at P_0 = (1,0,0)** (pr-lay L61-80): with J = 0, G = G_0 = (Delta^W + D R D^T + Q^T a Q)^{-1}, G_1 = G_0, and
  A(P_0) = C_V^T [ iota^T {(Q G_0 Q^T)^{-1} - a} iota + K_GF ] C_V,
  with R the projector built from G' = (D^T D + Q'^T a Q')^{-1}, C_V the derivative of the pivot graph, K_GF the soft gauge Hessian, a the row weight (xi_c^{-2} = 1 on level-k rows at P_0, per row 990 Step 3).
- **Lemma LR** (row 990 Step 4): local equivariant rules descend to tori, commute with pull-back, and their derivatives at an invariant point are periodizations of finite-range stencils.
- **Account's block map** (row 990 Step 6b): CA-I L808-835 defines M bond by bond by citing CMP 109 (0.11)-(0.12) on S_c (built on the inner mean (0.10)), and (0.4) off S_c. At U = 1 only branch (a) is used.
- **Sources on this machine:** `~/ym4d-papers/cmp109.txt`, `cmp119.txt`, `cmp102.txt` with PDFs. Credit: T. Balaban, CMP 102 (1985), 109 (1987), 119 (1988).

### Step 2a. CMP 119 (3.28)-(3.33) read from the PDF (05:10Z)

Source: Balaban, CMP 119 (1988) 243-285, PDF page 31 (journal p. 273), read as an image; the OCR at `cmp119.txt` L1507-1515 is garbled there.

- **(3.33), exact.** "The factor z^(k) comes from elimination of the delta-functions, and is equal to the product of the factors z^(k)(c) for c in Lambda_{k+1}^{(k+1)}. We have
  log[ z^(k) int dA exp(-(1/2)<A, C^* Delta^(k) C A>) ] = sum_{c in Lambda_{k+1}^{(k+1)}} log z^(k)(c) - (1/2) log det(C^* Delta^(k) C) + log int dA exp[-(1/2)|A|^2]. (3.33)
  The last term is a number, which contributes to the vacuum energy renormalization, so we include it into the definition of E_0^(k). The first term has already the localized form".
- **Consequence 1 (the constant of (3.33)).** The only constant in (3.33) is log int dA exp(-|A|^2/2), with dA the Lebesgue measure on the variables A that remain after the delta-functions are removed (to be confirmed in CMP 109 Sect. 2, Step 2b). For a real vector space of dimension N with the standard Euclidean norm this is exactly (N/2) log 2 pi, one factor (1/2) log 2 pi per real coordinate. That is CA-I L106147's "(N/2) log 2 pi". So the "constants of the measure of (3.33)" are this number, plus whatever normalization of dA CMP 109 fixes. PROVED for the Gaussian integral (elementary: int_R e^{-x^2/2} dx = sqrt(2 pi), Fubini over N coordinates).
- **z^(k)(c) is not defined in CMP 119.** CMP 119 p. 267, L1263-1268: "The next steps are exactly the same as in Sect. C [16], and in fact the same as in Sect. 2 [I]. We expand all the expressions with respect to A_k, and we linearize the expressions in the delta-functions for bonds in Gamma_{k+1}. Finally we remove the delta-functions using the operator C, and we perform the scaling transformation A_k = g_k A_k. All the applied formulas are the same as in Sect. 2 [I], only the symbols represent different operators, determined by the sequence {Omega_j}." Reference [I] is CMP 109 (CMP 119 reference list). So the definition of z^(k)(c) and of C is CMP 109 Sect. 2: the same section as (ID-b)'s (2.4)-(2.11).
- **(3.15)** (CMP 119 p. 267-268, garbled OCR L1270-1280) carries a term "+ log sigma_0 |B(Gamma_{k+1})^*|" (to be read from the PDF in Step 2b): a constant per bond of a set, of the same type as SA's sigma_0^{|F|} of (QC25).
- **(3.39) covariance.** CMP 119 p. 274: "If they are constructed assuming that Lambda_{j+1} is the whole space, i.e. assuming Omega_j = Lambda_j = T_eta for j = 1,...,k+1, then they are also Euclidean covariant ... E^(k+1)(tau U_{k+1}, tau^{-1} b) = E^(k+1)(U_{k+1}, b) ... tau an arbitrary Euclidean transformation ... transforming the lattice T^(k+1) into itself." This is the setting of P_0 (all Omega_j the torus). It states covariance for the localized terms (3.37), whose first term is the localized z-factor.

### Step 2b. CMP 109 read from the PDF: the block map, the step integral, the delta elimination (05:35Z)

Source: Balaban, CMP 109 (1987) 249-301, PDF pages 5-7, 13, 17-20 (journal pp. 253-256, 261, 265-268), read as images. Formulas below are transcribed from the images, not the OCR.

**The block map (item (2) of the row).**
- (0.4), p. 253: Ubar(c) = M(U,c) = exp[ i sum_{x in B(c_-)} L^{-d} sum_{Gamma in G(c_-,x)} |G(c_-,x)|^{-1} sum_{Gamma' in G(c_+,x')} |G(c_+,x')|^{-1} (1/i) log U(Gamma u [x,x'] u (-Gamma') u (-c)) ] U(c).
- (0.5)-(0.9), p. 253: axioms of a group average M({U_j}): inverse, two-sided covariance M({u U_j v}) = u M({U_j}) v, permutation symmetry, (1/i) log M({exp iA_j}) = (1/n) sum A_j + higher order, G-valued for G-valued input.
- (0.10), p. 253: "The average of the set {U_j} is the element U in G^c such that U_j are in a small neighborhood of U, and it satisfies the equation sum_{j=1}^n (1/i) log U_j U^{-1} = 0." (Federbush's definition; Balaban credits [35 (II)] for the properties.)
- (0.11), p. 253: U(y,x) = M({U(Gamma)}_{Gamma in G(y,x)}).
- (0.12), p. 254: Ubar(c) = exp[ i sum_{x in B(c_-)} L^{-d} (1/i) log U(c_-,x) U([x,x']) U(x',c_+) U(-c) ] U(c).
- p. 254: "both definitions are equally good for our purposes, in fact we may use many other definitions."
- **Match with SA.** (0.10) is SA (QC1), (0.11) is SA (QC2), (0.12) is SA (QC3) with Z_x = U(y,x) U([x,x']) U(x',y') U[c]^{-1}, U(x',c_+) = U(c_+,x')^{-1}, d = 4. So the account's branch (a) (CA-I L808-835, "Balaban's symmetrised average [(0.11)-(0.12)] built on the inner group mean [(0.10)]") is the outline's (QC1)-(QC3), given that G(y,x) is the same contour family (checked in Step 4).

**The step integral (CMP 109 Sect. 0 and 2).**
- (0.15)-(0.16), pp. 254-255: exponential gauge fixing exp[-(1/alpha)(1 - Re tr U(y,x))] for y in T^(1), x in B(y), x != y, normalized by z = int du exp[-(1/alpha)(1 - Re tr u)] chi(|u - 1| < eps_0): one number depending on (alpha, eps_0) only, one factor per pair (y, x), x != y. Torus-free.
- (0.17), (0.19), p. 255: A_{k+1}(V) = log N_k^{-1} int dU prod_{c in T^(k+1)} delta(Ubar(c) V^{-1}(c)) chi_k exp[-(1/g_k^2) sum_y sum_{x in B(y), x != y} (1 - Re tr U(y,x)) + A_k(g_k, U)], "where the constant N_k is given by the integral above with V = 1" (p. 256).
- **Consequence 2.** In Balaban's own normalization every constant of the step, including the delta-elimination factor at the background 1, is divided out by N_k, the same integral at V = 1 on the same torus. Balaban's actions carry no torus-dependent constant by construction; the constants that the account carries as z^(k)(c) and E_0 are what the account keeps when it undoes this normalization (CA-I (n1)-(n3)). So (ID-a) asks whether N_k, split per cell, is torus-free; Balaban's text does not split N_k.
- (2.4), p. 266: M(V' V^(k)) M(V^(k))^{-1} = exp i Qtilde(B'), with V' = exp iB' the fluctuation and V^(k) = M^k(U_{k+1}) the critical point (2.3).
- (2.5), p. 266: G(B') = sum_{y in T^(k+1)} sum_{x in B(y), x != y} (1/2)|Btilde'(y,x)|^2 + G_3(B') = (1/2) G^(2)(B') + G_3(B').
- (2.10), p. 267: the integral is log N_k'^{-1} int dB' sigma(B') delta(Qtilde(B')) chi_k exp[...], "where the factors sigma_0 are included into the normalization factor N_k'".
- p. 267: h maps g-valued functions on bonds of T^(k+1) to functions on bonds of T^(k), zero except on {b_0(c)}, with "L Qtilde h = I on T^(k+1)"; "(hB)(b_0(c)) = h(c) B(c), where h(c) is a linear operator on the Lie algebra g, equal to an inverse of a coefficient at the variable B'(b_0(c)) in (Qtilde B')(c), multiplied by L^{-1}". b_0(c) is the bond of T^(k) in the corridor B(c) = {b : b_- in B(c_-), b_+ in B(c_+)}. The nonlinear change B' = B - h Dtilde(B) linearizes Qtilde: L Qtilde B' + Ctilde(B') = L Qtilde B.
- (2.11), p. 267: order-zero terms <H_1 h Ctilde^(2)(B'), J> - (1/2) G^(2)(B') - (1/2) <H_1 B', Delta_1 H_1 B'>. "The quadratic form in B' above is equal to -1/2 <B', Delta^(k) B'>, see the definition (3.156) [13] with the delta-function gauge fixing term replaced by the exponential one."
- p. 268: "using delta(Qtilde B') we eliminate the variables B'(b_0(c)), c in T^(k+1). Denoting the remaining variables by B we have B' = CB, C is the operator determined by the configuration V^(k), and the measure becomes a Gaussian measure in variables B, with the covariance C^(k) = C^(k)(U_{k+1}) = (C^* Delta^(k) C)^{-1}."
- (2.12), p. 268: the new action contains [log Z^(k)(U_{k+1}) - log Z^(k)(1)] and log N_k''^{-1} int dmu_{C^(k)}(B) chi_k exp[Tr log(I - h (delta/delta B) Dtilde)(g_k CB) + log sigma(g_k CB - h Dtilde(g_k CB)) + ...]; "the normalization constant N_k'' is equal to the integral above at U_{k+1} = 1". (2.14): log N_k'' = E^(k+1)(g_k, 1).
- (1.5), p. 261: <B, Delta^(j)(U_k) B> = <H_{1,j}(U_k) B, Delta_1(U_k) H_{1,j}(U_k) B> - 2 <H_{1,j}(U_k) h Ctilde^(2)(Ubar_k^j, B), J> + G^(2)(B), "where the operators H_{1,j}, Delta_1 are defined in Sect. D [13]".

**Where z^(k)(c) comes from (derived here from the quoted text; Balaban gives no formula for it).** delta(Qtilde B') at linear order is prod_c delta_g((Qtilde B')(c)), a product of Dirac deltas on g = R^3, one per coarse bond c. By "L Qtilde h = I", (Qtilde h B)(c') = L^{-1} B(c') for every c'; since h B is supported on the pivots, the pivot variable B'(b_0(c)) enters (Qtilde B')(c') with coefficient L^{-1} h(c)^{-1} if c' = c and 0 if c' != c. So the elimination is diagonal in the pivots: int prod_c dB'(b_0(c)) prod_c delta((Qtilde B')(c)) = prod_c |det_g(L^{-1} h(c)^{-1})|^{-1} = prod_c L^3 |det_g h(c)| (dim g = 3), and the remaining variables are B' = CB with C B = B - h Qtilde_np B ... (the non-pivot part substituted). Hence **z^(k)(c) = L^{dim g} |det_g h(c)| up to the sigma_0 factors that Balaban puts in N_k'**, with h(c) = L^{-1} [coefficient of B'(b_0(c)) in (Qtilde B')(c)]^{-1}. This is ARGUED: the derivation is elementary (delta-function change of variables on R^3) but the identification "z^(k)(c) of CMP 119 (3.33) = this Jacobian" rests on CMP 119's sentence "The factor z^(k) comes from elimination of the delta-functions" and CMP 109 p. 268, not on a printed formula.

### Step 2c. CMP 119 (3.15): the constants of the step, exact (05:50Z)

Source: CMP 119 p. 267 (PDF page 25), read as an image; OCR L1270-1280 is garbled.

(3.15): (T rho_k)(V_{k+1}) = sum_{{Omega_j},{Lambda_j}} sum_{Omega_{k+1}} chi_{k+1}(Omega_{k+1}) int dV_k|_{Omega^c_{k+1}} delta(Vbar_k V_{k+1}^{-1}) zeta(Omega^c_{k+1})
 . T_k exp[ A_k(1/g_k^2, U_{k+1}) + log g_k d(g) |B(Gamma_{k+1})^*| + log sigma_0 |B(Gamma_{k+1})^*| - log z (L^4 - 1) |Gamma_{k+1}| ] z^(k) int dA_k|_{Omega_{k+1}} chi'_k(Omega_{k+1})
 . exp[ -(1/2) <A_k, C^* Delta^(k) C A_k> + P^(k)(g_k, U_{k+1}, A_k) + {...} ].

Reading of the constants (d(g) = dim g = 3 for SU(2)):
- d(g) log g_k per bond of B(Gamma_{k+1})^*: the Jacobian of the scaling A_k' = g_k A_k (p. 267: "we perform the scaling transformation A_k' = g_k A_k"), one log g_k per real coordinate.
- log sigma_0 per bond of B(Gamma_{k+1})^*: the Haar density at 1 in exponential coordinates (CMP 109 (2.10): "the factors sigma_0 are included into the normalization factor").
- -log z per site x != y of each block, (L^4 - 1) per block, |Gamma_{k+1}| blocks: the gauge-fixing normalizer z of CMP 109 (0.15), a number depending on (alpha, eps_0) only.
- z^(k) = prod_c z^(k)(c): the delta-elimination factor (Step 2b).
- In (3.33): log int dA exp(-|A|^2/2) = (N/2) log 2 pi.

**Lemma C (the constants of (3.15) and (3.33) are torus-free per cell or bond). PROVED, given the reading of (3.15) above.** At P_0 (all Omega_j, Lambda_j equal to the torus T_n of side n L^{k+1} in level-0 units; Gamma_{k+1} all coarse sites), each constant is c_i times a count, with c_i in {d(g) log g_k, log sigma_0, -log z, (1/2) log 2 pi} depending only on the group, (alpha, eps_0) and the coupling g_k, and the count one of |Gamma_{k+1}| = n^4, |B(Gamma_{k+1})^*| and N. *Proof.* The coefficients are as listed, with no reference to n. The counts: |Gamma_{k+1}| = n^4. B(Gamma_{k+1})^* is a set of bonds of T^(k) determined by the blocks of Gamma_{k+1}; whichever of "all bonds of T^(k) in the blocks and corridors" (4 L^4 per coarse site) or "the same minus the pivots b_0(c)" (4 L^4 - 4 per coarse site) it denotes, it is a fixed number of bonds per coarse site, since each block with its 4 positive corridors is a translate of one reference set, and these translates tile the torus once n >= 1 (every fine bond lies in exactly one block or corridor of exactly one positive coarse bond's double-block decomposition: interior bonds of B(y) in that block, crossing bonds in exactly one corridor). N = d(g) times the number of remaining bond variables, the same count minus pivots. So each constant is (torus-free number) x n^4. QED.

What this does not show: which of the two counts Balaban means by B(Gamma_{k+1})^* (it does not matter for torus-freeness); whether the account's constants (CA-I L106147-106150, "the constants of the measure of [(3.33)] for the cells of Z^s") are exactly these. The latter is a transcription question for CA-I, not a torus-freeness question: every candidate is of the form proved.

### Step 3. (ID-a'), (ID-a) and E_0^(j): verdicts (06:10Z)

**Lemma ZB (Balaban's elimination factor). Statement.** In the step of CMP 109 Sect. 2 (and CMP 119 p. 267, "the same as in Sect. 2 [I]"), at a background U_{k+1} with V^(k) = M^k(U_{k+1}) (CMP 109 (2.3)), the delta-elimination factor is z^(k) = prod_{c} z^(k)(c) with
  z^(k)(c) = |det_g K_c(V^(k))|^{-1},  K_c(V) := d/dt|_{t=0} Qtilde_V(t e_{b_0(c)} X)(c) as a linear map X -> . on g,
where Qtilde_V(B')(c) = (1/i) log[M(e^{iB'} V)(c) M(V)(c)^{-1}] (CMP 109 (2.4)) and b_0(c) the pivot of c. Equivalently z^(k)(c) = L^{d(g)} |det_g h(c)| with Balaban's h(c) (CMP 109 p. 267), d(g) = 3.
- (a) **Diagonal elimination. PROVED.** b_0(c) lies in the corridor of c and crosses the face between B(c_-) and B(c_+); by (0.12) the variable on b_0(c) enters M(.)(c') only if c' = c (the contour variables U(c'_-, x) read bonds inside the block B(c'_-), and the straight segments [x,x'] of c' cross only the face of c'). So the matrix of the linearized constraint restricted to the pivot variables is block diagonal, with block K_c(V) at c. The change of variables "eliminate B'(b_0(c)) using delta(Qtilde B')" (CMP 109 p. 268) then gives int prod_c dB'(b_0(c)) prod_c delta_g((Qtilde_lin B')(c)) = prod_c |det_g K_c(V)|^{-1}: the Dirac delta on R^3 under a linear change, one cell at a time (each pivot variable appears in exactly one constraint, so Fubini applies cell by cell). The nonlinear remainder is Balaban's Tr log(I - h (delta/delta B) Dtilde) in (2.12), field dependent and 0 at B = 0, not part of z^(k).
- (b) **Identification with the z^(k)(c) of CMP 119 (3.33). ARGUED.** Balaban prints no formula for z^(k)(c). CMP 119 p. 273 says only "The factor z^(k) comes from elimination of the delta-functions, and is equal to the product of the factors z^(k)(c)". (a) is the elimination CMP 109 p. 268 describes. Any other normalization of the same elimination (for example delta(L Qtilde B') in place of delta(Qtilde B'), or a sigma_0 put into z^(k)(c) instead of N_k') changes z^(k)(c) by a fixed power of L or of sigma_0 per cell, which Lemma C already covers.
- (c) **(ID-a'). PROVED on the formula of (a).** Locality: K_c(V) depends on V only on the bonds that M(.)(c) reads, i.e. the double block B(c_-) u B(c_+) with its corridor (CMP 109 (0.11)-(0.12); Step 4 below for G(y,x)); V = V^(k) = M^k(U_{k+1}) on those bonds depends on U_{k+1} only on the k-fold blocks of their endpoints. So log z^(k)(c) is a rule reading U_{k+1} on a bounded patch of c. Covariance: (0.4), (0.10)-(0.12), the contour families G(y,x), the blocks and the pivot b_0(c) are defined from relative positions only, so for every translation tau preserving T^(k+1), K_{tau c}(tau V) = K_c(V), and so z^(k)(tau c)(tau U) = z^(k)(c)(U). Dependence on (L, k, couplings): none beyond L (the rule does not contain g_k). This is (ID-a') with (L), (E) of row 990's Lemma Z'.
- (d) **Value at U = 1. PROVED.** At U_{k+1} = 1, V^(k) = 1. By (0.10) at U_j = 1 the mean is 1, and its derivative at 1 is the arithmetic mean (0.8). So the linear part of Qtilde_1 is row 990's (QC15): (K_I a)(c) = sigma_a(y) + L^{-4} sum_{x in B(y)} a([x,x']) - sigma_a(y'). The pivot appears only in the middle sum, in the L segments [x, x + L e_mu] with x on the central line of B(y) (row 990, hand check of (QC16)), each with coefficient +1 x Ad(1) = identity. Hence K_c(1) = L * L^{-4} I_3 = L^{-3} I_3 and z^(k)(c)|_{U=1} = |det(L^{-3} I_3)|^{-1} = L^9, for every cell c, on every torus. This matches SA's (det J_c(I))^{-1} = L^9 (row 990 Lemma Z) and YM4_1400 RF61 "36 N_{k+1} log L" (four cells per coarse site: 4 x 9 log L = 36 log L).

**(ID-a). PROVED for z^(k)(c) and for the constants of (3.15) and (3.33), on Balaban's text as read above, with the identification (b) ARGUED.** At P_0: sum_c log z^(k)(c) = 4 n^4 . 9 log L (direct, (d); also by Lemma Z' from (c)); the constants are torus-free numbers times n^4 (Lemma C).

**E_0^(j): two readings, two answers.**
- *Reading (i): CA-I (n2)'s E_0^(j) is the vacuum-energy part of the prefactor*, the constants that CMP 119 p. 273 puts there: "The last term [log int dA exp(-|A|^2/2)] is a number, which contributes to the vacuum energy renormalization, so we include it into the definition of E_0^(k)", together with the constants of (3.15). CA-I (n2) repeats this sentence. On this reading E_0^(j)(X) = (number) x |X| with the number torus-free (Lemma C): **the same additive set function on both tori. PROVED.**
- *Reading (ii): Balaban's full vacuum counterterm* E^(j)(Lambda_j, g_{j-1}, 1) of CMP 119 (2.25) (p. 259), whose localized form (2.26)-(2.27) is sum_{z} sum_{X ni z, X subset Lambda_j} E^(j)(X, 1, z). On this reading E_0 is **not** in general the same set function on two tori, exactly. Counterexample to exact equality (its simplest piece, written for hand check): the Gaussian part -1/2 log det at 1. For the 1D operator -Delta + m^2 on the cycle Z_n, log det / n is log m^2 at n = 1 and (1/2)[log m^2 + log(m^2 + 4)] at n = 2: different. The per-site difference comes from localization domains X that wrap the torus; Balaban's bounds (2.27)-(iv) (|E^(j)(X)| <= E_0 exp(-kappa d_j(X))) make it O(exp(-kappa' n)) per site, which (DET) tolerates (it asks a bound c_det, not equality) and which row 987's Lemma A already handles for the determinant. **Exact equality FAILS on reading (ii)** at the line CMP 119 (2.25)-(2.27): the per-site function E^(j)(Lambda_j, 1, z) is a sum over X subset Lambda_j, and the family of such X depends on the torus.
- *Which reading the chain uses.* CA-I L106125-106150 keeps -(1/2) log det(C^* Delta^(k) C) explicit in the prefactor and puts only "(N/2) log 2 pi plus the constants of the measure" into const_s. So the account's E_0^(j) is reading (i), and reading (ii)'s log det is the separate term that (DET) and Lemma A treat. ARGUED (it rests on the account's wording L104010-104013 and L106147-106150, read by row 990).

### Step 4. Item (2): the account's block map is a bond-by-bond local covariant rule (06:25Z)

Sources: CMP 109 p. 252 (PDF page 4, image) for blocks and contours; CA-I L800-840 at c7fef8b (Sussman and Alpoge's repository, sparse clone in my scratch `/tmp/idab993/sa/repo`, HEAD c7fef8b, the commit rows 986-990 used; not committed).

**Quotes.**
- CMP 109 (0.3), p. 252: "a block of k-th order, determined by the point y, is defined by B^k(y) = Delta(y) n T^(n-k)_{L^{-k} delta} [Delta(y) is a continuous space cube with a center at y and with the size delta]. Blocks of order 1 are denoted by B(y)."
- CMP 109 p. 252: "For a point x in B(y) we take a family G(y,x) of shortest contours with the initial point at y, and the final point at x. If x - y = sum_mu delta n_mu e_mu (... |n_mu| <= (L-1)/2), then we construct contours of G(y,x) in the following way: take a permutation {pi(1), pi(2), ...} of indices mu with nonzero numbers n_mu, next take |n_{pi(1)}| bonds in the direction sign n_{pi(1)} e_{pi(1)} starting at y, |n_{pi(2)}| bonds in the direction sign n_{pi(2)} e_{pi(2)} starting at y + delta n_{pi(1)} e_{pi(1)}, and so on. We define G(y,x) as the family of contours generated by all such permutations. For a bond c and a point x in B(c_-), let [x,x'] denote a contour which is obtained by a parallel transport of c to the point x."
- CA-I L808-840 (`1.5:eq-block-average-1`): S_c = {U : |U(dp) - 1| < omega_M(L) for all p in P_c}, P_c the plaquettes in the double block of c; M(U)(c) is "(a) For U in S_c ... Balaban's symmetrised average [(0.11)-(0.12)]{B-CMP109}, built on the inner group mean [(0.10)]{B-CMP109}. Every logarithm in it is the intrinsic logarithm of G. (b) For U not in S_c, ... the double-contour average of intrinsic logarithms [(0.4)]{B-CMP109} ... On the remaining set, which is null for Haar measure, M(U)(c) is the parallel transport of U along the straight path joining the endpoints of c. (c) ... M(U)(-c) := M(U)(c)^{-1}." CA-I L800: "The map M ... is defined bond by bond".

**Identity of the definitions. PROVED (by comparison of the quoted texts).** With odd L, B(y) = {x : |x - y|_inf <= (L-1)/2} in level-k units, which is SA L7946. G(y,x) is the set of coordinate-monotone paths, one per order of the nonzero coordinate displacements: SA L7956-7958 ("the shortest paths which complete one coordinate displacement before starting the next", at most 4! = 24). [x,x'] is the straight segment of length L parallel to c: SA's [x,x']. (0.10) = (QC1), (0.11) = (QC2), (0.12) = (QC3) (Step 2b). So on S_c the account's M(.)(c) is the outline's one-step map, formula for formula.

**Lemma LR applies to the account's M. PROVED.** Take X = bonds of T^(k), Y = positive bonds of T^(k+1), H = L Z^4 in level-k units, u_0 = 1, O = {U : sup_b |U(b) - 1| < r}.
- (O in branch (a)). A plaquette variable is a product of four bond variables; with |.| the normalized Hilbert-Schmidt norm (tr 1 = 1) and unitary factors, |U_1 U_2 U_3 U_4 - 1| <= sum_i |U_i - 1| < 4r. So for r <= omega_M(L)/4 every plaquette is within omega_M(L) of 1, U lies in S_c for every c, and on O the rule is branch (a) at every c. (For complexified configurations near 1 the same bound holds up to a factor (1 + r)^3; take r smaller.)
- (L) The patch P(c) is the bond set of the double block D_c = B(c_-) u B(c_+): a contour in G(y,x) runs inside the coordinate box spanned by y and x, which is inside the cube B(y); the segment [x, x + L e_mu] with x in B(c_-) has its sites in B(c_-) u B(c_+), since the two cubes are adjacent along e_mu; the straight path c is [y, y + L e_mu]. So M(U)(c) depends on U on bonds of D_c only.
- (E) Each ingredient is defined by relative positions (cube about the centre, path family by x - y, segment by c - c_-), so M(tau_v U)(tau_v c) = M(U)(c) for v in L Z^4.
- Differentiability and the derivative at 1: row 990 Step 4 ("Application to the one-step plain map"): the inner mean (0.10) is the implicit solution of an analytic system with invertible derivative at 1, analytic near 1, with derivative the arithmetic mean ((0.8)); the derivative of M at 1 is the stencil K_I of (QC15).
Hence the conclusions (a)-(d) of Lemma LR hold for the account's M and its k-fold composite on every admissible torus (period larger than the double block: SA L7953, period > 4L + 4). This closes row 990's Step 6b: **(I-loc) for the account's own block map, at and near U = 1: PROVED** (it was ARGUED there). Branch (b) and the null-set branch are not used on O.

What this does not touch: the account's map away from 1 (not needed at P_0); Euclidean covariance beyond translations (not needed by (I-loc)).

### Step 5a. (ID-b): the two forms at U = 1, and the variational identity (06:45Z)

**The two sides.**
- *Balaban.* CMP 109 (1.5) at U = 1: the current J = D^* xi^{-2} pi Im dU (CMP 109 (1.8)) vanishes, so <B', Delta^(k)(1) B'> = <H_1 B', Delta_1 H_1 B'> + G^(2)(B'), with B' the level-k fluctuation (V = e^{iB'} V^(k), CMP 109 p. 265), H_1 = H_{1,k} the linear part of the background (fine field in Landau gauge) as a function of B', Delta_1 the operator of Sect. D of [13] = CMP 99 (1985) 389-434, and G^(2)(B') = sum_{y in T^(k+1)} sum_{x in B(y), x != y} |Btilde'(y,x)|^2 (CMP 109 (2.5); Btilde'(y,x) is the linear part of the averaged contour variable of B' from y to x inside the level-(k+1) block). Then C parametrizes the non-pivot variables of the kernel of the linearized one-step constraint (CMP 109 p. 268). (Note: in CMP 109, [13] = CMP 99 pp. 389-434, "Propagators for lattice gauge theories in a background field"; [15] = CMP 102 pp. 277-309, "The variational problem and background fields"; (174) and (41) are [15]'s.)
- *SA (1c.1)*, outline L10208 (quote): "At the pair (U_{k+1}, J(U_{k+1})) of the step, one has A = C^T Delta^(k) C. In this identification (1c.1), the elimination and the gauge-fixing term are obtained directly from the definitions. The only step of substance is the quadratic term of the action of the background, regarded as a function of its datum. This is Balaban's expansion 102, 277, (174), together with 109, (2.4)-(2.8), (2.11). There the derivation is carried out on the whole lattice, using Balaban's own rows and his averages. For M and the straightened rows ... the expansion is obtained from the system with a multiplier of (1b)." Classification (rule 9): **sketched**.
- *pr-lay (7) at P_0* (Step 1): A(P_0) = C_V^T [ iota^T {(Q G_0 Q^T)^{-1} - a} iota + K_GF ] C_V, G_0 = (Delta^W + D R D^T + Q^T a Q)^{-1}. At P_0 the J-terms vanish and G_1 = G = G_0.

So (ID-b) at U = 1 splits into three comparisons: (b1) background-action Hessian: (Q G_0 Q^T)^{-1} - a versus H_1^T Delta_1 H_1; (b2) gauge-fixing Hessian: K_GF versus G^(2); (b3) elimination: C_V versus C, and the coordinates (datum) in which each form is written.

**Lemma V (variational form of the Schur complement). PROVED.** Let M >= 0 be a real symmetric operator on a finite-dimensional space X, Q: X -> Y surjective, a > 0 symmetric on Y, and N = M + Q^T a Q > 0. Then for every B in Y,
  <B, [(Q N^{-1} Q^T)^{-1} - a] B> = min { <A, M A> : Q A = B }.
*Proof.* Q N^{-1} Q^T > 0 since Q^T is injective and N^{-1} > 0. Minimize <A, N A> on the affine space QA = B: the Lagrange condition N A = Q^T nu with Q A = B gives nu = (Q N^{-1} Q^T)^{-1} B and minimum value <B, (Q N^{-1} Q^T)^{-1} B> (strict convexity, N > 0). On QA = B, <A, N A> = <A, M A> + <B, a B>. Subtract. QED. (No invertibility of M needed.)

Applied with M = Delta^W + D R D^T (at U = 1, on a torus at P_0; N = G_0^{-1} > 0 by pr-lay W): pr-lay's row form is B -> min{ <A, (Delta^W + D R D^T) A> : Q A = B }.

**Lemma R (R is the orthogonal projector onto ker(Q' G')). PROVED.** P := G' Q'^T (Q' G'^2 Q'^T)^{-1} Q' G' is symmetric (G' symmetric) and P^2 = P (direct multiplication), so R = I - P is the orthogonal projector onto (ran G'Q'^T)^perp = ker(Q'G'). Hence D R D^T >= 0.

**Lemma GS (the gauge term drops out of the row form). PROVED given (QD) below.** Assume (QD): Q D = Dbar Q' at U = 1 (Dbar the level-k difference). Then min{<A,(Delta^W + D R D^T)A> : QA = B} = min{<A, Delta^W A> : QA = B}.
*Proof.* ">=" since D R D^T >= 0. "<=": let A attain the right side (Delta^W >= 0 and the constraint set is affine, so a minimizer exists on the finite-dimensional space: the quadratic form is bounded below and attains its infimum on an affine subspace). Put nu = (Q' G'^2 Q'^T)^{-1} Q' G' D^T A and lambda = G'^2 Q'^T nu - G' D^T A. Then Q' lambda = Q'G'^2Q'^T nu - Q'G'D^TA = 0. With G'^{-1} = D^T D + Q'^T a Q' and Q' lambda = 0, D^T D lambda = G'^{-1} lambda = G' Q'^T nu - D^T A, so D^T(A + D lambda) = G' Q'^T nu is in ran(G'Q'^T) and R D^T (A + D lambda) = 0. By (QD), Q(A + D lambda) = B + Dbar Q' lambda = B. Delta^W D = 0 (the Wilson Hessian at 1 is d^T d, and d D = 0), so <A + D lambda, Delta^W (A + D lambda)> = <A, Delta^W A>. So A + D lambda is admissible on the left with the same value. QED.
(Q'G'^2Q'^T is invertible because G' > 0 and Q' is surjective; pr-lay W gives G'.)

**(QD) at U = 1.** SA L10139 states QD = Dbar Q' for the straightened rows (and that it fails for the plain averages). One-step check at 1 (from row 990's (QC15)): the plain linear part K satisfies K D lambda(c) = lambda(y') - lambda(y) (row 990 Step 3); the straightened row is Q^st = K + Dbar s with s the linear part of the site factor, s(a)(y) = L^{-4} sum_{x in B(y)} abar(y,x) up to SA's sign convention, and for a = D lambda, abar(y,x) = lambda(x) - lambda(y); so Q^st D lambda = Dbar(lambda(y) + mean_{B(y)} lambda - lambda(y)) = Dbar(Q' lambda) with Q' the block mean (PX31 at T = 1). The sign of s is SA's; with the other sign, Q^st D lambda = Dbar(2 lambda(y) - mean lambda), not of the form Dbar Q' with a positive average, so SA's construction fixes the sign as used. ARGUED (one step, sign taken from SA's statement); by composition of one-step linear parts it holds for k steps with Q' the k-fold mean.

**Lemma PS (plain and straightened data give the same background form). PROVED.** Let K be the plain k-fold linear average at 1 and Q = K + Dbar s (s linear, from fine fields to level-k sites). Let f_p(B) = min{<A, Delta^W A> : K A = B}, f_s(B) = min{<A, Delta^W A> : Q A = B}. If for every level-k site function mu there is lambda with K D lambda = Dbar mu and with Q D lambda = Dbar mu, then f_p = f_s.
*Proof.* Both f are invariant under B -> B + Dbar mu (shift A by D lambda; Delta^W D = 0). Given A with QA = B: KA = B - Dbar s(A), so f_p(B) = f_p(B - Dbar s(A)) <= <A, Delta^W A>; minimize: f_p <= f_s. Symmetrically f_s <= f_p. QED. The hypothesis holds: for K take lambda with lambda = mu at the block centres (K D lambda = Dbar(lambda at centres), row 990); for Q take lambda = the k-fold "constant on blocks" extension of mu (Q' of it is mu).

**What Step 5a gives.** At U = 1, pr-lay's row form (Q G_0 Q^T)^{-1} - a equals f(B) := min{<A, Delta^W A> : (plain or straightened) k-fold linear average of A = B}, the quadratic part of the background action as a function of its datum, in either chart. Comparison (b1) thus reduces to: Balaban's <H_1 B', Delta_1 H_1 B'> at 1 equals f(B'). That needs H_1 and Delta_1 from CMP 99/102 (Step 5b).

### Step 5b. (b1): Balaban's background form at U = 1 (07:05Z)

Source: CMP 102 (1985) 277-309 (= [15] of CMP 109), pp. 289-294, read as images (pp. 293-294) and OCR (pp. 289-292, checked where used).

**Quotes.**
- (74)-(79), pp. 289-290: the functional F(A') = A(U_0) + <A' - HD(A'), J> + (1/2)<A' - HD(A'), Delta_A (A' - HD(A'))> + V_0(...) on configurations with L^j eta Q_j A' = B on Lambda_j and "RD^*(A' - HD(A')) = RD^* A' = 0" (75)-(76). (79): "a quadratic form in the expansion of F(A') is equal to (1/2)<A', Delta_A A'> - <H C^(2)(A'), J> = (1/2)<A', Delta_1 A'>, where we have used again the fact that A' satisfy the Landau gauge condition RD^* A' = 0."
- p. 293: "We take the operators H_1, P defined by the operator Delta_1. Let us recall that P is an orthogonal projection in a space of configurations A' with a scalar product defined by the operator Delta_1 + D^*RD + aQ^*Q, onto a subspace of A' satisfying the conditions QA' = 0, RD^*A' = 0. We make the translation A' = A_1 + H_1 B. Using the identity <dA', Delta_1 H_1 B> = 0 following from the definitions of H_1 ..." with (100) "Q dA' = 0 (i.e. Q_j dA' = 0 on Lambda_j), RD^* dA' = 0" and (102) "Q A_1 = 0, RD^* A_1 = 0".
- p. 294: "We denote by G_1 an inverse operator to the operator Delta_1 + DRD^* + aQ^*Q."
- p. 291 (87): (Delta_A + DRD^*) H D(A') = (G^{-1} - Q^* a Q) G Q^*(QGQ^*)^{-1} (L^j eta)^{-1} D(A'), i.e. H = G Q^*(QGQ^*)^{-1} (times the scale factor) with G = (Delta_A + DRD^* + aQ^*Q)^{-1}; "the symbol a above represents the operator of multiplication by (L^j eta)^{-2} (we put the constant a = 1)".
- CMP 102 (174), p. 305: A = A_1 + H_1 B - H D(A_1 + H_1 B), with A_1 solving (175); (177): "the expansion of A begins with the first order term H_1 B".

**Reading (ARGUED from the quotes; the formula for H_1 is the Delta_1-analogue of (87)'s H, which p. 293 states as "defined by the operator Delta_1").** H_1 = G_1 Q^*(Q G_1 Q^*)^{-1} with G_1 = (Delta_1 + DRD^* + Q^* a Q)^{-1}; H_1 B satisfies Q H_1 B = B and RD^* H_1 B = 0. At U_0 = 1 the current J = D^* xi^{-2} pi Im dU_0 (CMP 109 (1.8)) is 0, so by (79) Delta_1 = Delta_A at 1, the Hessian of the Wilson action at 1, which is Delta^W = d^T d (gauge invariant: Delta^W D = 0).

**Lemma B1 (Balaban's background form at U = 1 is the row form). PROVED given the reading.** With N := G_1^{-1} = Delta^W + DRD^* + Q^* a Q, nu := (Q N^{-1} Q^*)^{-1} B and H_1 B = N^{-1} Q^* nu:
  <H_1 B, Delta_1 H_1 B> = <B, [(Q G_1 Q^*)^{-1} - a] B> - |R D^* H_1 B|^2.
*Proof.* <H_1 B, N H_1 B> = <N^{-1}Q^*nu, Q^*nu> = <nu, Q N^{-1} Q^* nu> = <B, (QG_1Q^*)^{-1} B>. <H_1B, Q^*aQ H_1B> = <B, aB> since Q H_1 B = B. <H_1 B, DRD^* H_1 B> = |R D^* H_1 B|^2 since R is an orthogonal projector (R^2 = R = R^*; Lemma R for pr-lay's R; for Balaban's R the projector property is his, CMP 99 pp. 389-434, not re-read here). Subtract. QED.
With Balaban's Landau condition R D^* H_1 B = 0 (CMP 102 (75), (102)), Balaban's <H_1 B, Delta_1 H_1 B> at 1 equals (QG_1Q^*)^{-1} - a, which by Lemma V is min{<A, (Delta^W + DRD^*) A> : QA = B}, and by Lemma GS (given (QD) for Balaban's pair Q, Q') equals f_p(B) = min{<A, Delta^W A> : QA = B}.

**This is SA's own remark.** Outline L10208: "Balaban also gives a second expression for the first two terms of Delta_k, namely H_1^T[G_1^{-1} - DRD^T - Q^T a Q] H_1. It differs from them by -H_1^T DRD^T H_1, a term that vanishes on shell." Lemma B1 is that sentence with its proof; "on shell" is R D^* H_1 = 0.

**Consequence for (b1). PROVED given the reading of H_1, Delta_1 and (QD) for both charts.** At U = 1, Balaban's <H_1 B', Delta_1 H_1 B'> = f_p(B') (Lemma B1 + V + GS in Balaban's chart) and pr-lay's (QG_0Q^T)^{-1} - a = f_s(B) (Lemma V + GS in the straightened chart, with (QD) from SA L10139), and f_p = f_s as functions on level-k bond variables (Lemma PS). With iota = identity at P_0 (single layer: every row is a level-k bond, Step 1), the background parts of the two forms are the same quadratic form on the level-k bond variables.

Open inside (b1): Balaban's R and Q' (his CMP 99 pp. 389-434, Sect. D, (3.127)-(3.128), (3.156)), to confirm R is an orthogonal projector of Lemma R's type and that his plain Q satisfies Q D lambda = Dbar(lambda at centres) with the residual gauge group {lambda = 0 at centres} (CMP 109 (0.21): "gauge transformations u defined on T and satisfying the condition u = 1 on T^(k)"). Lemma GS needs only: R D^* is a projection onto the complement of a gauge slice reachable by gauge moves preserving Q A. The (0.21) quote gives the residual group; the projector property is not re-read here. Mark for that sub-step: ARGUED.

### Step 5c. (b2) gauge term, (b3) elimination, and the (ID-b) assembly (07:25Z)

**Quotes (SA outline at c7fef8b = 31a47c543775, hash d7f77d4d...; credit Sussman and Alpoge, with Claude and Codex as authors of their text).**
- L7180-7183: G_k(V; P'') = prod_{y in P''} prod_{x in B(y) minus y} z_G^{-1} 1{|V(y,x) - 1| < eps_k} e^{-x_k(1 - (1/2) Re tr V(y,x))}, GF_k(V) = sum_{y,x}[1 - (1/2) Re tr V(y,x)] >= 0.
- L6854: "a sequence of running inverse couplings x_0 = beta, x_k = x_{k-1} - b_k", beta = g_0^{-2}.
- L7188: "G' = (Delta_{U_0} + Q'^* a Q')^{-1}, and R is the orthogonal projection onto Delta_{U_0} N(Q')."
- L10200-10206: "Let C_V be the elimination of the pivot bonds, and let G^(2)_V be the quadratic part of the soft axial gauge fixing. Let E^(2) be the quadratic part of the one-step constraint, which is imposed through the plain M at V and whose linear part is the Q_V ... Delta_k = (Q G_1 Q^T)^{-1} - a - E^(2)[H_1^T J], A = C_V^T (G^(2)_V + Delta_k) C_V." pr-lay (7) is this display with iota explicit (pr-lay L82: "This is SA 10200-10208 and 14091-14107").

**(b2) Gauge term. PROVED (comparison of definitions).** Balaban's gauge function is (1/g_k^2) sum_{y in T^(k+1)} sum_{x in B(y), x != y} [1 - Re tr V(y,x)] with tr 1 = 1 (CMP 109 (0.19), p. 255; (2.5)). SA's is x_k sum_{y,x}[1 - (1/2) Re tr V(y,x)] with the matrix trace (tr 1 = 2 for SU(2)), x_k the running inverse coupling (L6854), so the same function of V for SU(2) at a common coupling (x_k = g_k^{-2}). The contour variables V(y,x) are the same ((0.11) = (QC2), Step 4). The Hessian at V = 1 in the chart V = e^{iB} is therefore the same quadratic form: Balaban's G^(2) (CMP 109 (2.5): G(B') = (1/2) G^(2)(B') + G_3(B')) equals SA's G^(2)_V = pr-lay's K_GF at V = 1. One check of the normalization: for X in su(2) with tr 1 = 1, 1 - Re tr e^{iX} = (1/2) tr X^2 + O(X^4), and with the matrix trace 1 - (1/2) Re tr e^{iX} = (1/4) Tr X^2 = (1/2) tr X^2: equal.

**(b3) Elimination. PROVED.** Let F(V) = M(V) W^{-1} be the one-step constraint at the level-k field V near 1 (W = M(1) = 1 at U = 1), in the chart V = e^{iB}. Both C (Balaban: "using delta(Qtilde B') we eliminate the variables B'(b_0(c)) ... B' = CB", CMP 109 p. 268; with his nonlinear change B' = B - h Dtilde(B), Dtilde of second order) and C_V (SA: "the elimination of the pivot bonds"; pr-lay: "the derivative of the actual pivot graph") are the derivative at 0 of a parametrization psi of the fibre {F = 1} by the non-pivot variables, with the pivot variables as the dependent ones. By Step 3 (a), the pivot block of DF(1) is the diagonal K_c(1) = L^{-3} I_3, invertible; so by the implicit function theorem the fibre is locally a graph over the non-pivot variables, and every such parametrization has derivative C = (I_np, -K_p^{-1} K_np) at 0 (K = DF(1) = (QC15) split into non-pivot and pivot columns). Unique. Hence C = C_V at U = 1.
Second-order terms: for Phi = background action + gauge function, Hess(Phi o psi)(0) = C^T Hess Phi(1) C + DPhi(1)[D^2 psi(0)]. At U = 1, DPhi(1) = 0 (the action and the gauge function are minimal at 1), so the second term vanishes. This is SA's term -E^(2)[H_1^T J] (L10208: "Paired with the gradient, this term yields -E^(2)[H_1^T J]"), which vanishes at J = 0. Balaban's Tr log(I - h ...) and h Dtilde terms (CMP 109 (2.12)) are of higher order in B and do not enter the quadratic form.

**(b1) Background.** Step 5b: Balaban's H_1^T Delta_1 H_1 at 1 = f_p, and pr-lay's (Q G_0 Q^T)^{-1} - a = f_s = f_p (Lemmas V, GS, PS, B1). By Lemma V the value is independent of the row weight a > 0, so Balaban's a ((L^j eta)^{-2}, "we put the constant a = 1", CMP 102 p. 291) and pr-lay's a (xi^{-2} = 1 at P_0) need not be matched.

**Assembly: (ID-b) at U = 1.** C^* Delta^(k)(1) C = C^T [H_1^T Delta_1 H_1 + G^(2)] C (CMP 109 (1.5) at J = 0) = C_V^T [ {(Q G_0 Q^T)^{-1} - a} + K_GF ] C_V = pr-lay (7) at P_0 (with iota = identity, E_amb[0] = 0).
Mark: **PROVED given four read-offs, two of which are ARGUED**:
- (r1) Delta_1(1) = Delta^W and J(1) = 0 (CMP 102 (79), CMP 109 (1.8)): read, PROVED.
- (r2) H_1 = G_1 Q^*(Q G_1 Q^*)^{-1} with Landau condition R D^* H_1 = 0 (CMP 102 pp. 291-294, (75), (102)): ARGUED (the formula is the Delta_1-analogue of (87)'s H, "defined by the operator Delta_1").
- (r3) Balaban's R is the orthogonal projection onto Delta N with N = {lambda : lambda = 0 on T^(k)}, needed for Lemma GS in Balaban's chart: to be read in CMP 99 pp. 389-434 (Step 5d). SA's R is this projection by L7188 with N = N(Q').
- (r4) The overall scale of the two forms: Balaban rescales B' = g_k B, so his form carries coefficient 1 on <B, Delta^(k) B>/2; SA's A is written in the same normalization (L10208 asserts A = C^T Delta^(k) C with no factor). pr-lay's "matched physical bilinear pairings" are SA's. ARGUED. A mismatch would be one positive scalar c(L, eta, g_k) multiplying the whole form; it would change log det by (N/2) log c, a per-coordinate torus-free number, so (DET) would not be affected.

### Step 5d. Balaban's R and Q'; a shorter route for Balaban's side of (b1) (07:45Z)

**CMP 99 (1985) 389-434 (= [13] of CMP 109), p. 394 (OCR L240-275, the formulas used are legible):** "(Q'(U)lambda)(y) = sum_{x in B^j(y)} L^{-dj} R(U(Gamma_{y,x})) lambda(x) (3.19) ... The above averaging operators Q'_j(U) are linear parts of the averaging operations R_u^j for gauge transformations u = e^{i lambda}"; "R = R(U) is an orthogonal projection in the Hilbert space L^2(Omega_0, g) onto the subspace R = Delta_U N(Q'), N(Q') = {lambda : Q' lambda = 0} (3.21)"; (3.114), OCR L1673: "(Q D_U lambda)(c) = (Q'lambda)(c_+) - (Q'lambda)(c_-) = (Dbar Q' lambda)(c)". So in Balaban's propagator paper R has exactly Lemma R's form and (QD) holds with the block mean Q'. This settles (r3) for that paper's averages. SA's R (L7188) is the same object.

**Caveat found.** CMP 109's average (0.12), linearized at 1, satisfies Q D lambda = Dbar(lambda at the block centres), not Dbar(block mean of lambda): direct computation from (0.12) (or row 990's (QC15)): for a = D lambda, abar(y,x) = lambda(x) - lambda(y) and the sum telescopes to lambda(y') - lambda(y). Its residual group is CMP 109 (0.21)'s "u = 1 on T^(k)". So for the CMP 109 average the matching Q' is point evaluation at centres, and SA L10139 says the same ("For the plain averages, the identity QD = Dbar Q' fails" with the block mean). CMP 109 p. 254 says the results of [12] "are valid for it. The proofs are in most cases unchanged; in others only minor and obvious modifications are needed". Which Q' CMP 109's R uses is not printed in CMP 109. This does not affect (ID-b), by the route below.

**Lemma MIN (Balaban's background form at 1 is the Hessian of the constrained minimum). PROVED, given CMP 109 (0.21) and (2.6)-(2.8).** Let m(B') = A(U_k(e^{iB'})) at U_{k+1} = 1 (so V^(k) = 1), where U_k(V) is a minimizer of the Wilson action A on {U : M^k(U) = V} (CMP 109 (0.21): "the minima of the functional U -> A''(U) on U : Ubar^k = M^k(U) = V"). Let K be the linear part of M^k at 1 and f_p(B) = min{<A, Delta^W A> : K A = B}. Then the quadratic part of m at 0 is (1/2) f_p.
*Proof.* Write A(e^{iA}) = (1/2)<A, Delta^W A> + O(|A|^3) near A = 0 (the Wilson action is analytic, minimal and 0 at 1; Delta^W its Hessian). M^k(e^{iA}) = e^{i(KA + O(|A|^2))} (analytic, Lemma LR setting).
Upper bound: fix B' and A with K A = B'. K is surjective (it has the pivot block L^{-3} I per coarse bond at one step, Step 3 (d), and composition of surjections), so by the implicit function theorem there is A_t = tA + O(t^2) with M^k(e^{iA_t}) = e^{itB'} exactly. Then m(tB') <= A(e^{iA_t}) = (t^2/2)<A, Delta^W A> + O(t^3). Minimize over A: m(tB') <= (t^2/2) f_p(B') + O(t^3).
Lower bound: the minimizer U_k(e^{itB'}) can be written e^{iA_t} with |A_t| <= C t: in Landau gauge A_t = A_1 + H_1(tB') - HD(A_1 + H_1(tB')) (CMP 102 (174)) is analytic in t and 0 at t = 0, since A_1 is an analytic function of H_1 B beginning at second order (CMP 102 pp. 305-306, (176)-(177)); gauge choice does not change the action. The constraint gives K A_t = tB' + O(t^2). So m(tB') = (1/2)<A_t, Delta^W A_t> + O(t^3) >= (1/2) f_p(K A_t) + O(t^3) = (t^2/2) f_p(B') + O(t^3), using that f_p is a quadratic form (continuous, and f_p(tB' + O(t^2)) = t^2 f_p(B') + O(t^3)). QED.
CMP 109 (2.6)-(2.8) at J = 0 say m(B') = (1/2)<H_1 B', Delta_1 H_1 B'> + V(H_1 B') with V of third order. Comparing quadratic parts: <H_1 B', Delta_1 H_1 B'> = f_p(B'). This replaces (r2) and (r3): no formula for H_1 and no property of Balaban's R is needed. What remains used from Balaban: (0.21) (U_k(V) is a constrained minimizer), the O(t) bound, and the statement (2.8).

**pr-lay's side** still uses Lemma GS in the straightened chart: R the orthogonal projection onto Delta N(Q') (SA L7188; pr-lay's R formula is this projection by Lemma R, since ker(Q'G') = G'^{-1} N(Q') = Delta N(Q')), and (QD) for the straightened rows with the block mean Q' (SA L10139 implies it by contrast with the plain average; one-step check in Step 5a, sign from SA's construction): ARGUED for (QD), PROVED otherwise.

**(ID-b) final.** C^* Delta^(k)(1) C = pr-lay (7) at P_0: background parts equal (Lemma MIN; Lemmas V, GS, PS), gauge parts equal (b2), eliminations equal and second-order fibre terms zero (b3). **PROVED, conditional on two ARGUED inputs**: (QD) for SA's straightened rows at 1 (sign), and (r4) the common overall normalization of SA's display L10200-10206 and Balaban's (2.11) (any mismatch is one positive scalar and is harmless for (DET)).

### Step 5e. (QD) for the straightened rows at 1, settled (07:55Z)

**Lemma QD. PROVED on SA's definitions as quoted (row 990 Step 3: SA L9634).** At U_0 = 1 the straightened row Q^st and the block mean Q' satisfy Q^st D lambda = Dbar Q' lambda, at one step and at k steps.
*One step.* SA's chart: M(e^{iA})(c) = v(c_-) e^{i Q^st(A)(c)} v(c_+)^{-1}, with v(y) "the mean over a block of the change in the contour variables", i.e. v(y) = mean_{x in B(y)} [U(y,x) U_0(y,x)^{-1}], linear part s(y) = L^{-4} sum_{x in B(y)} abar(y,x). Linear parts: K A(c) = s(y) + Q^st A(c) - s(y'), so Q^st A = K A + Dbar s (Dbar s(c) = s(y') - s(y)). For A = D lambda (with (D lambda)(b) = lambda(b_+) - lambda(b_-), the convention in which row 990 found K D lambda(c) = lambda(y') - lambda(y)): abar(y,x) = lambda(x) - lambda(y), s(y) = (mean_{B(y)} lambda) - lambda(y), and Q^st D lambda(c) = [lambda(y') - lambda(y)] + [mean_{B(y')} lambda - lambda(y')] - [mean_{B(y)} lambda - lambda(y)] = mean_{B(y')} lambda - mean_{B(y)} lambda = Dbar(Q' lambda)(c).
*Consistency check on the sign of v.* Under a gauge transformation u, U(y,x) -> u(y) U(y,x) u(x)^{-1}; at U = 1 the block mean of the contour variables becomes u(y) mean_x u(x)^{-1}, so v -> u(y) ubar(y)^{-1} v with ubar the block mean, and M(U^u)(c) = u(y) M(U)(c) u(y')^{-1} forces e^{iQ^st} -> ubar(y) e^{iQ^st} ubar(y')^{-1}: covariance under the block mean, which is the linear statement above. With the inverse reading of "change" the straightened row would be covariant under u(y)^2 ubar(y)^{-1}, which is not an average; so the reading used is the one SA's text describes.
*k steps.* SA L10212: Q^st_k = eta Q(W_{k-1}) ... Q(W_0), a composite of one-step linear parts; at 1 each satisfies Q_1 D = Dbar Q'_1, so the composite satisfies it with Q'_k = (Q'_1)^k, which for nested centred odd blocks is the mean over B^k(y) (a mean of L^4 means of L^4 values each). QED.

So the (QD) input of Step 5d is PROVED on SA's definitions; (ID-b) now rests only on (r4) (overall normalization), ARGUED.

### Step 7. Verdicts (08:00Z)

| Item | Mark | Where |
|---|---|---|
| (3.33) of CMP 119, exact: sum_c log z^(k)(c) - (1/2) log det(C^* Delta^(k) C) + log int dA e^{-|A|^2/2} | read from PDF | Step 2a |
| z^(k)(c) is defined nowhere by formula; CMP 119 sends the elimination to CMP 109 Sect. 2 | read | Step 2a |
| Lemma C: the constants of CMP 119 (3.15) (d(g) log g_k, log sigma_0 per bond; -log z per non-centre block site) and of (3.33) ((1/2) log 2 pi per coordinate) are torus-free numbers times counts proportional to n^4 | PROVED | Step 2c |
| Lemma ZB (a): the delta elimination is diagonal in the pivots, z^(k)(c) = abs det_g K_c(V^(k))^{-1} | PROVED | Step 3 |
| Lemma ZB (b): this is the z^(k)(c) of CMP 119 (3.33) | ARGUED (no printed formula) | Step 3 |
| (ID-a'): log z^(k)(c) is a local, translation-covariant rule of the background on the double block of c | PROVED on (a) | Step 3 |
| z^(k)(c) at U = 1 equals L^9 for every cell on every torus (matches SA's L^9 and RF61's 36 log L per coarse site) | PROVED | Step 3 |
| (ID-a): z^(k)(c) and the measure constants are torus-free per cell/bond at U = 1 | PROVED (identification (b) ARGUED) | Step 3 |
| E_0^(j), reading (i) (the constants of the prefactor, as CA-I (n2) and CMP 119 p. 273 say): the same additive set function on both tori | PROVED | Step 3 |
| E_0^(j), reading (ii) (Balaban's full vacuum counterterm E^(j)(Lambda_j, 1), CMP 119 (2.25)-(2.27)): exactly the same on both tori | FAILS at CMP 119 (2.27): the sum over X subset Lambda_j depends on the torus through wrapping domains; hand example: log det(-Delta + m^2)/n on Z_1 vs Z_2. Differences are O(e^{-kappa' n}) per site (ARGUED from (iv)); (DET) needs only a bound | Step 3 |
| The account uses reading (i) | ARGUED (CA-I L104010-104013, L106147-106150) | Step 3 |
| Item (2): CMP 109 (0.3), G(y,x), (0.10)-(0.12) are SA's (QC1)-(QC3) formula for formula; the account's M is a bond-by-bond local covariant rule near 1; Lemma LR applies; row 990 Step 6b closed | PROVED | Step 4 |
| Lemma V (Schur complement = constrained minimum; independent of a) | PROVED | Step 5a |
| Lemma R (pr-lay's R = orthogonal projection onto Delta N(Q') = SA L7188's R) | PROVED | Steps 5a, 5d |
| Lemma GS (the DRD^T term drops out of the row form, given QD) | PROVED | Step 5a |
| Lemma PS (plain and straightened charts give the same background form) | PROVED | Step 5a |
| Lemma QD (straightened rows satisfy QD = Dbar Q' at 1, k steps) | PROVED on SA's definitions | Step 5e |
| Lemma MIN (Balaban's H_1^T Delta_1 H_1 at 1 = Hessian of the constrained minimum = f_p) | PROVED given CMP 109 (0.21), (2.6)-(2.8), CMP 102 (174)-(177) | Step 5d |
| Lemma B1 (Balaban's second expression; SA's "vanishes on shell" remark) | PROVED as identity; not needed after MIN | Step 5b |
| (b2) gauge term: Balaban's G^(2) = SA's G^(2)_V = pr-lay's K_GF at 1 (same function, x_k = g_k^{-2}, trace normalizations checked) | PROVED | Step 5c |
| (b3) elimination: C = C_V at 1 (unique derivative of the pivot graph); second-order fibre term 0 at J = 0 | PROVED | Step 5c |
| (ID-b): Balaban's C^* Delta^(k) C at U = 1 equals pr-lay (7) at P_0 | PROVED up to (r4), the common overall normalization of SA L10200-10206 and CMP 109 (2.11): ARGUED; a mismatch is one positive scalar and leaves (DET) unchanged | Steps 5a-5e |
| CMP 109's plain average has Q' = point evaluation at centres, not the block mean of CMP 99 (3.19); harmless for (ID-b) by Lemma MIN | caveat, PROVED | Step 5d |

**Credits.** T. Balaban, CMP 102 (1985) 277-309, CMP 99 (1985) 389-434, CMP 109 (1987) 249-301, CMP 119 (1988) 243-285: definitions, the step integral and the delta elimination, read from the PDFs on this machine (not committed). Sussman and Alpoge's outline and complete account (with Claude and Codex as authors of their text), commit c7fef8b = 31a47c543775 (outline SHA-256 d7f77d4d...): QC1-QC4, the chart L9634, the soft gauge L7180-7188, the display L10200-10208. Rows 987, 989, 990 of this repository: Lemmas A, P, LR, Z, Z', the (QC15)-(QC16) hand checks.

**What is left (for the lead).** (1) The other-provider line-by-line check of this note (gpt-6-astra). (2) (r4): one sentence from Sussman and Alpoge, or a reading of SA L14091-14107, on the normalization of A relative to Balaban's (2.11). (3) The identification of z^(k)(c) with Lemma ZB's Jacobian rests on CMP 119's sentence, not a printed formula; any normalization variant is covered by Lemma C. (4) Nothing here touches pr-lay W (existence of the inverses) or the top weight of row 990 (iii).

RESULT: Row 993 (Claude Opus 5.5 high, Mac mini worker 3; checked by no one; no numeric run). (ID-a') PROVED: Balaban's delta elimination (CMP 109 p. 268, CMP 119 p. 267) is diagonal in the pivots, so z^(k)(c) = abs det K_c(V^(k))^{-1} is a local covariant rule on the double block of c, and z^(k)(c) = L^9 at U = 1 on every torus. The identification with CMP 119 (3.33)'s unprinted z^(k)(c) is ARGUED. The constants of (3.15) and (3.33) are torus-free numbers per bond, site or coordinate (Lemma C, PROVED). So (ID-a) is PROVED with that identification ARGUED. E_0^(j) is the same additive set function on both tori under the account's reading, the prefactor constants (PROVED). Exact equality FAILS for Balaban's full vacuum counterterm (CMP 119 (2.27), wrapping domains), but (DET) needs only a bound. Item (2) PROVED: CMP 109 (0.3), G(y,x) and (0.10)-(0.12) are SA's (QC1)-(QC3), so the account's block map is a bond-by-bond local covariant rule and Lemma LR closes row 990 Step 6b. (ID-b) PROVED up to one ARGUED normalization (r4). At U = 1, C^* Delta^(k) C equals pr-lay (7) at P_0: the background parts agree (Lemmas V, GS, PS, QD, MIN), the gauge terms are the same function, and the eliminations have the same derivative with no fibre term at J = 0. Open: the other-provider check, (r4), and pr-lay W.
