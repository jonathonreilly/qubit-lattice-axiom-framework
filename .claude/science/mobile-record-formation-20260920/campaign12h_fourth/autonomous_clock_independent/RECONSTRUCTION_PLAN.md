# Independent PRE route, before clock-author access

The supplied premise is the sealed finite battery and marked collision packet.
It provides energy-conserving lifts V_j of scheduled collision gates, a common
coherent finite battery, and a dimension-independent error eta_L for every
prefix, including references. This reconstruction does not import its builders.

I will use a finite spin-J=N/2 clock. Its nearest-neighbor Hamiltonian has
couplings (nu/2)sqrt(j(N+1-j)), positive energy shift nu N/2, and initial
position 0. Its exact clock distribution is Binomial(N,sin²(nu t/2)). A
programmed Feynman conjugation by the gate-prefix unitaries makes each clock
position carry the appropriate conserving prefix. Every system/battery free
energy is exactly conserved.

Two obstructions require explicit corrections:

1. Uniform collision durations do not give uniform physical time. The spin
   clock advances as sin²(nu t/2), so endpoint transfer alone has an O(1)
   interior timing error even as N grows. Use the inverse grid
   t_j=(2T/pi)arcsin sqrt(j/N), with nu=pi/T.
2. Adding the physical free Hamiltonian to a program whose gates already
   include free evolution doubles that evolution. Program the conserving
   increments exp(+i(t_j-t_(j-1))Q_free) V_j instead. Then compare in the
   system interaction picture and count all bare clock/interaction resources.

The proposed uniform proof uses a Hellinger chord bound for the binomial
clock: E|t_J-t| <= T/sqrt(2N), including both endpoints. The inverse grid has
max step <=T/sqrt(N); summing the supplied variable-step collision errors and
using the interaction-picture channel's Lipschitz constant <=2g should give
eta_L+[T²(7g²+4hg)+sqrt(2)gT]/sqrt(N).

Independent controls will include full finite-space symbolic conservation and
programmed-clock conjugation, direct numerical evolution of a single finite
Hamiltonian, full reference-sensitive channel comparisons, and persistent
failures of the naive uniform grid and uncorrected free evolution. Positive
clock energy, its coherent preparation, pure flags, battery reserve, the
interaction norm and recurrence beyond the requested horizon will be retained.
Uniform one-time reduced channels will not be called a multitime process or an
unbinned event-time instrument. No author clock source is to be read before PRE.
