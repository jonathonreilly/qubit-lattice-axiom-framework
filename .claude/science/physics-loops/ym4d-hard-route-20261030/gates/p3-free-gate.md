# P3 free-field port: one line-by-line check

First failing step: none

Port checked: `library/port/p3-free.md` (590 lines, written by Codex). Source: `ca_II.tex`, sha256 `6a1f74b0...d4b6f`; `ca_I.tex`, sha256 `4cb5cb5e...e93`. Both match the hashes in the port's table. I read CA-II 69440-70153 in full. I also read the cited lines 68376-68420, 68722-68818, 73248-73260, 145216-145224, 145576-145584, CA-I 27-46 and CA-I 46035-46045.

## Statements

A script compared each of the five ```latex blocks in the port with the source line ranges 69457-69467, 69516-69540, 69682-69736, 69849-69872 and 69925-70000. All five are byte-identical. No statement is strengthened or weakened.

## Section 1. `8.1:lem-gaussian-squares` (port 35-69)

- F1 holds. E exp(t.Z) = exp(t^T S t / 2) also holds for singular S, through Z = S^{1/2} U. Domination by e^{eps|U|^2} with eps < 1/2 justifies the four derivatives. The degree-four term (t^T S t)^2/8 gives the three pairings.
- With a=b=xi and c=d=eta, Cov(xi^2, eta^2) = 2(E xi eta)^2. Bilinear expansion and nonnegativity then follow. Same route as the source.

## Section 2. `8.1:lem-free-curvature-covariance` (port 71-163)

- Standard Gaussian on V has covariance Pi_V. d_1 d_0 = 0. d_1^* d_1 is bijective on W = im d_1^*, with ker d_1 = W^perp. Hence P_ex = Pi_{im d_1}. All checked.
- F2 checked term by term. (d_1^* d_1 xi)_nu and (d_0 d_0^* xi)_nu are as written. The mixed terms cancel for mu != nu, and the mu = nu term completes -Delta. So Delta_1 = -Delta componentwise.
- ker(-Delta) = constants, so G has mean zero, (-Delta)G = delta_0 - 1/V, and (-Delta)^+ v = G*v for mean-zero v. Checked.
- F3: nabla^-_b delta_y = delta_y - delta_{y+e_b}. G*nabla^-_b delta_y = nabla^-_b G(. - y). The pairing is -nabla^+_a nabla^-_b G(x-y). Checked. Signs for the same plane (two minus signs in direction nu) and for planes (mu nu),(mu sigma) (direction mu, both +) agree with the printed lines.
- Diagonal: negation and permutation invariance (equal periods) give -nabla^2_mu G(0) = (1 - 1/V)/4. So P_ex(p,p) = (1 - 1/V)/2. Checked. The count is at most 2 x 4 = 8 values, at most 16. No correction needed.

## Section 3. Definition, F4, `8.1:lem-kernel-positivity` (port 166-283)

- H-BG retains these: the massless gauge-fixed Gaussian, the block map, A_B = Balaban's (1.19) minimiser, colour independence, and Cov(d_1 A) = P_ex. The source asserts all of them at 69605-69612 and 69642-69645 without proof in this lemma. Retaining them as a named hypothesis is correct.
- F4 checked. If v is in ker D, then S Q^* v = 0. So S Q^* D^+ D = S Q^*, and Cov(A - TB, B) = 0. Gaussian independence then gives E[A|B] = TB with no invertibility assumed. The total-covariance split P_ex = C^bg + C^fl follows correctly under H-BG.
- (a) The factor 1/4 x 2 x n = n/2 is correct. The specialisations use Section 2 and F4 (H-BG for F_B only). Correct.
- (b) Each independent summand has zero variance. The Gaussian has positive density on im d_1, so q_f = 0 on im d_1, and polarisation follows. F5 checked. Corner equation e_nu = (c-a) e_rho mod periods: the entries are at most 2 and the periods are at least 6, so rho = nu, a = 0, c = 1. Signs: d_1 delta_b(pbar) = +1 and d_1 delta_b'(pbar) = -1 (direct from d_1). So 0 = -f(pbar). Correct.
- (c), (d) Correct. Delta_1^+ is the componentwise (-Delta)^+, and each bracket has at most two second differences.

## Section 4. `8.1:lem-background-tower` (port 285-327)

- Nesting, telescoping, E[M_i | G_{i+1}] = M_{i+1}, and orthogonality for i<j and j<i are correct. F6 integrability (conditional Jensen, then Cauchy-Schwarz) is correct.
- Small gap, not a failure: M_0 = F_B needs F_B to be sigma(B)-measurable. F4 supplies this (F_B = d_1 T B), but Section 4 does not say so. Repair: one clause.
- H-TOWER is correct as a named hypothesis. Source 69904-69911 rests on the flat-step identification. CA-II 145581-145582 lists that identification as "printed without proof in [B-CMP95 §1]; cited as printed". I checked this.

## Section 5. `8.1:lem-kernel-bounds` (port 330-574)

- Inputs. H1-MIN carries (a) as the operational consequence of (h1). This matches the source, which at 70010-70016 only says that (h1) gives the two bounds. So (a) is an assumption in substance, and the port says so. CA-I 46035ff. is a theorem with (A1), (A2) nest premises (checked). 145220-145222 says the continuum-kernel lemma is "not written out" (checked). H2-FLUX and H3-CONT are faithful to the hypotheses (h2) and (h3).
- F7 checked. The eta-cube half-diagonal is eta. The 4-ball volume is pi^2 r^4/2 (the slicing integral is correct). pi < 22/7 by the Dalzell integral, and (242/49)(2401/1296) = 11858/1296 < 10. The distance range [rho, 10 rho] comes from the triangle inequality, 2 rho + 6 rho + 2 rho.
- (b) and F11 are correct. The support is nonempty because ||phi_P||_1 = eta^{-2} > 0.
- (c) and F8 are correct. Rounding gives |x_P - x_0| <= 1, which is better than the <= 2 used, and harmless. Then |x_q - x_0| <= C_d + 2 <= theta rho/2, and keeping the diagonal (q,q) term gives (1/4)||f||^2 c_d^2 eta^8.
- (d) and F9 are correct. The squared terms give 16 + 16, the mixed contraction gives 4, so the sum is 32 - 8 = 24. Each restricted term has 4 ordered copies, giving 6. The algebra (1 - 2u_1^2)(1 - 2u_2^2) - 4u_1^2 u_2^2 = 1 - 2u_1^2 - 2u_2^2 holds. k >= (1/3)(6/pi^4) eta^8 |x-y|^{-8} = c_* eta^8 |x-y|^{-8}.
- (e) First line: there are 36 entries, each at most C_u^2 eta^8 rho^{-8}. The lower bound uses (10 rho)^{-8}, and c_* 10^{-8} = c_K. Correct. The second-line lower bound uses only the class bound n >= theta ||f|| rho^4. Correct.
- C1 is correct. I read the cited witness definition myself. Item (e) at 68762-68763 reads "n(f) <= 10 rho^4 ||f||_inf whenever eta <= rho/6". The proof at 68808-68818 uses rho + eta <= 7 rho/6. The kernel-bounds proof at 70138-70142 cites it with no condition, but the lemma claims the upper bounds "for every such pair". The condition is not vacuous. Take rho = eta/2 and f(z) = max(0, 1 - |z-x|/rho) about a bare site x. This f is in F^+(d, theta) for every theta <= 1: n = eta^4 = 16 rho^4 >= theta rho^4, and Lip = 1/rho. A second copy at distance 2 eta has support distance 2 rho, which is in [rho, 6 rho]. So the mass upper bound fails (16 > 10). The printed route then gives only 256 C_K, not 100 C_K. Restricting the second-line upper bound to eta <= rho/6 is the right minimal repair. It changes no constant. Line citations in C1 are slightly off: the bound is at 68762-68763 (not 68760-68762), and its proof is at 68808-68818 (68804-68806 is the threshold remark). This is cosmetic.
- Note for consumers: C1 costs nothing for pairs admitted through witness-definition (h). Its threshold eta <= theta^2 rho/32 implies eta <= rho/6, since theta <= 1. The same holds for (g): int phi <= (pi^2/2)||phi|| and ||phi|| <= Lip phi, so the (g) threshold is at most pi^2 rho/64 < rho/6. The port is right not to insert this into the lemma.
- (f) and F10 are correct. At fixed s, the cell is fixed in physical units, and rho and Lip_{k_0} f are fixed. The Riemann-sum error is at most Lip x eta x vol, which tends to 0. The liminf/limsup passage is correct. Reading n(f) as n_infinity in the first line, and fixing witness membership for all large K, are explicit readings of an ambiguous source sentence. They neither strengthen nor weaken the statement.

## Verdicts

- `8.1:lem-gaussian-squares`: ported faithfully.
- `8.1:lem-free-curvature-covariance`: ported faithfully.
- `8.1:lem-kernel-positivity` (a)-(d): ported faithfully (the F_B case is conditional on H-BG, as stated).
- `8.1:lem-background-tower`: ported faithfully as an implication (H-TOWER). One missing clause (M_0 = F_B by F4).
- `8.1:lem-kernel-bounds` (a)-(f): ported with repairs. C1 is a correct and needed correction to the source's second-line upper bound. (a) holds only as the H1-MIN assumption. (d) and the (e) lower bounds rest on H3-CONT.

Checked line by line by Claude (fresh session).
