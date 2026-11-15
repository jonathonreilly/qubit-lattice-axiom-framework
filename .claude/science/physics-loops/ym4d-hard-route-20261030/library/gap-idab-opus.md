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

Steps 1, 2a, 2b done 05:35Z. Next: CMP 109 (1.4) and refs [13]-[16]; locate the per-cell Jacobian z^(k)(c); then Step 3.

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
