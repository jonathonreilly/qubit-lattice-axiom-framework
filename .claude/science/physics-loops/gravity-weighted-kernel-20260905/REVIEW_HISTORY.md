# Review history — block 213

(conformance-gate pass and sol checker findings recorded at block close)

## 2026-09-04T22:03+00:00 — blind Opus F2 (Schur/metric) prediction: CHECKED (supervisor)
Deliverable: F2_blind_metric_prediction.md (1,074 lines, inline sympy script). Supervisor re-ran the script independently: PASS=59 FAIL=0. Hand-verified: with G = pi0*gamma0 and g = (1-G) I + [G(1-G)/(1-2G)] J, spec(g) = {(1-G^2)/(1-2G), 1-G, 1-G} and PD iff G < 1/2 (G=3/5 gives eigenvalue -16/5; G=1/4, -3/5, 0.499 positive) — reproduces Block 211's offset-0 PD condition. Route independence: the seat opened no other route's output.
Findings for the block (CHECKED): (F-A1) the cell metric identified from the deg-1 block via Schur is g = (1-gamma0^2) M1^{-1}, RIEMANNIAN at every PD point, so the real null cone is {0}: "the cone = the metric's cone" as literally stated is vacuous-or-false; the falsifiable form is PROPORTIONALITY of the symbol's principal quadratic part to M1 (projective conic (1+G) N = G (sum k)^2), cone invariant rho1 = -G. (F-A2) gamma0 enters and is the entire content; gamma1 does not enter at all (volumes enter only via v0/v1 = 1-gamma0^2) — kernel-side shear registration exists: the #7970 TENSION is real and must be carried. (F-A3) the metric's REFERENT is not fixed off-flat by the supplied objects: deg-1 and deg-2 both pass the Schur test and positivity cannot break the tie; rival readings differ by rho_A = -G1 (offset-1) and rho_B = G1/(1-G1) (Hodge slot); full four-slot Hodge consistency holds only at flat. Witnesses W1/W2 lie on G0 = G1 and CANNOT discriminate; W3, the mixed point, and the B209 point can. Consequence for the primary comparison: the exact symbol DECIDES which slot the kernel's metric is — that identification is itself the block's result if it holds; if the symbol matches none, that is the exact discrepancy.

## block 213 — V1-V5 (primary)

Recorded by the Fable primary (resumed seat) at block delivery; not an audit certificate.
Runs: certified baseline `TOTAL: PASS=36 FAIL=0` (exit 0, 75 s); 36 mutations, each `TOTAL: PASS=35 FAIL=1` or `PASS=34 FAIL=2` inside one family, exit nonzero, census `A 2, B 6, C 5, D 2, E 3, F 8, G 3, H 4, I 3`.

- **V1 — specific verdict-identified obstruction.** R5's named successor design task, quoted in
  GOAL.md: "the weighted-kernel construction (the cone = the metric's cone hypothesis)". The
  block turns that hypothesis into an exact statement on the Block 211 family in both
  directions: true as a cone statement exactly on the codimension-one locus `S1 = -E S0 E`,
  `g0 = g1/(1 + pi0 g1)` of eight sign cells (graded assembly), false everywhere else off flat
  (the cone is the union of two distinct Hodge readings' cones, discrepancy in closed form),
  false under the overlap assembly everywhere measured, and false in the strong form (one
  quadratic form times the identity) on the whole curved three-direction family, the locus
  included (`mu - 1 != 0`). The #7970 planning constraint is answered separately: the kernel
  registers the shear, not the diagonal metric — tension recorded.
- **V2 — genuinely new content.** (i) The fraction-free principal-part lemma at a fully
  symbolic block-diagonal cell form (`det B = +D3 (k^T D1 k)(k^T E adj(D2) E k)`, block
  structure `B = [[k^T D1, 0], [D2 W, D3 E k]]`, `W k = 0`). (ii) The observation that Block
  211's corner-sign gauge is not a symmetry of the weighted kernel, and the sixty-four-cell
  coincidence census it forces (48 flat-only, 16 curve cells) with the closed form
  `P = M1 E M2 E = (1 - 2 g0 g1) I + (g1 - g0 - pi0 g0 g1) S0`. (iii) The locus theorem
  with its branch constants `{1, mu, 1/(1-g1^2) x2}` and two explicit QQ(sqrt 6) witnesses
  on the family. (iv) The exact overlap cone `Q+ Q-` and the two-direction effective shear
  `c_K = 2 c v^2/(3 v^2 + 1 - c^2 (v^2 + 1))`. None of these exists in Blocks 105-212; R5
  proved only the flat symbol.
- **V3 — audit lane could NOT already complete this.** The result needs the chain's specific
  objects (Block 201's graded raising part and completion pattern, Block 105's two assemblies,
  Block 209's wedge signature, Block 211's family and gauge classes) and exact symbolic
  linear algebra over QQ(t, u), QQ(g0, g1, v0, v1) and QQ(sqrt 6); the audit lane's generic
  checks carry no such construction, and the draft runner it would have audited never
  completed a baseline.
- **V4 — no observed target, fit, literature constant or continuum equation is load-bearing.**
  Every number is an exact rational or symbol on a finite bench; no float is evidence (gate I);
  PR #7970 is quoted at its own conditional scope as the other side of a tension, not as input;
  no literature dispersion formula is used.
- **V5 — materially changes rather than relabels.** The first draft's headline ("never one
  metric's cone off flat") is refuted and replaced by a sharper two-sided theorem (correction
  113, against this block's own draft); eight predecessor defects are fixed with their reasons
  (three of them declared literals whose gates would have failed); and the block converts R5's
  open hypothesis into a closed statement with an explicit locus, an explicit discrepancy, and
  a named tension for Block 214. Nothing is relabelled: the flat control, Block 201, Block 211
  and R5 reproduce unchanged.
