# Personal frontier plan: replace the external schedule by a finite clock

2026-09-24, unsealed derivation before controls. The preceding finite supply
construction proves a scheduled gate approximation. The next question is an
autonomous finite-horizon, one-time reduced-channel realization, with an
explicit positive clock Hamiltonian and resource/error bounds. It still does
not select a native model or establish the exact continuous event-time law.

Candidate: use a Feynman history Hamiltonian for the already energy-conserving
lifted gates V_1,...,V_n. On clock positions x, let G_x be the gate product
through clip(x,0,n), and gauge-conjugate a positive tight-binding clock
2J I-J(T+T*) by sum_x |x><x| tensor G_x. Because every gate commutes with the
same H_system+H_battery and flags have zero energy, the history Hamiltonian
also commutes with that free sum. Add the free sum if desired, but inspect
its extra system free evolution: the history program must use the interaction
picture or compensate that evolution before claiming the original generator.

Key newly noticed obligation: using H_total=H_free+H_history naively adds
free H evolution to gates that already include exp(-i H tau). This would
double-count it. Possible correct route: program the interaction-picture
time-dependent dissipative step e^(+iH k tau) K_j e^(-iH k tau) with the
right endpoint conjugations, or choose the full positive autonomous Hamiltonian
H_history alone while H_free remains a separately conserved observable and
state clearly which operator is designated total physical energy. Prefer the
first route so the microscopic H remains the actual additive free term.
This must be resolved exactly before promoting any theorem.

A perfect-transfer spin-chain clock gives k/n approximately sin²(pi t/(2T)),
which matches an endpoint but reparametrizes intermediate physical times.
Do not claim it yields the requested linear-time semigroup. Instead consider
a finite-support sine wavepacket on negative clock sites, phase i^x, moving
under the uniform chain. Put width w>=2, theta=pi/(w+1), and choose
2J cos(theta)=1/tau. Its mean position is -(w+1)/2+t/tau.
On the infinite chain, velocity V=iJ(T-T*) commutes with the clock Hamiltonian,
so X(t)=X+tV. For the sine packet:

    mean(V)=2J cos(theta),
    Var(V)=4J² sin²(theta)/(w+1),
    sd(X)<= (w-1)/2.

Thus the expected mismatch between clipped clock time and physical t is at
most tau w + T tan(theta)/sqrt(w+1), uniformly0<=t<=T. Verify every sign,
endpoint and covariance term. This uses the norm triangle inequality, not an
assumption of statistically independent initial position and velocity.

For a finite clock whose boundaries are distance R from the initial support,
the finite and infinite adjacency powers agree below order R. The Taylor tail
bounds the vector error by2 exp(a) a^R/R!, a=2JT. Choosing R a sufficiently
large multiple of a yields an exponentially small uniform error, while clock
dimension stays O(n+w). Keep complete gate-history buffers at both ends.

If the free-evolution issue is resolved, combine the clock time mismatch with
the semigroup Lipschitz bound ||L||<=2(h+g), the collision error T tau A, and
the single shared battery error eta. This would give a uniform one-time
diamond bound, including entangled system inputs. It does not automatically
give a process-tensor/intervention or unbinned marked-path theorem.

For the star h=O(C²),g=O(C), C=S(S+1), a possible sufficient scaling is
battery width L=O(C²), clock width w=O(C³), tau=O(C^-7), producing channel
error O(C^-2), clock mean energy O(C^7) and battery mean O(C^4). These are
tentative loose sufficient costs, not optimality claims. The full Hamiltonian
must be positive and time independent, and its initial clock/interaction
energy must be accounted explicitly. Every clock/flag preparation and spectral
coupling remains supplied, finite-horizon and potentially nonlocal.

Resolution of the free-evolution issue, still before controls: program

    W_k = exp(+i H k tau) V(U_k) exp(-i H (k-1)tau).

These gates conserve H+H_R. Their product is exp(+i H k tau) times the
lifted collision product. With H_aut=H+H_R+H_history, the separate free
evolution then yields the interaction-picture construction with the right
physical time. The exact interaction-picture target channel
Psi_I(t)=exp(-t A)exp(t(A+D)) has derivative D_I(t)Psi_I(t), and
||D_I(t)||_diamond<=2g. Its time-Lipschitz constant is therefore2g, not the
looser2(h+g), despite rapid microscopic H phases. This potentially sharpens
the clock term to2g[tau w+T tan(theta)/sqrt(w+1)].

Consequently w=O(C²), tau=O(C^-5), battery widthL=O(C²) may already yield
O(C^-2) uniform channel error, clock mean energyO(C^5), battery meanO(C^4).
The program's phases and strong couplings remain supplied. Verify the gauge
orientation, finite-clock truncation bound, interaction-picture telescoping,
and initial product preparation in complete matrices before sealing a claim.
