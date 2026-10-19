<!-- Original PR9797 source SHA256 f26b49ba8c18885319a23ee9ac87500ff3c02bd9a669fa650f0dc593d44efc72. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Actual particle-relative extended environment from native kinetic energy

Status: bounded-support. This extends NATIVE_DRESSED_PATCH_PROOF.md in the
same supplied one-qubit Hamiltonian, height four and even transverse boxes
R comparable to lambda^-1. It derives a growing conditional environment in
actual near-minimal two-wall states, rather than only constructing a trial
patch or measuring the center-of-mass spread. The microscopic action and
weak-coupling slab remain explicit premises. No observed particle is fitted.

## 1. State and coordinate qualifications

Take normalized states supported in the actual isolated two-wall spectral
cluster, with energy within O(Jlambda^(5/2)) of its minimum. The established
local SW map and N=2 projection have O(lambda³) leakage. Project further to
the singleton sector and normalize; its omitted half-sector weight is at
most O(lambda^(3/2)), or is exactly absent in odd physical-Z parity.
A small mean energy without the spectral-cluster restriction is insufficient.

In the dressed singleton basis write the state as background-valued position
components psi_i. For mixed states use purification or linearity. Native
link signs Uij are diagonal commuting unitaries on the background. The
previous energy and flux inequalities give, uniformly along this box family,

 delta=<T+4>=sum_edges ||psi_i-Uij psi_j||² <=C lambda^(3/2),
 F=sum_i,p incident i ||B_p psi_i||² <=C lambda^(3/2),        (1)

where B_p=(I-Pp)/2 is the bad-plaquette projector. This is the derived
particle-conditioned local environment estimate; it assumes neither a
classical background nor a fixed particle position.

## 2. Transport to a displaced plaquette

Anchor one plaquette at each column j and define

 S_d=sum_i ||B_(i+d) psi_i||².                              (2)

It is the probability of bad flux at displacement d relative to the particle,
not the particle's participation ratio. Choose a fixed translated shortest
path of length r=|d|_1 from i to i+d and let W_i,d be its link transport.
Every B commutes with every U. Splitting psi_i into W_i,d psi_(i+d) plus
the transport difference and using the squared triangle inequality yields

 S_d <=2 S_0+2 sum_i ||psi_i-W_i,d psi_(i+d)||².

Telescoping the r path edges and Cauchy-Schwarz give

 sum_i ||psi_i-W_i,d psi_(i+d)||² <=r² delta.                (3)

For each step, summing its translated gradient over i gives a directional
part of delta. There is no volume multiplier. Thus the exact bound is

 S_d <=2F+2r² delta <=C lambda^(3/2)(1+r²).                 (4)

It holds without translation invariance of the state. For a length L
comparable to lambda^-q, the maximum individual bad-flux probability over
|d|_1<=L tends to zero for q<3/4. This controls each marginal uniformly; it
must not be called a simultaneous all-flat event at that exponent.

## 3. A joint growing flat patch

Let D_L be a square of plaquette anchors of side O(L) relative to the
particle. All the B commute, so the event of any bad flux in that square is

 Q_i,L=I-product_(d in D_L)(I-B_(i+d)),
 Q_L=sum_i |i><i| tensor Q_i,L, 0<=Q_L<=I.

The union inequality gives

 <Q_L> <=sum_(d in D_L) S_d
       <=C lambda^(3/2)(L²+L⁴).                            (5)

For every fixed 0<q<3/8, choosing L comparable to lambda^-q makes this
failure probability vanish as O(lambda^(3/2-4q)). A joint measurement of
the dressed position and flux therefore finds an all-positive-flux square
around the particle with probability tending to one, on a scale growing
without bound. At q=3/8 this estimate is only order one. Since q<1, the
relative region and paths fit inside R comparable to lambda^-1.

This is a property of every state satisfying the specified energy and
spectral support conditions, not merely of the patch trial state. It does
not select the feature's radius, a domain boundary, or individual column
signs. Flat plaquette flux still permits row/column sign freedom and quantum
superpositions. It does not require a localized center of mass.

## 4. Actual-state transfer

Q_L has norm one for every L and R. Transferring it through the established
spectral projection therefore costs O(lambda³), without an L² factor.
One can condition on the singleton projection, or count half-sector events
as failure, adding O(lambda^(3/2)). Both are negligible in the stated range.
The same bounded-operator transfer applies to the marginal S_d. Throughout,
these are SW-dressed observables in the actual microscopic state. Replacing
them by bare microscopic local measurements requires a separate estimate.

## 5. Contrast with the actual vacuum

Use a translation- and x/y-exchange-symmetrized actual ground density matrix
as the explicit vacuum reference. The exchange includes the native spin
rotation, and the equivariant reduction preserves these symmetries. Project
its transformed state to N=0. Leakage is O(lambda³), using the order-one
wall gap; no internal spectral gap of the neutral coefficient K is needed.
Its normalized vacuum-block energy is within O(Jlambda³) of the minimum.

Write n=R². The vacuum block is scalar+Jlambda^4 K/128, K=-5E-4P.
The logical-X polarized trial gives min K<=-10n. Consequently

 -5<E>-4<P> <=-10n+O(lambda^-1).

Using <P><=n and n comparable to lambda^-2 gives
<E>/(2n)>=0.6-O(lambda). Symmetry makes this the expectation of each edge.
An edge crossing a plaquette boundary anticommutes with that plaquette, so

 <Pp>²+<Eedge>²<=1,
 <B_p> >=0.1-O(lambda).                                   (6)

The bounded dressed plaquette incurs only O(lambda³) transfer error. Thus
the actual symmetrized vacuum retains a nonvanishing local bad-flux
probability, while near-minimal heavy states have vanishing particle-relative
probability uniformly over a growing set of displacements. This is an
environment contrast, not only center-of-mass delocalization. No clustering,
independent-defect distribution, or unsymmetrized-vacuum theorem is assumed.

## 6. Scope and next obstacle

A many-site conditional dressing neighborhood has now been derived from
native hopping and energy minimization without assigning its profile. The
native assisted hopping vertex is derived separately in
NATIVE_ASSISTED_HOP_PROOF.md. Its full dynamics in this relaxed growing
environment, rather than a prepared vacuum background, remain unresolved.
Neither result derives three-dimensional isotropic propagation, fermionic
statistics, a measured scalar, universal gravity, or cosmological initial
conditions. All calculations are exposed model development.
