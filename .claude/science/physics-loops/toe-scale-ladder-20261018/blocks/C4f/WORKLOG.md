# C4f WORKLOG

## 2026-10-19 start
- Read C4e NOTE/REVIEW, C4b, C4c Obs. M, C4d P1, C4 action conventions (axis Q(R) = sgn(perm R)|R|).
- Key derivation: for odd R, D(Q(R)) is antidiagonal in the n-basis (Q(R)n = -n) => beta_R = (U(1) phase in N) o P_R o C.
  So axis-O covariance <=> [U,P_R]=0 (R in T) and [U, P_R C]=0 (R odd). Constraint maps k-magnon sector over
  vacuum to k-hole sector over antivacuum; NO extra constraint inside the k-magnon sector beyond T.
- Plan: U = L2 o L1, L1 = C4e squares; L2 = one involutive family {B-tetra-axes controlled by A(k) EMPTY} u
  {A-tetra-axes controlled by B(k) FULL}; generalized Lemma I with read sets F = S u Gamma,
  N1(u) = {w != u : F_w n S_u != 0 or F_u n S_w != 0}.
- Prediction (declared before computing): magnon pairs = C4e glider v = rho_b rho_c e_a; hole pairs v = -rho_b rho_c e_a.

## progress (~1h in)
- scripts: c4f_core.py (sparse), c4f_dense.py (dense torus, separate N1/N2 via incidence matrices), c4f_su2.py,
  c4f_01_axis_action.py (DONE, log PASS=10), c4f_02_verify.py sections sym/sectors/radius/inv_dense DONE (all PASS),
  inv_sparse running in background (then sym re-run). c4f_03_interface.py, c4f_04_stress.py written, not yet run.
- RESULT SO FAR: construction works: O-covariant (axis, phases), U(1), frozen singles+holes, magnon face pairs glide
  (C4e glider), hole pairs glide with -v. CA radius per layer 3.
- Resume: run `python3 c4f_02_verify.py inv_sparse` (if log missing), c4f_03, c4f_04 (<20 min each), then SUMMARY + NOTE.

## DONE (~2h)
- All runs complete; logs/SUMMARY.txt TOTAL: PASS=37 FAIL=0. NOTE.md written.
- Disclosed: first c4f_01 Part-B criterion (orbit-restricted images) gave a FAIL vs C4c r=1 count; replaced by
  C4c's exact criterion; that log was overwritten (disclosed in NOTE).
- Open for review: Lemma I' (read-set N1), parity step, Step 1.

## review corrections applied
- NOTE: status line, Lemma I' wording (56/400 site-sharing failure; one-sided variants observation), descriptive results marked not re-checked, Review dispositions.
- logs/c4f_01_superseded_RECONSTRUCTED.txt (labelled reconstructed from session output; not in SUMMARY). From now on new runs go to new log files.
