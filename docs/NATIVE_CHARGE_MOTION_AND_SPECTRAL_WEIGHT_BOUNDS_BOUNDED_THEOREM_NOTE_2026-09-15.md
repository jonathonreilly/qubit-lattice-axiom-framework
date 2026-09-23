---
claim_id: native_charge_motion_and_spectral_weight_bounds_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/native_motion_check_2026_09_15.py
upstream_dependencies: ["docs/NATIVE_RK_CHARGE_STABILITY_NOTE_2026-09-08.md", "docs/NATIVE_GLOBAL_CHARGE_CONNECTIVITY_AND_EXCHANGE_NOTE_2026-09-08.md", "docs/NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md", "docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md"]
claim_scope: "Bounded conditional native motion and spectral-weight bounds; supplied hypotheses and limit order retained in full proofs."
---

# Native motion and spectral-weight bounds

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope and actual premises

The complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.

Actual mathematical dependencies:

- [NATIVE_RK_CHARGE_STABILITY_NOTE_2026-09-08](NATIVE_RK_CHARGE_STABILITY_NOTE_2026-09-08.md).
- [NATIVE_GLOBAL_CHARGE_CONNECTIVITY_AND_EXCHANGE_NOTE_2026-09-08](NATIVE_GLOBAL_CHARGE_CONNECTIVITY_AND_EXCHANGE_NOTE_2026-09-08.md).
- [NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08](NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md).
- [NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md).

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK7_NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT

Original source identity: `BLOCK7_NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Native charge motion and long-wavelength spectral weight

Personal derivation, 2026-09-15. Status: proposed conditional finite-volume
theorems, with explicit uniform constants. The Hamiltonian, low-charge
domain, gates, and couplings are supplied. This is not a derivation of that
Hamiltonian from the minimal axioms, an independently audited result, a
physical mass, or a long-time transport theorem.

#### 1. Scope and inputs

Use an even periodic cubic graph with each extent at least four. On edge
bits n_e, let G_v=sum_(e incident v)n_e-3, epsilon_v=(-1)^sum(v),
Q_v=epsilon_v G_v, and D=sum_v Q_v^2. Restrict to |G_v|<=1 and D=2;
there is one positive charge p and one negative charge m. Keep every
winding sector and do not impose fixed native cycle eigenvalues.

The supplied native Hamiltonian is

    H=H_ring+2U+t T,
    H_ring=sum_p J_p F_p(I-S_p),  0<=J_p<=J_max,
    T=sum_(undirected e) P_low T_e P_low.

Here F_p tests alternating plaquette bits and S_p is the native cycle
involution. It includes its operator phase. The native dictionary and
RK stability notes of September8 supply the following conditional inputs:

* Ring terms preserve every Q_v and are positive.
* Each allowed hop moves exactly one signed charge to a neutral neighbor,
  with modulus-one amplitude. At each charge there are four eligible edge
  bits; an eligible edge joining the two charges is excluded.
* In the ordered signed-hole frame c_p c_m|F>, all allowed hops are -1,
  and the alternating ring flip is +1. This frame follows from the full
  native dictionary; it is not an unsigned replacement of the native law.

Consequently the total hopping degree is six or eight, the positive-charge
degree is three or four, and ||T||<=8. Setting lambda=|t|, a diagonal
epsilon_p epsilon_m change of frame handles t<0. We henceforth write
H=H_ring+2U-lambda A with A the nonnegative hopping adjacency matrix.
None of the arguments below needs a proof that the entire hopping graph
is connected, or uniqueness of its lowest eigenvector.

#### 2. An exact local escape coefficient

Let Pi_x project onto p=x. For any unit vector phi with Pi_x phi=phi,
including arbitrary coherent superpositions of negative positions and
electric backgrounds,

    ||(I-Pi_x) T phi||^2 = <phi,d_+ phi>,
    3 <= <phi,d_+ phi> <= 4.                         (1)

To see this without discarding interference, label a resulting positive
position z. It specifies the unique physical edge e={x,z}. Toggling e is
an involution on its allowed configurations. Thus two different initial
configurations cannot give the same final configuration with that z;
different z belong to orthogonal sectors. The positive-hop columns have
disjoint support and squared norm equal to their number of allowed moves.
Negative-charge hops remain in Pi_x. The native phases have modulus one
and do not change the argument.

This proves an escape coefficient, not yet a finite-time bound. A naive
remainder using ||H_ring|| would grow with the volume. The next step avoids
that problem through the actual native commutation relations.

#### 3. A volume-independent commutator bound

In this sector,

    ||[H_ring,T]|| <= 192 J_max.                     (2)

Write H_p=J_p F_p(I-S_p). H_p commutes with P_low because its only
off-diagonal action flips an alternating face and preserves every charge.
If e is not an edge of p, F_p commutes with native T_e: its Z factors
commute and T_e flips only e. The native cycle S_p commutes with every
ambient T_e. Hence [H_p,P_low T_e P_low]=0 when e is not in p. This
uses the native algebra rather than asserting locality of its ordered
Pauli strings.

For e in p, a column of either product H_p T_e or T_e H_p has absolute
sum at most 2J_p. Thus a column of their difference has absolute sum at
most 4J_p. For this difference to act on an initial configuration, e must
meet one of that configuration's two charged vertices: a ring flip keeps
those vertices fixed. There are at most twelve such physical edges and
four plaquettes per edge. Summing gives a column sum at most 192J_max.
The commutator is anti-Hermitian, so its row sums obey the same bound.
The row/column norm estimate proves (2). Extensive diagonal ring terms
cancel in the commutator; they were not silently dropped from H.

Let H0=H_ring+2U and V=tT. In the interaction picture,

    U_I(s)=exp(i s H0) exp(-i s H),
    V_I(r)=exp(i r H0) V exp(-i r H0).

Equation (2) gives ||V_I(r)-V||<=192 J_max lambda |r|, while
||V_I(r)||<=8lambda. Unitarity and the integral equation give
||U_I(r)-I||<=8lambda |r|. Subtracting the linear term in that equation,

    ||U_I(s)-I+i s V||
      <= s^2(96 J_max lambda+32 lambda^2).           (3)

This estimate uses the unitary norm directly; no exponential Dyson
majorant or restriction proportional to inverse volume is required.
It holds for positive and negative real s.

H0 commutes with Pi_x. Combining (1) and (3), the actual probability of
finding the positive charge away from its initial position satisfies

    P_leave(s)=||(I-Pi_x) exp(-i s H) phi||^2,

    sqrt(P_leave(s)) >= sqrt(3)lambda |s|
                     -s^2(96J_max lambda+32lambda^2).

For lambda>0 and

    0<|s|<=s0=sqrt(3)/(192J_max+64lambda),

we obtain

    P_leave(s) >= (3/4)lambda^2 s^2.                (4)

The constant is uniform over the stated volumes, backgrounds, and initial
vectors with a definite positive position. A matching leading upper
coefficient is at most 4lambda^2. Time s is the unitary time of the supplied
Hamiltonian, with hbar=1; no formation-clock or measured-time calibration
has been established. Equation (4) does not imply motion at arbitrarily
late times or at distances growing without bound.

#### 4. A symmetric nonnegative ground state without connectivity

For the rest of this note take an L by L by L torus, even L>=4, and
uniform J_p=J>=0. In the signed-hole frame H has real nonpositive
off-diagonal entries. Taking absolute values of a lowest eigenvector
cannot increase its Rayleigh quotient, so a normalized nonnegative
ground vector exists.

An ordinary translation of bits by an odd-parity lattice vector exchanges
the signed charges. The translation which preserves their identities is

    (tau_a n)_e = n_(e-a)              if epsilon_a=+1,
                  1-n_(e-a)          if epsilon_a=-1.             (5)

Indeed its G is epsilon_a times translated G, so its Q is translated Q.
These operations form the translation group because complement commutes
with translation and epsilon_(a+b)=epsilon_a epsilon_b. They preserve
alternation, allowed hopping, and the signed-frame matrix H. Cubic point
symmetries fixing the origin, and global bit complement, also preserve H;
the latter exchanges positive and negative charges.

Average a nonnegative ground vector over this finite symmetry group and
normalize. The sum cannot vanish, is still a ground vector, and is
invariant. Call it psi. This construction avoids importing uniqueness or
an all-configuration connectivity theorem. It gives uniform positive
position marginal 1/L^3, equal positive/negative hopping expectations,
and equal expectations in the three coordinate axes.

The permutations just described act in the signed-hole frame. Conjugating
by the explicit native phase map gives the corresponding native unitaries.
Ordinary bit permutations are not asserted to preserve all native ordered
Pauli phases by themselves.

#### 5. Ground-state hopping strength

For completeness the parent uniform trial bound has a short counting proof.
Let A0 be configurations where the adjacent charges share an eligible
edge, and B0 all other D=2 configurations. Their hopping degrees are six
and eight. Every A0 configuration has six neighbors in B0. A B0
configuration has at most four neighbors in A0: two distinct vertices of
the stated cubic torus have at most two common neighbors, and either
charge can move. Adjacent ineligible pairs give no such neighbor. Therefore

    6|A0|<=4|B0|,
    average degree >=36/5.

The uniform vector over all D=2 configurations has zero ring energy and
this hopping expectation. Thus the lowest D=2 energy E2 obeys

    2U-8lambda <= E2 <= 2U-(36/5)lambda.             (6)

For the symmetric ground vector, H_ring>=0 immediately implies

    <A>_psi >= (2U-E2)/lambda >=36/5,
    <A>_psi <=8.

No differentiability of E2, Hellmann-Feynman interchange, or thermodynamic
limit is needed. Let A_+ denote hops of the positive charge and set
c_+=<psi,A_+ psi>. Charge complement symmetry gives

    18/5 <= c_+ <=4.                                (7)

#### 6. Exact momentum trial and its spectral measure

For k in (2pi/L) Z_L^3, k not zero modulo 2pi, put

    f_k(n)=exp(i k.p(n)),   phi_k=f_k psi.

Then ||phi_k||=1 and <psi,phi_k>=0, by the uniform position marginal.
It has translation character exp(-i k.a) under (5). The ground-state
identity, proved by expanding H psi=E2 psi and symmetrizing, is

    <f psi,(H-E2)f psi>
      = (1/2) sum_(n,n') [-H_(n,n')] psi_n psi_n'
                                      |f_n-f_n'|^2.              (8)

Ring flips and negative-charge hops keep f_k fixed. A positive hop in
axis i contributes 1-cos(k_i) after the factor one half in (8).
Axis symmetry and (7) therefore give the exact expectation and bounds

    Delta_trial(k) = (lambda c_+/3) sum_i(1-cos k_i),

    (6lambda/5) sum_i(1-cos k_i)
      <= Delta_trial(k)
      <= (4lambda/3) sum_i(1-cos k_i).               (9)

The bottom E2(k) of that translation sector consequently obeys

    0 <= E2(k)-E2 <= (4lambda/3) sum_i(1-cos k_i).   (10)

For k=(2pi/L,0,0), the right side is
(8lambda/3)sin^2(pi/L)<=8pi^2 lambda/(3L^2). There are thus orthogonal
states in the charged sector with energies arbitrarily close to its
ground energy as L grows. This concerns excitations WITHIN D=2. It is
compatible with the parent's positive energy to create a pair from the
neutral ground when U>4lambda.

Let mu_k be the probability spectral measure of H-E2 in phi_k. It is
supported on nonnegative energies and has mean (9). Markov's inequality
also gives the volume-independent weight statement

    mu_k([0,(8lambda/3) sum_i(1-cos k_i)]) >=1/2.    (11)

This is genuine low-energy spectral weight for the specified position
observable. It does not identify a single eigenvalue, a sharp particle
pole, or a nonzero curvature of the lowest band. In particular the LOWER
bound in (9) is a lower bound on a spectral MEAN, not on E2(k)-E2.

#### 7. A propagation upper bound independent of the ring coupling

For any initial positive position x, let R(n) be graph distance from x to
p(n) on the torus. Every allowed positive hop changes R by at most one;
negative hops and rings commute with R. In the signed-hole frame the
absolute row and column sums of [H,R] are at most 4lambda. Thus, for
Pi_x phi=phi and all real s,

    ||R exp(-i s H) phi|| <=4lambda |s|,
    E_phi[dist(x,p(s))^2] <=16lambda^2 s^2.          (12)

The first inequality follows by writing [R,exp(-i s H)] as the time
integral of unitarily conjugated [R,H]; R phi=0. The finite torus makes
all operators bounded, and the constant has no volume or J dependence.
This upper bound permits slower motion and does not assert ballistic
transport. Together with (4) it bounds the short-time mean squared
displacement from below by (3/4)lambda^2 s^2.

There is also an exponential tail. For kappa>0, conjugate H by exp(kappa R).
Only positive hops change, and their distance increments have magnitude
at most one. The Hermitian part of -i exp(kappa R)H exp(-kappa R) has
operator norm at most 4lambda sinh(kappa), by its row/column sums.
The differential norm inequality therefore gives

    P_phi[dist(x,p(s))>=r]
      <= exp[-2kappa r+8lambda |s| sinh(kappa)].      (13)

For r>4lambda |s|>0, choose kappa=arcosh[r/(4lambda |s|)] to get

    P_phi[dist>=r] <= exp[-2r arcosh(r/(4lambda |s|))
                          +2sqrt(r^2-16lambda^2 s^2)].             (14)

This is a supplied-Hamiltonian charge propagation bound, not an identified
physical light speed. It remains valid for nonuniform bounded nonnegative
J_p, as in Sections2-3. The signed-hole frame is diagonal and therefore
preserves every charge-position probability in the native representation.

#### 8. Outstanding matter obligations

The supplied model has unavoidable short-time charge motion and a
controlled long-wavelength spectral trial. The next substantive question
is whether this weight concentrates near a dispersing particle pole, or
whether the electric background creates broad or anomalous transport.
Uniform control of ground amplitudes, the many-charge sector, an
infinite-volume charged state, and a physical clock/mass dictionary remain
open. These results neither solve the TOE nor force an axiom change.

Literature routing: Wan, Carrasquilla and Melko, arXiv:1510.00979v2,
main text read in this block, studies a related diamond-lattice spinon
walk using approximate uniform ground states, path weights and numerical
continuation. Its effective mass is not imported into the present cubic
native model. The finite-volume identities above avoid those approximation
steps. Source: https://arxiv.org/html/1510.00979v2.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: native_motion_check_2026_09_15](../scripts/native_motion_check_2026_09_15.py); [current cache](../logs/runner-cache/native_motion_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).
