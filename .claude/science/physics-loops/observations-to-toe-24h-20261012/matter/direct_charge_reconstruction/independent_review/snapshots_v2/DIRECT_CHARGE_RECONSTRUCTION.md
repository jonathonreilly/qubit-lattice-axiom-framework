# Matter charges reconstructed from consistency and measured neutrality

Direct parent derivation. Status: conditional-support. The gauge algebra,
chiral representation inventory, one Higgs doublet, allowed mass couplings
and ordinary local anomaly conditions below are supplied hypotheses informed
by observed matter. This is a reverse reconstruction inside a known effective
theory family. It does not derive the gauge algebra, particle inventory,
three generations, masses or a native microscopic chiral phase.

## 1. Keep the unknowns upstream of their familiar numerical values

Work with left-handed Weyl fields, including conjugates of right-handed
fields. For one generation use the following SU(N_c) x SU(2) representations
and unknown hypercharges; the physical application takes N_c=3.

| Field | Color | Weak representation | Hypercharge |
| --- | --- | --- | --- |
| Q | fundamental | doublet | q |
| u^c | antifundamental | singlet | u |
| d^c | antifundamental | singlet | d |
| L | singlet | doublet | l |
| e^c | singlet | singlet | e |
| n^c, when present | singlet | singlet | n |
| H | singlet | doublet | h |

Here e is a hypercharge variable, not the measured elementary charge. Later
we write e_ref=|q_e| for the latter. The Higgs is a scalar and contributes
no Weyl-fermion anomaly. Supply h>0 and a vev in its lower component. The
unbroken generator that annihilates that vev is

    Q_0=T_3+Y/(2h).

Its overall gauge coupling defines an as-yet-unfixed charge unit e_0. Taking
h=1/2 is a convenient Lie-algebra normalization, not a choice of the
primitive global charge lattice.

Gauge invariance of Q H u^c, Q H^dagger d^c, L H^dagger e^c and, if supplied,
L H n^c requires

    u=-q-h, d=-q+h, e=-l+h, n=-l-h.                 (1)

The relevant weak contractions use the invariant antisymmetric tensor or
the conjugate doublet; (1) records their hypercharges. It does not predict
that any particular Yukawa coefficient is nonzero. Nonzero mass terms
connect components of equal unbroken electric charge, so electromagnetism
is vectorial on the resulting Dirac fields. This is a consequence of the
supplied Higgs/mass structure, not an extra assumption of the final fractions.

In an all-left-handed convention the local anomaly coefficients, with
irrelevant common group-index factors suppressed, are

    A_3=2q+u+d,
    A_2=N_c q+l,
    A_G=2N_c q+N_c(u+d)+2l+e+[n],
    A_Y=2N_c q^3+N_c(u^3+d^3)+2l^3+e^3+[n^3].     (2)

Square brackets denote the optional n^c. The SU(N_c)^3 anomaly cancels
between two fundamentals and two antifundamentals. Mixed nonabelian/abelian
coefficients with a single traceless nonabelian generator vanish. There is
no perturbative SU(2)^3 anomaly, but its ordinary global doublet obstruction
requires N_gen(N_c+1) even. For N_c=3 this is automatic for every integer
generation count; it does not select three generations. We assume ordinary
four-dimensional spin gauge theory and no additional anomaly-cancelling
sector or inflow. These polynomial and doublet tests are not a classification
of all possible global anomalies or quantum-gravity completions.

## 2. Which mass hypotheses remove which freedom

Without n^c, substituting (1) yields

    A_3=0,
    A_G=l+h,
    A_Y=(l+h)^3-6h^2(N_c q+l).                    (3)

Together with A_2=0 the one-generation conditions give
l=-h and q=h/N_c. Thus at N_c=3, h=1/2 the usual electric fractions follow.
The cubic condition would also give l=-h on this real one-generation
surface. The representation and Yukawa premises carry essential information.

With a Dirac n^c the linear coefficient instead vanishes identically and

    A_Y=-6h^2(N_c q+l).                           (4)

Consequently A_2=0 is the only remaining charge relation after (1). Define
epsilon by q=h(1+2epsilon)/N_c and l=-h(1+2epsilon). For N_c=3,

    Y=2h [Y_SM+epsilon(B-L)],
    Q_0=Q_SM+epsilon(B-L).                        (5)

The B-L values here are +1/3 on Q, -1/3 on u^c,d^c, -1 on L, +1 on
e^c,n^c and zero on H. Equation(5) is a familiar anomaly-free freedom, not
a newly discovered matter theory. Positivity of the earlier gravitational
scalar kinetic matrix places no restriction on this separate gauge charge.

For the physical particles at N_c=3, in e_0 units,

    Q_u=2/3+epsilon/3,   Q_d=-1/3+epsilon/3,
    Q_e=-1-epsilon,      Q_nu=-epsilon,
    Q_p=1+epsilon,       Q_neutron=epsilon,
    Q_W+=1.                                             (6)

The nucleon charges follow from the conserved vector charge of their quark
content: sea quark-antiquark pairs and electrically neutral gluons do not
alter the total. Confinement and the identification of nucleons with those
three-quark charge sectors are supplied physical identifications. No nuclear
mass or strong-interaction spectrum is calculated here.

A bare n^c n^c Majorana term carries hypercharge2n=4h epsilon. A Weinberg
operator (L H)^2 carries2(l+h)=-4h epsilon. Either supplied nonzero term
forces epsilon=0 in this family if the same electromagnetic U(1) remains
unbroken. A scalar vev must have zero charge under the unbroken generator
Q_0; nonzero hypercharge alone does not forbid it, as the Higgs illustrates.
For the displayed gauge-singlet n^c n^c or singlet (LH)^2 operator, a scalar
compensator is an SU(2) singlet. Its compensating nonzero hypercharge then
also gives nonzero Q_0 charge, so its vev cannot preserve that same photon.
Extra gauge factors or different weak contractions/breaking sectors require
a different analysis.

This does not infer a Majorana mass from oscillations. A general mass matrix
can pair opposite charges into charged Dirac states; the statement just made
uses the common-charge family in (5), where the relevant charges are equal.
Neither neutrino oscillation nor a small finite charge bound supplies an
exact zero or proves a particular mass-generation operator.

## 3. Why inter-family mixing is a real hypothesis

In a mass basis write the charged-current term schematically as
bar(e_alpha) gamma^mu P_L U_alpha_i nu_i W^-_mu. Unbroken electric gauge
invariance requires, for every nonzero entry,

    Q_nu_i-Q_e_alpha=Q_W+.                        (7)

This sign also follows from W^- -> e^-+antinu. Make a bipartite graph with
charged and neutral mass eigenstates as vertices and nonzero U entries as
edges. At fixed Q_W, define a_alpha=Q_e_alpha+Q_W and b_i=Q_nu_i.
Every edge says a_alpha=b_i. The incidence matrix on six vertices has rank
6-c, where c counts connected components including isolated vertices. Thus
a connected graph has one common value and removes flavor-dependent
electric charges. The same reasoning applies to connected quark charged
currents. This is an exact algebraic connectivity statement; tiny but nonzero
edges suffice. It does not derive observed mixing from an arbitrary matrix.

As a check on the necessity of this premise, take three generations without
n^c, common q=h/3, and l_1=-h+t, l_2=-h-t, l_3=-h. All local anomaly
sums vanish for any real t after the charged Yukawa relations. This is the
well-known lepton-family-difference loophole. Its flavor-dependent charge
assignments cannot satisfy a connected observed charged-current graph with
nonzero mixing across the differently charged sectors. Additional mass
operators must also be checked; a massless disconnected example does not
explain neutrino oscillation. The one-generation result in (3) alone was
never a proof covering every three-generation theory.

The runner checks all512 possible three-by-three support graphs. This proves
an incidence-rank identity by exhaustive finite control, supplementing the
elementary path proof. It does not claim that every graph is the support of
a unitary mixing matrix. Connected physical mixing is a supplied observation-
motivated condition; no oscillation angle or charged-current likelihood is
fit here.

## 4. Local charge algebra is not a global charge lattice

For a specified compact U(1) with fixed period, its representation weights
are integers in a primitive normalization. Equation(5), considered for all
real epsilon, is only a Lie-algebra statement. Arbitrary irrational epsilon
does not exponentiate to the chosen compact group.

First impose the extra global hypothesis that z=6Y is integer with h=1/2,
so the Higgs has fixed integer weight z_H=3. The weights are

    z_Q=1+2epsilon,  z_u=-4-2epsilon, z_d=2-2epsilon,
    z_L=-3-6epsilon,z_e=6+6epsilon,  z_n=6epsilon, z_H=3. (8)

For the direct-product group they are all integers iff

    epsilon in (1/2) Z.                           (9)

For the specified standard Z6 quotient, a field of color triality t and
weak-doublet parity w must also obey

    z+2t+3w = 0 mod6.                            (10)

This follows directly from the phase of the center element
(exp(2pi i/3)I_3, -I_2, exp(i pi/3)). The Q row of (8) then requires
2epsilon divisible by6, and that is sufficient for every row:

    epsilon in 3 Z.                              (11)

The intermediate fixed-lattice Z2 and Z3 quotient hypotheses give epsilon
in Z and (3/2)Z respectively. They are checked as supplemental group
controls selected before the first runner execution. No experimental
monopole, line-operator spectrum or primitive lattice was supplied.

Under any of these fixed-lattice hypotheses, a sufficiently small finite
bound can select epsilon=0 from the discrete set. In the near-standard
branch epsilon>-1, the direct-product lattice's smallest nonzero absolute
neutron charge in electron units is1/3; the standard Z6 lattice's is3/4.
These gaps depend on fixing the primitive embedding, not merely uttering
the word compact.

If that embedding is left unknown, compactness alone supplies no such
finite gap. For epsilon=1/D with D=10^k, k>=1, all the hypercharges in
(5) with h=1/2 are integer multiples of1/D. Indeed D is even and D=1
mod3; the n^c weight becomes exactly1 and the Higgs weight becomes D/2.
These are primitive, well-defined representations of a compact direct-
product U(1), with the gauge coupling rescaled consistently. Anomaly and
Yukawa identities remain exact. The normalized neutron charge is1/(D+1),
arbitrarily small but nonzero. This construction changes the globally
allowed charge lattice; it does not claim to keep the fixed lattice (8).

The distinction prevents two opposite overclaims: a continuous real family
is not automatically a representation of a fixed compact group, and an
unspecified compact group does not by itself remove every sufficiently
small rational charge deformation.

## 5. Define the measured charge unit before using a neutron result

Near epsilon=0 take epsilon>-1, so e_ref=|q_e|=e_0(1+epsilon). Define

    delta=epsilon/(1+epsilon), epsilon=delta/(1-delta).

The observable charges in electron-charge units are exactly

    q_p/e_ref=1, q_e/e_ref=-1, q_neutron/e_ref=delta,
    q_nu/e_ref=-delta,
    q_u/e_ref=(2-delta)/3, q_d/e_ref=(-1+2delta)/3,
    q_W+/e_ref=1-delta.                           (12)

Thus beta-decay charge conservation holds:
q_neutron=q_p+q_e-q_nu. In particular hydrogen neutrality is automatic
throughout this family; it cannot select delta=0. A nominally neutral atom
or molecule with Z protons, Z electrons and N neutrons instead has

    q_body/e_ref=N delta.                         (13)

This is the appropriate composition-dependent electric signal, despite
q_p+q_e vanishing exactly. It is not a change in the universal scalar
gravitational coupling.

## 6. Return the neutrality experiment to its measured combination

Let x=(q_p+q_e)/e_ref and y=q_neutron/e_ref without imposing (12).
An electrostatic force on a gas molecule depends on Zx+Ny. The SF6
experiment of Bressi et al. explicitly assumed neutral antineutrinos to
interpret its summary as x=y. We instead use the same published response
coefficient for the combination

    s=(Zx+Ny)/(Z+N),
    Z=70, N=76, A=146.                            (14)

These are the nominal integer molecular counts used in the paper's table.
This is a summary-level recasting at that composition/nucleon-mass
approximation, not an isotope-resolved or raw acoustic reanalysis. The
experiment's polarization calibration and subtraction of opposite-polarity
systematics remain assumptions of the published s estimate. An unresolved
even-polarity offset would be degenerate with a true charge signal.

The reported polarity means, in10^-21 units, are+9.1+/-1.4 and-9.3+/-1.6.
Their half-sum is-0.1 with uncorrelated propagated uncertainty about1.063,
reported rounded as1.1. The half-difference9.2 is the odd nuisance component,
not evidence of molecular charge. We use the published rounded s result
(-0.1+/-1.1)e-21. The primary source and its explicit neutrino assumption
were inspected in the text and rendered pages2,3,13. No figure points were
digitized as new independent observations.

Use the separately published Baumann et al. neutron summary
y=(-0.4+/-1.1)e-21 to calibrate delta in (12), without using s. The frozen
transfer prediction is then

    s_pred=(76/146) delta_cal.                    (15)

The molecular value is already exposed development data, so even a good
agreement is not a blind empirical validation. Report the residual and its
uncertainty under an explicit independent-Gaussian summary approximation.
An optional joint fit uses both summaries with design vector(1,76/146);
its parameter estimate is a new calibration, not the preceding transfer test.

For comparison, without the anomaly-family relation x=0, the two summaries
give directly

    y=y_neutron,
    x=(146 s-76 y)/70,
    q_nu/e_ref=x-y=(146/70)(s-y).                  (16)

The last equality uses beta charge conservation and the ordinary particle/
antiparticle sign, but never neutrino neutrality. Covariances must be
propagated through the entire linear map; x and y are correlated after the
inversion. In the candidate (12), q_nu/e_ref=-delta is a model relation,
not an independently measured neutrino charge.

Neither selected historical summary is claimed to be the latest or strongest
limit. We have no raw neutron events, acoustic likelihood, covariance between
systematic effects or global neutrino-charge fit. Reported uncertainties
cannot be promoted to rigorous bounds on every theory. Finite measurements
constrain this residual parameter; exact zero requires an additional exact
structural input such as the mass or fixed-lattice premise above.

## 7. What joins the earlier gravity candidate, and what stays free

One may place these gauge, Higgs and Weyl fields in a generally covariant
matter action S_m[gtilde,A,H,psi], with gtilde=exp(2alpha.phi)g_* from the
previous tensor/scalar reconstruction. Gauge-covariant derivatives and a
spin connection then couple the same specified matter sector to the physical
metric. Masses from the Higgs/Yukawa sector are proper masses; their rest
energies and clock splittings couple to proper time as in the earlier clock
block. At classical level in four dimensions, Maxwell/Yang-Mills kinetic
terms are conformally invariant and share the physical null cone.

This embedding is a supplied effective action, not a derivation of its
parameters. Its local gauge anomalies must cancel for consistency of the
gauge and gravitational Ward identities. Their cancellation does not fix
G_*, alpha, K, the Higgs scale, gauge couplings, Yukawa matrices or the
scalar quantum state. Quantum running and trace anomalies require a
specified renormalized matter theory; this block has not computed them or
established composition-independence of arbitrary quantum material bodies.

The surviving inference is narrower and useful: adding a Dirac neutrino
sector can reopen electric-charge freedom, observed mixing removes separate
flavor freedoms only under its connectivity hypothesis, and molecular
neutrality tests a neutron-weighted combination that must be reconstructed
before selecting the theory parameter. This closes a source-to-observable
relation while leaving the larger TOE reconstruction open.
