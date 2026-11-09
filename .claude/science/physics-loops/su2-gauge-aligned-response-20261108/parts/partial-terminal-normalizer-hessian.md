# Partial terminal deletion: exact normalized Hessian and conditional transfer

Author proof, 2026-11-09; independent checking pending. This is a conditional
finite-model statement, not a compact coercivity proof or physical spectral gap.
Source revision: `551840d63d189573688c763445b2eff9f99559d1`.
No numerical job, network search, Git mutation, or source tilt is used.
Parent supplied the completed first repository/literature pass: the existing
all-terminal compact argument pays every terminal mismatch; Dimock (2014)
is an abelian comparator, not an applicable sparse-removal theorem. The
calculation below is elementary differentiation of the actual Haar integral.

## 1. Exact law on the same forest

Fix odd L>=3, torus side L^2 m with m>=3, kappa>0, u>=1, beta=u,
lambda=t=kappa*u. Fix any subset J of terminal edges and O=E2\J.
Terminal outputs on O are I. Use the actual paired coordinate-order arithmetic
path means and the terminal-root fine forest of `flat-two-step-bound.md` §2:
only fine forest edges are fixed I; all intermediate edges are retained.
Write a=(a0,a1), U_e=exp(i a_e dot sigma), and w(U)=Re Tr(U)/2.
All coordinate norms count independent positive retained links and three colors.
The number of retained group links is n=m^4(3L^8+1+4L^4).

With probability Haar dQ, define

    Z(s)=integral exp(s w(Q)) dQ, h(s)=log Z(s)-s,
    r_h,c=|M_h,c|, gamma_h,c=r_h,c-<output_h,c,M_h,c>,
    E_J=W0+kappa sum_(all c at level 0) gamma_0,c
                 +kappa sum_(c in O) gamma_1,c.

The level-zero output is U1,c; the surviving terminal output is I.
Normalize q_u=Z_fine(u)^(-1) exp(-u W0), and let

    Q_J=integral q_u K0 product_(c in O) k1,c(I|U1) dU0 dU1.

The posterior hidden law is q_u K0 product_O k1,c / Q_J.
Every surviving kernel is exp(t<output,M>)/Z(t r). Removing J removes
both parts of those kernels and no part of any other kernel.

The root-fixed gauge transformation is determined uniquely by fine tree links.
Conditional on those links it acts by left/right translations on all free
fine and intermediate links. Haar invariance gives Jacobian one, and tree
Haar variables integrate to one. The integrand is invariant even after
deletion: transformations are identity at every terminal vertex. Thus the
quotient has product probability Haar on exactly these n retained links;
there is no extra forest determinant or residual-orbit division.
On the injective identity chart this is

    product_e [(2pi^2)^(-1) j(a_e) d^3a_e],
    j(a)=(sin|a|/|a|)^2, j(0)=1.

Consequently the exact normalized negative logarithmic chart density is

    S_J(a)=log Q_J+log Z_fine(u)+n log(2pi^2)+u E_J(a)
       +sum_(all level 0 c) h(t r_0,c(a))
       +sum_(c in O) h(t r_1,c(a))-sum_e log j(a_e).       (1)

If q_u was supplied unnormalized, omit log Z_fine and define Q_J with that
same convention. Either convention gives the same normalized density.
An additional coordinate-independent normalization changes the Hessian by zero.
Equation (1) is the unrestricted posterior evaluated in its chart, not a
claim that the chart has total probability one.

## 2. Direct finite-u differentiation

For one mean write its positively weighted paths P_gamma, with weights
alpha_gamma summing to one. Let p_gamma=P_gamma a denote the signed linear
link sum along that path; repeated occurrences count repeatedly. Set

    q=sum_gamma alpha_gamma p_gamma,
    v=sum_gamma alpha_gamma |p_gamma|^2-|q|^2 >=0.

Along epsilon a each path quaternion has scalar part
1-epsilon^2|p_gamma|^2/2+O(epsilon^3) and vector part
epsilon p_gamma+O(epsilon^2). This follows from its unit norm and its first
derivative at I, so possible second-order commutators do not change the
scalar coefficient. Hence, for output exp(i epsilon b dot sigma),

    r=1-epsilon^2 v/2+O(epsilon^3),
    <output,M>=1-epsilon^2(|b-q|^2+v)/2+O(epsilon^3),
    gamma=epsilon^2 |b-q|^2/2+O(epsilon^3).              (2)

Here b is the level-one hidden tangent or zero for terminal outputs.
Writing B(t)=Z'(t)/Z(t), differentiation under the compact Haar integral gives
B(t)=E_t[w(Q)]. The symmetry w -> -w implies Z'(t)>=0 for t>=0,
while w<=1 implies B(t)<=1. In particular 0<=B(t)<=1. Since r'(0)=0,

    log Z(t r)=log Z(t)-epsilon^2 t B(t) v/2+O(epsilon^3),
    -t<output,M>+log Z(t r)
       =constant+epsilon^2 t[|b-q|^2+(1-B(t))v]/2
          +O(epsilon^3).                               (3)

Thus the log-normalizer alone has NEGATIVE Hessian -t B(t)v; the
complete kernel has the POSITIVE variance correction t(1-B(t))v.
Equivalently h(t r) contributes t(1-B(t))v to the Hessian relative to
t gamma. No Z'' term survives at identity because r'(0)=0.

Let Q_h be these actual linear means, and define V0 and V1,O by summing
v over all level-zero factors and only the level-one factors in O,
respectively. Both are positive semidefinite. With P_O the terminal-edge
restriction and eta_u=kappa[1-B(kappa*u)], (2) and the Wilson plaquette
expansion give

    <a,H_E,J a> := D^2 E_J(0)[a,a]
      =||d0 a0||^2+kappa||a1-Q0 a0||^2
                             +kappa||P_O Q1 a1||^2,
    u^(-1) D^2 S_J(0)
      =H_E,J+eta_u diag(V0,V1,O)+(2/(3u)) I.           (4)

All operators are restricted to the same fine-tree slice. The Haar term
follows from -log j(a)=|a|^2/3+O(|a|^4). Every complete local term has
zero differential at identity, including W0 and Haar; therefore DS_J(0)=0.
Equation (4) is exact for finite u, with no large-u substitution for B.

## 3. Conditional transfer and deletion-uniform upper control

Assume, separately, that on this compact forest slice

    E_J(U)>=c sum_(retained e) [1-w(U_e)]                (5)

with c>0 uniform in volume (and in J if that stronger uniformity is wanted).
Here E_J(I)=0. Applying (5) to exp(i epsilon a), dividing by epsilon^2/2,
and taking epsilon -> 0 gives H_E,J>=c I, since
1-w(exp(i epsilon a_e dot sigma))=epsilon^2|a_e|^2/2+O(epsilon^4).
Equation (4) and eta_u>=0 prove exactly

    u^(-1) D^2 S_J(0)>=(c+2/(3u)) I.                  (6)

Only the local germ of (5) is needed for this implication; establishing (5)
on other means/configurations is an independent compact obligation. In
particular this proof asserts no c for arbitrary deleted J. It does not
conflict with a compact counterexample, including the eight-edge example.

For upper control, each complete terminal kernel's Hessian is positive
semidefinite by (3). Thus deletion decreases the action Hessian in Loewner
order. The full-kernel estimate of the flat supplier gives, with
ell=5L-4 and C=8ell^2,

    0<=u^(-1)D^2 S_J(0)<=[16+kappa(2+3C)+2/3] I, u>=1. (7)

This uses no positive lower bound for deleted J. The source's range-two
terminal-cell reader property also persists under deletion and coordinate
restriction; Haar is diagonal. Uniform absolute row bounds, if needed,
follow from fixed bounded reader counts, local Hessian coefficients and
bounded incidence, not from the operator bound alone. Arbitrary J may break
translation symmetry but cannot enlarge any factor support or incidence.

These are gauge-coordinate precision bounds. No physical spectral gap,
nonlinear concentration, response decay, or compact coercivity is inferred.
No original source tilts, shifted means, or chart re-centering are covered.

## 4. Source identities and recovery

SHA-256, paths relative to this pack unless stated otherwise:

- `parts/flat-two-step-bound.md` (full):
  `0f028f694bb686cf4272d8620329f1f2e8535d8af9a2d028bbde6965cab3f03a`.
- `parts/frozen-gaussian-producers.md` (needed §§1,5):
  `ac4984909f5edbc5e79f9cb3ffd212862f43295d9a0537e0102fb4e38d0900c3`.
- `parts/partial-terminal-normalization.md` (needed §1):
  `722e622dd64763e7f85461ef037f78810ec1c96d5bb71ddc7d60647c858b9867`.
- Repository `AGENTS.md`:
  `7def904fdd52d811e7aba87a0d3d859bfb017cccd59703125f4a53f2805aaab2`.
- Repository `docs/ai_methodology/SCIENCE_WORKFLOW.md`:
  `1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca`.

Current checkpoint: exact identity (4) and conditional implication (5)->(6)
proved at author level; fresh checker pending. Missing input for an actual
deleted-J gap is (5), not a radial-normalizer estimate. No failed numerical
route exists in this worker. Parent holds the science lease and supplied
preflight; this file is the only edited artifact.
