# The finite-patch term missing from Resp

Author: openai/gpt-6-astra/max macbook-codex, 2026-11-01.
Source: `25a86977f538eb6bb104f097c435b44fd42138b7`.
**Unchecked:** author proof, not an independent check or an audit.
The exact scalar check below was run; no nonlinear SU(2) simulation ran.
Credit: the contour-gradient block map is the mapped part's Text 3.1
(Balaban's average). The calculation here rebuilds the needed scalar
minimization directly; no paper lemma is used.

## 1. The literal statement and the test

**Unchecked (counterexample to literal Resp).** The local lift in
`quiet-boundary-rarity.md:19,31` minimizes on a FINITE patch, with a
free edge. W_ref in its ST/J comparison is the global unfrozen lift
of the same global parent field. Resp at line 33 asserts

    ||Theta(Lift_b^d)-Theta(W_ref)||_Q^2
      <= C_r sum_{Q' older} exp[-2 rho dist(Q,Q')/L] a(Q').

At the first freeze the sum is empty. Thus this asserts exact equality
of the two curvatures on Q, for every regular parent field, not merely
exponentially small error. The example below violates that equality
already at one blocking step on a finite four-dimensional torus.
It uses no rough cells, labels, frozen-data junction or large field.
It does not refute AE-R or the conclusion of J with a patch-tail term.

Take any odd L>=3, and an even number M of parent blocks in direction
1. All torus sides can be enlarged to fit the actual periodic brick
tiling. Choose M sufficiently large that a parent slab j=j_* lies
outside b's entire finite patch, with an extra block margin. Put

    V_2(j)=exp(i t L mu_j sigma_3),  mu_j=1_{j=j_*},
    V_1=V_3=V_4=1,                                      (P)

independent of transverse coordinates. Here t>0 will be arbitrarily
small AFTER this finite geometry has been fixed. All parents on the
patch are identity. The free-edge local lift has action zero there,
so its curvature is exactly zero. The question is whether W_ref is
also flat there. Sections 2-4 show that it is not, for small t.

## 2. Exact abelian map and the full quadratic minimum

**Unchecked (exact map on the scalar family).** Put fine links
U_2(x)=exp(i t h(x_1) sigma_3) and all other links equal to 1.
For small t all logarithms are principal. In the comb formula
Q=Q_path+Phi(y)-Phi(y'), Phi=0 on this family: for every axial order,
the direction-2 contour contribution is (x_2-y_2) times h evaluated
at either x_1 or y_1. Its average over the symmetric x_2 block is
zero. The other link components vanish. Hence the exact nonlinear
abelian parent is (P) whenever

    (1/L) sum_{r=0}^{L-1} h(jL+r)=mu_j.                  (MEAN)

The shift between jL and a site-centred block is only a choice of
origin. Each direction-2 line has L equal link angles. The action is
N_perp sum_n [1-cos(t(h(n+1)-h(n)))], where N_perp is the number of
fine transverse sites. In particular piecewise constant h=mu_j is
an exact admissible trial, identity on b and its patch, with action
O(t^2). Every link and plaquette is small for sufficiently small t.

**Unchecked (this is the full quadratic problem, not only an ansatz).**
Linearize the action and the map at identity. For a Lie-algebra
1-form H, the quadratic action is E(H)=sum_p |dH(p)|^2/2 and the
constraint is QH=P^(1), with P^(1)_2=L mu_j sigma_3.
Average QH_2 over all transverse coarse sites. The Phi difference
telescopes in direction 2. In Q_path, the block offsets and coarse
transverse sites cover every fine transverse site; the L line steps
give a factor L. Thus the transverse average h_bar(n) of H_2 obeys
(MEAN), with mu_j sigma_3 on the right.

The transverse average of dH_12 is h_bar(n+1)-h_bar(n), since the
direction-2 difference of H_1 telescopes. Jensen on each plane gives

    E(H) >= (N_perp/2) sum_n |h_bar(n+1)-h_bar(n)|^2.    (LOW)

Minimize the scalar right side with (MEAN). Its minimizer h_* is
unique: the only null vectors of the cyclic difference operator are
constants, and the homogeneous block-mean constraints kill them.
The vector problem has h_* sigma_3 as its minimizer; the other two
colors have zero prescribed means and zero minimum. The field
H_2=h_* sigma_3, H_1=H_3=H_4=0 satisfies the FULL Q constraint by the
Phi calculation, and attains (LOW). Consequently every quadratic
minimizer has dH_12(n,x_perp)=(h_*(n+1)-h_*(n))sigma_3 and all other
curvatures zero. Equality in Jensen proves the first assertion;
positivity of the other curvature terms proves the second. No
assumption of a transversely invariant minimizing field was used.

## 3. The tail is nonzero at every finite distance

**Unchecked (explicit solution).** Write
p_j=h_*(jL)-h_*(jL-1) for the interface slope. The multiplier equation
for (MEAN) says h_*(n+1)-2h_*(n)+h_*(n-1) is constant within block j.
Therefore, for r=0,...,L-1,

    h_*(jL+r+1)-h_*(jL+r)
      = (1-(r+1)/L)p_j + ((r+1)/L)p_{j+1}.              (SLOPE)

With c_j=h_*(jL), summing these slopes and averaging gives

    mu_j=c_j+[(L-1)/2-b_L]p_j+b_L p_{j+1},
    c_{j+1}-c_j=[(L-1)/2]p_j+[(L+1)/2]p_{j+1},
    b_L=(L^2-1)/(6L).

Subtract the mean equations at j and j-1 to obtain

    b_L p_{j-1}+a_L p_j+b_L p_{j+1}=mu_j-mu_{j-1},
    a_L=L-2b_L=(2L^2+1)/(3L)>2b_L>0.                  (REC)

Set D_L=sqrt(a_L^2-4b_L^2)=sqrt((L^2+2)/3) and
q_L=(a_L-D_L)/(2b_L), so 0<q_L<2-sqrt(3)<1. On the infinite
chain the inverse kernel is g_s=(-q_L)^|s|/D_L. For the stated bound,
q_L+1/q_L=a_L/b_L=4+6/(L^2-1)>4, and q_L is the root in (0,1).
The quadratic
equation for -q_L verifies (REC) away from zero, and
a_L g_0+2b_L g_1=1 verifies it at zero. Periodize this absolutely
convergent sequence. For even M and 0<=r<M the cyclic inverse is

    G_r = (-1)^r (q_L^r+q_L^(M-r)) / [D_L(1-q_L^M)].    (GREEN)

Indeed summing g_{r+kM} gives this geometric series and commutes with
the finite-range operator. For the single nonzero mean in (P),

    p_j=G_{j-j_*}-G_{j-j_*-1},                         (TAIL)

with indices modulo M. Consecutive G entries have opposite nonzero
signs, INCLUDING across the periodic seam because M is even.
Hence p_j is nonzero for EVERY j. Select a plaquette crossing a
parent-block interface strictly inside b, and a testing cube Q
containing it. Such an interface exists since b has side >=8L.
The global quadratic minimizer has nonzero curvature at that
plaquette, however far the parent slab is from the local patch.

The formula proves nonzero, exponentially small tails; it makes no
claim of a positive lower bound uniform in separation or volume.
Its decay parameter has the uniform upper bound 2-sqrt(3); its
amplitude depends on L, M and the distance, as displayed.

## 4. Passage to an actual small SU(2) minimizing lift

**Unchecked (finite-dimensional argument, no uniform R3 input).**
Fix L,M and the compatible torus first. Let W(t) minimize the Wilson
action among regular fields with parent (P). The fibre is nonempty
by the exact scalar trial. On the regular branch, with T chosen
small in L as in the source, the finite-block logarithms are
continuous: each relative comb loop bounds at most C(L) plaquettes,
and C(L)T<pi/4 keeps its principal logarithm away from the cut.
The closed condition flux<=T in the compact link space
therefore gives a minimizer. The trial implies A(W(t))<=C t^2.

Here is the gauge control needed to expand that minimizer, rather
than assuming a differentiable minimizing branch. For SU(2),
1-cos(theta)>=2 theta^2/pi^2 on [0,pi]. Thus each plaquette angle is
O(t). Fix an axial tree inside each parent block, with gauge equal
to 1 at the block centre. Every remaining internal bond is a loop
of a fixed finite number of plaquettes, so it is 1+O(t) in this
gauge. The product estimate used here is
dist(1,g_1...g_s)<=sum dist(1,g_i); conjugation preserves distance.
The same estimate compares any two centre-to-centre comb paths in
two neighboring blocks, since their difference bounds a finite
plaquette surface there. Their transports differ by O(t).
For the regular log average, write the paths relative to one such
transport P_0; their relative logarithms are O(t), so the average
is (1+O(t))P_0. Its prescribed value V(t) is 1+O(t), whence P_0 and
every crossing bond in the block-tree gauge are 1+O(t). This includes
periodic neighboring blocks. Constants in this paragraph may depend
on the fixed finite geometry. No top-scale or infinite-volume
regularity estimate has been assumed.

Consequently H_t=log W(t)/(i t) is bounded in this gauge. From any
sequence t down to zero take a convergent subsequence H_t -> H.
Differentiating products and the smooth local logarithms at identity
gives QH=P^(1); expanding 1-cos(theta) gives

    lim A(W(t))/t^2 = E(H).

The scalar trial exp(i t h_* sigma_3) has the prescribed parent
EXACTLY, not just to first order. Its scaled action tends to the
minimum in (LOW). Minimality and (LOW) force H to be a quadratic
minimizer. Section 2 determines its curvature uniquely, even though
its gauge potential need not be unique. Thus, for the chosen
plaquette p at interface j, every subsequential limit gives

    Theta_p(W(t))/t -> p_j sigma_3 != 0.                 (LIMIT)

The block-tree curvature frames have the same first-order limit;
all compared transports in the fixed block are 1+O(t). Compactness
of the bounded H_t then makes (LIMIT) a full limit. For sufficiently
small positive t, Theta_p(W(t)) is nonzero, all fine fluxes are <T,
all labels are zero, and the parent fluxes are <T_2. The minimizer
is therefore within the regular class required for W_ref.

Finally freeze b FIRST with identity data. These data are feasible:
the piecewise constant scalar trial from section 2 is identity on
b and its patch and still has parent (P). They are quiet with
Dev_b=0. Before this freeze d is empty, Lift_b^d is flat, and W_ref
is W(t). The left side of Resp is positive on Q and its right side
is zero. No finite C_r or choice of rho repairs that literal formula.
One level and one admissible first brick suffice; a second age is
not needed. This is not a counterexample to positive rarity for R.

The smallness threshold on t and the O(t) constants above are allowed
to depend on the finite geometry. That is sufficient to disprove a
universal zero-right-side estimate; it supplies no uniform nonlinear
estimate, no derivative bound at nested data, and no response theorem.

## 5. A corrected input that the cube argument can read

**Gap (Resp+).** Keep the common global reference, and require

    ||Theta(Lift_b^d)-Theta(W_ref)||_Q^2
      <= C_r sum_{Q' older} exp[-2 rho dist(Q,Q')/L] a(Q')
         + tau_b(Q)^2,
    sup_{b,Q, histories} tau_b(Q)^2 <= kappa_tail e,
    e=eps_q^2 T^2.                                    (Resp+)

C_r,rho>0 and kappa_tail>=0 must be absolute after fixed geometry
choices, free of x,L,depth,volume and the frozen history. The patch
radius may depend on L,T,eps_q in the consumer's prescribed order.
Increasing C_r without the additive term cannot repair an empty sum.
The source already intended an exponentially small patch tail; the
point is to retain and bound it in the actual displayed inequality.

One sufficient route makes two obligations explicit. With W^d the
GLOBAL constrained lift with the older frozen data, prove

    ||Theta(W^d)-Theta(W_ref)||_Q^2
       <= C_G sum_{Q' older} exp[-2 rho dist(Q,Q')/L] a(Q'),
    ||Theta(Lift_b^d)-Theta(W^d)||_Q^2 <= (kappa_tail/2)e.

The squared triangle inequality gives Resp+ with C_r=2C_G.
These estimates, existence and regularity of W^d, and their
multilevel uniformity are gaps. A finite-dimensional O(t) argument
from section 4 supplies none of their uniform constants. The
MARK-TAIL request is a related entire-brick version of the second
line; the cube bound alone must not be renamed that brick bound.

**Implication (author algebra, with the geometry of the cube note).**
Keep h=t_0/1024, r=t_0/64, N_0=35^4, S(rho) and the rank <=5 from
`active-energy-junction-cubes.md`. Set

    B=2 C_r N_0,  P=1+B+B^2+B^3+B^4,
    D=2 C_r S(rho) exp[-rho t_0/(64L)].

Relative quietness and Resp+ give

    a(Q)<=2(1+kappa_tail)e+2 C_r sum_{older Q'} w(Q,Q')a(Q'),
    A_k<=2(1+kappa_tail)e+B A_{k-1}+D A.

Unroll through five ranks and choose PD<=1/2. Then

    A<=4P(1+kappa_tail)e.                             (J+)

Thus C_J=2P(1+kappa_tail) in sup a<=2C_J e for the aligned
partition, or C_J=32P(1+kappa_tail) for all translated cubes.
The absorption condition is unchanged. This is an a priori
same-level implication, not a solution of Resp+ or an existence
proof. Its constants are free of x,L,depth,volume precisely when
the stated response and tail constants are, with t_0/L large enough.
If different levels enter those hypotheses, their uniformity must
still be proved; the geometry does not sum nested physical energies.

## 6. Computation actually run

**Unchecked (finite exact arithmetic check, not a theorem by sampling).**
Criteria were saved before execution in
`checks/active-energy/CRITERIA.md`. Preflight returned go; acquire
returned acquired; the single job ran under nice with all five thread
variables set to 1, and release returned released. Both OS address/data
limit calls were unavailable on this Mac. The script enforced the
2 GiB RSS stopping check at each elimination pivot; peak RSS was
17,186,816 bytes. Logs retain those facts, including the unavailable
OS limits. The matrix dimension was bounded by 128 before allocation.

`response_scalar_exact.py` separately assembled the fine-site KKT
matrix and the M by M recurrence. With exact fractions, all equations,
means, slopes and energies agreed for (L,M)=(3,12),(5,12),(7,12),(5,16).
At the remote interface j=0, p_0 was respectively

    3072/7522955, 5120/10066329, 229376/515797425,
    81920/2576980377.

All interface slopes were nonzero. Zero-mean and constant-one controls
gave exactly constant minimizers and zero energy. The full stdout is
`checks/active-energy/response_scalar_exact.log`. There were no failed
runs or parameter changes. These rings are too small to test the
actual brick patch; (GREEN) covers arbitrary even M analytically.
No nonlinear minimizer, two-age configuration or AE-R search was run.

## 7. Scope stress test (no no-go packet or audit status claimed)

**Unchecked (N1-N8 author check).**

- N1, actual repair routes: an additive local/global tail (section 5);
  a local lift with boundary trace taken from W_ref, which changes the
  free-edge definition and its locality contract; or a global lift in
  the quiet test, which changes what the stopping algorithm may read.
  These are live changes of statement, not refutations of sections
  1-4. They were examined on paper, not implemented. There are three
  real families here; no five-family packet PASS is claimed.
- N2: the counterexample has one defect, a missing baseline term.
  The global frozen response and the local/global tail in section 5
  are sufficient conditions with no proved independence. AE-R and
  nonlinear frozen regularity remain open and may share dependencies.
- N3: the load-bearing inputs are the actual regular comb map, Wilson
  action, finite periodic geometry, free patch edge and common global
  reference. Section 4 derives the small-field minimizing limit;
  it does not import R3 or assume a smooth minimizer branch.
- N4: the earlier frozen-action and junction-response notes concern
  different residuals. They are not witnesses for this counterexample.
- N5: the failure is one positive plaquette contribution in one Q at
  one level, on a finite lattice. The runner checks scalar quadratic
  rings only. The full SU(2) assertion rests on section 4's author
  proof, not on a numerical simulation or a test of all fields.
- N6: an explicit additive term repairs the zero-data contradiction;
  no new physics axiom is needed. Its uniform estimate remains open.
- N7, steelman: “W_ref might mean the unfrozen lift on this same
  patch, or the displayed Resp might suppress a tail.” If it means
  a patch-dependent reference, sections 1-4 do not refute that new
  comparison; J must then compare the different references across
  bricks. If a tail was intended, Resp+ states the required repair.
  At the pinned wording ST/J use one global W_ref and write no tail.
- N8: the earlier cube note already listed local/global lift tails
  as open, and the paid-inputs junction note's IR explicitly allows
  their inclusion in C_R eps_q T. That approximate route remains
  live. This note only proves why the zero-source formula cannot
  silently omit the term.

**Gap at stop.** Prove Resp+ (or explicitly change the local reference)
with the uniform constants above. No impossibility of a corrected
response bound, J, AE-R, or Yang-Mills existence is asserted.
