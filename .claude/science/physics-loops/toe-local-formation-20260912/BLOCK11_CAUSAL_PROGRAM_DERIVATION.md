# A single-seed growing Record domain on the prepared protected carrier

Companion author derivation to BLOCK11_DERIVATION.md, written before the
growth checks. This changes the program placement and occurrence conditions;
it is an alternative to that note's static endpoint-program preparation.
All quantum carrier and clock assumptions remain conditional. No independent
audit or derivation of objective formation is claimed.

## 1. Disjoint physical roles and one conditional content law

Keep native qubits at one-odd-coordinate edge centers, and the same candidate
x edges with odd virtual y. Define the program graph P to consist of physical
sites having at least two odd coordinates, with literal nearest-neighbor
edges. Its three-odd sites are the vertices of a cubic graph of spacing two;
its two-odd sites subdivide each edge once. P is connected, with degree six
at a coarse vertex and degree two at an edge interior. It is disjoint from
all native edge qubits and all all-even physical vertex sites.

Place an optional native fuel qubit at the all-even tail 2v of each candidate
edge (v,v+e_x), initially unrecorded in |1>. Candidate tails are distinct.
This replaces the static version's transverse fuel location; it does not
add a second qubit at a program site. The four transverse nearest neighbors
of a candidate native qubit belong to P. Its two endpoint neighbors are
unrecorded fuel/spectator sites.

Initially one three-odd program site o is a supplied digital Record. Every
other program qubit is prepared in |+x>. Program sites are not rotated or
otherwise used as controls until they themselves are already Records, except
for their own single formation pulse. No static endpoint program Records
are present. Existing Records serve only as digital Z controls.

The content law at every new program or native event is exactly

    F(eta)=(1/n) sum_(rho in eta)
            [(3/4)delta_rho+(1/4)delta_(I-rho)], n=|eta|>0.       (C.1)

Eta lists all actual nearest-neighbor Record contents. In the common
digital context let their signs sum to b. Then p_+=1/2+b/(4n). The common
law is covariant under neighbor permutations and simultaneous conjugation,
and varies with the supplied conditions. All digital event probabilities
lie in [1/4,3/4]. From the same fixed seed, finite birth orders and all-plus
or all-minus signs at a candidate's four neighbors therefore have positive
probability. The different candidate probabilities 3/4 and 1/4 occur within
one prepared history family, not only after changing the preparation.
The role pattern and initial
Pauli/preparation context are additional conditions, as before.

An unrecorded program site becomes enabled when at least one of its program
neighbors has formed. It uses (C.1), including any already formed native
neighbors in eta. In fact a native candidate adjacent to an unrecorded
program target cannot yet have formed, because its four-neighbor enabling
condition includes that target. Thus those native contributions are absent
at the program site's actual first event. Its ready |+x> factor is rotated by

    U_program=exp(+i theta sigma_y/2), theta=arcsin(b/(2n)),

then measured in Z. The sign of this rotation matters: its final Z mean is
sin(theta)=b/(2n). All its controls are fixed Records. A native candidate
becomes enabled after its four program neighbors have formed. It then uses
the cycle pulse of the companion note with theta=arcsin(b/8). Its n is
exactly four, so its probabilities are again (C.1).

This is a forward process whose supplied occurrence rule uses the Record
configuration to select enabled unrecorded targets. It does not define a
readout value for an absent Record. It also does not implement the presence
guard as a reversible quantum operation on an otherwise unspecified ready
space. Program occurrence, initial readiness, and the single seed remain
conditions. The optional native fuel realizes a native absorbing channel;
no extra per-program fuel factor has been silently allocated.

## 2. Full finite-history closure

Take an initial product of the program ready/seed factors, native fuel,
and any native matter code state (possibly with a matter reference).
The program instruments commute with the protected matter algebra: their
targets are disjoint, and every native control is a candidate Z which
commutes with that algebra. Their scalar effect on the still untouched
|+x> target gives (C.1), independently of the matter state.

Every native event is the scalar-effect isometry in the companion note.
It leaves all program Records unchanged. Any unused candidate's cycle
check survives all earlier events because its witness contains no other
candidate edge. Program events preserve those checks as well, including
when a native Z is used as a control: that control is already a fixed
Record and its cycle check was removed earlier. Therefore induction over
every supported finite history proves:

* every new content law equals F of the actual nearest-neighbor Records;
* every old Record is unchanged;
* every still-unrecorded program target is ready for its stated pulse;
* the protected matter state functional equals its event-free H_B dwell.

Shared controls need not make all abstract program event operators commute.
Events use their actual causal histories; the induction does not reorder
events whose condition sets change. This distinction avoids extending the
static commuting-instrument statement beyond its hypotheses.

The construction still reveals no protected matter information. All Record
histories, including occurrence times below, have the same law for every
initial protected matter state on the same code and program preparation.

## 3. A supplied nonexplosive clock process

Each program site receives an independent Exp(gamma) waiting time when it
first becomes enabled; each candidate native site likewise receives one
when all four program neighbors have formed. Enabling is permanent. Content
draws use independent uniform random variables with the probabilities (C.1).
The waiting times do not depend on those draws or on matter.

If N_P program sites have formed, at most 6N_P unformed program sites are
enabled. At most 6N_P native candidates could yet have been activated, since
activation requires adjacency to a formed program site. Thus the total
event rate is at most 12 gamma N_P, and hence at most 12 gamma N_total.
Comparison with the linear pure-birth process proves nonexplosion. More
explicitly, its successive mean holding times are (12 gamma n)^(-1);
the centered independent holding-time series has summable variances while
the sum of the means diverges. The comparison process has no finite-time
accumulation, so neither does this one.

Assign each program site v≠o an independent Exp(gamma) variable E_v at the
start; unused clocks may be sampled in advance. Its formation time satisfies

    T_P(o)=0,
    T_P(v)=E_v+min_(u adjacent to v in P) T_P(u).                (C.2)

It is the minimum sum of site waiting times along a path from o to v.
Positive weights allow minimizing paths to be simple. Native events do not
alter program enabling, so their content dependence does not change (C.2).
Every fixed program vertex is reached almost surely by bounding (C.2) with
the finite waiting-time sum along one fixed path. Countability makes this
true simultaneously for all sites. Every candidate is subsequently enabled
and forms almost surely. The infinite program process thus produces
unboundedly many Records without explosion.

This infinite statement concerns the supplied classical Record/time law and
its local instruments. The companion note supplies finite physical native
states for arbitrarily large regions, not an unproved global infinite
native cycle-code state. The finite-window conclusion below uses only
finite carriers and finite portions of this process.

## 4. Explicit growing front bounds without simulated growth

Distance in P from a three-odd o equals the physical Manhattan distance:
one may change coordinates that end odd by even steps through subdivided
coarse edges, then, if necessary, make the final step to the one even
coordinate. Thus B_P(n) lies in a physical cube with at most (2n+1)^3 sites.
For each v in B_P(n), fix one path of length at most n. The exponential
moment at gamma/2 gives

    Pr[T_P(v)>s] <= 2^n exp(-gamma s/2).

A union bound, requiring no independence between these path sums, yields

    Pr[B_P(n) not all formed by s]
      <= (2n+1)^3 exp(n log(2)-gamma s/2).                     (C.3)

Set n=floor(gamma T/(8 log(2))). All candidates at physical Manhattan
distance at most n-1 from o have their four program neighbors in B_P(n).
Applying (C.3) at s=T/2 and the remaining native exponential waits gives

    Pr[one such candidate is unformed at T]
      <= (2n+1)^3 [exp(-gamma T/8)+exp(-gamma T/2)].            (C.4)

For small T the right side may exceed one; (C.4) is then a valid but
uninformative bound. It is not a probability estimate fitted from growth
simulations. For n>=7, let m=floor((n-1)/3). The contained cube of coordinate
radius m has at least m² floor(m/2) candidates: odd x and even z each occur
at least m times, and physical y congruent to 2 modulo 4 occurs at least
floor(m/2) times. Thus (C.4) gives a positive constant times T³ native
formations with probability tending to one. No constant continuing rate
inside an already saturated fixed region follows.

For an upper front, reaching program distance at least n before time T
requires a simple ancestry path whose first n waiting times sum to at
most T. There are at most 6^n such path prefixes. When n>gamma T, the
optimized exponential lower-tail bound for a sum of n independent waits is

    Pr[sum_(j=1)^n E_j<=T] <= (e gamma T/n)^n.

Therefore

    Pr[program distance >= n reached by T]
       <= (6 e gamma T/n)^n <= 2^(-n),
       if n>=12 e gamma T.                                  (C.5)

A formed native candidate is adjacent to a formed program site, so its
physical radius exceeds the program radius by at most one. The constants
are deliberately loose analytical bounds, not a claimed limiting shape
or a relativistic propagation speed.

## 5. Joining the front to finite native transport

For any prescribed finite T and observation region, choose the finite
native box and even-parity preparation by companion equations (11.11)–
(11.13). Include the candidate ball used in (C.4), every corresponding
protected witness cycle, its program paths, and the current observation
region. Program paths chosen for (C.3) stay inside that ball. A finite
program domain containing it satisfies the same lower bound even if the
domain boundary blocks external paths. Take the native boundary farther
out by the current margin d=O(tT+log(1/epsilon)).

This supplies arbitrarily large finite histories, a growing number of
genuine native one-site Z Records with a varying nearest-neighbor content
law, and nonzero protected current throughout the requested finite window.
The required physical region scales as
O((R+(gamma+t)T+log(1/epsilon))³), up to the explicit role and boundary
constants. This counts carrier sites, programs, and optional native fuel;
it does not include a full coherent controller for the hybrid occurrence
rule or its fresh collision storage. It does not derive gamma/t, a physical
clock, role preparation, or matter readout from the axioms.

The advance over a finite list of scheduled fair edge deletions is the
explicit varying local content law, complete supported-history closure,
and a finite growing-window construction. Its central remaining limitation
is equally exact: the Record channel is blind to protected matter.
