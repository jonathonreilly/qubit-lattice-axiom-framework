# Direct weak-field inverse map with a supplied Ricci operator

Author: parent /root, 2026-10-13. Status: conditional-support.
Trace: frontier_discovery; reachability unknown_frontier.
This is a new parent derivation from the checked induced-curvature action.
The standard post-Newtonian (PPN) response formulas below are imported and
identified explicitly. Their apparatus/data reduction is not rederived.
No numerical execution or independent check has yet occurred at this freeze.

## 1. Observation first, and the physical bridge

The exposed Cassini summary is gamma-1=(2.1 +/- 2.3) 10^-5
(Bertotti, Iess, Tortora 2003, doi:10.1038/nature01997).
The historical lunar summary is eta=(4.4 +/-4.5)10^-4
(Williams, Turyshev, Boggs 2004, arXiv:gr-qc/0411113v2).
The latter combines lunar ranging with a composition experiment and a
geophysical self-energy model. It is not independent of the earlier campaign
lunar comparison. Its Cassini-derived beta estimate is NOT additional data.
Both summaries were exposed before this candidate was developed.

The intended question is what these response parameters reconstruct in the
new action, rather than whether a chosen parameter curve resembles a datum.
Assume a common almost constant local background x=y=0, light scalar on the
experiment's length/time scales, weak self-gravity and a controlled PPN
expansion. Matter couples universally to g_J=B^2 g_hat; no additional
composition coupling is present. Cosmological curvature is negligible on
the apparatus scale. Frozen auxiliary integration constants are held fixed
locally. These are candidate premises, not recovered observations.

The x=y=0 sector is locally consistent: neither the conformal factor nor the
u kinetic entry depends on x,y, so its transverse matter force and
Gamma^x_uu,Gamma^y_uu vanish. Background transverse fluctuations are not a
new linear fifth-force source in this sector. This does not dispose of
nonlinear/environmental/strong-body effects.

## 2. Coupling coordinates derived from the action

Use a>0, t=sqrt(a)u, s=zeta/q and z=s exp(2t). Define

    F/q=1+z,  J=1+(1-3a)z,
    Khat_uu=J/(1+z)^2,  B^2=exp(2t)/(1+z).

The positive tensor and scalar kinetic domain is 1+z>0,J>0.
The Damour-normalized scalar coordinate satisfies
d phi/du=sqrt(Khat_uu); it makes the action
q/2 [R_hat-2(d phi)^2] in this sector.
With alpha=d ln B/d phi and beta_D=d alpha/d phi, direct differentiation gives

    alpha=sqrt(a)/sqrt(J),
    k=alpha^2=a/J,
    beta_D=-a(1-3a)z(1+z)/J^2.                         (1)

Here beta_D is a coupling derivative, not the PPN parameter beta.
The supplied Ricci coefficient zeta is also unrelated to any symbol used
for a second-PN parameter in the cited literature.

For k !=1/3 these equations invert:

    a=k(1+z)/(1+3kz),
    J=(1+z)/(1+3kz),
    beta_D=-k(1-3k)z,
    z=-beta_D/[k(1-3k)].                              (2)

Thus k and beta_D determine a and the local z, not separately s and t.
For 0<k<1/3, the physical domain is simply z>-1.
For k>1/3 it is z>-1/(3k), which also implies z>-1.
At k=1/3, a=1/3 and beta_D=0 for every z>-1: the inverse map
has a genuine degeneracy. At k=0 the finite a>0 model is not attained;
the GR point is a boundary/limit, not a finite reconstructed a.

## 3. Imported response formula, then the model-specific inverse

Equations (1.1), (1.3), (1.4a,b) of Damour & Esposito-Farese,
arXiv:gr-qc/9602056v1 supply the normalized long-range PPN bridge:

    delta_gamma=-2k/(1+k),
    delta_beta= beta_D k/[2(1+k)^2],
    eta=4 delta_beta-delta_gamma
       =2k[(1+k)+beta_D]/(1+k)^2.                    (3)

The weak-body measured Newton coefficient is

    G_N=B^2(1+k)/(8 pi q).                            (4)

The positivity of k implies delta_gamma<0 for finite a in this regime.
An arbitrary positive measured central delta_gamma cannot be inverted to
positive k without considering measurement uncertainty/model limitations.
For -2<delta_gamma<0,

    k=-delta_gamma/(2+delta_gamma),
    beta_D=2(1+k)^2 delta_beta/k,
    z=-2(1+k)^2 delta_beta/[k^2(1-3k)].               (5)

If eta is supplied instead, use delta_beta=(eta+delta_gamma)/4.
The inverse is ill-conditioned at the GR boundary k=0 and at k=1/3.
A numerical fit near k=0 is not evidence of separate identification of a,z.

At the t=0 origin branch, z=s and H_J=H_v only when the supplied effective
constant satisfies C/H_v^2=3s/2. With G_N used for normalization,

    q=(1+k)/[8 pi G_N(1+s)], zeta=s q.                (6)

This calibrates q; it neither derives G_N nor selects s or H_v. In the formal
s->infinity limit at fixed k<1/3, a->1/3 from below, q->0,
and zeta approaches a finite value set by G_N. Finite positive q is required;
no quantum validity at this limit is established.

## 4. A cancellation which must not be confused with decoupling

For any 0<k<1/3 choose

    z_null=(1+k)/[k(1-3k)],
    a_null=(1-k)(1+3k)/4.                            (7)

Then beta_D=-(1+k), eta=0 and delta_gamma=-2k/(1+k) is nonzero.
This is an explicit candidate family, designed after seeing the response
summaries. It is not a blind prediction or a new exclusion escape theorem.

Along a change of local background with fixed a,s,q,

    d ln G_N/d phi=2 alpha[1+beta_D/(1+k)],
    eta=alpha/(1+k) d ln G_N/d phi.                  (8)

Thus (7) is also a stationary point of the weak-body G_N as a function of
the scalar background. It does not force phi_dot=0, and a Gdot constraint
cannot there be divided by a nonzero generic coefficient. Higher order
changes, independent clocks, finite scalar mass and body effects remain.
This derivative is along fixed theory parameters, NOT along the reconstruction
curve with k artificially held fixed.

On the tuned origin branch the previous exact local physical u mass becomes

    m_J,u^2/H_v^2=nu+3 k s(nu+4), nu>0.              (9)

The null family has s>0 and hence positive local origin mass; x,y physical
mass squares there remain 9/4 and 2. This is a local fixed-constant Hessian
statement. No global or boundary-constrained stability theorem follows.
Using a light-scalar PPN bridge additionally requires
sqrt(m_J,u^2/H_v^2) H_v L/c <<1, not merely positive mass.

## 5. Frozen descriptive comparisons and unresolved scope

Use n=1,2,3 multiples of each published uncertainty as rectangular diagnostic
bands, not joint confidence regions. For the Cassini band the allowed
finite k must obey

    0<k<=(n sigma_gamma-mu_gamma)/
            [2-(n sigma_gamma-mu_gamma)]            (10)

when n sigma_gamma>mu_gamma. Equality is a band edge; k=0 is a limit.
At fixed k<1/3 write

    eta=2k/(1+k)-D_k z,
    D_k=2 k^2(1-3k)/(1+k)^2>0.                      (11)

Intersect z from the eta band with z>-1; map through (2). All cases,
including excluded kinetics, positive gamma central values, failed band
membership, degenerate cases and singular inversions remain in the output.
No joint Gaussian likelihood or model-selection probability is constructed.
The principal frozen k=10^-5 is a supplied illustration inside the two- and three-uncertainty
Cassini bands, but outside the one-uncertainty band; it is not a best fit. Values chosen by (7) are deliberate null designs.

An extremely negative beta_D can invalidate a weak-source expansion or
produce strong-body phenomena; small k alone is insufficient. We record
|beta_D| times supplied compactness values as expansion diagnostics, with
no neutron-star exclusion claim. The original homogeneous fluid history and
global theorem have not been reconstructed for zeta !=0. This local inverse
map does not fill that cosmological gap, derive quantum matter, or establish
a TOE.
