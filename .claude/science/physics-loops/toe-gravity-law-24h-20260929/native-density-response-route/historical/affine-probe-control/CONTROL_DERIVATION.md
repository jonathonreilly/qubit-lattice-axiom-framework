# Frozen finite control, before execution

One standard-library Fraction job, at most30CPU/40wall seconds and150MiB peak
RSS, expected below5CPU/50MiB. One available slot coordinated with root.
Original deadline/STOP, resource checks and BLAS1 apply. No eigenvalue or EOS
inference is made from this control; no author source/helper is imported.

Expected identities, derived from the literal fields before implementation:
* H0=mu D+sum_e,f K_ef B_e* B_f. On an actual graph edge the diagonal onsite
  two-particle contribution is2mu. Its attractions and its S completion agree.
* Before cancellations, the absolute row bound for S is2mu on axial edges
  and3mu on plane edges; for W it is20tau,20tau,16tau in the three axial
  directions and24tau on each of six plane directions. Plane edges have TWO
  centers. Thus every absolute K row is bounded by3mu+24tau.
* If A=sum phi_x n_x, w_e=phi_x+phi_y, then
  [A,[H0,A]]=-sum K_ef(w_e-w_f)^2 B_e*B_f. The diagonal D/onsite/triple
  terms commute. The current identity is [H0,A]=-sum K_ef(w_e-w_f)B_e*B_f.
  These will be checked by direct finite-bit matrices, including overlap,
  separately from coefficient-word assembly. The factor1/2 in the ground
  spectral first moment is an analytic spectral identity, not a fitted value.
* Each local S/gradient row moves endpoint coordinates through at most three
  sites in any chosen direction. For a nearest-neighbor Lipschitz phi,
  |w_e-w_f|<=6 Lip(phi); for cos(k x1), Lip=2sin(|k|/2).

The finite control covers all nine physical edge orientations and four local
row types. It is not a full finite-density ground-state computation. The
report will separately prove the operator, volume and limit statements.
