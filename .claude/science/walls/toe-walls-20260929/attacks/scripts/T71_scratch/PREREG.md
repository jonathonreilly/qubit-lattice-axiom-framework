# T71 pre-registration (written before any of my own test scripts were run)

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family checks).

Wall: L14-W12, "That gravity attracts (the sign of the coupling) is not derived".

## Best route under test (R1)

Claim: in the linearised foliation-preserving class (the natural symmetry class of a
fixed lattice with a distinguished time; Horava / khronometric gravity), the sign of
Newton's coupling is not a separate datum. It is a computed function of the action's
coefficients, and the four stability conditions (tensor no-ghost, tensor gradient
stability, scalar no-ghost, scalar gradient stability) already force it positive.

Static energy functional used (lapse phi, spatial conformal factor psi, TT amplitude h):
    E = -(1/16 pi G_H) * [ xi * ((sqrt(g) R3)^(2) + phi R3^(1)) + eta * (grad phi)^2 ] + m * phi(x0)
with N = 1 + phi, g_ij = exp(2 psi) delta_ij. Hand derivation: G_N = 2 G_H / (2 xi - eta).
Published check: Blas-Pujolas-Sibiryakov, PRL 104, 181302 (arXiv:0909.3525), eq. (22)
G_N = 1/(8 pi M_P^2 (1 - alpha/2)) with xi = 1, alpha = eta; eq. (19) scalar speed.

## Test 1 (script: test1_static_sign_lock.py)

1a. Symbolic: re-derive (sqrt(g) R3)^(2) coefficients for the conformal and TT channels,
    the scalar-sector kinetic coefficient and c_s^2, and G_N.
    PASS: conformal coefficient +2 (grad psi)^2 + 4 grad phi . grad psi; TT coefficient
    -(1/4)(grad h_ij)^2; c_s^2 = xi (2 xi - eta)(lambda-1)/(eta (3 lambda-1)); G_N = 2 G_H/(2 xi - eta).
    FAIL: any mismatch (then R1's lemma is wrong as stated).

1b. Scan 2e6 random parameter draws (sign G_H, lambda, xi, eta).
    PASS for R1: zero draws with all four stability conditions true and G_N <= 0.
    Also record (not a pass condition): how many unstable draws have G_N > 0 (the converse
    fails), and that G_N changes sign through a pole exactly at eta = 2 xi.
    FAIL: any stable draw with G_N <= 0.

1c. Independent lattice solve (L=24 torus, discrete gradients, two masses, dense linear solve
    of the stationarity conditions, NOT using the closed form). Cases:
      GR-like (c=2xi, b=2xi, eta=0), Horava window (eta=1, xi=1), Horava outside window
      (eta=3, xi=1), "ground-state conformal channel" (c=-2xi, b=2xi, eta=0),
      Nordstrom-like healthy scalar (b=0, eta<0).
    PASS: pair-energy sign equals the sign of Q_eff = a (b^2/c - eta) in every case; GR-like
    and Horava-window attract; the ground-state conformal channel with eta=0 repels;
    Nordstrom-like attracts; outside the window repels.
    FAIL: any sign disagreement (then the elimination algebra is wrong).

## Test 2 (script: test2_sea_rate_hessian.py) -- member-programme face (R2)

Question: if the walker's filled sea is the only field energy for the clock (rate) field,
what is the sign of the static two-body interaction?
Model: P6 walker H = sum_x,j psi^dag (sigma_j/2i) t_j(x) psi_(x+j) + h.c., antiperiodic
L^3 torus, hops modulated t_j = 1 + eps cos(q.(x + e_j/2)) (rate at the hop midpoint).
Sea energy = sum of negative eigenvalues.
    PASS (R2 wounded, as predicted): the second-order sea energy Pi(q) <= 0 at every q
    tested (all directions, L=8 and L=12), Pi -> 0 at q -> 0 in the linear-rate variable and
    -> E_0 in the log-rate variable; sea-only two-body energy is repulsive.
    FAIL (R2 promising): Pi(q) > 0 at any q outside numerical noise.
Also record the size of the bare positive stiffness needed to make the net kernel positive.

## Kill criteria for the routes (applied in the report)

R1 dies if 1a-1c fail. R1 is wounded if it needs a premise the lattice has not delivered
(emergent spatial-diffeomorphism R3 structure of the static energy, which P6 says the fixed
lattice breaks at k = 0). R2 dies if Pi(q) > 0 anywhere. R3 (misframed) dies if the question
"sign of the TT static (shear-gradient) energy" is not equivalent to the sign in the class.
