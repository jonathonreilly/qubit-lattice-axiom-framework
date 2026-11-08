# Coarse-vertex records across every encoding origin

**Claim type:** bounded_theorem. **Research status:** conditional-support;
this is a branch-local continuation, not an independently audited claim.

The approved neighborhood wording landed in PR #10143. The result here is a
conditional quantum construction, not a derivation of the native record law.
It answers the specific storage question left by the five-site electric reader:
can output records be accommodated without choosing a preferred encoding origin?

## Conditions and target

Use the four-qubit isometry J, its projector Q=JJ^dagger, the spacing-five
placement and supplied H_native of
`docs/SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_BOUNDED_THEOREM_NOTE_2026-11-08.md`.
The five logical states carry (0,0) direct-sum (1/2,1/2). The code satisfies
J^dagger J=I, Q|0000>=0, and geometric reversal FJ=JK, with
K=diag(1,-1,-1,-1,1). Electric projectors are P0=|0><0| and P1=I-P0,
with electric readout 3b/4. These are explicit model conditions.

Ordinary tensor quantum states, Born/Kraus instruments, code and blank-pointer
preparation, the classical record-presence flag, and a uniform finite-volume
attempt scheduler are supplied. No primitive provides these choices. We use a
torus Lambda=(Z/(5n)Z)^3, n>=3, and allow arbitrary passive external entanglement.

## 1. The enlarged code and unchanged local detectors

For a residue p in (Z/5Z)^3 let V_p have all three residues equal to p, A_p
exactly one different residue, and F_p at least two different residues.
Encode J(R) on the disjoint four-site coarse-edge interiors A_p. Free every
qubit of V_p, and retain |0> on every site of F_p. Call the resulting subspace E_p.
Per coarse cell this gives 12 active data qubits, one arbitrary output qubit,
and 112 fixed qubits. Its dimension is 5^(3n^3)2^(n^3).

For p!=q, let Delta be the coordinates in which they differ. When |Delta|=1,
choose a q-edge direction outside Delta; each interior point differs from p
both in that fixed coordinate and in the edge coordinate. When |Delta|=2,
choose the remaining direction. When |Delta|=3, any direction works. The last
two cases retain two fixed coordinate differences. In all cases an entire
q-edge is inside F_p: it is |0000> in E_p and in range Q in E_q. Thus E_p and
E_q are orthogonal, for arbitrary entangled data and outputs.

At x, the old D_x is the product of Q over the six incident length-five edge
interiors, on 24 disjoint qubits. If x has residue p it is identity on E_p.
Otherwise the preceding local witness is one of its six factors, and it
annihilates E_p. Therefore

    D_x I_p = delta_(x mod 5,p) I_p,

where I_p is the enlarged isometry. Translations and proper rotations permute
the E_p; reversal covariance of Q supplies the reversed edges. The direct sum
of all 125 E_p is covariant, with no new physical site or local dimension.

## 2. A finite local instrument, including the record guard

Let r be the partial map of recorded sites to bits. Absence and recorded zero
are distinct; |0> of the native pointer alone does not distinguish them.
Compatible states have records only in V_p, recorded pointers fixed at their
recorded values, and all unused vertex pointers prepared in |0>. Empty r permits
coherent superpositions of origins; a nonempty record location fixes p.

For each of the six unoriented coarse edges e incident to x, put
q_(e,b)=J_e P_b J_e^dagger. They sum over b to Q_e and commute with D_x.
Let S(x) be the 24-qubit detector support. Define

    m_x(r) = 1 if ({x} union S(x)) intersect dom(r) is empty, else 0,
    A_x = m_x(r) |0><0|_x D_x,
    L_(x,e,b) = sqrt(m_x(r)/6) |b><0|_x q_(e,b) D_x,
    L_(x,empty) = I-A_x.

A_x is a projector. Using Q_e D_x=D_x gives

    sum_(e,b) L_(x,e,b)^dagger L_(x,e,b) = A_x,
    L_(x,empty)^dagger L_(x,empty) = I-A_x.

This proves trace preservation on the full native Hilbert space, including
off-code states. A successful b branch appends r(x)=b; the null branch leaves r
unchanged. The support guard makes every branch identity on old recorded sites,
including an already-recorded zero. On a compatible true-phase input the guard
on S(x) is automatic, since no active-link site carries an old record. It is
included to protect records in the off-code completion too.

At a fresh true-phase vertex the branch is the logical electric projection
P_(e,b) with weight 1/6, writing b into x. At a false-phase vertex the attempt
is null. These operations preserve active code and the Gauss subspace because
P0 and P1 are endpoint-invariant representation-sector projectors. All equations
extend with identity on an arbitrary external system.

Choose x uniformly in the finite torus at each supplied step, or regard x as a
specified attempted site. Including the 1/sqrt(|Lambda|) factors for uniform
choice gives a normalized covariant hybrid quantum/record update. Spatial
permutations send each L_(x,e,b)^r to L_(gx,ge,b)^(gr), using the geometric guard
and reversal invariance of P_b. Each attempted instrument has support at most
25 qubits in native radius four. This is not a native adjacent-gate compilation
of D_x and does not derive a physical clock or scheduler.

If e is unobserved, add its six completely positive branches, not amplitudes.
Conditional on a compatible fresh true-phase vertex, the b effect is
(1/6)sum_e P_(e,b). A record b is a sampled past electric
value. Its content alone does not identify which edge was selected; an identified
edge requires a known selector or separate recorded provenance. Later magnetic
evolution need not preserve the past measured value.

A success at x projects a coherent origin superposition onto p=x mod 5. Null
attempts also can change origin coherence. The instrument is defined on coherent
origin inputs; it does not promise to preserve their coherence.

## 3. The supplied Hamiltonian preserves the stored outputs

Keep exactly the prior D-sandwiched H_native, with its supplied electric and
magnetic plaquette terms. On E_p every false-phase seed vanishes. Each true-phase
seed acts only on encoded edge interiors, so the prior counting argument gives

    H_native I_p = I_p (H tensor I_outputs).

Self-adjointness makes E_p reducing; the corresponding exponential identity holds
for every finite time. Thus interleaving this supplied evolution with the
instrument preserves already-recorded output values on the compatible code.
This is sector-wise output protection. It is not a commutator identity with every
site's qubit algebra on the full native space: a vertex in one origin can be an
active site in another. No off-code protection by H_native is asserted.

Only n^3 outputs are available in a realized origin, regardless of the 125-origin
sum. With k records the success probability per uniform attempt is
(n^3-k)/|Lambda|. At capacity the attempts are null. There is no renewal or
infinite-volume uniform-site scheduler construction.

## 4. The next physical bridge is precise

The constructed process has joint input (rho,r). It has not been shown to factor
through r alone. An explicit Gauss-compatible diagnostic uses the same blank r
and pointer preparation for (i) all logical links in vacuum and (ii) the four
occupied links of one elementary plaquette. The second state exists by pairing
the two spin-1/2 endpoint factors into a singlet at each plaquette corner; all
other ends are trivial. At a corner x, two of six incident links are occupied.
Conditional on attempting that x, the b=1 probability is respectively 0 and 1/3.

Consequently a record-only realization must supply allowed classes S_r or a
reconstruction rho(r), prove identical next-record measures throughout each S_r,
and prove that the conditional updates and any interleaved evolution preserve
those classes. It must then show the resulting kernel depends on the permitted
neighborhood conditions. Preparation/program/history records are a live route;
the diagnostic does not rule them out or establish a need for an axiom change.
This unresolved law step is necessary for the proposed native realization;
it does not address the continuum or mass-gap questions.

## Evidence and comparison

PRIMARY.md was frozen before the supervisor read INDEPENDENT.md. The separate
fresh-context derivation recovered the geometry and projector construction and
added the support-wide old-record guard and Gauss-compatible diagnostic. The
supervisor checked the full argument, normalization, guard, phase coherence,
Hamiltonian restriction and 0-versus-1/3 calculation. Same model family and
shared model premises limit independence. This is research checking, not formal
landing review or independent audit.

geometry_probe.py exhausts the 15,500 distinct phase pairs and 375,000 class
images under proper rotations, preserving a fixed-zero edge witness. It uses
exhaustive support search rather than the proof's direction selector. The
free-all-unused mutation is rejected; disjoint active sets at p=(0,0,0) and
q=(1,1,1) also give a concrete nonzero intersection for that incorrect enlargement.
These checks supplement the proof and do not verify physical identifications.

The closest branch inputs are the native-placement and electric-reader notes.
The main projective-history candidate of 2026-08-21 supplies a conditional finite
history kernel but leaves its local carrier open; it does not contain this
spacing-five output-register construction. Bounded lexical main searches and
both Luna reports are preserved; no exhaustive literature-priority claim is made.
The primary-source literature search found Carmeli, Heinosaari and Toigo,
"Covariant quantum instruments" (https://arxiv.org/abs/0805.3917), and Chiribella,
D'Ariano and Perinotti, "Realization schemes for quantum instruments in finite
dimensions" (https://arxiv.org/abs/0810.3211). Their abstract-level context is not
used as a theorem input; normalization and covariance are proved above.
