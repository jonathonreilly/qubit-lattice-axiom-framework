# Which native instrument and formation pieces actually compose

2026-09-13, around11:10UTC. Provisional assembly derivation, written before
its small comparator. Inputs are the explicit native instrument of PR8089
at0b00d351b4c6d4ef6fd737925f5ae403e086cc95, its supplied protected hopping
Hamiltonian, and extra supplied ready fuel/rates. No new physical axiom or
independent source-review status is claimed.

## Informative marks with a matter-independent waiting clock

Let K_ez=Q_ez U_e be the FULL physical pulse/readout operators of the
native parity instrument. Each candidate has its own extra fuel qubit,
initially|1>, with lowering a_e=|0><1| and n_e=a_e†a_e. Fix rates gamma_e>0
and a supplied active set. Define

\[
L_{ez}=\sqrt{\gamma_e}\,K_{ez}\otimes a_e,\qquad
\sum_z L_{ez}^\dagger L_{ez}=\gamma_e I\otimes n_e.
\tag{1}
\]

The identity holds on the full physical carrier, since sum_z Q_ez=I and
U_e is unitary. The no-jump generator is
H_eff=H_B-(i/2)sum_e gamma_e n_e. H_B commutes with the fuel projectors,
so a ready candidate's survival probability is exp(-gamma_e t), regardless
of matter state. For several ready candidates the race probabilities are
gamma_e/sum_f gamma_f and the waiting rate is their sum. The outcome mark
conditional on e and its time has the informative native Born probabilities
from PR8089. It is not generally a fair mark.

After the jump, that fuel is0, so all its later L_ez vanish. On each legal
branch, H_B and other candidate pulses preserve the old Z_e Record. A
supplied activation rule based only on formation geometry therefore retains
its original site-clock process when fair marks are replaced by these
informative marks. An activation rule depending on the mark values can
change the site process and is not covered by that conclusion.

This is a conditional trajectory construction, not a physically selected
Lindblad law, clock or fuel-preparation mechanism. In particular it does
NOT prove that the marks satisfy the complete neighboring-Record content
law of the earlier growing-current construction. That different model's
matter-independent probability program cannot simply be reused here.

## Exact mean matter-energy account

Write eta_e=cos(theta_e), and let H_inc,e be the sum of protected hopping
terms incident to the measured vertex. On every legal ready code branch,
the instrument identity gives

\[
\mathcal L^*(H_B)
=-\sum_e\gamma_e(1-\eta_e)n_e H_{\rm inc,e}
\tag{2}
\]

in expectation. More precisely each summand is compressed to the incoming
code of its still-unused candidate. Without that compression the full
U_e†H_B U_e has a cross term involving Z_e S_e. Its expectation vanishes
on the ready code, but it is not the zero full-carrier operator. The fuel
factor removes already consumed candidates from(2).

Since ||H_inc,e||<=6t, integrate the expected jump intensities to obtain

\[
|\overline E(T)-\overline E(0)|
\le6t\sum_e(1-\eta_e)\mathbb P(e\text{ forms by }T).
\tag{3}
\]

The same fixed H_B and energy zero are used throughout. The equality for
each jump's mean change and the triangle inequality give(3); no Gaussian
closure or state-independent sign of the energy change is assumed. This
prices the mean matter-energy change only. Controller/battery energy and
fuel preparation are separate resources, not supplied by the Lindblad form.

All K_ez and H_B commute with total matter N for the parity specialization.
The nonselective generator therefore preserves every function of N, while
individual outcome conditioning can reweight sectors exactly as in PR8089.
Sharp-N branches remain in their initial sector. No late-time current
lower bound follows from these identities alone.

## Finite collision representation

For one candidate and0<=q<=1, define full-system Kraus operators

\[
M_0=I\otimes(|0\rangle\langle0|+\sqrt{1-q}|1\rangle\langle1|),
\qquad M_z=\sqrt q\,K_z\otimes|0\rangle\langle1|.
\tag{4}
\]

Their squared sum is I. Three orthogonal environment labels realize the
isometry V=sum_mu M_mu tensor|mu>, using two qubits with one unused label.
Finite-dimensional orthonormal completion extends V to a unitary for a
supplied ready environment. With q=gamma dt, expansion of sqrt(1-q)
gives the dissipator in(1) at first order; an H_B dwell adds its Hamiltonian
term. This does not give a volume-uniform finite-step error bound, an
energy-conserving unitary extension, nearest-neighbor gate synthesis or
an autonomous controller. The finite fuel/environment cost is explicit.

## Consequence for the campaign assembly

Native matter information and the supplied geometry-based occurrence
clock can coexist on this conditional carrier, at the stated mean energy
cost. The remaining content-law/physical-program bridge is still real.
The local-program Record construction in Block19 supplies an abstract
prepared probability tree on M2, not yet the physical native control/Record
dictionary for this apparatus. Equal matrix labels are not that bridge.

The growth-current Hamiltonian also differs from the translation-invariant
full cubic Hamiltonian used in the positive-star/infrared PR8086. Its
protected-edge deletions and chosen current state do not automatically
inherit that spectral theorem. The Regge transfer construction supplies
another conditional action/sign/section and is not yet sourced by either
matter instrument. These are distinct assembly obligations, not a connected
TOE proved by collecting the separate results.
