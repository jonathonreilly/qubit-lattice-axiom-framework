# Ladder LD: local large deviations at speed N^2 (the estimate that spends N)

Target (row 1708, library/gap-largen-build-fable.md section 7): for 4D SU(N) Wilson at 't Hooft coupling beta, with master field W_beta, a cube is bad if some loop of length <= l0 in it has |tr U_l - W_beta(l)| > eps; for separated cubes Delta_1..Delta_k at distance >= L, mu(all bad) <= exp(-c N^2 k), uniformly in volume and boundary condition.

| Rung | Statement | Status | Row | Gate |
|---|---|---|---|---|
| LD1 | (LD) at strong coupling with explicit constants, from a log-Sobolev inequality with constant of order N (Shen-Zhu-Zhu 2023; Nissim 2025 Theorem 1.5, as Luna reports) | in progress | 1717 | proof by hand, checked |
| LD2 | Concentration of one Wilson loop at speed N^2 conditional on a good boundary (single cube, any beta in a stated range) | open | | |
| LD3 | Decoupling of separated cubes: conditional (LD) given the exterior, distance L of order (1/m) log(1/eps), using (PS) at rate m | open | | joint with PS |
| LD4 | (LD) at order-one beta | open | | the large-N spend |
