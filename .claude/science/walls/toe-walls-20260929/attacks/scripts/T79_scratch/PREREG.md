# T79 pre-registration (written BEFORE running test_T79.py)

Claude Sonnet 5.5 (same family as supervisor; same-family checks only).

Wall: the seven-item Maxwell dynamics class (L06-W10) is supplied.
Best route (R1+R3 combined): the class is not seven independent supplies. On the
compiled torus, "conserved positive diagonal energy" (item 6) is the same content
as neutral stability (bounded orbits, both time directions), and with both Gauss
rows (the granted ice rule) held as invariants the vertex/cube payload (item 7
first half) drops out. What is left is: payload count (no coin), neutral
stability / reversibility, locality. Also: the class is the Hessian of an exact
conservative gauge-invariant law, not an exact law on a bounded product domain.

## Test A (algebra, exact structure; sides 4 and 6)
Extended covariant NN class (block 03 classification, taken as given):
  phi' = w phi + g_ve d0^T E
  E'   = g_ev d0 phi + u E + r C^T B
  B'   = q C E + v B + g_bc d2^T psi
  psi' = w_c psi + g_cb d2 B
A1. Spectrum of G equals the union of 2x2 sector blocks (gradient, transverse,
    cube) plus zero-mode singles, for random parameters.
    PASS: max matched eigenvalue error < 1e-8 on both sides.  FAIL otherwise.
A2. Brute force on the grid {-1,0,1}^10 at side 4 (59049 members): "bounded" =
    all orbits bounded for t in R (numerical: Re(lambda) ~ 0 and sup norm of
    expm(tG), |t| <= 40, below 50). Predictions:
      - bounded and nonzero, no Gauss condition imposed: exactly 26 grid points
        (u=v=w=w_c=0; (g_ev,g_ve) in {(0,0),(1,-1),(-1,1)}; same for
        (g_bc,g_cb); (q,r) in {(0,0),(1,-1),(-1,1)}; minus the zero generator).
      - bounded, nonzero, and electric+magnetic Gauss invariant in the
        zero-charge sector (g_ev = 0 = g_bc): exactly 2 grid points, (q,r) =
        (1,-1) and (-1,1), everything else 0.
    PASS: both counts exact and the 2 points are those.  FAIL: any other count
    or any extra point (which would mean neutral stability plus the Gauss rows
    leave more than the one-speed curl pair, or fewer).
A3. Every bounded member admits a positive diagonal conserved form (so
    "diagonal" is not an extra demand). PASS: found for all 26.
A4. Side 6 spot check: the 26 predicted points bounded; 300 random non-predicted
    grid points unbounded.

## Test B (time-rule fork = one friction rate)
Mean dynamics of the Maxwell member with friction gamma on E (Kramers form,
noise 2 gamma keeps the Gibbs weight exp(-|E|^2/2 - |B|^2/2) invariant).
Prediction: modes propagate iff gamma < 2 sigma (sigma^2 in spec C^T C);
slow root -> -sigma^2/gamma as gamma -> inf (the diffusive rule); gamma = 0 is
the conservative member.  PASS: these hold numerically on side 6 and the
Lyapunov residual for the Gibbs weight is < 1e-12 for every gamma.
Arithmetic: ticks in 13.8 Gyr at t_Planck.

## Test C (bounded domain)
Prediction: the Maxwell flow does not preserve the cube [-1,1]^N (every sign
vertex has an exiting coordinate) while it preserves the l2 ball; so an exact
class on a product of bounded per-site intervals is empty, and the class is a
weak-field statement with per-site amplitude <= 1/sqrt(N) for a unit energy
budget.  PASS: 100% of sampled vertices exit; l2 norm preserved to 1e-12.

## Test E (class = Hessian of an exact conservative law)
Classical compact rotor law H = sum_e U E_e^2/2 + sum_f K (1 - cos (C A)_f),
Hamilton's equations on (A, E).  Prediction: exact nonlinear flow conserves H
and d0^T E; its linearisation in (E, B=CA) is the class member q=U, r=-K
(qr<0, all other coefficients 0); nonlinear-minus-linear deviation scales as
amplitude squared.  PASS: energy drift < 1e-8, Gauss drift < 1e-10, Jacobian
equals the member to 1e-12, deviation ratio ~ 4 when amplitude doubles (within
20%).  FAIL: a surviving vertex/cube coupling, or qr >= 0.

Decision readings (before seeing numbers):
 - All PASS: the price is exactly {payload count, exact reversibility (neutral
   stability), locality}, with no separate energy/diagonal/vertex/cube supply;
   outcome PRICED (sharper than "equivalent to the class").
 - A2 FAIL with extra bounded points: the class is bigger than block 02/03 say
   (report which); outcome STANDS with that as the new residual.
 - Test E FAIL: the Hessian reading is wrong; drop the misframing remark.
