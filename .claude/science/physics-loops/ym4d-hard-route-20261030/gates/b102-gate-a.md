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
