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

Steps 1-4 done 06:25Z. Next: Step 5, (ID-b): CMP 109 (1.5), (2.4)-(2.11), Sect. D of [13], CMP 102 (174) vs pr-lay (7) at P_0.

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
