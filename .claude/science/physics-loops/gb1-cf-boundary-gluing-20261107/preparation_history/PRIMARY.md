# Frozen preparation/history candidate

Source head: 40bf8ab61128cfa0ff7c2e99663300d4ee2b5c1f.
Main/instruction source: 43a1fcc374711ca50626eca667441d3ca575c7d1.
Author candidate, frozen before reading the separate check. No axiom edit.

## Target and supplied ingredients

Keep the native_records/RESULT.md enlarged code E_p, the supplied finite
gauge Hamiltonian H, and the incident-edge instrument. Fix a finite preparation
catalogue indexed by d bits, a finite control alphabet assigning exact unitary
maps exp(-i tau H), and a controller that is a fixed function of the preparation
label and recorded prefix. These inputs are not derived by the axioms.

For a known preparation sigma_empty=rho_alpha, define, at the next fresh
true-phase vertex x_j,

  sigma_(h b) = Phi_(h,b)(sigma_h),
  Phi_(h,b)(X) = (1/6) sum_(e incident to x_j)
                  P_(e,b) U_h X U_h^dagger P_(e,b),
  Pr(b|h) = Tr sigma_(h b) / Tr sigma_h.

The unobserved edge is summed as completely positive branches. Histories
with zero trace are not conditioning domains. Induction gives positive,
normalized prefix cylinders, unique reconstructed rho_h, and update closure.
Unitary evolution is part of the recorded-step recipe. No unspecified elapsed
time, hidden event-order choice or additional dynamical density is allowed.

## A finite binary carrier on already-free coarse vertices

Let M=d+N, N>=1, and choose the coarse torus side n>=2M+8. A prepared marker
component consists of the seven coarse vertices

  a, a+5e1, a+5e2, a+10e2, a+5e3, a+10e3, a+15e3,

all carrying bit 1. Its unique degree-three center and arms of lengths 1,2,3
recover a right-handed ordered frame intrinsically. The coarse adjacency
here is distance five in one native axis; the record positions also identify
p=a mod 5. Put header and successive output slots at

  v_j = a + 10j e1 + 20e2, j=1,...,M.

These are isolated in the distance-five record graph, and separated from the
marker component, including around the periodic boundary by the stated n
bound. Initially v_1,...,v_d encode alpha; later slots carry exactly a prefix
of N output bits. Presence distinguishes recorded zero from absence. The
marker and header are supplied permanent boundary records; their physical
manufacture/calibration is not proved. No F_p site is freed or written.

All seven marker sites and all M word sites are distinct coarse vertices.
Every allowed R uniquely decodes a, frame, alpha and ordered h. The next target
is v_(d+|h|+1), so no host counter is used. Every record needed to decode it
lies within native graph radius 10M+35 of that target. Thus the probability
formula is a fixed finite-neighborhood content kernel on this finite prepared
domain. At the common next site it chooses b, not an outcome-dependent site.
Transport both records and quantum preparations/programs by every native
translation and proper rotation; the intrinsic parser makes this one
covariant law on the union of transported domains, without privileging a
frame in the law. The preparation catalogue and controller must themselves
transport with that recovered frame. The fixed parameters d,N,n and the
dictionary remain supplied. No volume-uniform fixed-range claim is made.

On E_p, H_native acts as H tensor I_outputs. At every selected fresh slot the
old detector and record guard permit the electric instrument. Hence header,
marker and earlier output bits are preserved by both quantum evolution and
the new instrument, for all N stages. The joint quantum realization agrees
with the record-only kernel by induction provided its preparation is exactly
the declared rho_alpha. Record count is 7+d+k after k events, at most 7+M.

This proves a finite compatibility construction only if the geometry and
induction hold. It does not infer the catalogue, Born instrument, controller,
Hamiltonian, support/calibration or preparation genesis from the axioms.

## Discriminating controls and state criterion

The existing empty-record vacuum/loop example shows that a label unconnected
to preparation cannot supply sufficiency. For timing/order, use the two-state
invariant subspace of the pair's B_L (span empty,L), where B_L=2X and an outer
left-edge electric event is P1=|L><L|. From empty, an unrecorded magnetic
angle changes the next electric probability sin^2(2t). This is a probe of a
declared local magnetic control, not the uniform full cubic Hamiltonian.

For general histories a density matrix need not be unique: it suffices that
all represented states agree on every effect obtainable from the allowed
future instrument words. Equal one-step odds alone do not establish this.
Hidden Kraus indices need not be logged when their calibrated CP sum is known.
Likewise, known unobserved events can be marginalized; missing event-time or
intervention information cannot simply be replaced by an identity map.

Next decisive checks: independently reconstruct the conditional filter and
test state sufficiency; exhaust the finite marker/parser geometry without
using the proof's uniqueness criterion as an expected answer; check the
probability witnesses by a separate exact matrix route; inspect the full
integrated source with the checker. No formal audit or landing review implied.
