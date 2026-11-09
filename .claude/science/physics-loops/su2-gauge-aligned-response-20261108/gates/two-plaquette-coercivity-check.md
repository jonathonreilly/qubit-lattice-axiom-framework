# Two-plaquette deletion: independent compact and normalized-Hessian check

Research gate, 2026-11-09. The independent argument below was derived before
receipt of either new author proof. Both final candidates and the two final
claim surfaces have now been read completely and checked at the exact hashes
below. **Research-gate signal: advance. No material defects found.** The
claim-surface consistency check is complete. This is neither a landing
review nor a formal audit and grants no retained status.

Assigned source HEAD: `551840d63d189573688c763445b2eff9f99559d1`.
Same-provider fresh context at the inherited supervisor model and effort;
no override was requested or made. The parent supplied the completed shared-
host preflight and active lease. No numerical job, network search, Git
mutation, or source-proof edit was performed. Only this report is written.
The parent's prior-art report identifies a scope mismatch in the old fully
pinned result; no matching outside theorem is imported. Repository AGENTS,
SCIENCE_WORKFLOW, and reviewer/proof-check instructions were read at this
frozen revision. Installed reviewer-skill drift was detected; the repository
copy was then used. Remote-main freshness was not reasserted.

## Source identities actually inspected

Paths are relative to `.claude/science/physics-loops/su2-gauge-aligned-response-20261108/`.

| File | Read scope | SHA-256 |
|---|---|---|
| `parts/compact-energy-coercivity.md` | Complete | `7e8e798759239aadfc8c137125bf23f6d1de2cac18b714ddca70ea294cbaa4aa` |
| `parts/flat-two-step-bound.md` | Sections 1–3 | `0f028f694bb686cf4272d8620329f1f2e8535d8af9a2d028bbde6965cab3f03a` |
| `parts/partial-terminal-normalization.md` | Section 1 | `722e622dd64763e7f85461ef037f78810ec1c96d5bb71ddc7d60647c858b9867` |
| `parts/released-terminal-gauge-directions.md` | Section 4 | `a8271fb33178da46f747075f8b98f266cb06833ae900b99ef0544f36adcb403b` |
| `parts/frozen-gaussian-producers.md` | Sections 1, 5 | `ac4984909f5edbc5e79f9cb3ffd212862f43295d9a0537e0102fb4e38d0900c3` |
| `parts/partial-terminal-normalizer-hessian.md` | Complete, 170 lines | `a17f372f928930bd9be6e81d68349a62232a027f17a13a7cd47e813f43584139` |
| `parts/two-plaquette-compact-coercivity.md` | Complete, 236 lines | `b77fdb722d19c96594cddded301d9dd019c412b875721f5c28d1461415bb246e` |
| `../../../../docs/SU2_TWO_PLAQUETTE_MARGINAL_COERCIVITY_BOUNDED_THEOREM_NOTE_2026-11-09.md` | Complete, final notation revision included | `3ccad623a10d425a72fdba6aaf63cd41910e687bd1e89d16084b7c56e3f42403` |
| `PROOF_TREE.md` | Complete, claim-surface consistency | `141d59926631c69ac1815dc1dc690c00364fec4a291c1b93316ef9dafeec72eb` |

The fifth old science file was needed only to check the Hessian author's
additional upper-bound/support paragraph. No previous gate verdict was used
as mathematical evidence. The parent reported its own favorable reading of
the Hessian file when delivering it and similarly reported no defect in the
compact file. The derivations below had already been obtained independently;
neither conclusion was adopted from those reports. The independently
selected geometric detour is the same mechanism as the author's, while the
closure here keeps root transporters explicit rather than restoring the
auxiliary terminal gaps. Both checks share the stated old compact premises.

## 1. Exact target and surviving law

The terminal graph is the four-dimensional periodic nearest-neighbor graph
of side m>=3, with fine side L²m, odd L>=3 and kappa>0. J is the seven
positive-edge variables of two distinct elementary terminal plaquettes
whose edge sets intersect in exactly one edge. Coplanar and hinged pairs,
every translation/orientation, and periodic seams are included. O is the
complement. The zero-source hidden law is exactly

    q_u(U0) K0(U1|U0) product_(c in O) k1,c(I|U1),

up to its global normalization. Every K0 factor and every surviving radial
normalizer remains. The fine forest has one internal spanning tree per
terminal block, rooted at its terminal vertex; all intermediate links remain.
The target is

    sum_retained [1-w(a_e)] <= C(L,kappa) E_J,
    E_J = W0+kappa sum_all gamma0+kappa sum_O gamma1,

on the full compact configuration space, uniformly in m, location,
orientation, and all those tree choices. No all-depth or physical mass
statement is part of this check.

## 2. Independent local replacement for the seven deleted constraints

The two squares together use at most three coordinate axes. Choose a fourth
axis tau unused by both. All vertices and edges of J have one common
tau-coordinate. For any positive deleted edge e=(x,x+e_mu), use the oriented
three-edge detour

    D_e: x -> x+e_tau -> x+e_tau+e_mu -> x+e_mu.

Both side edges have direction tau and cannot belong to J. The parallel
middle edge has a different tau-coordinate from J because m>=3, so it too
belongs to O. The last side is traversed backwards; its positive-edge
variable is still in O. This is an explicit bounded detour, not an appeal
to connectivity or a graph spectral gap.

Let T_c be the straight fine root-to-root transporter for terminal edge c,
and d_c=||I-T_c||². Replace the three detour edges by their straight fine
paths. Their product and T_e bound the lifted L² by L² fine square S_e in
the mu,tau plane. Peeling its L⁴ plaquettes and telescoping in the
bi-invariant quaternion distance gives

    ||T_e-T_(D_e)||² <= 2 L⁴ sum_(p in S_e) W0,p.

The squared triangle inequality and three-factor telescoping then give

    d_e <= 4 L⁴ sum_(p in S_e) W0,p
                             + 6 sum_(c in D_e) d_c.       (IC1)

A deliberately loose global charge bound already suffices: there are only
seven squares/detours, each has three distinct terminal edge variables, and
each fine square uses any projected fine plaquette at most once. Therefore

    sum_J d_e <= 28 L⁴ W0 + 42 sum_O d_c.                  (IC2)

The coefficient 42 only uses the bound seven on repeated detour use; no
disjointness or unproved charge cancellation is assumed. One can improve
it because side-edge use is at most the degree three of the two-square
graph, but the improvement is unnecessary.

To finish without importing the fully pinned conclusion into the deleted
law, keep the terminal transports explicit in the old proof. Its sections
3, 5, 6 establish, before using terminal pinning, a finite A(L) such that

    sum_retained [1-w(a_e)]
       <= A(L) [W0 + sum_all gamma0 + sum_all_terminal d_c]. (IC3)

Section 4, applied only where the kernel survives, establishes a finite
B(L) with

    sum_O d_c <= B(L) [W0 + sum_all gamma0 + sum_O gamma1].  (IC4)

Each is a finite, nonnegative local-stencil bound. Their constants are
independent of volume and tree choice for the reasons checked in section 3.
Combining (IC2)–(IC4) proves the requested compact inequality with a finite
constant K(L) max(1,kappa^(-1)). Missing gamma1 factors never enter it.
This also supplies the exact missing implication between the old pinned
argument and the new law.

## 3. Edge cases and discriminators checked analytically

- **Small torus, seams, coplanar pair.** On m=3 let x=(2,2,2,0). Take the
  (1,2) plaquettes based at x and x-e2. Their positive-edge boundaries
  intersect only in (x,1). They wrap across coordinate 1 and one across
  coordinate 2. Choosing tau=4 places every middle detour edge at coordinate
  4 equal to 1, whereas J lies at 0. All fourteen side occurrences have
  direction 4, outside J. No distinctness assumption fails modulo 3.
- **Small torus, seams, hinged pair.** At the same x take the (1,2) and
  (1,3) plaquettes. Their only common edge is (x,1), and they cross seams
  in three used directions. The same tau=4 construction is entirely in O.
  Translating the pair to coordinate 4 equal to 2 merely makes that detour
  cross another seam; the lift still has identical comparison endpoints.
- **No winding-loop substitution.** Each comparison is made in the lifted
  mu,tau rectangle and only then projected. Its perimeter has zero lifted
  displacement. This remains true when its sides cross one or more seams.
  No noncontractible torus loop is filled.
- **Zero mean.** For M the path average, r=|M|, and unit V,T, independently
  expanding |V-M|²=(1-r)²+2gamma and applying Jensen gives
  |V-T|²<=4gamma+3 average|P-T|². At M=0 the average on the right is exactly
  2; no division by r or preferred polar direction occurs. Thus the old
  local mismatch and curvature bounds used in (IC3),(IC4) cover zero means.
- **Curvature and stencil reuse.** All right sides are positive sums with
  multiplicity. Seven repairs cost at most seven uses of any curvature
  charge in (IC2). The old forest and path templates have bounded extent
  depending only on L. Projection may identify stencil offsets, but cannot
  create more than their fixed total coefficient mass. This proves bounded
  congestion, rather than relying on the complement graph's connectivity.
- **Arbitrary rooted trees.** A simple internal fine-tree path has at most
  L⁸-1 edges. Each comparison involves one or two terminal blocks. There
  are finitely many possible internal trees and path templates, so taking
  coefficient maxima before summing covers independent tree choices in
  every block. Intermediate edges of length L cannot skip a terminal block.
- **Root modes.** For a root potential xi, its forest-slice gradient has
  terminal differences xi(x)-xi(y). Deleted differences are the sum of the
  three surviving detour differences. Thus the same factor-three
  Cauchy–Schwarz bound controls them. No volume-uniform Poincare inequality
  for the norm of xi itself is invoked. This distinguishes the requested
  link-coordinate norm from the vertex-potential norm. The eight-edge
  isolated-root example fails the detour hypothesis and remains intact.

These are exact analytic cases and arguments, not claimed numerical runs
or exhaustive computer enumeration. Dropping the curvature term from (IC1)
would be invalid for nonflat fields: the detour holonomy need not equal the
direct transporter. Dropping the surviving mismatch terms from (IC4)
would leave flat holonomies uncontrolled. Both terms are load-bearing.

## 4. Independent normalized-kernel calculation and transfer

For one actual kernel set t=kappa*u and
Z(t)=integral exp(t w(Q)) dQ under probability Haar. Write p_gamma for the
signed first-order path sum, q=average p_gamma, and
v=average|p_gamma|²-|q|²>=0. Along epsilon a, unit norm fixes each path's
scalar coefficient even when its second-order vector part is noncommutative:

    r(epsilon)=1-epsilon² v/2+O(epsilon³),
    <exp(i epsilon b.sigma),M(epsilon)>
       =1-epsilon²[|b-q|²+v]/2+O(epsilon³).

With B(t)=Z'(t)/Z(t), symmetry under Q -> -Q gives B(t)>=0 and w<=1
gives B(t)<=1. Direct differentiation of the complete kernel action yields

    D²[-t<output,M>+log Z(t r)](0)[a,a]
       =t[|b-q|²+(1-B(t))v].                            (IC5)

The radial log-normalizer ALONE contributes -t B(t)v; it is not positive.
There is no Z'' contribution because r'(0)=0. The positive variance
correction belongs to the complete normalized kernel relative to t gamma.

A second check avoids the radial representation. Put
N(M)=integral exp(t<Q,M>) dQ. At M=I its gradient is t B(t) I and its
ambient Hessian is t² Cov_t(Q). Along M(epsilon), M'(0)=(0,q) and the
scalar component of M''(0) is -average|p_gamma|². Haar invariance under
left multiplication by exp(i epsilon sigma_i), applied to
Q_i exp(t Q_0), gives the exact identity

    t E_t[Q_i²]=E_t[Q_0]=B(t).

Transverse means vanish and transverse covariance is isotropic. Therefore
the chain rule directly on N gives
D² log N=-t B(t) average|p_gamma|²+t B(t)|q|²=-t B(t)v.
This covariance/rotation calculation independently discriminates the sign
and the variance subtraction in the radial calculation.

Taking b=a1 for K0 and b=0 only for the surviving terminal kernels gives

    u^(-1) Hess S_J(0)
      =Hess E_J(0)+kappa[1-B(kappa*u)] diag(V0,V1,O)
                                                  +2/(3u) I. (IC6)

The last term follows directly from -log[(sin|a|/|a|)²]
=|a|²/3+O(|a|⁴). Product Haar on retained links follows by conditioning on
fine tree variables and using left/right Haar invariance; no intermediate
tree is removed. The retained-link count m⁴(3L⁸+1+4L⁴) and the additive
normalization constants in the author's formula (1) are consistent.
Global Q_J and Z_fine are coordinate independent.

If E_J>=c sum_retained(1-w), its expansion along epsilon a gives
Hess E_J(0)>=c I with exactly that c. Equation (IC6) then proves

    u^(-1) Hess S_J(0) >= c I+2/(3u) I.

All surviving variance terms are retained and have the required sign. No
large-u limit or chart normalization assumption enters this implication.
For an arbitrary J without compact coercivity it proves no positive c.

The Hessian candidate's additional upper bound is also consistent: each
deleted complete terminal factor has positive semidefinite identity
Hessian, so deletion decreases the action Hessian on the unchanged slice.
The path length ell=5L-4 and eight adjacent block-edge footprints give the
loose reader bound C=8ell², hence the displayed
16+kappa(2+3C)+2/3 for u>=1. Deletion and coordinate restriction cannot
enlarge factor supports or bounded incidence. Operator norm alone would
not prove absolute row bounds; the candidate explicitly uses reader counts.

## 5. Exact final-file comparison

Both candidate hashes in the table matched the delivered identities. No
material error was found in either complete file. Specifically, the compact
candidate's equations (4)–(7) retain all discrepancies: W1<=A has the
correct factors 4 and 2L²; H=2F+2L sum D pays the path-to-straight error;
B=8gamma1+6F+2L sum D pays the terminal-to-straight error; and the auxiliary
missing gamma1 is bounded above by H+d(I,T)². Its equations (9)–(10) then
pay both the curvature rectangle and all three surviving B terms. Nothing
silently converts a centered gap into an uncentered energy summand.

The coefficient-mass argument defining Q(L) is valid after periodic
projection because coefficients add, stay nonnegative, and retain their
finite total mass. The factor seven controls every repair overlap. Its
equation (11), E_all<=constant E_J, is established before the old all-terminal
forest inequality is invoked; the latter is therefore used legitimately
as an auxiliary deterministic comparison, not substituted as a posterior.
The finite tree-template argument and the resulting formula (12) cover
all of the target's tree, position, orientation, and volume quantifiers.
The additional locality statement also follows directly from
a_e=H_x U_e H_y*: each H path remains inside an endpoint terminal block.
This check did not import an additional theorem from compact-forest-exchange.

The Hessian candidate's exact law, complete-kernel signs, conditional lower
bound, and stated upper control agree with section 4. In particular deleting
an output deletes its entire kernel; every surviving normalizer is retained.
Together the two proofs establish the requested compact bound and its
finite-u full-chart identity-Hessian consequence for this seven-edge family.
They do not establish concentration, connected-response decay, a physical
mass, or a repeated-blocking result. The eight-edge counterexample is
unchanged. No mathematical repair is requested.

## 6. Final claim-surface consistency and verification limits

The complete primary note and proof tree were read at their tabled hashes;
both exact proof hashes were refreshed at the same time and remained fixed.
The primary note was reread completely after its final notation-only update
explicitly defined n=m⁴(3L⁸+1+4L⁴); the final hash above supersedes the
initial `5bc9b77afc2928d96cdc7cc7c945fc2f453060a3eb2dfc20757a4cc6d51fae62`.
The primary note's compact theorem, displayed energy comparison, constant,
exact posterior chart density, and finite-u lower bound match the two proofs.
Its arbitrary-tree, seam, m>=3, zero-mean, zero-source, identity-exterior and
two-step qualifications are preserved. Its `proposed_retained` header is
qualified by `actual_current_surface_status: bounded-support` and an explicit
separate-audit requirement; it makes no effective-retained assertion.

The proof tree's new Q-coercivity and Q-precision entries match those results.
The complete response for the deleted law remains open, and the map requires
new local nonlinear, regional relative-energy, and source-marked compact
suppliers before that response is claimed. Larger conditionals, nonidentity
backgrounds, iteration, continuum reconstruction and physical spectral
control remain open. The eight-edge residual-gauge example is not repurposed
as a refutation of the seven-edge theorem. No scope correction is requested.

A deterministic filesystem check found all 8 local Markdown links in the
primary note and all 31 in the map present. This verifies availability, not
the mathematics of every linked historical file. The earlier twenty-part
response packet and external literature search were not recertified here;
the present map was checked for consistency with the newly examined claims.
The Fable advice record was not read or used in this independent derivation.
Final refreshed hashes of all five inspected old science inputs also matched
the table. No numerical test or formal verification is claimed.

There is no unresolved mathematical step in the assigned compact/Hessian
target or in this claim-surface check. The only edited artifact is this gate
report; no editable prompt or scientific proof file was modified.
