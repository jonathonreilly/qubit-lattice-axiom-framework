# x11b criteria (written 2026-10-28 ~05:07 UTC, AFTER the x11 run (05:04:36-05:04:41) had been read, and before any x11b script)

Disclosure. x11 showed that κ_PO and κ_V are **each** independent of ξ to 1e-16 (every Wick contraction in both parts has
a curl L_r of a corner plaquette on one side, and covariant-gauge changes add only gradient⊗gradient terms). So x11's A1
("gauge independence") is satisfied structurally and does **not** test the relative sign and normalisation of κ_V against
κ_PO. x11 D failed its pre-registered absolute threshold (e(1e-3) = 0.108 > 1e-2, ratio 0.19 ≤ 0.2): the threshold was not
scaled to the quartic size |X|⁴ of unit Gaussian SU(3) link logs, and the two g values used different random samples.
x11b supplies the discriminating check that x11 lacked, plus a same-sample re-test of D. Both are post-x11 and labelled so.

F (load-bearing for κ's value; discriminating). Complete axial ("comb") gauge on the periodic T⁴ torus: tree = all
  direction-4 links except those leaving x_4 = T - 1; direction-3 links on {x_4 = 0} except leaving x_3 = T - 1; direction-2
  links on {x_3 = x_4 = 0} except x_2 = T - 1; direction-1 links on {x_2 = x_3 = x_4 = 0} except x_1 = T - 1 (a spanning tree;
  T⁴ - 1 links). It contains a star corner tree at the origin (U_1(0), U_2(0), U_3(0), U_2(e_1), U_3(e_2), U_3(e_1)), so the three
  corner plaquettes are single non-tree links and the path-ordering part κ_PO^tree is identically 0. Gaussian on the
  non-tree links with S_2 = ½Σ_P|L_P|² (no gauge-fixing term; trivial Faddeev-Popov determinant for a complete tree gauge);
  the flat (toron) null directions are removed by the minimum-norm solution (CG from 0; the corner curls are orthogonal to
  the null space). κ^tree := κ_V^tree computed with the same vertex formula as x11.
  - F1 PASS iff |κ_PO^tree| ≤ 1e-12 at every T (structural).
  - F2 PASS iff |κ^tree(T) - κ^cov(T)| ≤ 0.05·|κ^cov(T)| for T ∈ {6, 8, 12}, with κ^cov(T) the x11 covariant value at the same T
    (recomputed at T = 6, 8). A sign error in κ_V would give ≈ 0.0037 against ≈ 0.0128; a factor-λ error in S_3 is excluded
    because the covariant value is κ_PO + λκ_V^cov and the tree value λκ_V^tree.
D' (post-hoc re-test of D). The same 200 random plaquettes (unit Gaussian logs, 100 SU(2) + 100 SU(3)) at g ∈ {1e-2, 1e-3, 1e-4},
  S computed from the eigenphases (2/g²)Σ_i 2 sin²(θ_i/2). PASS iff e(1e-3)/e(1e-2) and e(1e-4)/e(1e-3) are both in [0.08, 0.12]
  (linear convergence: the remainder is the O(g) quartic term).

Resource rules as x11. Expected < 5 min, < 1.5 GB.
