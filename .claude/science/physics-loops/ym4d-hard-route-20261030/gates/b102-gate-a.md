lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T11:42Z

# b102-gate-a: referee of `library/b102.md`, first half (H1-H14, through Lemma O)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, at commit 799a4acd0. One line-by-line reading; not an audit.

Status: in progress. Sections are added as they are checked.

## Working notes (replaced by the final report at the end)

- H1 (L244-319): redone. C>0, QH=I, P^2=P, G=PG=GP*, KG=P*, QG=0, the minimum and the equivalence of stationarity with (H1.3) all hold. No defect.
- H2 (L321-408): redone. Self-map (4C_2 r^2 <= r/B_0), Cauchy bound 9C_2 r, contraction 1/2, (H2.4) by shrinking s, range r/4 and (H2.5). No defect.
- H3 (L410-515): redone. Weight ratio e^{kappa d} needs the triangle inequality for d (stated as a metric); scale ratio L^A e^{delta d/4} from g delta/4 >= A log L; (H3.4) by differentiating D = C(A'-HD) twice. No defect.
- H4 (L517-598): redone. Image bound B_0|J| + 4B_0C_4 r^2 < r; Cauchy on |t| = 2r/N(v) gives 8C_4 r; Lipschitz 1/4; (H4.3) with 4/3 <= 2. No defect.
- H5 (L600-631): redone; the premise U in U_k(t_0) is implicit in the wording. No defect.
- H6 (L633-802): the plaquette expansion, the cubic coefficient (H6.1), the word bound, the Cauchy steps, (H6.2), (H6.4)-(H6.6) (all eight terms) and the eight term-by-term bounds were redone; each holds under (H6.7). The identification with CMP 102 (39), (80), (189) is checked against the paper below.
- H7 (L804-847): redone. (H7.2) from differentiating (H7.1), Neumann bound (H7.3) and the kernel reading with v = l^{-d} delta. Holds under its stated operator premises. No defect.
- H8 (L849-896): redone. Both Gram inequalities, the Schur bound tM on WNW^{-1} - N and the entry bound (2/m) e^{-td}. No defect.
- Section 4 (L898-1105): Open lemma O matches CMP 99b (3.26) with a = 1 (checked on the printed page 393-394: (3.16), (3.21), (3.25), (3.26)). Attack 1's flat example (da = 0, RD*a = 0, D*a = f) is right; Attack 2's seam configuration is right. Neither is used later.
- Lemma O's statement (L905-937) against the printed CMP 99b: K_U is Balaban's Delta_a(U) of (3.26) at a = 1 with the Dirichlet compression Omega_0 Delta_a Omega_0 of (3.27); (O2) is the first two members of (3.42) for G(U), which Theorem 3.3 asserts (p. 399). Theorem 3.1/3.3 assume only (3.35); O also assumes (3.36), which only weakens O. The other members of Theorem 3.3 (G nabla*, Delta_U G, Hoelder (3.43)-(3.45)) are not in O.
- H9 (L1247-1344): (H9.1) matches (3.16) at d = 4, a = 1 with the physical row pairing. (H9.2) is the flat composite of the straight average: CMP 98 (89) carries endpoint factors that cancel the contour terms at the identity, and (125) is the straight main term, so Q_j(1) = n^{-5} sum over the block and the path. The telescoping and Q^0 D ker Q'^0 = 0 hold with the bond-before-difference convention.
- H10 (L1346-1457): redone. (H10.2) is a fixed-L Taylor bound; (H10.3) second line: coarse plaquette minus I vanishes on pure gauge, linear part has l^1 weight L^2, remainder C_L(u+v)v; the bootstrap (H10.4) closes with sum t_r < 1/(L-1); (H10.5) by submultiplicativity of row and column norms and telescoping; (H10.6) site transports; (H10.7) by Schur (row C_L s times column C_L eta^4 s^{-3}). CMP 98 (124)-(126) confirms the one-step Jacobian is the straight main term plus O(L^2 alpha_0) corrections. No defect.
- H11 (L1459-1567): redone. (H11.3) pillar Poincare with cutoffs; Q'Q'* = I in the top pairing; P is the orthogonal projection onto ran(SQ'*), so R = proj onto D*D ker Q' independent of the scalar mass; (H11.5) and (H11.6) re-derived by elimination; the Gram lower bound via the right inverse F. The local flat inverse is flat-port (8.1)-(8.5), the same four-variable system (B_v = C*C + DD* + Q*aQ, a = 1). No defect.
- H12 (L1569-1679): redone. (H12.1) by expanding forward and backward shifts; (H12.2) through the quadratic forms; (H12.3) the Wilson Hessian in the chart e^{i eta a}U is q*q with q = the holonomy curl, plus sixteen insertion terms each carrying P_p - I, so the error is eps s^{-2}, matching (3.10)'s (Re U(dp) - 1) and Im U(dp) terms; (H12.4) by multiplying out; (H12.5) with bounded overlap and the dual-norm localisation; Schur complement and the E-norm lower bound c_L J_E; then L_U >= (c_L/2) J_E. No defect.
