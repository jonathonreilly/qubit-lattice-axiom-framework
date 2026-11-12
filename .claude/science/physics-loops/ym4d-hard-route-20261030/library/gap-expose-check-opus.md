# Check of library/gap-expose-astra.md (FINISH row 810), by Claude Opus 5.5, line by line

Clone: `/Users/jonreilly/ym4d-lead/clone` at `07667f860941c5497a2c39cdedf018b2d9793edd`.
Lane D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
Target: `D/library/gap-expose-astra.md` (658 lines, Codex gpt-6-astra max, row 809), read in full.
Context read: `gap-block-astra.md` sections 1, 4, 6, 7 (and 8); `gap-block-check-opus.md` section headers;
`gap-tree-check-opus.md` sections 2-3 for (G12)-(G21); `gap-ext-astra.md` lines 60-135 for (FQ).
All steps were checked by hand. One small GUIDE run (Bessel series, under 1 MB) is reported in item 5 and 7;
it decides nothing. No repository file was edited.

## 1. (E1)-(E5)

**(E1) and the transfer.** C_beta is convolution by the normalized kernel w/z, with eigenvalue
r_j = I_{2j+1}/I_1 on spin j. So z^{|E|} K is convolution by the full temporal weight w on every link.
L_m = z^{|E|} K^{1/2} B_m K^{1/2} is cyclically equivalent to the half-action cut B^{1/2} K B^{1/2}.
Periodic time with integrated temporal links gives the gauge projection, so Z^m = Tr L_m^t on H. K is
trace class (Tr K = prod_e sum_j d_j^2 r_j), injective (all r_j > 0), and B_m is bounded with bounded
inverse. Hence L_m is positive, injective, trace class. HOLDS.

**J_e and the vertex identity.** (J_e f)(U) = f(U with U_e -> -U_e) is an involutive, measure-preserving
substitution, so J_e is a self-adjoint unitary. The J_e commute pairwise. Since -I is central, J_e commutes
with every gauge transformation, so it preserves H. It commutes with convolution: substituting V' = -V
in the link integral shows C J_e = J_e C. The gauge transformation g_v = -I at v, I elsewhere, sends
U_e -> -U_e for each edge incident to v (either orientation, as (-I)^{-1} = -I) and fixes the rest.
Periods are at least three, so there are no self-loops. Thus prod_{e at v} J_e = g_v, which is the
identity on H. HOLDS.

**(B4) is killed.** In row 807, Theta at a boundary vertex v is exactly prod_{e at v} J_e on the slab
graph. If v is also gauge-projected, P_gauge g_v = P_gauge, so P_gauge (1 - Theta_v)/2 = 0. HOLDS.

**(E2).** For b != c some factor pair (1+J)/2 (1-J)/2 vanishes, so the E_b are mutually orthogonal
projections. The sum over b factorizes into prod_e [(1+J_e)/2 + (1-J_e)/2] = I. On ran E_b,
J_e = (-1)^{b_e}; the vertex identity then gives I = (-1)^{(partial b)_v} on ran E_b, so E_b = 0 unless
partial b = 0. Conversely every closed b has E_b != 0 (decompose b into edge-disjoint cycles and take the
product of their fundamental characters), a fact the note does not need but which item 4 uses. In the
Peter-Weyl basis D^j(-U) = (-1)^{2j} D^j(U), so E_b selects the parity of 2j per edge and keeps all other
labels. HOLDS.

**Theta_omega.** Under Theta each plaquette holonomy picks up (-1)^{(d omega)_p} = 1, so the
multiplication operator B_m commutes with Theta. K commutes with each J_e. On E_b, Theta =
(-1)^{<omega,b>}. If omega = d lambda, then Theta = prod_v g_v^{lambda_v}, trivial on H. HOLDS.

**(E3).** Flipping the temporal plaquettes (r,e) at one seam, for e crossing the x_i-cut, is the standard
(r,i) twist stack. Since w(-g) = e^{-beta x(g)}, the flip equals J_e on those links in the transfer, giving
Z^{m+v} = Tr(Theta L^t). Then Z^m - Z^{m+v} = Tr((1-Theta)L^t) = 2 Tr(P_- L^t). Since Theta commutes with
K^{1/2}, its placement in the half-kernel cut is immaterial. HOLDS (agrees with (K9)).

**(E4).** Insert I = sum_b E_b before each of the t factors L. P_- E_{b_1} = E_{b_1} if <omega,b_1> = 1,
else 0. For the other layers: Theta E_b L E_c = (-1)^{<omega,b>} E_b L E_c, and also
E_b L E_c Theta = (-1)^{<omega,c>} E_b L E_c, while Theta commutes with E_b L. So E_b L E_c = 0 unless
the pairings agree. Hence every b_s pairs oddly, and every b_s is closed or E_{b_s} = 0. The index set is
finite (F_2^E). Each nonzero E_b has norm one. "b_{t+1} = b_1" is unused but harmless. HOLDS.

**(E5) and the closed-surface reading.** exp(beta sum eta x_p) = prod_p (cosh + sinh), expanded over
subsets s. sinh is odd and cosh even in x_p, and J_e sends x_p -> -x_p exactly when e is in the boundary
of p. So J_e B_{m,s} J_e = (-1)^{(partial s)_e} B_{m,s}. Conjugating E_b B_{m,s} E_c by J_e gives
(-1)^{b_e + (partial s)_e + c_e}, so the term vanishes unless b + c = partial s. In the word, E_{b_s}
commutes with K^{1/2}, so consecutive constraints are b_s + b_{s+1} = partial s_s. Closedness of the
4D mod-two two-chain at a spatial edge e of layer s is exactly this equation; at a temporal edge above
vertex v it is (partial b_s)_v = 0. The pairing is constant in s because <omega, partial s> = <d omega, s>
= 0. The area bound a^2 is READ from Lemma M (odd pairing forces one plaquette in each of the
L_r L_i (r,i)-stacks). The note correctly says the refined factors are no longer L_m. HOLDS.

**Verdict, item 1: HOLDS.**

## 2. Lemma 1, (E6), and its applications

**Injectivity and density.** R = A K^{1/2}: K^{1/2} injective and A invertible, so ker R = 0.
R* = K^{1/2} A: A injective and K^{1/2} injective, so ker R* = 0. Then ran R and ran R* are dense, by
(ran X)^perp = ker X*. T = RR* is injective: <f,Tf> = ||R*f||^2. HOLDS.

**The unitary.** ||R* f||^2 = <f, RR* f> = ||T^{1/2} f||^2. The map R*f -> T^{1/2}f is a well-defined
isometry from the dense set ran R* onto ran T^{1/2}, which is dense since T^{1/2} is injective and
self-adjoint. Its extension U is an isometry with closed range containing a dense set, so U is unitary.
U R* = T^{1/2}; the adjoint gives R U* = T^{1/2}, so R = T^{1/2} U. Then T_F = RFR* =
T^{1/2} (UFU*) T^{1/2}, and ||UFU*|| = ||F|| = 1. HOLDS.

**Optimal constant.** <f, T_F f> = <R*f, F R*f> <= ||R*f||^2 = <f,Tf>, so c = 1 works. If T_F <= cT,
then <g,Fg> <= c||g||^2 on the dense set g in ran R*. Both sides are continuous in g, so the inequality
holds for all g. A unit g in ran F gives c >= 1. HOLDS. The uniqueness claim also holds:
T^{1/2} Y T^{1/2} = 0 forces Y T^{1/2} = 0 (T^{1/2} injective), hence Y = 0 (dense range).

**Remark (not an error).** The hypothesis "F commutes with K" is not used in the proof. It is used only to
read T_F as the transfer with K replaced by K^{1/2} F K^{1/2}.

**Application to E_b.** A = z^{|E|/2} B_m^{1/2} is positive with bounded inverse and preserves H.
T = z^{|E|} B^{1/2} K B^{1/2} is the half-action cut, and R*R = L_m. E_b commutes with K, so
K^{1/2} E_b K^{1/2} is the parity-selected convolution, and T_b = R E_b R*. A common positive scalar
multiplies T_b and T alike, so it cannot change the optimal c. HOLDS.

**Application to spin cutoffs.** P_J (all link spins <= J) and Q_J = 1 - P_J commute with K and with
Theta (both are diagonal in the Peter-Weyl basis, and Theta acts by (-1)^{2 j_e} signs). On P_- H,
K and A restrict to operators meeting the hypotheses, since both commute with P_-. A simple straight
winding loop C carrying chi_j, j half-integer, has spin j on every edge of C (the character of a product
expands into products of spin-j matrix entries). It is gauge invariant and Theta-odd, since C crosses the
cut once. So Q_J P_- != 0 for every J and P_J P_- != 0 once J >= 1/2. Both relative norms equal one.
HOLDS.

**The application-limit paragraph.** X = RF gives XX* = T_F and X*X = F L_m F, so their nonzero
spectra agree. ||RQ_JR*|| = ||Q_J L_m Q_J|| <= z^{|E|} e^{beta|P|} ||Q_J K Q_J||, which is the absolute
eta_J bound of (B16) in this cut. The step T_high <= eps_J T with eps_J -> 0 is refuted by the optimal
c = 1. The note also correctly notes that (E13) does not claim a unit eigenvalue of A_J in (B15). HOLDS.

**Verdict, item 2: HOLDS.**

## 3. (E7)

P_- commutes with L_m, so 2P_- L^n = L^{n/2}(2P_-)L^{n/2}. The inequality 2P_- L^n <= eps L^n is
<L^{n/2}f, (eps - 2P_-) L^{n/2} f> >= 0 for all f. L^{n/2} has dense range, so this is
eps - 2P_- >= 0, that is eps >= 2 when P_- H != 0 (and eps >= 0 on the even part). Sufficiency is
0 <= P_- <= I. For a rank-one positive exterior |f><f|, the ratio 2<f,P_- L^n f>/<f, L^n f> lies in
[0,2] and equals 2 at any odd f, whose denominator is positive by injectivity. The note correctly limits
the claim: it does not identify a rank-one odd exterior with a positive Wilson kernel. HOLDS.

**Verdict, item 3: HOLDS.**

## 4. The class and theorem, (E8)-(E10)

**Is the class precise?** Yes, in the sense needed. Clause 3 fixes the cost functional: for a history
(selectors F_1, ..., F_t, each refined as F_s = sum_alpha c_{s,alpha} Y_{s,alpha}) with scalar coefficient
c, the charged cost is |c| prod_s sum_alpha |c_{s,alpha}| ||Y_{s,alpha}||. The total cost is the sum of
these over all histories. The proof uses only this functional, so the theorem is well posed. Two phrases are
looser than the proof needs, and neither changes the conclusion:
- Clause 1 allows resolution by representation sectors, finer than parity. Then "the winding-loop history"
  is a family of fine histories. Their words sum to the E_C word, whose trace is positive, so at least one
  fine history has a nonzero word, and its cost is at least 2 by the same (E8). Under clause 3 even
  histories with zero words are charged, so the bound holds a fortiori.
- The "coarse selectors" paragraph conditions on the winding-loop history "surviving" the grouping. This
  condition is unnecessary. Any history built from nonzero orthogonal selectors costs at least 2, and at
  least one such history exists, because the sum of all words is 2 Tr(P_- L^t) > 0.

**(E8).** For an operator-norm absolutely convergent F = sum c_alpha Y_alpha, the triangle inequality
gives 1 = ||F|| <= sum |c_alpha| ||Y_alpha||. A factored Y with charged product of norms costs at least
||Y|| by submultiplicativity. A kept error term is one more summand. Rescaling c_alpha and Y_alpha by
inverse scalars leaves |c_alpha| ||Y_alpha|| unchanged. HOLDS.

**The winding history is nonzero.** C is a straight loop in direction i, the twist direction, so it
crosses the omega-cut once and <omega,C> = 1. E_C != 0, because chi_{1/2}(U_C) lies in its range.
E_C L E_C = (L^{1/2}E_C)*(L^{1/2}E_C) is positive and nonzero (L^{1/2} injective). Since E_C^2 = E_C,
cyclicity gives Tr(E_C L ... E_C L) = Tr((E_C L E_C)^t) > 0. The contribution to (E4) is twice this. Its
temporal faces are the (r,e), e in C, at all times: one flat (r,i) plane. HOLDS.

**(E9).** Expanding the Cartesian product, the history's cost is exactly 2 prod_s (sum_alpha |c||Y|),
and each factor is at least 1 by (E8). Unsplit, the product is 1. Costs are nonnegative, so other
histories cannot lower the total. HOLDS.

**Does (B30) bound the total norm cost before the trace?** Yes. Row 807 (gap-block-astra.md, section 6)
states its hypotheses on two quantities per connected set gamma of area A: the total absolute scalar
coefficient, at most h^A, and "their operator product in (B29)", at most q^{A/D-1}. Both are norm-cost
data. The trace enters only afterwards, through (B29). Summing, with at most 400^{A-1} connected sets
of area A through a root and N_p roots, and A >= a^2:
sum_gamma |c_gamma| prod ||X|| <= N_p sum_{A>=a^2} 400^{A-1} h^A q^{A/D-1}
= (N_p/(400q)) rho^{a^2}/(1-rho). This is (E10). Row 807's (B31) is this bound followed by (B29), so the
note's reading is the literal one. HOLDS.

**The contradiction.** N_p = 6a^2cd <= 24a^4, and rho < 1 is fixed, so the right side of (E10) tends to 0
as a -> infinity. The left side is at least 2 for every a by (E9). For large a this is a contradiction.
A fixed prefactor absorbing the factor 2 changes 2 to 1 and leaves the contradiction. The class requires
the bound on all boxes, so one large a suffices. The argument is pointwise in beta, so it holds at each
beta in I. HOLDS.

**Scope remark (not an error).** The theorem is close to definitional. Under the class, every history is
charged at least its coefficient, because (B29) applied to norm-one projections gives no decay. The
substantive inputs are that every layer selector of (E4) has norm one and that (B30) controls the summed
norm cost. Row 807's own hypotheses speak of terms "after all nonwrapping decorations have been
resummed". Such a resummation would normally be joint across layers, which clause 3 excludes. The note
states this limit itself (lines 299-307, 362-369, 635-644).

**Verdict, item 4: HOLDS**, with two wording remarks (fine resolution; the "survives the grouping"
condition is unnecessary).

## 5. Lemma 2, (E11)-(E12)

**Orthonormality.** U_p = U_1 U_2 U_3^{-1} U_4^{-1} is Haar distributed when the four links are
independent Haar. So the phi_j = chi_j(U_p) are orthonormal. They are gauge invariant. HOLDS.

**K phi_j = r_j^4 phi_j.** chi_j(U_p) = sum D^j(U_1)_{ab} D^j(U_2)_{bc} D^j(U_3^{-1})_{cd} D^j(U_4^{-1})_{da}.
Each factor is a spin-j matrix coefficient of its link (D^j(U^{-1}) is a matrix coefficient of the
contragredient, which is equivalent to spin j). Convolution on spin j multiplies by r_j; the other links
carry spin 0, with r_0 = 1. HOLDS.

**Recursion.** 2 cos(theta) sin((2j+1)theta) = sin((2j+2)theta) + sin(2j theta) is the product-to-sum
formula. Divide by sin(theta): 2x chi_j = chi_{j+1/2} + chi_{j-1/2}, with x = cos(theta) = tr/2, for
j >= 1/2. HOLDS.

**(E11).** K^{-1/2} phi_j = r_j^{-2} phi_j; M_f gives (phi_{j+1/2} + phi_{j-1/2})/2; K^{1/2} multiplies
by r_{j +- 1/2}^2. The displayed formula follows. HOLDS.

**(E12).** r_{j-1/2}/r_j = I_{2j}/I_{2j+1}. The recurrence I_{n-1} - I_{n+1} = (2n/beta) I_n with
I_{n+1} > 0 for beta > 0 gives I_{n-1}/I_n >= 2n/beta. With n = 2j+1:
I_{2j}/I_{2j+1} >= 2(2j+1)/beta. Equivalently I_{n+1}/I_n <= beta/(2(n+1)). HOLDS.
GUIDE (series to 60 terms): at beta = 1, I_{2j}/I_{2j+1} = 4.163, 6.123, 10.08, 22.04 for
j = 1/2, 1, 2, 5, against 4, 6, 10, 22.

**Divergence.** The image has orthogonal components, so its norm is at least the phi_{j-1/2}
coefficient (1/2)(I_{2j}/I_{2j+1})^2 >= 2(2j+1)^2/beta^2. This is unbounded in j. The reverse conjugation
has raising coefficient (1/2)(r_j/r_{j+1/2})^2 = (1/2)(I_{2j+1}/I_{2j+2})^2 >= 2(2j+2)^2/beta^2.
All inverses act on finite-spin vectors. HOLDS.

**Odd-flux version.** A straight winding loop C avoiding the four edges of p exists for periods at
least 3 (offset it in a transverse direction). Functions of disjoint edge sets are independent under
product Haar, so phi_j chi_{1/2}(U_C) remain orthonormal. Theta acts by +1 on phi_j, because
<omega, partial p> = <d omega, p> = 0, and by -1 on chi_{1/2}(U_C). The common K factor
r_{1/2}^{|C|} cancels in the conjugation, and M_f acts only on p. Replacing beta by beta_+ in the lower
bound gives uniformity on I. HOLDS.

**Verdict, item 5: HOLDS.**

## 6. (E13), the control table, and finite-group positivity

**(E13).** For a finite-spin unit psi in ran F, K^{-1/2} psi is defined: the spin-<=J part of H is finite
dimensional on a finite lattice, and K is invertible there. A^{-1} is bounded and preserves H. So
f = A^{-1}K^{-1/2}psi lies in H, and R*f = K^{1/2} A A^{-1} K^{-1/2} psi = psi. Then
<f,T_F f> = <psi,F psi> = 1 = ||R*f||^2 = <f,Tf>. HOLDS. The caveat that this is not a unit eigenvalue
of A_J in (B15) is correct.

**READ part of section 5.** The control lower bounds beta_-/(4e^{beta_+}) for Gamma and
beta_-/(2e^{beta_+}) for U(1) agree with the checked (G16)-(G17a) compact-interval extension, which
needs no e < 3 step (gap-tree-check-opus.md, item 2). READ, consistent.

**Table.** Row 1: -1 lies in U(1) and in Gamma, so J_e, E_b, Theta and (E4) carry over verbatim. Row 2:
matches row 807 section 4 and (G17a). Row 3: Lemma 1 needs only K injective and A invertible, so it
applies to all three groups. HOLDS.

**U(1) positivity.** e^{beta cos theta} = sum_n I_n(beta) e^{in theta}, with I_n > 0 for beta > 0. Each weight
appears in the binomial expansion with positive coefficients. HOLDS.

**Gamma positivity.** The matrix entries of the faithful V separate points of Gamma. The algebra they
generate with their conjugates separates points and contains constants, so on a finite set it is every
function (Lagrange-type interpolation). V-bar is equivalent to V through the invariant alternating form
of SU(2), restricted to Gamma. So every irreducible rho of Gamma occurs in some tensor power V^{tensor n}
(Burnside-Brauer). exp(beta chi_V/2) = sum_n (beta/2)^n chi_V^n/n!, and chi_V^n has nonnegative
multiplicities, positive for rho at some n. So the coefficient of chi_rho is positive, and convolution acts
on the rho-isotypic part by that coefficient over d_rho, up to the positive normalization. HOLDS.
Winding fundamental characters (weight one for U(1), chi_V for Gamma) have unit norm and are Theta-odd,
so the odd selectors are nonzero. HOLDS.

**Verdict, item 6: HOLDS.**

## 7. (E14)-(E15)

**(E14).** From (G21), e^{beta x}/z = sum_j d_j r_j chi_j, so each face with label j_p > 0 contributes
d_{j_p} r_{j_p} chi_{j_p}(U_p), and faces off gamma contribute 1. |chi_j| <= d_j gives
|integral prod chi_{j_p}| <= prod d_{j_p}. So |a(j)| <= prod_p d_{j_p}^2 r_{j_p}. The sum over labels
0 < j_p <= J factorizes into W_J^{|gamma|}. No sign or branching assumption is used. HOLDS.

**r_{1/2} formula.** With x = cos theta and density (2/pi) sin^2 theta: E e^{beta x} = 2I_1/beta and
E[x e^{beta x}] = d/d beta (2I_1/beta) = 2I_2/beta, so the ratio is I_2/I_1 = r_{1/2}. HOLDS.

**Lower bound.** g -> -g preserves Haar and sends x -> -x, so odd moments vanish. E x^2 = 1/4 (chi_{1/2} = 2x
has unit norm). The numerator sum_n beta^n E x^{n+1}/n! has nonnegative terms (only even moments survive),
and the n = 1 term is beta/4. The denominator is at most e^beta since x <= 1. So r_{1/2} >= beta/(4e^beta).
On [1/2,1], beta >= 1/2 and e^beta <= e < 3 give beta/(4e^beta) > (1/2)/12 = 1/24. HOLDS.
GUIDE: r_{1/2}(1/2) = 0.1237 and r_{1/2}(1) = 0.2402, against lower bounds 0.0758 and 0.0920.

**W_J.** For J >= 1/2, W_J >= d_{1/2}^2 r_{1/2} = 4 r_{1/2} > 1/6. Then 400 W_J > 66 > 1, so the
majorant with row 807's count 400 cannot give rho < 1. Splitting W_J^A as h^A (q^{1/D})^A keeps the
product h q^{1/D} = W_J. HOLDS. The note correctly calls this a failure of the upper bound (E14), not a lower
bound on the true branched weight, and it is tied to the crude count 400.

**Verdict, item 7: HOLDS.**

## 8. (E16)-(E18)

**(E16).** By (E3) with t = a, Tr(P_{-,i} L^a)/Tr L^a = (Z^m - Z^{m+v})/(2Z^m) = (1 - R_m(v))/2. The
maximum over m_2 = 0, i = 3,4 is the Q_F of gap-ext-astra.md (FQ), with v = v_{1i} in frame 1. HOLDS.

**(E17) suffices for (FQ).** If Q_F <= C a^p eta_*^{a/2} and S_ev >= eta_*^a, then
8 Q_F <= 8 C a^p eta_*^{a/2} <= K(a) sqrt(S_ev) with K(a) = 8 C a^p, which is polynomial. Q_F < 1/192
holds for large a because eta_* < 1. Lowering eta_* keeps S_ev >= eta_*^a true. Row 807 and gap-ext-astra
use the large-a (FQ), so "for all sufficiently large a" matches the consumer. The note proves neither (E17)
nor (FQ) and says so. HOLDS.

**(E18).** |sum_p eta_p x_p| <= |P| gives e^{-beta|P|} <= B_m <= e^{beta|P|}, hence
c_- K <= L_m <= c_+ K with c_+- = z^{|E|} e^{+-beta|P|}. Both operators are compact and positive.
Courant-Fischer gives lambda_k(L) in [c_- lambda_k(K), c_+ lambda_k(K)] for the decreasingly ordered
eigenvalues. P_- commutes with L_m and with K, so the same holds on P_- H. Raise to the power t and sum:
Tr(P_- L^t) <= c_+^t Tr(P_- K^t) and Tr L^t >= c_-^t Tr K^t. The ratio gives (E18); z^{|E|} cancels. The
note avoids the false operator-monotonicity of A -> A^t. HOLDS. |P| t = 3acd a is of order a^4, so the
prefactor swamps any e^{-sigma a^2} gain, as stated.

**Verdict, item 8: HOLDS.**

## 9. Is the RESULT line fair?

Mostly yes. Each claim in it matches a checked section: (E4) keeps the full transfer; the layerwise class
cannot meet (B30); the cost is at least two; the relative low- and high-spin selectors have norm one; the
degree-twelve distinction survives only at the absolute-tail step; the joint resummation, (FQ) and (V)
remain open. The label "scoped obstruction" matches the narrow, near-definitional class of section 3.

One wording correction. "The attempted contraction fails for both controls at named steps" omits that
it fails for SU(2) at the same step. In this programme a failure for the controls is the desired
behaviour, so a reader could take the phrase as a passed binding test. The body says the opposite
(lines 474, 489-491). Suggested text: "the attempted relative contraction fails at the same norm-one
selector for SU(2) and for both controls".

## 10. Verdict table

| Item | Content | Verdict |
|---|---|---|
| 1 | (E1)-(E5): vertex identity, (B4) killed, E_b, Theta, (E3), (E4), closed surfaces | HOLDS |
| 2 | Lemma 1, (E6): U, T_F <= T, optimal c = 1, E_b and spin cutoffs | HOLDS (the commutation hypothesis is unused) |
| 3 | (E7) | HOLDS |
| 4 | Class and theorem, (E8)-(E10); (B30) bounds the norm cost before the trace | HOLDS (two wording remarks; theorem is near-definitional) |
| 5 | Lemma 2, (E11)-(E12), odd-flux version | HOLDS |
| 6 | (E13), control table, finite-group positivity | HOLDS |
| 7 | (E14)-(E15) | HOLDS |
| 8 | (E16)-(E18) | HOLDS |
| 9 | RESULT line | FAIR AFTER A WORDING CORRECTION (say SU(2) fails at the same step as the controls) |

No step FAILS. No mathematical correction is required.

RESULT: Every mathematical step of gap-expose-astra.md checked HOLDS by hand, including Lemma 1, Lemma 2, (E15), (E18) and the section 3 theorem (which follows because (B30) bounds the summed norm cost before the trace, though the theorem is close to definitional for its class); the only correction is to the RESULT line, which should say the relative contraction fails for SU(2) as well as for both controls.
