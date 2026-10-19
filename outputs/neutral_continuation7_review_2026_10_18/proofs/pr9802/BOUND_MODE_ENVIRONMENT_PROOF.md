<!-- Original PR9802 source SHA256 9b6c653959ae91a779a784676446e8d1959f5e540624f8d83833503f90d3ca90. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native bound-mode coupling and the heavy environment

Status: conditional-support. Same supplied one-qubit Hamiltonian and fixed even slab height L>=10 as TEN_LAYER_NEUTRAL_BOUND_PROOF.md. This block derives a prepared heavy-return coupling to that mode and solves a separate static-background heavy scattering problem. It does not combine them into a full native on-shell emission rate or relaxed universal charge. No interaction is added.

## 1. The actual heavy background is not a free wave

In singleton-over-column coordinates the first heavy hopping coefficient is

 T_s(i,j)=-1 on x edges, -s_i s_j on y edges.

A shortest neutral feature flips two adjacent column signs. For a horizontal pair at (0,0),(1,0), T_s differs from free -Adj by +2 on four vertical bonds joining these sites to their upper and lower neighbors. These signs are fixed by the microscopic XX/YY terms.

Let R be a quarter-turn spatial rotation, P_R its site permutation and U_s=diag(s_i). Direct bond evaluation gives T_(Rs)=P_R U_s T_s U_s P_R^dagger. The physical spin rotation contributes phase i s_i to a singleton relative to its background. The complementary x vertex -a E becomes the y vertex +a Z_i Z_j E, a=2^-(L-2)lambda^(L-1), with exactly the same phase rule.

Consequently correctly rotated outgoing waves have opposite endpoint signs on the flipped columns. Their x and y channel amplitudes add in the even physical combination. Replacing both outgoing waves by identical free waves instead gives cos(K_y)-cos(K_x), zero at rest. That zero is a property of the specified free prepared state, not an exact selection rule of the background-dependent Hamiltonian. Absence of a symmetry-forced zero does not prove a nonzero threshold rate.

## 2. Prepared closed-return coupling to the native pole

Use matched canonical vacuum and heavy embeddings, a singleton prepared at fixed site i and layer, evolution for t=hbar*tau/(Jlambda), and a final return to i with the neutral pole readout. Remove the common heavy energy phase. The preparation and conditional final readout are explicit protocol premises; this is not a relaxed heavy ground experiment.

Let Delta4=L/16, c=(gamma_L/Delta4)lambda^(L-4), and T_bg=sum_e E_e. The vacuum is g0+c T_bg g0+..., while the even pole tends to b0=(A+B)/sqrt2 and has the compensating flat component -c sqrt2 R g0. Thus its return amplitude starts

 c/(sqrt2 R) sum_edges [r_e(tau)-r_0(tau)],
 r_e=<i|exp(-i tau T_e)|i>.

The subtraction follows from eigenstate orthogonality; omitting it gives an incorrect nonzero amplitude at zero time. Each edge syndrome has b0 amplitude1/(sqrt2 R). Closed returns are invariant under the flat-background diagonal gauge, so averaging the flat orbit does not change this expression.

Translation and gauge-covariant quarter-turn symmetry convert the edge sum to twice a trace difference for one horizontal defect:

 sum_edges(r_e-r_0)=2 Tr[exp(-i tau T_def)-exp(-i tau T_free)].

The first two even return moments agree. The exact fourth diagonal moment is 28+2 sum_(p incident i)P_p. Each of the four nearby plaquettes belongs to eight edge syndromes, giving a summed fourth-moment change -128, or a single-defect trace change -64. Therefore

 amplitude = -(8sqrt2/3) gamma_L/(Delta4 R)
              lambda^(L-4) tau^4
             +O(lambda^(L-4)tau^6/R)+higher-lambda terms.       (1)

At fixed sufficiently small nonzero tau this is a nonzero native coupling to the bound mode. Its leading small-tau squared weight is (128/9)gamma_L²/(Delta4² R²)lambda^(2L-8)tau^8. The normalized single-site to zero-momentum overlap explains 1/R, rather than a volume-independent charge.

The trace difference has a well-defined infinite-array limit at fixed tau: the perturbation is finite rank and the closed-walk expansion is absolutely summable. If V=T_def-T_free, telescoping gives |Tr(T_def^n-T_free^n)|<=n||V||_1 4^(n-1), with ||V||_1=8sqrt2. Bipartiteness removes odd moments. This bounds the higher-time remainder uniformly and guarantees the sign for sufficiently small tau. Exact controls give trace moments -64,-1440,-26112,-439840 at orders4,6,8,10.

## 3. Why the small amplitude survives microscopic evolution

A generic O(lambda) Duhamel error would swamp (1) and is not sufficient. Use exact analytic block identifications, or a finite construction whose error after time1/lambda lies beyond the signal order. The exact plane-parity pattern selects the singleton/complement sector within N2.

Split the effective return into background-preserving and background-changing contributions. A changed even background pair in a singleton hop needs at least L-1 native insertions, so the rescaled generator first changes it at lambda^(L-2). At fixed tau this is later than lambda^(L-4). The background-preserving return is diagonal in background labels and constant on the flat orbit by plane symmetry: the same-position endpoint phases cancel. It consequently has no flat-vacuum to orthogonal-pole transition until the vacuum/pole admixture c is included. Its O(lambda) correction therefore gives O_R,tau(lambda^(L-3)), not an uncontrolled O(lambda) signal. Higher admixtures and the endpoint-mode tail are also subleading.

This establishes (1) for matched dressed preparations at fixed admissible R and fixed tau, with the subsequent small-tau coefficient expansion. It does not establish the same coefficient for an uncorrected bare spin pulse: the older O(lambda) estimate for bare versus dressed preparation is insufficient. A simultaneous tau(lambda) limit likewise needs an additional comparison with tau^4. The pole's actual-ground interpretation retains the separate fixed-size selection qualifications of the preceding block.

## 4. Static threshold environment: exact six-site reduction

Now consider a different, explicitly specified question: the native leading heavy coefficient in the fixed horizontal-pair background. Put L0=4-Adj and Lmag=L0+V. On a large box with boundary value one, its zero-energy solution obeys u=1-G_R V u, G_R=L0_Dirichlet^-1. Only six sites enter V. This is an exact finite-rank reduction, not an assumed barrier.

Use the potential kernel for L0,

 A(x)=integral_BZ [1-cos(k.x)]/[4-2cos kx-2cos ky] d²k/(2pi)².

The local values are A10=1/4, A11=1/pi, A20=1-2/pi, A12=2/pi-1/4. The origin equation supplies A10; integrating one Fourier variable gives A11, and the harmonic recurrences give the last two. The standard killed-walk Green identity and potential-kernel asymptotics yield G_R(i,j)=g_R-A(i-j)+o(1), g_R=log R/(2pi)+O(1). Our normalization is one quarter of the usual simple-random-walk kernel. These standard mathematical inputs are documented in Lawler and Limic, Random Walk: A Modern Introduction, sections4.4 and4.6 (https://www.math.uchicago.edu/~lawler/srwbook.pdf); they supply no physical constants or fitted values.

Let a denote the common central-site amplitude and b the common outer-site amplitude in the limiting reflection-symmetric six-node system. Since Vu is4b at each central site and2a at each outer site, the two equations are

 0=1-8g(a+b)+b+4a/pi,
 0=1-8g(a+b)+4b/pi+2a.

Set r=(4-pi)/(4-2pi)=-.37596919694205444. Then

 a/b=r,
 source=u(0,0)+u(1,0)=2r/[8g_R(1+r)-1-4r/pi]+o(1/log R),
 log R * source -> pi*r/[2(1+r)]=-.9463812213285369.          (2)

For completeness the full six-site matrix controls small asymmetries. If C=I-A V and p=1/pi, det C=4(8p²-1)(8p²-4p+1) is nonzero, as is 1^T V C^-1 1=-4(8p-3)/(8p²-1). Sherman-Morrison gives a bounded inverse and solution O(1/g_R); the o(1) Green remainder changes it only by o(1/g_R). The numerical helper uses a rectangle symmetric about x=1/2 and y=0, and checks the six-site solution against the full sparse system.

The endpoint response is negative and nonzero for large finite boxes but vanishes logarithmically. A signed-bond Laplacian need not have positive site amplitudes. Unit boundary data are a specified static protocol, not an outgoing scattering normalization.

## 5. Finite-energy coefficient scattering

The outgoing continuation is also explicit. For epsilon>0 near the lower free band edge use G_epsilon^+=(L0-epsilon-i0)^-1 and an incident plane wave phi satisfying epsilon=4-2cos kx-2cos ky. The exact defect values solve

 u_S=(I+G_epsilon^+ V)^-1 phi_S.

For fixed sites, G_epsilon^+(i,j)=g_epsilon-A(i-j)+o(1). With the parameter convention for the complete elliptic integral,

 g_z=2/[pi(4-z)] K(16/(4-z)²),
 g_epsilon=(1/(4pi))log(32/epsilon)+i/4+o(1).

The sign follows from the chosen outgoing resolvent. The same bounded six-site inverse and phi_S=1+O(sqrt epsilon) give

 source=2r/[8g_epsilon(1+r)-1-4r/pi]+o(1/log(1/epsilon)),
 log(1/epsilon)*source -> pi*r/(1+r)=-1.892762442657073.      (3)

The helper uses a plane-wave phase centered on the flipped pair, high-precision elliptic/one-dimensional Green evaluation and the full six-site inverse. The small positive imaginary regulator is explicitly1e-12 epsilon; its numerical values corroborate the limiting calculation rather than prove the i0 limit.

Thus the correctly distorted coefficient scattering channel generally couples, but its threshold endpoint amplitude is logarithmically suppressed. Equation(3) is not a full microscopic scattering result: the neutral feature is held fixed in this coefficient problem, its recoil and energy transfer are omitted, and other connected native vertices may contribute to a complete emission amplitude. No rate, universal charge or cosmological coupling is inferred by multiplying (3) by an isolated vertex.

All calculations are exposed model development. The derived prepared-return channel and the static/scattering environment calculations answer distinct parts of the source/detector obstacle. Their synthesis into a relaxed, energy-conserving native heavy-plus-neutral channel remains open.
