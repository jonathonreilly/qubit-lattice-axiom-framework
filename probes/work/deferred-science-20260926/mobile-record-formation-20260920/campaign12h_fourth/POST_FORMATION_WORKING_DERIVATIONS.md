# Fourth campaign: provisional post-formation calculations

Recorded by the primary author at 2026-09-23 17:33 UTC, before implementing
the proposed second-event and cube controls. These are working arguments,
not independently checked results or retained claims. The first ring-spectrum
packet is separate and already has author controls; its blind reconstruction
is in progress.

## Eight-site rotor ring: proposed second-event clock

Take the checked supplied rotor target H = eta H2 + delta H4,
eta = delta/epsilon^2, on the alternating eight-site ring after one formation.
There are six occupied sites (one negative and five positive records), two
B holes, and P has dimension 36 per rotor phase. Enumerate the full 168
charge configurations: P=36, Q1=96, Q2=36. If A=T[Q1,P] and
Z=T[Q2,Q1] A, use H2=-A* A and H4=(A* A)^2-Z* Z/2 from the checked parent.
Effective resolved formation B_{e,sigma}=-j_{e,sigma} A lands in the fully
occupied 28-state charge sector. Coherent formation sums the two signs.

Prediction to check: Gamma=sum kappa B*B = 4 kappa Q_adj, where Q_adj
selects adjacent occupied B pairs, and the two-hole complement is also adjacent.
The weighted word-shift decomposition has six sectors. Each sector's
H2+4I is bipartite between four adjacent and two opposite B-pair states.
For generic word twist its off-diagonal rectangular block has rank two.
The two-dimensional zero subspace lies entirely in Q_adj; the other
eigenspaces have Q_adj compression one half. Thus the secular loss should be
2 kappa I + 2 kappa P_flat. Each actual localized first-formation output
should have flat weight one half, independently of normalizable field state
and resolved/coherent choice. H4's secular compression preserves P_flat.

Proposed compact-time survival limit as eta tends to infinity:
S(t) = (exp(-2 kappa t)+exp(-4 kappa t))/2.
Exceptional rotor phases with a rank drop must be separately identified;
they cannot be assigned positive mass by a normalizable rotor wavefunction.
Prove pointwise finite-matrix averaging and then dominated convergence for
each fixed trace-class field state. Do not claim a uniform phase/volume gap,
full field-density convergence, or convergence of mean waiting times merely
from compact-time distribution convergence.

Before first formation this ring has H2=-8I, H4=24I and total first-event
rate 16 kappa, if the checked parent formulas apply. Then proposed limiting
count probabilities are
P4=exp(-16 kappa t),
P6=(4/7)exp(-2 kappa t)+(2/3)exp(-4 kappa t)-(26/21)exp(-16 kappa t),
P8=1-(4/7)exp(-2 kappa t)-(2/3)exp(-4 kappa t)+(5/21)exp(-16 kappa t).
Check every normalization, algebraic identity, averaging hypothesis and
instrument dependence. Instantaneous hazard at t=0 may differ from the
derivative of the limiting curve; this is a possible boundary layer, not
an excuse to assert convergence of derivatives.

Scope: a unit-rotor-first limit has no generated electric E^2 term. This is
not the simultaneous finite-spin scaling that produces the prior field.
An eight-site ring has no four-edge magnetic loop. A checked clock theorem
here would close one repeated-formation question, not the common matter/field
or TOE objective.

## Cube: proposed second-event loop readout

Use cube vertices 0..7 (bit labels), edges differing in one bit, and
A={0,3,5,6}, B={1,2,4,7}. Orient edges from low to high. Five independent
cycle phases remain after a spanning-tree gauge choice. The after-first-birth
charge-space dimensions again are 168,36,96,36. The terminal sector has 28
states. The same A,Z,H2,H4,B formulas apply with degree three.

Condition on first resolved formation on oriented edge 0->1, sign sigma1.
The old positive record at A0 moves to B2 or B4. Its actual normalized output
is the coherent sum of these two paths, including their link shifts and the
creation link shift. A second formation on edge 6->7 has two paths that
exchange the old-hop destinations 2 and 4. Both paths give the same final
charges and creation shifts. Their relative phase is the square
0-2-6-4-0. Proposed per-sign second instantaneous marked rate:
kappa [1 + cos(Phi_square)]. Proposed total second-event instantaneous
hazard, summing all second marks: kappa [8 + 2 cos(Phi_square)].
These coefficients are predictions before the matrix calculation, not facts.
Check resolved and coherent first instruments separately, exact link-word
signs, all alternate paths and normalization. Preserve a falsified prediction.

If established, the composed formation instrument would measure a
gauge-invariant loop. This is only an immediately subsequent event / zero
intervening-time statement. Fast motion is order epsilon^-2, so its survival
under finite laboratory-time averaging is a distinct proof obligation. The
next useful calculation is the full H2-secular loss/instrument on cube
fibers, including H4, degeneracies and actual normalizable outputs. A rotor
phase-dependent count is still not a theorem for joint spin/epsilon field
scaling or dynamical electric E^2.

## Finite-matrix averaging route to scrutinize

For K_eta=eta H+F, F=delta H4-i Gamma/2 with Gamma>=0, write the contraction
in the H interaction picture. F_bar=sum_lambda P_lambda F P_lambda.
The integral of each off-diagonal block has norm bounded by
2 ||P_lambda F P_mu||/[eta |lambda-mu|]. Integration by parts in Duhamel
gives a compact-time O(1/eta) estimate at each fixed finite fiber. A bound
by two then allows state-weighted dominated convergence over phases even
without a uniform gap. Check the nonautonomous contraction and integration
by-parts details explicitly before using this as a theorem. This alone
controls survival/count observables diagonal in phase; it does not control
the full cross-phase density matrix in the original picture.
