# Fresh charged records read spin-half gauge-loop coherence

Date: 2026-09-22. Status: personal conditional construction with direct
operator proof; independent checking pending. The gauge carrier, control
pulses and birth instrument are supplied. No axiom-selected measurement law,
microscopic homogeneous-site compiler or physical photon is derived.

## 1. The operational question

The current September 4 pure-link note correctly distinguishes a fixed
electric-record distribution from an off-diagonal plaquette expectation.
Two field states can have identical complete electric-basis probabilities
and different ring expectations. This note supplies an explicit additional
probe: a local gauge-invariant pulse followed by formation of a fresh
oppositely charged record pair. Its charge contents reveal the ring
expectation. No existing record is overwritten and no extra readout bit
is appended to the charge alphabet.

The probe is a different, supplied instrument. It does not contradict the
fixed-readout statement or infer the availability of that instrument from
the framework axioms. The link-qubit quantum algebra and the record register
are explicit roles, as in the earlier gauge-matter test models.

## 2. Local gauge and pair-formation algebra

On an oriented square, let W be the product of spin-half raising/lowering
operators around its boundary. Choose a distinguished edge e whose field
is raised by W. Write

    X=W+W^dagger,       Y=-i(W-W^dagger),
    P=W^dagger W+W W^dagger,       Z=2 E_e.

Then P projects onto the two alternating/flippable field words. Direct
spin-half algebra gives

    X^2=Y^2=P,    X^3=X,    Y^3=Y,
    [Z,W]=2W,    [Z,P]=0.

X,Y,P,Z preserve every field Gauss charge, except that Z is already
diagonal and so trivially does. Thus X and Y act as Pauli matrices on the
flippable doublet and vanish on its complement. Z restricts to its Pauli Z
there; Z can be nonzero outside it.

Let the distinguished edge run from x to y. Require its matter endpoints
to be vacant for this trial, with vacuum projector P_v. The qutrit matter
contents are vacancy, charge +1 record, charge -1 record. For q=+1,-1 let

    V_q = |q,-q><0,0|_(x,y) tensor U_e^q,                             (1)

where U_e^+ is the spin-half raising operator and U_e^- its adjoint. They
act as the identity on the other field and matter factors. With incidence
positive at the tail, the full constraint is G_v=div(E)_v-Q_v. Each V_q
commutes with every G_v. Moreover

    V_q^dagger V_q = P_v (I-q Z)/2,
    sum_q V_q^dagger V_q=P_v,
    [N,V_q]=2V_q.                                                     (2)

The charge of the new record at x is q; the one at y is -q. Its complete
content is unchanged after formation in this instrument. Classical
alternative q outcomes use the separate CP branches V_q rho V_q^dagger.
At rate beta the total instantaneous loss is beta P_v, independently of
the field. This scalar loss does not imply an unchanged subsequent quantum
state or an identical motion law after the charges have been created.

## 3. Phase-cycled formation measures the real loop operator

Supply a setting s=+1 or -1, and before formation apply

    S_s=exp[-i s(pi/4)Y].                                             (3)

It can be controlled on P_v and acts only on the four field links. It
preserves all Gauss constraints and does not change existing matter
contents. The normalized birth instrument on a vacant pair is

    B_(s,q)=V_q S_s.                                                  (4)

The possible new charges remain exactly q=+1,-1. From (2), their mean is

    m_s=sum_q q Tr[B_(s,q) rho B_(s,q)^dagger]
       =-Tr[rho S_s^dagger Z S_s],                                  (5)

where rho is the normalized pre-pulse field/matter state supported on P_v.
All formulas include arbitrary spectator systems and their correlations.
The Pauli rotation, including the nonflippable complement, is

    S_s^dagger Z S_s=Z(I-P)-s X.

Consequently

    m_s=-<Z(I-P)>+s<X>,
    (m_+-m_-)/2=<X>.                                                  (6)

The cancellation of the nonflippable contribution is essential: one charge
mean by itself is generally not the ring expectation. The pair of settings
uses the same input ensemble; applying the two probes sequentially to the
same unreset state is not that ensemble comparison.

For independent trials, choose s uniformly independently of the input and
read only the new charge q. The bounded estimator s q has expectation
<X>. If the setting is itself supplied as an existing permanent control
record, both read variables are record contents; a setting label is not
silently extracted from a vacant site. A readout of the new record at y
can instead use its charge -q with the corresponding known sign.

To measure Y, replace (3) by exp[-i s(pi/4)X]. Then

    S_s^dagger Z S_s=Z(I-P)+sY,
    (m_- - m_+)/2=<Y>.                                                (7)

Thus two real charge-readout contrasts determine the complex loop
expectation <W>=(<X>+i<Y>)/2. With no pulse, the same birth probe measures
<Z>=-m_0. These are separate experimental contexts, not simultaneous
sharp values of noncommuting observables.

## 4. Explicit separation of electrically indistinguishable states

Let |a>,|b> be the flippable doublet, with W|a>=|b> and Z|b>=|b>.
The two states

    |psi_+>=(|a>+|b>)/sqrt(2),
    |psi_->=(|a>-|b>)/sqrt(2)

have identical probabilities for every complete electric-basis readout.
They satisfy <X>=+1 and -1. Because P=1 on both states, setting s=+1 in
(3) gives q=+1 with certainty for psi_+ and q=-1 with certainty for psi_-.
The opposite setting reverses those outcomes. Therefore fresh record
formation after the supplied pulse distinguishes this relative phase
exactly. The readout is the newly formed charge; no direct empty-site or
off-diagonal record measurement is assumed.

On an isolated square with the standard directed boundary and suitable
zero external flux, the two words have identical zero divergence. Thus
the example can be placed inside an actual fixed-Gauss sector, rather than
being an algebraic comparison of unphysical field states. On a larger
lattice the statement applies to any allowed flippable environment with
the same exterior data.

## 5. Apparatus, local support and fresh resources

The Y pulse can be synthesized from the same ring X and a diagonal edge
phase, since with D=exp[-i(pi/4)Z], D X D^dagger=Y. This is a statement
about supplied controllable Hamiltonians. A model containing only a fixed
time-independent X coupling does not automatically supply both settings,
the edge phase, pulse durations or a choice of apparatus location.

The probe occupies one plaquette and its distinguished matter endpoints.
Rotating or translating the complete oriented apparatus context rotates or
translates the equations with it. A selected plaquette/edge/setting is
supplied context, not a symmetry-invariant preferred site in the law.
No one-site M_2 nearest-neighbor implementation of all these roles is
claimed by this local-support statement.

A finite fresh-probe dilation can make the CP branches explicit. Take
orthogonal neutral probe states |fuel>,|spent,+>,|spent,-> and set

    C=sum_q V_q tensor |spent,q><fuel| + adjoint.

Its initial fuel subspace obeys C^dagger C=P_v, C^3=C, and it commutes with

    D_resource=N_records+2 |fuel><fuel|.

At interaction angle pi/2, exp(-i pi C/2) produces the two birth branches
-iV_q from a vacant pair and a fuel probe. Tracing the distinct spent states
gives the classical q instrument, and prepending the controlled S_s gives
(4). This is the chi=0 fresh-memory construction, with explicit outcome
orthogonality. It conserves the displayed resource/rest energy, not an
arbitrary additional interacting field Hamiltonian.

The entire finite joint gate commutes with D_resource and all Gauss charges.
It can therefore replace the gate on the single weighted bond in the
already checked autonomous-carrier construction. That inherits its
arrival-probability channel estimate for a supplied directed packet and
infinite outgoing lead. It inherits its limitations too: fresh resources,
engineered gate/lead geometry, possible return at finite packet width,
and the distinction between a reduced irreversible instrument and a
reversible closed dilation. This is not exact permanent-record dynamics
for every instant of a finite closed apparatus.

## 6. Relation to site reuse and the physics target

After formation the two records can be transported by a separately specified
Gauss-preserving motion law. If both leave the local probe sites, a fresh
fuel probe can act on their now vacant endpoints. The old contents remain
unchanged. This statement is conditional on the transport path being
available; spin-half gauge restrictions can block motion, as the earlier
three-dimensional counterexamples show. No universal export/completion
claim is included.

Each probe disturbs the field and creates charges. In particular, a sequence
of these probes has its own instrument correlations; it cannot simply be
identified with the unperturbed two-time ring correlator or photon spectral
function. State preparation, statistical error, pulse errors, field-energy
exchange, native admissibility, and physical identification remain distinct
obligations. The bounded advance is a concrete record-only readout protocol
for a supplied off-diagonal gauge observable, with its backaction exposed.

Controlled rotations followed by pointer readout are standard quantum
measurement machinery. The contribution here is the explicit fresh charged
pair instrument, its gauge/resource checks, the nonflippable-sector
cancellation, and its interface to permanent moving records. It does not
claim a new general measurement principle.
