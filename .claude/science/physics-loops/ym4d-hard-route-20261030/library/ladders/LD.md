# Ladder LD: local large deviations at speed N^2 (the estimate that spends N)

Target (row 1708, library/gap-largen-build-fable.md section 7): for 4D SU(N) Wilson at 't Hooft coupling beta, with master field W_beta, a cube is bad if some loop of length <= l0 in it has |tr U_l - W_beta(l)| > eps; for separated cubes Delta_1..Delta_k at distance >= L, mu(all bad) <= exp(-c N^2 k), uniformly in volume and boundary condition.

| Rung | Statement | Status | Row | Gate |
|---|---|---|---|---|
| LD1 | (LD) at strong coupling with explicit constants, from a log-Sobolev inequality with constant of order N (Shen-Zhu-Zhu 2023; Nissim 2025 Theorem 1.5, as Luna reports) | PROVED (unchecked) | 1717 | proof by hand, checked |
| LD2 | Concentration of one Wilson loop at speed N^2 conditional on a good boundary (single cube, any beta in a stated range) | split: variance N^-2 for most sources PROVED at every beta (unchecked) | 1717 | |
| LD3 | Decoupling of separated cubes | PROVED at every beta, no PS (unchecked) | 1717 | |
| LD4 | (LD) at order-one beta | REDUCED (Theorem R, Lemma I, Corollary U of row 1717) to (GPU) | 1717 | |
| LD5 = GPU | Planar uniqueness in a ball with free boundary: tracial w on loops in a cube with planar defect <= delta is eps-close to W_beta at the centre (quantitative); or exact uniqueness of the tracial solution of the planar equations on Z^4 (qualitative, enough for some N0) | in progress | 1720 | proof, checked; joint with PS |
