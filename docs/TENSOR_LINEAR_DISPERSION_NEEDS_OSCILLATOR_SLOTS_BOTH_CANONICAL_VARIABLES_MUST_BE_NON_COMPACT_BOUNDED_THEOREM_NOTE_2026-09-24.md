---
claim_id: tensor_linear_dispersion_needs_oscillator_slots_both_canonical_variables_must_be_non_compact_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied noncompact canonical tensor slots, integer vector/scalar stencils, J,g>0 and the specified quadratic comparator. Exact polynomial identities prove two physical modes at every nonzero Brillouin-zone momentum with omega squared = 4 J g sum sin(k_i/2)^2. Nonconstant quadratic energies do not descend to independent compact coordinates; a tested cosine replacement fails scalar invariance, without excluding every compact completion. Exact truncated-oscillator CCR defect and state-dependent coherent-state bounds do not prove approximate gauge dynamics or a finite-qubit phase.
upstream_dependencies:
- minimal_axioms
runner: scripts/tensor_linear_dispersion_needs_oscillator_slots_in_both_canonical_variables_2026_09_24.py
---

# The specified linear tensor comparator: noncompact slots and exact lattice dispersion

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** conditional-support; supplied-model mathematics, unaudited.

## Inputs and scope

The [landed tensor model](LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md)
supplies the canonical slots, integer stencils and quadratic comparator.
The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select these inputs.
No slot type, Hamiltonian, constraint prescription, state or physical interpretation
is adopted here. The historical filename records the original broader proposal;
the claims below concern this particular comparator.

Use canonical coordinates q=(h_xx,h_yy,h_zz,2h_xy,2h_yz,2h_xz) and momenta
E=(E_xx,E_yy,E_zz,E_xy,E_yz,E_xz), with pairing E dot dq. The vector stencil is

    (GE)_j(x)=E_jj(x+e_j)-E_jj(x)
               +sum_(i!=j)[E_ij(x)-E_ij(x-e_i)].

The scalar row S is the sum of the three planar pieces in the parent. The
comparator is H_N=J E† M E/2+g q† X q/2, summed over momenta, with J,g>0 and
M=diag(1,1,1,2,2,2)-vv^T/2, v=(1,1,1,0,0,0).
This is an unbounded canonical quadratic model, not a finite-qubit Hamiltonian.

## Exact symbol and two physical modes

Let K_i=2 sin(k_i/2), t=K_x²+K_y²+K_z² and use face order xy,yz,xz. Define

    F=diag(1,1,1,exp[-i(k_x+k_y)/2],
                    exp[-i(k_y+k_z)/2],exp[-i(k_x+k_z)/2]).
    G(k)=diag(i exp[i k_j/2]) G_r F,    X(k)=F† X_r F.

The real matrix G_r has (G_r)_(j,j)=K_j. Its face ij column has K_j in row i
and K_i in row j. All other entries vanish. The symmetric X_r is given by:

- distinct diagonal-slot indices a,b: X_(a,b)=-K_c², with c the remaining axis;
  its three diagonal-slot self entries vanish;
- diagonal a to face ij: K_i K_j when a is the remaining axis, zero otherwise;
- face ij self entry: K_c²/2;
- different faces ij and il: -K_j K_l/2.

These formulas reproduce the submitted planar rows exactly, using
exp(ik)-1=i exp(ik/2)K and 1-exp(-ik)=i exp(-ik/2)K.
The apparent half phases cancel into the periodic original lattice symbol.

Set s_r=(-(t-K_x²),-(t-K_y²),-(t-K_z²),K_xK_y,K_yK_z,K_xK_z)^T.
Direct polynomial multiplication gives

    G_r X_r=0,  G_r s_r=0,
    M s_r=G_r^T K,
    X_r M X_r=t X_r+s_r s_r^T/2.

The primary checks these identities exactly, not by sampling momenta.
For any K_i!=0, the minor of G_r using columns ii,ij,il and rows i,j,l
is K_i³. The principal X_r minor on slots jj,ll,jl is -K_i^6/2.
Thus rank G_r=rank X_r=3 at every nonzero K, and ker X_r=im G_r^T.
Also s_r!=0 and is orthogonal to im G_r^T. Consequently the configuration
quotient ker(s_r^T)/im(G_r^T) has dimension two. On ker(s_r^T), the last
identity implies (M X_r-tI)q belongs to ker X_r, so M X_r acts as tI on that
quotient. Hamilton's equations therefore give exactly

    omega² = J g t = 4 J g sum_i sin²(k_i/2)

for both physical modes. This is positive for every nonzero momentum in the
Brillouin zone and equals Jg |k|²+O(|k|^4) near zero, giving isotropic leading
linear dispersion. At k=0 the constraints and X vanish; the six homogeneous
canonical pairs must be treated separately, not counted as two oscillators.

Uniqueness also has an algebraic proof. Two continuous Hermitian solutions
with the prescribed diagonal rows differ only in their face-face block D.
G_r,face D=0 and det(G_r,face)=2K_xK_yK_z. Thus D=0 on a dense open set and,
by continuity, everywhere. The 486-coefficient Fourier fit is a numerical
cross-check, not the uniqueness proof.

In complex coordinates S is a ROW s=s_r^T F, and the E-gauge vector is s†.
The numerical E representatives therefore use ker(s KG), where KG spans
ker G. Conjugating s again at this step would select the wrong orthogonal
complement. Axis and zone-corner controls compare the corrected reduction
with the exact formula.

## Weak invariance, compact coordinates and penalties

Since M s_r=G_r^T K and G_r s_r=0, the momentum form is invariant under
E→E+s_r beta on G_r E=0; its change off that surface is generally nonzero.
The primary also tests this with the integer matrices on a 4³ torus
(384 slots, ker G dimension 195). The identities carry the general result;
random vectors only illustrate it.

A nonconstant quadratic polynomial cannot be periodic independently in each
coordinate: Q(x+T e_i)-Q(x) has linear term 2T e_i^T A x, forcing A=0 if
every such shift vanishes. Thus the specified nonconstant quadratic energies
do not define globally single-valued energies on independently compact
canonical coordinates. An ordinary rotor assignment does not realize the
exact polynomial H_N unchanged. The primary tests one cosine replacement
with the same momentum Hessian and finds that it fails scalar invariance.
That counterexample does not exclude every periodic completion or every
emergent linear mode.

The parent's cubic bound additionally requires lifted integer characters,
exact gauge actions, a nonsingular canonical structure and the stated
spatial-moment summability. Finite-N aliases, nonlinear gauge actions,
singular limits, additional fields and nonlocal mechanisms remain outside it.
The bare unconstrained quadratic comparator has an indefinite scalar sector.
For the particular finite quadratic vector/scalar penalties, the parent
derives a scalar kinetic determinant -J²/2, so those penalties cannot make
that comparator bounded below. This is not a theorem about every penalty
or the full bounded clock model.

## What finite oscillator truncation actually controls

For N Fock levels, the compressed single-slot matrices satisfy

    [x_N,p_N]=i(I-N |N-1><N-1|).

Their CCR defect has operator norm N, so there is no uniform operator-norm
approximation as N grows. For the normalized projection of the unit coherent
state, the top probability is

    P_top = [1/(N-1)!] / sum_(j=0)^(N-1) [1/j!],

and the absolute expectation defect is N P_top. The unnormalized infinite
coherent-state weight exp(-1)/(N-1)! is different. The primary reports the
normalized quantity for N=8,16,32,64. Small errors for this particular state
do not control arbitrary states, constraint commutators or long-time evolution.

Compressing a polynomial is also different from evaluating it on compressed
matrices: P_N x² P_N-x_N²=(N/2)|N-1><N-1|. The runner verifies this boundary
term. Products in multi-slot constraints can propagate boundary defects;
no general gauge-algebra error bound is proved here.

Infinite oscillator constraints can require distributional or group-averaged
reduction: a spectral projector onto the point zero need not have a nonzero
normalizable range. Finite truncated matrices instead have discrete spectra.
Neither observation supplies a finite commuting-stabilizer construction.

## Evidence, deferred work and negative-claim discipline

The [primary](../scripts/tensor_linear_dispersion_needs_oscillator_slots_in_both_canonical_variables_2026_09_24.py)
and [receipt](../logs/runner-cache/tensor_linear_dispersion_needs_oscillator_slots_in_both_canonical_variables_2026_09_24.txt)
contain exact polynomial/rank checks, integer torus checks, the fitted-symbol
comparison and finite-matrix truncation controls. The random momentum scan
is supplementary. Current review evidence separately constructs the real
symbols and checks the submitted phase convention. This is source review,
not an audit or a retained-grade verdict.

### N1
Examined routes are the exact noncompact comparator, its specified cosine
replacement, the parent's regular compact-character class, finite quadratic
penalties and finite oscillator compression. These do not exhaust qubit models.

### N2
Compactness, penalty instability and truncation error concern distinct models
and hypotheses. They are not independent proofs of a universal obstruction.

### N3
Canonical slots, constraints, couplings and the comparator are supplied.
No quantum state, readout, gravitational source or native qubit law is derived.

### N4
The actual landed tensor parent controls the compact-bound and penalty scopes.
Unlanded campaign summaries do not establish a broader physical conclusion.

### N5
Exact symbol identities close the sampled dispersion gap. Correct quotient
conjugation repairs the implementation. The failed cosine route is one tested
replacement. The exact CCR defect refutes uniform finite emulation, while
coherent-state errors remain bounded. The parent's precise penalty failure
does not close nonlinear or altered-constraint routes. These five resolutions
are reported separately by the runner; successful scope corrections are not
represented as failed alternatives.

### N6
A controlled finite model, selected low-energy state, constraint-domain
construction, dynamical error bound and physical source map remain open.
The original broad finite-emulation and universal slot-necessity claims are
deferred on the preserved PR head, not silently admitted.

### N7
The strongest counterroute is that compact or nonlinear models may realize
linear collective modes outside the regular-character hypotheses. This note
does not exclude them. Small coherent-state CCR expectation error alone
cannot establish a gauge-invariant phase.

### N8
The canonical continuum comparators and tensor constraints are inherited
from the parent and its prior-art discussion. The explicit lattice quotient
calculation sharpens the supplied-model result; no priority or physical
gravity claim follows.
