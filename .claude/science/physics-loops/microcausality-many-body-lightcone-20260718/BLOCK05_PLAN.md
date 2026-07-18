# Block05 plan — finite-range (plaquette-inclusive) walk-expansion LR bound

Date: 2026-07-18. Fifth block. Takes the many-body Hamiltonian-level
prerequisite of the CT note's named `U`-integrated open item: the term
class {bonds, faces} on Z^3 with ARBITRARY finite site dimensions
contains Kogut-Susskind-shaped gauge Hamiltonians with DYNAMICAL links
at fixed finite link dimension (edge -> endpoint assignment; magnetic
plaquette terms become face-supported, electric link terms
bond-supported). The gauge-measure / transfer / correlation-control
side of the U-integrated item is NOT touched and stays open.

## Inputs

- Worker b05 enumeration (worker_b05_analysis.md, worker_b05_enum.py)
  GRADED CORRECT against supervisor derivations computed independently
  before reading worker output: bonds/site 6, faces/site 12, bond-bond
  10, bond-face 20, face-bond 20, face-face 32, degrees 30 (bond
  start) / 52 (face start), D = 52, diameters 1 / 2, reach = exactly
  2k at k = 1,2,3 (tight), mixed length-2 walks 804 <= 936. Runner
  re-enumerates everything natively (worker output is scaffolding,
  never citation).

## Theorem shape

For H = sum h_S, S in {bonds} cup {faces}, h_S Hermitian, ||h_S|| <= J,
arbitrary finite site dims, A on X, B on Y, d >= 1 (tensor class, so
[A, B] = 0 and the clean form holds):

  ||[tau_t(A), B]|| <= 2||A|| ||B|| (n_X^S/52) sum_{k >= ceil(d/2)}
                        (104 J |t|)^k / k!

all t, volume-uniform; n_X^S <= 18|X|; activity scale 104J; cone
dilation factor 2 is REAL (face-jump sharpness exhibit: one adjoint
step reaches distance 2); readout v <= 208eJ, NOT sharp.

## Key gates

Native re-enumeration (two box radii); reach tightness k = 1,2,3;
face-jump one-step distance-2 arrival; ceil(d/2) arithmetic;
mixed-dimension instance (dims [2,3,2]) proving dimension-blindness;
Z2 KS-shaped instance (4 link qubits + far link, magnetic
face-supported, electric bond-supported, [B_p, E_l] != 0); coefficient
identity (2J)^k n 52^(k-1) = (n/52)(104J)^k; tail instance re-gate.

## Cluster discipline

PR #5: the evaluator must address B04's "no fifth block planned from
this session's toolkit" statement — honest reversal recorded: the goal
directive tasked running down the lane, and the new input (term-
adjacency geometry + range-2 dilation) is exactly the "genuinely new
input" that statement said was missing.
