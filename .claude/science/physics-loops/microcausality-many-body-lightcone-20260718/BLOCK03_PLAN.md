# Block03 plan — all-time volume-uniform walk-expansion Lieb-Robinson bound

Date: 2026-07-18. Family: microcausality-many-body-lightcone. This is the
third block, taking exactly the task both siblings name open: "the
integral-equation reorganization into walks adjacent to the previous
bond" (block02 Purpose and N6/N7).

## Mechanism (why the Taylor level could not do this)

Block02 proved the coefficient-level count is genuinely
accumulated-support: at order k a bond need only touch the support
accumulated so far, so sequence counts grow like a factorial product and
certify only a finite time window. The walk structure appears only after
reorganizing at the Duhamel level: differentiating f(t) = [tau_t(A), B],
reducing [H, A] to the bonds touching supp(A), and applying the Jacobi
identity term-by-term turns f into a solution of f' = i[Htilde(t), f] +
R(t) whose inhomogeneity involves [tau_t(h_b), B] — the evolved BOND, a
fixed two-site object, not the growing operator. Iterating on the bond
replaces accumulated-support sequences by walks on the bond-adjacency
graph (each next bond adjacent to the PREVIOUS bond), whose count is
geometric: n_X * 10^(k-1) on Z^3. Geometric-over-factorial converges for
all t, volume-uniformly.

## Pre-battery (all OK, session record)

- Jacobi + conjugation-commutator identities: symbolic zero.
- Variation-of-constants identity: exact at rational spectrum (the
  h1 = h2 Piecewise artifact resolved by distinct eigenvalues; the
  degenerate branch is itself zero under h1 = h2).
- Intertwiner d/dt(W f V) = W R V and unitarity d/dt(W V) = 0 with
  W' = -i W Htilde, V' = i Htilde V: symbolic zero (adjoint encoded as
  an independent symbol with the derived relation, valid for Hermitian
  Htilde).
- Bond-adjacency degree on Z^3 = 10 exactly (6 + 6 - 2); walks of
  length 2 from a single-site start = 60 = 6*10; length-3 walks per
  start bond = 100 = 10^2 (a length-k walk has k-1 adjacency steps —
  first-pass miscount corrected against the enumeration).
- Reach lemma at d = 3: no walk of length <= 2 touches Y, one of
  length 3 does (sharp).
- Coefficient assembly (2J)^k * n * 10^(k-1) = (n/10)(20J)^k symbolic.
- Tail, ratio, and window-comparison instances exact.

## Theorem to land

For finite Lambda in Z^3, supplied bond Hamiltonian with ||h_b|| <= J,
A on X (n_X <= 6|X| touching bonds), B on Y, d = d_{Z^3}(X, Y) >= 1:

  ||[tau_t(A), B]|| <= 2||A|| ||B|| (n_X/10) sum_{k>=d} (20 J |t|)^k / k!
                    <= 2||A|| ||B|| (n_X/10) ((20J|t|)^d / d!) e^{20J|t|}

all t, constants free of |Lambda|. Sharp rate NOT claimed; U-integrated
and fermionic-bridge slices stay open.

## Supplied analysis context (declared, siblings' class)

Matrix-exponential calculus for finite Hermitian matrices (existence,
unitarity, termwise differentiation), existence of the time-ordered
propagator for a continuous bounded self-adjoint generator, and the
Riemann limit passage in the integral triangle inequality (finite-sum
version rebuilt and gated; limit named). Every algebraic identity gated.

## Cluster discipline

This is PR #3 in the family: the cluster-cap evaluator MUST be run and
recorded in the certificate before opening the PR.
