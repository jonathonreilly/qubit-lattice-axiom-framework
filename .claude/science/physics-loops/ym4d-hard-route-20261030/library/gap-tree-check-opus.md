# Check of library/gap-tree-astra.md (FINISH row 805), by Claude Opus 5.5, line by line

Clone: `/Users/jonreilly/ym4d-lead/clone` at commit `974b24a77862404946a0c034285b4e59a8793e70`.
Lane directory D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
Target: `D/library/gap-tree-astra.md`, 650 lines, by Codex gpt-6-astra max (FINISH row 804). I read it in full.
Context read: `D/library/gap-kappa-order.md` 31-74; `D/library/gap-ext-astra.md` 78-128 and 4.2 (474-521);
`D/library/gap-cf-astra.md` Section 4 (428-526); `D/library/gap-kanazawa-astra.md` 605-660 (K25);
`D/library/gap-ac-lat.md` 132-153 for (TU); FINISH rows 802-805.

Method. Every verdict below rests on a hand derivation written here. One small numerical run (GUIDE only,
under 50 MB, file `guide.py` next to this report) built the 120 elements of the binary icosahedral group and
compared a few numbers. It decides nothing. Where I quote it, I mark it GUIDE.

Notation. x = beta/2. Haar measure on SU(2) in the class angle: (2/pi) sin^2(theta) d(theta) on [0, pi],
with (1/2) tr g = cos(theta) and chi_j(theta) = sin((2j+1)theta)/sin(theta).

## 1. Section 3: the two filters, (G5)-(G11), the U(1) control

**(G3) and (G4) inputs.** The ratio bound I_{n+1}/I_n <= beta/(2(n+1)) follows termwise. Write
I_n = sum_k a_k with a_k = x^{2k+n}/(k!(k+n)!). Then (2(n+1)/beta) I_{n+1} = sum_k a_k (n+1)/(k+n+1) <= I_n.
So (G3) holds. (G4): r_1 = (I_3/I_2)(I_2/I_1) <= (beta/6)(beta/4) = beta^2/24. Positivity: I_3 > 0. HOLDS.

**(G5)-(G6).** J_12 and J_23 are isometries since |s| = 1. P and Q are orthogonal projections of rank 2 in
the 8-dimensional H. All of H is centre-odd: -I acts as (-1)^3. HOLDS.

**Schur forms A = P + t(I - P), B = Q + t(I - Q).** k_beta is a class function. So
int k_beta(g) D_j(g) dg commutes with D_j and equals lambda_j I, with lambda_j = (1/d_j) int k_beta chi_j.
By hand: int (2/pi) e^{beta cos theta} sin(theta) sin((2j+1)theta) d theta
= (1/pi) int e^{beta cos theta}[cos(2j theta) - cos((2j+2) theta)] d theta = I_{2j} - I_{2j+2}
= (2(2j+1)/beta) I_{2j+1}. Dividing by z = (2/beta) I_1 gives lambda_j = I_{2j+1}/I_1 = r_j, as in (G3).
On V tensor V = spin 0 + spin 1, g tensor g has eigenvalue 1 on the antisymmetric line s and r_1 = I_3/I_1
on the symmetric spin-1 complement. In positions 1-2, ran P = s tensor V is the spin-0 part. So
A = P + r_1 (I - P). The same holds for B in positions 2-3. HOLDS.

**(G8).** I computed J_12^* (v tensor s). For v = e_+: e_+ tensor s = (|++-> - |+-+>)/sqrt2; contracting the
first two slots with s gives (0 - (1/sqrt2) e_+)/sqrt2 = -e_+/2. For v = e_-: e_- tensor s = (|-+-> - |--+>)/sqrt2;
<s, e_- e_+> = -1/sqrt2 gives -e_-/2. So J_12^* J_23 = -(1/2) I_V. Then
PQP = J_12 (J_12^* J_23)(J_23^* J_12) J_12^* = (1/4) P, and ||PQ||^2 = ||PQP|| = 1/4. The displayed example
vectors and the coefficient product -1/2 are correct. HOLDS.

**(G7).** A - P = t(I - P) has norm t. ||A|| = max(1, t) = 1. The identity AB - PQ = (A - P)B + P(B - Q)
gives ||AB|| <= 1/2 + 2t. With (G4) and 0 < beta <= 1: 1/2 + beta^2/12 <= 7/12. HOLDS.

**Strictness.** If ||int k D_1(g) x dg|| = ||x||, strict convexity of the Hilbert norm forces D_1(g)x to be
constant for k-almost every g. Continuity and full support make it constant on SU(2), hence equal to x.
Spin 1 has no fixed vector. So t < 1. Next, ||Bx||^2 = ||Qx||^2 + t^2 ||(I-Q)x||^2, so ||Bx|| = ||x|| forces
x in ran Q and Bx = x. Then ||Ax|| = ||x|| forces x in ran P. If x lies in both ranges, x = PQPx = x/4, so
x = 0. Compactness of the unit sphere gives ||AB|| < 1. HOLDS.

**(G9).** J_12^* J_r = (2(-1/2) + 1)/sqrt3 = 0. J_r^* J_r = (4 + 2(-1/2) + 2(-1/2) + 1)/3 = 1. So J_r is an
isometry orthogonal to J_12. Inverting, J_23 = (sqrt3 J_r - J_12)/2. Hence Q = J_23 J_23^* has coefficient
vector (-1/2, sqrt3/2) in the basis (J_12, J_r): Q = [[1/4, -sqrt3/4], [-sqrt3/4, 3/4]]. dim M = 4 because
ran P and ran Q meet only in 0. A and B preserve M and M-perp. HOLDS.

**(G10).** A^2 = P + t^2(I - P) = t^2 I + (1 - t^2) P, and likewise B^2. The 2x2 trace gives
tr(A^2 B^2) = 2t^4 + t^2(1 - t^2)(tr P + tr Q) + (1 - t^2)^2 tr PQ = 2t^2 + (1 - t^2)^2/4 = T.
det A = det B = t (eigenvalues 1 and t), so the product is t^4. HOLDS.

**(G11).** M-perp is the spin-3/2 part of V^{tensor 3}, where P = Q = 0 and AB = t^2 I. The larger
singular value on M is at least the geometric mean t, and t >= t^2. So ||AB||^2 is the larger root
(T + sqrt(T^2 - 4t^4))/2. Checks: t = 1 gives 1; t -> 0 gives 1/4, matching ||PQ|| = 1/2. HOLDS.
GUIDE: direct 8x8 norms agree with (G11) to 1e-15 at t = r_1(1), 0.3 and 0.7.

**U(1) control vector.** For g_theta = diag(e^{i theta}, e^{-i theta}), e_+ tensor e_- has pair charge 0, so
both pair averages fix e_+ tensor e_- tensor e_+. Total charge 1, so -I acts by -1. The product has norm 1.
The U(1)-invariant pair space is span(e_+e_-, e_-e_+), of dimension 2; the SU(2) singlet line is the step
that U(1) lacks. HOLDS.

**Verdict, item 1:** HOLDS for every statement.

## 2. Section 4: Lemma 2, the distinguishing filters, (G12)-(G17a)

**Conjugacy classes (1, 15, 20, 12, 12).** The icosahedron has 30 edges, 20 faces, 12 vertices. Edge axes:
15, one half-turn each. Face axes: 10, two rotations by +-2pi/3 each, 20 in all. Vertex axes: 6, four
nontrivial rotations each, 24 in all; 12 have angle +-2pi/5 and 12 have angle +-4pi/5. 1 + 15 + 20 + 24 = 60.
These are the class sizes of A_5. The binary group Gamma has order 120 and contains -I. HOLDS.

**(G13).** Integer spins factor through SO(3), so m_j = (1/60) sum over the rotation group of chi_j.
- Half-turn: 1 + 2 sum_{r<=j} (-1)^r = (-1)^j.
- Angle 2pi/3: 2cos(2pi r/3) is -1, -1, 2 for r = 1, 2, 0 mod 3; partial sums give b_j = 1, 0, -1, 1, 0, -1, 1
  for j = 0..6.
- Fifth turns: 1 + 2cos(2pi/5) + 2cos(4pi/5) = 0 (sum of the fifth roots of unity), so
  2(cos(2pi r/5) + cos(4pi r/5)) = -1 for r not divisible by 5 (multiplication by r permutes the nontrivial
  roots) and 4 for r divisible by 5. With the base value 2 at r = 0:
  d_j = 2 - (j - floor(j/5)) + 4 floor(j/5) = 2 - j + 5 floor(j/5). The note omits the roots-of-unity
  sentence; the formula is right.
- The two fifth-turn classes have 12 elements each, so they contribute 12 d_j.

Table, by hand (60 m_j = (2j+1) + 15(-1)^j + 20 b_j + 12 d_j):
j=0: 1+15+20+24 = 60. j=1: 3-15+0+12 = 0. j=2: 5+15-20+0 = 0. j=3: 7-15+20-12 = 0.
j=4: 9+15+0-24 = 0. j=5: 11-15-20+24 = 0. j=6: 13+15+20+12 = 60.
Every row of the table matches; m_1 = ... = m_5 = 0 and m_6 = 1. HOLDS.

**(G12).** A finite or compact group average of g^{tensor n} is the orthogonal projection onto the invariants
(the note's three-line proof is correct). Inv_SU(2) is contained in Inv_Gamma. V^{tensor n} contains only spins
j <= n/2. For odd n the centre kills all Gamma-invariants. For even n <= 10 only j <= 5 occur, and m_j = 0 for
1 <= j <= 5, so the two invariant spaces coincide. At n = 12 the spin-6 summand occurs once (Sym^12 V), and it
holds one Gamma-invariant line, orthogonal to the SU(2)-invariants (different isotypic component). So the
difference is the rank-one projection onto that line. Mixed V and conjugate-V tensors reduce to this case by the
equivariant identification of conj(V) with V. GUIDE: E_Gamma chi_V^n = Catalan numbers for n <= 11 and
133 = 132 + 1 at n = 12. HOLDS.

**Irreducibility under Gamma.** chi_1^2 = chi_0 + chi_1 + chi_2, so <chi_1, chi_1>_Gamma = m_0 + m_1 + m_2 = 1.
chi_V^2 = chi_0 + chi_1, so <chi_V, chi_V>_Gamma = m_0 + m_1 = 1. Both irreducible. HOLDS.

**"Lemma 1 is shared".** The finite-group pair convolution is a class-weighted average that commutes with an
irreducible spin-1 action, so it equals P + t_Gamma (I - P). Positivity: the coefficient of (beta/2)^n/n! in
3 z_Gamma t_Gamma is <chi_1, chi_V^n>_Gamma >= 0, and n = 2 gives 1. Strictness by full support. So (G8)-(G11)
and ||AB|| < 1 hold with t_Gamma. HOLDS.

**Correction (HOLDS AFTER CORRECTION).** The note says "(G7) is shared" (lines 68-69, 106). (G7) includes the
number 7/12. That needs t_Gamma <= 1/24 on 0 < beta <= 1, which the note does not prove; (G4) bounds only the
SU(2) coefficient r_1. A hand proof:
(a) 3 z_Gamma t_Gamma - 3 z r_1 = sum_n (beta/2)^n/n! [<chi_1,chi_V^n>_Gamma - <chi_1,chi_V^n>_SU(2)]. Each bracket
is >= 0 (restriction cannot lose invariant maps), is 0 for n <= 9 by (G12) (chi_1 chi_V^n = chi_V^{n+2} - chi_V^n),
and is <= 3 * 2^n. Also z_Gamma >= z (same argument with chi_V^n) and z_Gamma >= 1 (Jensen, E chi_V = 0). Hence
t_Gamma <= r_1 + sum_{n>=10} beta^n/n! <= r_1 + e beta^10/10!.
(b) (G4) is not enough at beta = 1, since there is no slack. A sharper termwise bound: the k-th term ratio of I_3
to I_1 is x^2/((k+2)(k+3)), which is x^2/6 at k = 0 and <= x^2/12 for k >= 1. So
I_3 <= (x^2/12)(I_1 + x), and with I_1 >= x + x^3/2, r_1 <= (beta^2/48)(1 + 1/(1 + beta^2/8)). This is increasing in
beta and equals 17/432 at beta = 1.
(c) So t_Gamma <= 17/432 + e/10! < 18/432 = 1/24 on 0 < beta <= 1, and ||AB||_Gamma <= 7/12. With this addition the
claim "(G7) is shared" holds as written. GUIDE: t_Gamma(1) = 0.03922510460, r_1(1) = 0.03922510452.

**(G14).** r_6 = I_13/I_1 = product over n = 1..12 of I_{n+1}/I_n <= (beta/2)^12 / (2*3*...*13) = (beta/2)^12/13!.
The Gamma density fixes the invariant unit vector (its average of a fixed vector is that vector). U(1) fixes the
zero-weight vector of Sym^12 V. HOLDS.

**(G15).** V tensor Sym^12 V = spin 11/2 + spin 13/2; 13 strands, so centre-odd. r_{11/2} = I_12/I_1 <= (beta/2)^11/12!
and r_{13/2} = I_14/I_1 <= (beta/2)^13/14!, the second no larger for beta <= 1. Both eigenvalues are positive, so the
norm is their maximum. HOLDS.

**(G16).** V tensor span(h) is a copy of V; the convolution acts there as int k_Gamma(g) D_V(g), which is the scalar
r_V^Gamma = E[chi_V e^{beta chi_V/2}]/(2 E[e^{beta chi_V/2}]) by irreducibility. Numerator coefficients are
E_Gamma chi_V^{n+1} >= 0, the n = 1 term is (beta/2) E chi_V^2 = beta/2; denominator <= e^beta since chi_V <= 2.
So r_V^Gamma >= beta/(4 e^beta). The U(1) weight-one eigenvalue E[cos e^{beta cos}]/E[e^{beta cos}] >= (beta/2)/e^beta.
**Minor correction:** the last step of (G16), beta/(4e^beta) > beta/12, and the U(1) bound > beta/6, need e^beta < 3,
i.e. beta < ln 3. The display states no range. Add "0 < beta <= 1" (the range of (G15)); the proof's use of e < 3
shows this is meant. With it: HOLDS AFTER CORRECTION (wording only). GUIDE: r_V^Gamma(1) = 0.2402 > 0.0920.

**(G17).** z_Gamma - z = sum_n (beta/2)^n/n! (E_Gamma chi_V^n - E chi_V^n). The bracket is 0 for n <= 11, 1 at n = 12,
and 0 at n = 13 (odd). So the difference is beta^12/(2^12 12!) + O(beta^14). Absolute convergence since |chi_V| <= 2.
HOLDS.

**(G17a) and the compact-interval extension.** Sym^n V is identified Gamma-equivariantly with binary forms of degree n,
compatibly with multiplication. So h^k is nonzero (polynomial ring is a domain) and Gamma-invariant in Sym^{12k} V.
r_{6k} = I_{12k+1}/I_1 <= (beta/2)^{12k}/(12k+1)!. Successive bound ratio (beta_+/2)^12/[(12k+2)...(12k+13)] -> 0.
On V tensor Sym^{12k} V the SU(2) eigenvalues are r_{6k-1/2} <= (beta/2)^{12k-1}/(12k)! and
r_{6k+1/2} <= (beta/2)^{12k+1}/(12k+2)!, uniformly small on I for large k. The Gamma and U(1) lower bounds
beta_-/(4e^{beta_+}) and beta_-/(2e^{beta_+}) follow from (G16) without the e < 3 step. HOLDS.

**Verdict, item 2:** HOLDS, except two corrections: "(G7) is shared" needs the added bound t_Gamma <= 1/24
(supplied above), and (G16)'s final strict inequalities need 0 < beta <= 1 stated.

## 3. Section 5: Propositions 3 and 4, (G18)-(G21)

**(G18), the oriented link tensor.** A link of the 4D lattice lies in 6 plaquettes. Four carry chi_{1/2}, two carry
chi_0 = 1. Each spin-1/2 factor contains a matrix entry of U_l or of U_l^{-1}. For SU(2), U^{-1} = U^dagger has the
entries of conj(U) transposed, and conj(U) = eps U eps^{-1}. So fixed unitaries turn the link integral into
H_4 = int g^{tensor 4} dg, the projection onto Inv(V^{tensor 4}). HOLDS.

**dim Inv(V^{tensor 4}) = 2.** (0 + 1) tensor (0 + 1) has invariants only from 0 tensor 0 and 1 tensor 1, one each.
h = s_12 tensor s_34 is a unit invariant vector. The four face coefficients are 2 r_{1/2} > 0. HOLDS.

**Identification with Hom_SU(2)(V, V^{tensor 3}) as an isometry.** Send T to x_T = (T tensor I)(s'), where s' is the
unit singlet pairing the input with the fourth factor (via eps). Then ||x_T||^2 = (1/2) tr(T^* T), the normalized
Hilbert-Schmidt norm. Example: T = J_12 gives x_T = s_12 tensor s_34 (up to sign), norm 1, and tr(J_12^* J_12)/2 = 1.
So the note's normalization is the right one for this (unit-singlet) map. Both spaces have dimension 2 (the
multiplicity of spin 1/2 in V^{tensor 3}). The map is equivariant in the first three factors, so A tensor I acts as
post-composition T -> A T. In the orthonormal basis (J_12, J_r): A J_12 = J_12, A J_r = t J_r, so A acts as
P + t(I - P); B acts as Q + t(I - Q) with Q from (G9). Their product K has ||K|| = the M-block norm of (G11)
<= 7/12 for 0 < beta <= 1. H_4 restricted to its own range is the identity. HOLDS.

**(G19).** 1 = ||I|| <= |alpha| ||L|| ||K|| ||R|| + ||E|| <= |alpha| ||K|| + eps. With eps = 0, |alpha| >= 1/||K|| >= 12/7.
HOLDS. **Scope remark (not an error).** The argument uses only ||H_4|| = 1 on its range and ||K|| < 1. It refutes the
same free factorization through any strict contraction K, not specifically the two-filter product. So Proposition 3
is the observation that a Haar projection has norm one; the filters play no special role in it. The note's
"ARGUED, scope" paragraph (513-520) states the limits correctly.

**(G20).** g^{tensor(2k+1)}(s^{tensor k} tensor v) = (g tensor g s)^{tensor k} tensor g v = s^{tensor k} tensor g v, so J_k is
equivariant. ||J_k v|| = ||s||^k ||v|| = ||v||. The image is a spin-1/2 copy; 2k+1 strands give centre-odd action;
the total Casimir is that of spin 1/2. HOLDS.

**(G21) normalization.** From the integral computed in item 1, int k_beta chi_j = d_j r_j, and characters are
orthonormal, so e^{beta tr g/2}/z = sum_j d_j r_j chi_j. Consistent with (G3). HOLDS.

**The single flat wrapping plane.** Take the (r,i)-plane P_ri(b) of A = n_r n_i plaquettes, both periods >= 2 (true
for a >= 3), so `gap-kappa-order.md` Lemma T(d) applies: int prod_p x_p = 4^{-A} with x_p = (1/2) tr U_p. With
chi_{1/2} = 2 x_p the integral is 2^A 4^{-A} = 2^{-A}. The face factors give (2 r_{1/2})^A, and the spin-0 plaquettes
give 1. The term equals r_{1/2}^A > 0. HOLDS.
Sign under the twist: a twist sheet flips eta_p on one (r,i)-stack (fixed (x_r, x_i)). Since e^{-beta tr U/2}
= sum d_j r_j (-1)^{2j} chi_j(U), each half-integer plaquette on the sheet contributes -1. The plane meets each
(r,i)-stack in exactly one plaquette (Lemma M of `gap-kappa-order.md`), so the sign is -1, and a spatial twist m in
another plane does not change it. The contribution to untwisted minus twisted is 2 r_{1/2}^A. The common divisor is
(e^{-beta} z)^{N_p}, matching the weight e^{-beta(1 - tr U_p/2)} of `gap-ext-astra.md` (E1). The plane has no branching
edge; each link carries two strands and one singlet. HOLDS.
The refuted exposure statement (lines 573-574) is refuted termwise, at every period. The note claims nothing more.

**Verdict, item 3:** HOLDS throughout. Scope remark: Proposition 3 does not depend on K being the two-filter product.

## 4. Section 6 and the tree sketch of Section 1

### 4.1 (G22) as a statement of what is missing

(a) **Under-specified.** M_B, the block, the "charged boundary space", the boundary norm and the reference measure
are named, not defined. (G22) is a schematic target, not a lemma that a later run could check as stated.

(b) **The factorization adds nothing by itself.** Take alpha = 1, L_B = M_B, K_B = R_B = I, E_B = 0. Then (G22) reads
||M_B|| < 1. Conversely (G22) implies ||M_B|| < 1. So (G22) is equivalent to a strict contraction of the block operator
in the chosen norm. The factorization through K_B has content only if K_B must be the two-filter product (or a
filter product of a stated kind). The note should say which.

(c) **Necessary, not sufficient.** The note says so: repeated exposures, accumulated boundary comparisons and scalar
factors at the original normalization remain (lines 602-605). No step from (G22) to (FQ) or (V) is claimed. The
fact that the scalar factor must come from the same integral and cannot be fixed after normalizing odd and even
sectors separately is the right guard; it matches (E1)-(E2) of `gap-ext-astra.md`.

(d) **Line 607-608.** "(G22) fails for the bare four-strand Haar tensor with K_B the proposed two-filter product" is
true, and in fact true for every K_B, since ||H_4|| = 1 on its range (see item 3 scope remark).

**Scope match.** The RESULT line and Section 6 claim OPEN, two hand-proved local statements, and two refuted
realization rules on their stated domains. Each matches a statement checked above. (FQ), (V) and a new seed are not
claimed. The only overstatement is "(G7) is shared", repaired in item 2.

Verdict: HOLDS AFTER CORRECTION. (G22) is a fair description of the missing step only as "a strict contraction of a
yet-undefined resummed block operator at the original normalization"; the factorization form is redundant unless
K_B is constrained.

### 4.2 The tree sketch: are B and C non-equivalent to the listed reformulations?

The discarded list (lines 126-143) is accurate against FINISH rows 783-803 and the context files: (26), (TR-F) with
(T7), (T9), (S19)-(S24), (K-RESP), row 802's recursion, the signed spin-foam problem, and the commutator value 1/4
shared by Gamma ((K25) in `gap-kanazawa-astra.md`). Route A is not a rewrite of F; Sections 3-5 confirm it.

**Route B.** (G2) is a functional inequality for the Gibbs measure, not a scalar rewrite of F. By the integrated
Bochner identity (integral of Gamma_2 = integral of (Lf)^2, Ric = 2 on the unit 3-sphere), (G2) gives a Poincare constant
kappa, uniform in volume, at each fixed beta. This differs from (TU) of `gap-ac-lat.md` 132, which continues the
constant in the coupling. So B is non-equivalent as a key lemma. Its downstream bridge (uniform Poincare to decay,
then to the twist) is the "end" statement of `gap-ac-lat.md` 132, recalled there and not rebuilt; the note admits a
missing spectral and normalization bridge (line 123-124).
**Correction to the U(1) column.** "The Ricci reserve of the abelian group is zero" is not the first failing step. The
U(1) analogue of (G2), with Ric = 0 in place of 2, needs integral Hess S(grad f, grad f) >= -theta integral ||Hess f||^2
+ kappa integral |grad f|^2. At beta = 0 the left side is 0, and on a product of unit circles a mean-zero f has
integral ||Hess f||^2 = integral (Delta f)^2 >= integral |grad f|^2. So the analogue holds at beta = 0 with any
kappa <= theta. The Hessian-square reserve, not Ricci, can carry the abelian case at weak interaction (where U(1)
does have a uniform gap). The binding test is U(1) in the Coulomb range, and the note names no failing step there.
The Gamma column ("no Haar manifold") means the route is not formulable for Gamma; that passes the finite-group test
by inapplicability, not at an identified step.

**Route C.** It names an estimate on generated interactions (entry into a convergent local-interaction ball after
finitely many exact block steps), not a rewrite of F. So it is non-equivalent to the scalar forms. It is the estimate
that (K-RESP) and Tomboulis-type matching lack, and, if proved, it would also be a seed for row 802's recursion; the
note's "without a new estimate" qualifiers keep the distinction formal but honest. Its stated input is the
conclusion of an order-one block analysis; no mechanism inequality is named. The U(1) cell cites a "nonabelian drift"
that the route statement does not contain. For U(1) in the Coulomb range the failure is the ball entry itself,
i.e. the route's conclusion. So C's binding-test cells are not checkable as written.

Verdict: HOLDS AFTER CORRECTION. B and C are not rewrites of the twist deficit. B's U(1) failing step is
misidentified; C's distinguishing step is unspecified. The GUIDE ranking (A, B, C) is a judgement; I see no reason to
reverse it.

## 5. Verdict table

| Item | Statement | Verdict |
|---|---|---|
| 1 | (G3)-(G4) inputs | HOLDS |
| 1 | (G5)-(G6) | HOLDS |
| 1 | Schur forms, t = r_1 = I_3/I_1 on spin 1, 1 on the singlet | HOLDS |
| 1 | (G8): J_12^* J_23 = -I/2, PQP = P/4, norm PQ = 1/2 | HOLDS |
| 1 | (G7) with (G4), 7/12 | HOLDS |
| 1 | strictness, t < 1, norm AB < 1 | HOLDS |
| 1 | (G9) J_r, Q; (G10) sum and product; (G11) | HOLDS |
| 1 | U(1) control vector | HOLDS |
| 2 | classes 1, 15, 20, 12, 12 | HOLDS |
| 2 | (G13) and table j = 0..6 (zeros for 1..5, m_6 = 1) | HOLDS (roots-of-unity step implicit) |
| 2 | (G12), rank-one difference at degree 12 | HOLDS |
| 2 | irreducibility of spin 1 and V under Gamma | HOLDS |
| 2 | Lemma 1 shared by Gamma: (G11) with t_Gamma, strictness | HOLDS |
| 2 | "(G7) is shared", i.e. 7/12 for Gamma | HOLDS AFTER CORRECTION (add t_Gamma <= 17/432 + e/10! < 1/24) |
| 2 | (G14), (G15) | HOLDS |
| 2 | (G16) | HOLDS AFTER CORRECTION (state 0 < beta <= 1 for the final > beta/12, > beta/6) |
| 2 | (G17) beta^12/(2^12 12!) | HOLDS |
| 2 | (G17a) and compact-interval extension | HOLDS |
| 3 | (G18), dim Inv = 2 | HOLDS |
| 3 | isometry with Hom(V, V^{tensor 3}) (unit-singlet map, normalized HS) | HOLDS |
| 3 | (G19), cost >= 12/7 | HOLDS (scope: independent of the filters) |
| 3 | (G20) | HOLDS |
| 3 | (G21) single plane term r_{1/2}^A, sign flip, 2 r_{1/2}^A | HOLDS |
| 4 | (G22) as the missing statement; scope | HOLDS AFTER CORRECTION (under-specified; factorization redundant unless K_B constrained) |
| 4 | routes B, C non-equivalent | HOLDS AFTER CORRECTION (B's U(1) step misidentified; C's distinguishing step unspecified) |

Nothing FAILS.

Not checked: the repo-search and source-reading claims (lines 1-44, 152-178, 626-648), including the SA outline line
numbers, and the absence claims of the searches.

RESULT: Every PROVED step of `library/gap-tree-astra.md` holds by hand and nothing fails; corrections are the missing bound t_Gamma < 1/24 behind "(G7) is shared", the range 0 < beta <= 1 in (G16), the redundancy of the factorization in (G22) (and Proposition 3's independence of the filters), and the misidentified U(1) failing step for route B with an unspecified one for route C.
