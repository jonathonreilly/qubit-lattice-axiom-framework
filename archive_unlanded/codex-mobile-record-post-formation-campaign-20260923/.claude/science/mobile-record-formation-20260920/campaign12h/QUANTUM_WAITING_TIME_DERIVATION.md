# Primary derivation: instantaneous rate consistency versus a full waiting law

2026-09-21. New primary conditional quantum-interface calculation. It follows
the separately confirmed positive rate-operator construction and now has a
completed separate pre-source check. No physical-qubit interpretation is imported into the
minimal axioms by this calculation.

## A necessary finite-time test

Prepare two unknown physical qubits independently in six-axis pure states
rho_a and rho_c. A vacancy is exposed to these two fixed record contents,
all other neighbors vacant; suppress motion for this probe. In the classical
permanent-record process, the first formation has constant hazard

```
h(a,c)=epsilon (W^2)_ac.
```

On the j-family W_ba=1+j v_b dot v_a, this is
h(a,c)=epsilon[6+2j^2 v_a dot v_c]. Therefore the requested no-formation
probability by a specified time t is

```
S_class(a,c;t)=exp[-epsilon t(6+2j^2 v_a dot v_c)].
```

Any fixed ordinary quantum experiment, including arbitrary ancillas initially
independent of the preparation labels, feedback, internal unobserved dynamics
and final parent disturbance, has one effect E_no(t) whose expectation on
rho_a tensor rho_c gives the probability of this observed no-event history.
No Markov or square-root-instrument assumption is needed for that statement.

Fix c=+x. Compare the equal +/-x input mixture for a with the equal +/-y
mixture. Both prepare exactly (I/2) tensor rho_(+x). The requested survival
probabilities instead have mixture difference

```
Delta S(t)=exp(-6 epsilon t)[cosh(2 epsilon j^2 t)-1].
```

This is strictly positive for epsilon t>0 and j!=0. Thus the exact classical
exponential waiting laws cannot all be obtained from those unknown physical
qubits without additional preparation information. This result does not
require the newborn content label to be observable, nor the parent states
to remain unchanged. A zero-rate experiment or j=0 is the trivial exception.

If delta(t) is the largest absolute no-event probability error over all 36
product preparations, operational linearity and the triangle inequality give
delta(t)>=Delta S(t)/2. At short times,

```
Delta S(t)/2 = epsilon^2 j^4 t^2 + O(t^3).
```

This is a finite-time statistics statement in the supplied abstract time
units. It does not identify an experimentally measured discrepancy.

## Why the positive instantaneous operator is not contradicted

The previously derived total rate operator is positive:

```
R=epsilon[6 I tensor I+2j^2 sum_i sigma_i tensor sigma_i].
```

Its triplet and singlet rates are
r_T=epsilon(6+2j^2) and r_S=6epsilon(1-j^2). Take the minimal quantum jump
instrument with effects F_b=epsilon(I+j v_b dot sigma) tensor
(I+j v_b dot sigma), no additional Hamiltonian, and no additional channels.
Before the first event its unnormalized state evolves with
K_no(t)=exp(-t R/2), so

```
S_quant(a,c;t)=(1-w_S)exp(-r_T t)+w_S exp(-r_S t),
w_S=(1-v_a dot v_c)/4.
```

This survival function is affine in the input density operator and gives
the desired initial derivative -h(a,c). Its conditional hazard changes
after observing no event because that absence filters the singlet/triplet
weights. It is generally not exp[-h(a,c)t]. A product input with identical
pure parents is entirely triplet and is a special exponential case.

The mixture of exponentials is at least the exponential of its mean rate,
by convexity. More explicitly,

```
S_quant-exp(-h t) = Var_(input)(R) t^2/2 + O(t^3),
Var_(input)(R)=64 epsilon^2 j^4 w_S(1-w_S).
```

For opposite parents the coefficient is 8epsilon^2 j^4; for orthogonal
parents it is 6epsilon^2 j^4. These are differences for a particular positive
quantum-jump construction, whereas Delta S/2 is a universal lower bound
on simultaneously reproducing all classical survival rows. They must not
be confused as the same optimization.

## Consequence for the campaign

The rate-selection result establishes an instantaneous event interface and
identifies a natural quantum instrument. It does not establish a quantum
realization of the fixed-content classical continuous-time chain. The full
waiting law and repeated formation histories require separate checks, even
before transport or continuum limits are considered.

An explicit orthogonal axis register accompanying each parent supplies
preparation information that changes this conclusion: the six encoded
states can be distinguished nondestructively, and a diagonal classical
clock realizes the exponentials. A changing quantum parent and its filtered
hazard provide another consistent process, with different histories. Neither
alternative is selected or derived by the minimal axioms here. These two
positive options help locate the missing operational definition of a record.

The primary symbolic check and 1,296 directly exponentiated matrix cases pass;
the largest spectral-formula error is 1.67e-16. The initial failed symbolic
comparison, its exact source and log are preserved under
`quantum_waiting_initial_failure/`; expanding the algebraic difference fixes
the comparison. Results and final source identity are in
`QUANTUM_WAITING_TIME_RESULTS.json`. The separate report
`independent_quantum_waiting/REPORT.md`, SHA-256
`29b4ae34525945f2272b4c0da3db4ac5640554013d6692cfc982cf3b3a43614b`,
sealed at 02:34:15 UTC, confirms the waiting-law argument and explicit jump
survival. The report and checker were read completely; all five sealed
artifacts were verified. It also derives a sharp single-deadline effect
approximation, credited and reconstructed in
`QUANTUM_DEADLINE_APPROXIMATION_DERIVATION.md`. That subsequent primary note
adds a time-consistent whole-deadline construction and needs a new selective
check; the earlier report does not cover that extension.
