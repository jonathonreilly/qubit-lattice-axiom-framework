# Finite cubic record cooling and an explicitly retuned ground-state channel

Status: personal conditional results, independent check pending. The exact
finite-spin arguments below and a complete864-state calculation concern the
supplied gauge model. No thermodynamic photon phase or native compiler is
inferred. A positive retuned channel is constructed with its nonlocal input
requirements exposed.

## 1. Fixed local cooler and its finite output cost away from RK

Use the finite connected plaquette component and jumps from
LOCAL_GAUGE_RECORD_COOLING_TO_RK_STATES.md. Let D>1 be its dimension, m the
number of plaquettes, gamma_min>0 and gamma_max their extreme rates. Set

    H_delta=J sum_p(P_p-X_p)-delta V_f,  V_f=sum_p P_p, J>0,
    K_loss=sum_p gamma_p L_p^dag L_p,
    u=D^(-1/2)sum_c |c>, P0=|u><u|.

Assume delta is nonzero and Var_u(V_f)>0. The companion Hamiltonian-change
note proves that the specified generator has no pure stationary density.
Here there is also a quantitative lower bound on stationary jump output.

### 1.1 A finite loss gap without a spectral assumption

For v perpendicular to u, connectedness gives a path of length at most D-1
between any pair of configurations. By the path Cauchy-Schwarz inequality,

    ||v||^2=(1/D)sum_(a<b)|v_a-v_b|^2
           <=(D-1)^2/2 sum_(undirected graph edges)|v_a-v_b|^2.

Each distinct graph edge occurs in at least one plaquette projector. Thus

    K_loss >= [gamma_min/(D-1)^2](I-P0).                     (1)

Parallel flip edges only increase the quadratic form. This deliberately
weak finite bound is not an efficient preparation or thermodynamic gap claim.

### 1.2 Positive stationary output and long-time expected count

For the trace norm on arbitrary matrices,

    ||G_delta||_(1->1) <= c,
    c=2m(2J+|delta|+gamma_max),                               (2)

using ||P_p-X_p||<=2, ||P_p||<=1 and ||L_p||<=1. For a stationary density rho,
equation(1) of the companion note, now in trace norm, gives

    2|delta|sqrt(Var_u(V_f))=||G_delta(P0)||_1
         <=c||rho-P0||_1 <=2c sqrt(1-<u|rho|u>).

Combining with (1), every stationary density obeys

    Tr(K_loss rho) >= gamma_min delta^2 Var_u(V_f)
                      /[(D-1)^2 c^2] = j_min >0.             (3)

No uniqueness assumption is needed. For any initial density, every limit
point of its Cesaro time averages is stationary because
G_delta[(1/T) integral_0^T rho(t)dt]=(rho(T)-rho(0))/T. Compactness then gives

    liminf_(T->infinity) E[N_jump(T)]/T >= j_min.              (4)

If each jump emits two permanent records, the expected record-output rate
has twice this lower bound. Equation(4) is an expectation statement; no
trajectorywise law of large numbers is asserted. It concerns this continuing
driven preparation apparatus, not the rate of record production in every
possible vacuum model.

## 2. Complete finite cubic calculation

The runner constructs the periodic2x2x2 lattice with24 directed positive-axis
links and24 plaquettes, and traverses the zero-Gauss, zero-flux component of
864 configurations. Its flippability distribution is

| Flippable plaquettes | 4 | 6 | 8 | 10 | 12 | 16 |
|---|---:|---:|---:|---:|---:|---:|
| Configurations | 120 | 64 | 492 | 96 | 80 | 12 |

Hence mean flippability is8 and variance16/3 exactly. Translations, proper
cubic rotations and field complement give384 distinct configuration actions.
The runner checks that every local jump transforms into another jump up to
a constant sign, under every action. Ordered configuration pairs have2723
orbits. This reduces the stationary operator equation, which is solved for
J=gamma=1 and delta=0,0.05,0.2,0.5,1.

Each resulting864x864 matrix is then checked against the full, unreduced
Lindblad equation, trace, Hermiticity and positive spectrum. The maximum
full-entry residual over this screen is6.12e-17 in floating-point arithmetic.
The runner passed its first complete run; its complete outputs and receipt
are preserved. A unique stationary solution inside the invariant operator
sector does not alone prove global uniqueness at nonzero delta; no such
inference is made.

For example at delta=0.2 the stationary purity is approximately0.55995,
the fidelity to the actual finite Hamiltonian ground state is0.74744, and
the total jump intensity is0.44714. At delta=1, the pure-ring Hamiltonian
has ground energy-9.0267209135 and within-component gap2.2257853859, while
the continuing old cooler has purity0.03138, ground fidelity0.15254 and
jump intensity1.82163. These are finite apparatus results, not an infrared
phase diagnosis. The single-mode Gaussian calculation in the companion
note remains a separate stipulated model, not a fit to these data.

## 3. A positive exact retuned construction

The finite H_delta has connected negative off-diagonal flip amplitudes for
J>0. Perron-Frobenius applied to a sufficiently shifted -H_delta gives a
unique normalized ground vector psi with every coefficient psi_c positive.
For each undirected configuration-graph edge e=(a,b), define

    w_e=psi_a^2+psi_b^2,
    s_e=(psi_a|a>+psi_b|b>)/sqrt(w_e),
    d_e=(psi_b|a>-psi_a|b>)/sqrt(w_e),
    A_e=|s_e><d_e|,       eta_e>0.

Use the original H_delta together with separate jumps sqrt(eta_e) A_e.
They annihilate psi, are partial isometries with orthogonal source/range,
and preserve the fixed Gauss sector. The state |psi><psi| is stationary.
More strongly, with f(t)=<psi|rho(t)|psi>,

    dot f=Tr(M rho),
    M=sum_e eta_e w_e |d_e><d_e|.                            (5)

This follows from <psi|s_e>=sqrt(w_e) and <d_e|psi>=0. Connectivity and
strict positivity of psi imply ker(M)=span(psi). If mu is its smallest
nonzero eigenvalue, then

    dot f>=mu(1-f),
    ||rho(t)-|psi><psi|||_1 <=2sqrt(1-f(0)) exp(-mu t/2).      (6)

Writing K_ad=sum_e eta_e |d_e><d_e|, the expected total number of emitted
jump records satisfies

    E[N_jump(infinity)] <= ||K_ad||(1-f(0))/mu < infinity.     (7)

Each jump has the same exact fresh-fuel partial-isometry collision dilation
as the local RK cooler, now with A_e substituted for L_p. Equations(5)-(7)
are a constructive escape from keeping a mismatched reservoir unchanged.

The price is explicit: these separate channels are indexed by full
configuration-graph edges, including spectator data, and require the ground
amplitude ratios. They are not the original24 local plaquette channels and
are not a finite-range implementation merely because a and b differ on one
plaquette. The whole-configuration condition can have volume-size support.
The finite runner verifies target annihilation and computes a numerical mu;
it does not implement those global conditions on the native lattice.

At the uniform target the resolved construction has
M=(2/D)sum_e eta_e |d_e><d_e|. Resolving spectator configurations can therefore
make the direct fidelity bound poor even when the loss operator has a good
gap. One must not rescale the many channels without also accounting for the
available total local coupling and record resources. No general efficient
ground-state preparation algorithm is claimed.

## 4. Next constructive question

The next useful test is a genuinely local approximation to the required
amplitude ratios, with independently measurable preparation error and with
the apparatus switched off or correctly adapted during the later field
evolution. A high overlap on this small torus alone would not establish a
Maxwell vacuum in the thermodynamic limit. The controls here identify the
compatibility problem and supply one exact, explicitly nonlocal alternative.
