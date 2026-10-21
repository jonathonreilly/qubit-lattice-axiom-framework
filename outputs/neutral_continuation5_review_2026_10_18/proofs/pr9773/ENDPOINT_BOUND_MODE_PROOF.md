<!-- Original PR9773 source SHA256 6550ac62b55a91e73b03f7fa042b9a750788595bdb8f18820d7846690ec8aca7. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Native four-column endpoint bound mode (root)

Use the supplied one-qubit compass Hamiltonian with Jx=Jy=lambda Jz. Consider four columns at the corners of one transverse unit square, each with one longitudinal domain wall of the same orientation: spins down at z<=h_c, up above. Exterior columns are uniformly up. This infinite-longitudinal boundary sector is supplied, not a cosmological preparation. Its finite excitation energy in H0 is8Jz. K1=P_N(V/(lambda Jz))P_N acts within this fixed-column height sector: an interior spin flip away from a wall adds two walls, as does a flip in an exterior uniform column, and no column in this sector can remove two walls. Hence N-preserving transverse flips must move existing walls on two occupied neighboring columns. No exterior bond is active at this order.

For an edge c,d, the active layers are {h_c,h_c+1} intersect {h_d,h_d+1}. Equal heights can both rise or both fall; heights differing by one can swap; larger differences have no transition. XX gives amplitude-1. YY gives +1 for equal-spin pair moves and -1 for mixed-spin swaps. This follows directly from -YY|s,t>=s t|-s,-t>, with s,t=+/-1. No height kinetic interaction is postulated.

For a finite flat rectangular droplet of areaA>2 and length>=3, these same endpoint moves give4 distinct non-rigid N-conserving target configurations per internal edge. Its squared first-order leakage from the flat fixedshape chart is4[Jx²(nx-1)ny+Jy²nx(ny-1)]. This is a matrix element statement, not an inverse lifetime or absence of collective bound states. Indeed the four-column height problem below binds despite that rigid-chart leakage.

# Exact four-ray reduction

Quotient common height shifts, using physical center R=sum h_c/4 as fiber gauge. Reachable states from flat F=(0,0,0,0) are four rays
X+_n=(0,0,n,n), X-_n=(n,n,0,0), Y+_n=(0,n,0,n), Y-_n=(n,0,n,0), n>=1,
and D+=(1,0,0,1), D-=(0,1,1,0). Applying the move rules exhausts this graph. Common translation acts freely, so all quotient orbit norms agree.

At momentumk let gamma=cos(k/2). A pair move changesR by+/-1/2. The two moves to the same relative state give ray hopping-2gamma onX,+2gamma onY and flat contacts with the same signs. All D contacts are swaps with amplitude-1. The normalized ray combination
b_n=[X+_n+X-_n+(-1)^n(Y+_n+Y-_n)]/2
has hopping-2gamma and flat contact-4gamma; its D contacts cancel. Atk0 the remaining channels have continuum[-4,4], a threshold D-symmetric channel and a decoupled zero state; none lies below-4. Neark0 the bound branch remains isolated by continuity.

Let r=1/sqrt3. The normalized bound state has flat amplitude1/sqrt3 and b_n amplitude2r^n/sqrt3. It obeys
 epsilon_b(k)=-8cos(k/2)/sqrt3,
so the first-order physical endpoint energy is8Jz+lambda Jz epsilon_b(k). Flat probability is1/3. This solves K1 exactly; it is not a full-H pole or a finite two-ended droplet eigenstate. The local half-angle band expression carries a gauge twist under a full Brillouin-zone shift and is only used near zero.

Under the physical combined quarter-turn about z and spin rotation taking X toY andY to-X, relative spin phases are(-1)^n on ray n. Geometric rotation exchanges X/Y rays. Their alternating signs above therefore make the bound branch even under this axial quarter-turn. This is not a proof of full rotational/Lorentz scalar behavior.

# Original distance-two readout: derived band vertex

For the single wall at h, the localized difference in C_p=sum_z exp[ip(z+1)]Z_zZ_(z+2) from its uniform value is -4cos(p/2)exp[ip(h+1/2)]. The infinite sum is used only through this localized excess. Summing four walls, its bound-band form factor is
F(p)=4/3+(16/3)sum_(n>=1)3^-n cos(pn/2)=4(1+cos(p/2))/(5-3cos(p/2)).
The original unnormalized probe vertex between nearby bound momenta is consequently
V(p)=-4cos(p/2)exp(ip/2)F(p).
Both bound internal vectors are identical in the chosen physical-center gauge. V(0)=-16 is constant and produces no internal inelastic transition; finitep transfers center momentum and V(-p)=conj V(p). A chosen volume normalization would multiply the displayed vertex accordingly. This is scattering within a supplied excited boundary sector, not vacuum creation, a detector model, or a cosmological scalar coupling.

For finite single-interval columns of length>=2, the uniform bare C excess is exactly-8 percolumn, so it is proportional to identity throughout the pureheight chart. Dressing, finite momentum or configurations outside that chart are required for an inelastic source. Do not claim a new nonzero uniform vacuum transition from the height solution.

# Open extensions

Finitepairedendpoints can approach and annihilate; higher-order native terms and other wall/shape sectors require separate control. Large transverse arrays have many height modes; rigid corner energy alone does not determine them. Numerical cutoffs corroborate exact coefficient formulas, not empirical predictions. The supplied H, anisotropy, boundary sector, normalization and physical measurement identification remain explicit. No observation calibrated or tested.
