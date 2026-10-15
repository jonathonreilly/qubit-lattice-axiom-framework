# Independent exact coherent two-leg composition result

Reviewer `/root/inertial_response_check`; root remains scientific author.
Before reading any new author coherent-link source or result, I derived and
froze the specified ideal stationary/free coherent two-leg response, retained
both perturbed bodies and the station proper clock, and computed its exact
massless laboratory-energy Gram. The already checked general joint theorem was
known; the new author `coherent_exact_energy` work was not read or imported.
This is a narrow independent composition check, not a formal audit.

The result, in the norm convention ||h||^2=2E, is

    G_11 = G_22 = 766/(405 pi),
    G_12 = G_21 = -1871/(1620 pi),

    G = [[3064,-1871],[-1871,3064]]/(1620 pi).

The eigenvalues are 1193/(1620 pi) and 329/(108 pi), both strictly positive.
The diagonal is approximately 0.6020379575723053 and the off-diagonal is
-0.3676282697838718. These values use the specified unit-duration averages,
receiver endpoints (7/5,12/5,17/5), second channel shifted by one, separation
R=3/5, instantaneous perfect turnaround, and coupling times turnaround equal
to one. They would rescale if the count normalization or coupling product
changed.

The direct null-leg calculation gives

    chi(s)=K[eta_S(s-2R)-eta_S(s)
              + e_1.(xi_S(s-2R)+xi_S(s)-2xi_C(s-R))].

Its arbitrary initial positions and velocities contribute only an affine
function of receiver time. The (1,-2,1) contrast annihilates that function.
The station initial-clock constant cancels within each phase difference, and
there is no independent spacecraft clock in this model. Thus the compact
weights were derived without selecting zero initial data. Their direct-field
coefficient integrates to zero, also removing an additive constant scalar
perturbation from this observable; no absolute background is thereby chosen.

The proof in `COHERENT_TWO_LEG_PRECHECK_v1.md` gives the compact H1 force weights,
L2 clock weight, arrival-coordinate amplitude, all normalization factors and
the independent coherent plane-wave derivation. It was frozen together with
the checker code before the checks ran. Two exact representations agree:

- The overlap of step-hat derivatives has angular integrals 3064/405 and
  -1871/405 for channel shifts zero and one; multiplication by 1/(4 pi)
  yields the stated Gram.
- The original coherent plane-wave particular solution gives a nine-endpoint
  phase sum. The exact radial cosine identity converts it to an angular sum
  of absolute endpoint separations. Its angular integrals are -6128/405 and
  3742/405; multiplication by -1/(8 pi) gives the same Gram.

All angular pieces have rational endpoints and polynomial integrands, and were
integrated exactly. The complete piece-by-piece trace is retained in the result
JSON; the second representation does not call the step-overlap routine.

All 61 controls passed: six exact two-representation checks, one positive-Gram
check, one stationary direct-field normalization, 48 separate original null-leg
integral comparisons, two symbolic arbitrary-initial-data cancellations, one
constant-field cancellation and two exact longitudinal-plane-wave cancellations.
The 48 numerical comparisons integrate the original forced free-body and proper
clock responses from a common initial epoch, then apply the null-leg phase and
count contrast. They do not use the compact-weight or exact-Gram routines.
Their largest absolute error was 1.0145207566569258e-12, below the fixed 2e-11 tolerance.
No failed test or tolerance adjustment occurred. Stdout exactly matches the
saved result JSON, and stderr is empty.

This supplies a checked sensitivity Gram for the stipulated massless ideal
link. It is not a physical observation fit, energy supplier, actual Cassini
transponder model, massive extension or selected scalar state. Delays,
noncoherent clock terms, external reference forces, calibration uncertainty,
media and nonlinear perturbation control retain their separate scope. No new
author coherent source/result was accessed in obtaining this report. All
reviewer writes are confined to this independent directory.
