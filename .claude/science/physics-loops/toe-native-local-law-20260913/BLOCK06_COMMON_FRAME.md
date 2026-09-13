# A common frame for both native Weyl nodes: candidate repair

Written before checking. The preceding commutator derivation treats one
linear cone at a time. A common gravitational interpretation additionally
requires both cones to see the same generic spatial metric, including shear.
This file constructs a specified finite-range free coupling to test that
requirement. Frame selection, interacting validity and gravity dynamics are
still supplied/open. No axiom update or uniqueness statement is proposed.

## 1. An explicit naive-frame witness

Write v=sqrt(1-zeta^2), F0=diag(1,1,v),

    u=(sin k1,sin k2,(zeta-cos k3)/v),
    r=2-cos k1-cos k2,
    d=F0 u+e3 r.

The two nodes are k_w=(0,0,w acos zeta), w=+/-1. The apparently natural
constant-frame family d_naive(F,k)=F u+e3 r has tangent

    D_w^naive=F R_w,  R_w=diag(1,1,w).

Its two quadratic cone metrics are R_w F^T F R_w. For a symmetric frame

    F=[[1,0,t],[0,1,0],[t,0,v]],

one gets offdiagonal metric entry g13=+/-t(1+v), with opposite signs at
the two cones when t is nonzero. This is a finite explicit two-cone witness
in that supplied family. It is not a general obstruction to a common metric.

## 2. A finite-range two-cone coupling

Let F=F0+f be any real constant3-by-3 frame. Define the following nine real
trigonometric vertex functions, indexed by Pauli row a and physical column j:

    V_aj(k)=sin k_j,                       a=1,2; j=1,2,
    V_a3(k)=(zeta-cos k3)sin k3/v^2,        a=1,2,
    V_3j(k)=sin k3 sin k_j/v,              j=1,2,
    V_33(k)=(zeta-cos k3)/v.

Set

    d_F,a(k)=d_a(k)+sum_j f_aj V_aj(k).                   (C1)

Every added vertex vanishes at both native nodes. Its first derivative there
is exactly

    partial_l V_aj(k_w)=(R_w)_aa delta_jl.

Since the original tangent is R_w F0, the deformed tangent is

    D_w=R_w F,      D_w^T D_w=F^T F.                    (C2)

Both nodes therefore have the SAME cone metric for every real F; when F is
invertible their chiralities remain opposite. No coefficient was extracted
from a fit. The trigonometric functions are an explicitly supplied constructive
choice; many higher-order additions could share their node data.

## 3. A global two-node preservation estimate

Let D=|d(k)| and b=zeta-cos k3. Then r>=0 and b>=-1/2. If r>=1,
 d3=r+b>=r/2, so r<=2D. If r<=1, put a_j=1-cos k_j. Since0<=a_j<=1,

    sin^2 k1+sin^2 k2=sum_j a_j(2-a_j)>=r.

Thus D>=sqrt(r)>=r in this region. Globally r<=2D and

    |b|<=|d3|+r<=3D.                                    (C3)

Also sin^2k1+sin^2k2<=D^2 and v<=1. For either of the first two rows,

    sum_j |V_aj|^2 <= D^2+9D^2/v^4 <=10D^2/v^4.

For the third row the bound is10D^2/v^2<=10D^2/v^4.
Cauchy-Schwarz, applied row by row, therefore gives

    |d_F(k)-d(k)| <= (sqrt(10)/v^2)||f||_F D.             (C4)

Consequently the explicit condition

    ||f||_F < v^2/sqrt(10)                              (C5)

implies |d_F(k)|>0 wherever |d(k)|>0. Since every added vertex vanishes at
k_w, the zero set remains exactly the original two nodes. Also
sigma_min(F)>=v-||f||_F>0 under(C5), so both nodes are simple. This is a
uniform Brillouin-zone proof for fixed zeta, not a search on sampled momenta.
It exposes its shrinking allowable frame neighborhood as the nodes merge.

The naive and repaired families agree at F=F0. At a generic small shear,
(C2) has a different physical consequence from the explicit naive witness.
Neither family is claimed as an axiom-selected metric law.

## 4. Physical native support and actual frame source

The new coefficients are finite Laurent polynomials. In particular,

    V_a3=zeta sin k3/v^2-sin(2k3)/(2v^2), a=1,2,
    V_3j=[cos(k3-kj)-cos(k3+kj)]/(2v), j=1,2.

For the orbital map (2x1+r,x2,x3), the sigma1,2 sin(2k3) term needs an
offdiagonal-orbital path with displacement plus/minus e_x plus/minus2e_z:
length3, using only protected x,z edges. A diagonal sigma3 xz term needs
plus/minus2e_x plus/minus e_z: length3. A diagonal yz term has length2 if
its y edge is protected; otherwise its x-plaquette detour followed by z has
length4. The remaining terms use the already specified paths of length at
most3. Thus every new hopping has a protected path of length at most4.
An open-box boundary must retain the same one-step x detour choice used in
the native construction; model terms exiting the box are omitted.

For a site-dependent real f_aj(x), use the Hermitian operator

    h_F=h0+(1/2)sum_aj {f_aj(x), sigma_a V_aj} .          (C6)

The finite-stencil native words are unchanged by these coefficients and
remain intertwined by candidate Record isometries. Differentiation gives the
actual frame source at site x:

    partial h_F/partial f_aj(x)={P_x,sigma_a V_aj}/2.     (C7)

This supplies a concrete stress candidate with reciprocal Hamiltonian
variation. It is not yet the complete geometric Dirac operator: for a
nonuniform frame, spin-connection terms and the full metric transformation
must be derived. The leading slowly varying first-order coefficient is
R_w F(x), so its common principal metric is already explicit. A local spin
term can change subprincipal transport without changing that principal metric.

## 5. Next coupled proof

Check(C1)-(C5) with exact symbolic node jets, a nonzero shear and the actual
finite Fourier coefficients; challenge the global bound at non-node corners
as well as near both nodes. Check protected physical routes. Then derive the
metric-dependent polar-frame action on spinor half-densities and its required
spin connection, retaining the field-dependent variation in the commutator.
The aim is a common continuum coupling with controlled native approximation,
not a relabeling of the one-cone normal/normal identity as full gravity.
