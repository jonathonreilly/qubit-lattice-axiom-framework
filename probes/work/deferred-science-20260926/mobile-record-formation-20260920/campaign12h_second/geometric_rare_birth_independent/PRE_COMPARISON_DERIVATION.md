# Independent reconstruction before author-checker access

The complete supplied note, SHA-256
`b6ae15f48bdab91922f13ff610853646a7cf91c74391d55887af39b583584611`,
was read. The unchanged geometric-partner note and this reviewer's previously
sealed proof/checker are the only scientific prerequisites. The author
rare-birth checker, outputs and logs remain unopened. No production
diagnostic, phase/wave evidence, Git command or external literature was used.

## Connectivity at the penultimate level

Let the bipartition have size K on each side, with positive common degree k.
For nonempty proper S in L, regularity gives k|S|<=k|N(S)|. Equality would
exhaust all edges incident to N(S), while all edges out of S already enter
N(S); the nonempty proper set S union N(S) would be a connected component.
Thus connectedness makes the inequality strict. The argument applies on
either side, including the K=1 degenerate case where no such S exists.

For a fixed near-perfect matching M with vacancies l0,r0, draw the directed
edge l->l' whenever an occupied neighbor r of l is partnered to l'. Let S
be the directed reachability set from l0. Every neighbor r of S other than
r0 has its distinct M partner in S\{l0}, so |N(S)|<=|S|. Strict Hall excludes
a proper S. A shortest directed path has distinct L vertices; its matched
R vertices are also distinct. Executing its slides consequently moves the
L vacancy to any desired L site with the R vacancy unchanged. Interchanging
the two sides gives the other positioning operation. These statements
depend on the frozen current matching, not on a guessed dynamically updated
directed path; distinctness makes that path remain legal during execution.

To connect M to a target M', first align their L vacancies and then their R
vacancies. Their symmetric difference is now a union of alternating cycles.
Let C be one cycle. Choose a shortest directed path from the L vacancy to
any L vertex of C. Its last matched R-L edge lies in C. Every earlier vertex
is outside C: any earlier R in C would have its M partner L in C, contradicting
the first entry. Write the final approach triple `(a,r,l)`, with a outside C.

After the approach slides, l is vacant and r is partnered to a. Starting
at l, use the desired M' cycle edge through its other R neighbor, then move
that R neighbor's old M partner into the vacancy. Repeat until the desired
cycle edge is incident to the entering r. The final slide uses the temporary
pair `(a,r)` and returns the vacancy to a. Every cycle edge has now changed
from M to M'. Reverse all earlier approach slides, excluding the final
entry, to restore their old edges and the original vacancy. Thus the change
is confined exactly to C. Repetition finishes the transformation. The cycle
need not bound a contractible face; the proof is purely graph theoretic.

Therefore the slide graph on all K-1-edge matchings is connected. Symmetric
positive slide rates imply uniform invariant measure on this finite space.
Adding any finite, fixed, nonnegative symmetric conservative transition
rates on the same matching space preserves uniformity and cannot destroy
the existing irreducible slide subgraph. Conservation here includes pair
number; marked-state irreducibility or content-dependent hidden dynamics
are not being asserted.

## Slow killing and arbitrary nonfull entrance laws

On the finite near-perfect space Omega, write S for the fixed conservative
generator and pi for its uniform invariant law. On a simple graph the two
vacancies admit at most one birth. Let h be its indicator, and let a_F be
the indicator that it completes the specified perfect matching F. For
beta>0, irreducibility and a nonempty killing set imply almost-sure eventual
birth. The absorption probability u_beta satisfies

    (-S+beta diag(h))u_beta=beta a_F,       0<=u_beta<=1.

This follows directly by first-step conditioning. The same hypotheses make
the killed matrix nonsingular. Along any beta-down-to-zero subsequence,
compactness gives a convergent subsequence. Its limit solves S u=0 and is
constant by irreducibility. Multiplication by pi in the exact equation gives
pi(h u_beta)=pi(a_F), hence the limiting constant is pi(a_F)/pi(h).

Each perfect matching has exactly K distinct one-edge deletions. Conversely,
each near-perfect matching with adjacent vacancies has exactly one full
completion. Thus pi(a_F)=K/|Omega| and pi(h)=K|F_all|/|Omega|, giving the
constant 1/|F_all|. All subsequences have this limit. Because Omega and the
full target set are finite, convergence holds in total variation uniformly
over the entrance state, and therefore uniformly over all beta-dependent
entrance distributions.

The previously checked filling theorem guarantees that every initially
nonfull state reaches this near-perfect level and then full packing. At the
first entrance, the strong Markov property and the uniform estimate above
remove all dependence on earlier birth/motion history. No equilibrium
claim at earlier levels is needed. An initially full configuration has no
such entrance and its first-full law is its initial law. The proof concerns
the random *first-full event*, not the configuration at fixed physical time
while beta tends to zero. Setting beta=0 freezes the pair count and is not
this limit. Graph size and all conservative rates are fixed; beta/kappa
must tend to zero. Nothing here bounds the error or relaxation time uniformly
over growing graphs.

## F1: qualify the post-filling observation sentence

The core first-full theorem above reconstructs. One subsequent sentence is
too broad without an observation-time qualification: “Total-variation
contraction makes any later observation time at fixed N no worse than the
initial discrepancy from that uniform law.” A common deterministic elapsed
time after first filling has this property, as does a state-independent
random delay. An arbitrary state-dependent stopping/observation rule does
not. Even a symmetric two-state full-matching flip chain started uniformly
and observed at its first visit/return to a specified matching after a
positive departure time gives a point mass. Its TV discrepancy is 1/2,
although the initial discrepancy was zero. A deterministic absolute clock
deadline also needs its random filling time and any conditioning treated;
it is not automatically one common post-filling semigroup kernel.

Narrow correction: say “at any common deterministic elapsed time after first
filling, or after an independent random delay.” No change to Eq. (5), the
connectivity proof or the rare-killing argument is requested. The parent
has acknowledged this intended scope and will preserve the reviewed source
until the report is sealed.

## Decisive controls, independent of author implementation

The code uses only this reviewer's previously sealed matching primitives.
All 106 labeled connected regular bipartite graphs with each class of size
at most four were generated: their 2381 near-perfect states satisfy strict
Hall, both fixed-opposite-vacancy reachability tests and full slide
connectivity. The explicit M-to-M' construction succeeds on every ordered
pair of near-perfect matchings for C6, C8, K3,3, K4,4 and the cube, including
9074 cycle excursions in total. The computation is a check of the proof,
not its general justification.

Two targeted 4^3 periodic examples flip a distant plaquette and a winding
axis cycle. Each has a four-slide approach and nine total slides. The checks
verify exact restoration of every edge outside the cycle and both original
vacancies. These examples test the nontrivial retracing segment omitted by
small dense examples whose approaches have length one.

Exact killed-generator controls on C4 and C6 give the uniform rare-birth
law from every near-perfect state. On C4, starting with an edge of the
specified full matching, its probability is `(b+2)/(b+4)` at kappa=1.
Consequential countercontrols are:

- Two disconnected C4 components are still regular and bipartite, but a
  near-perfect state with one fixed full component has rare first-full law
  `(1/2,1/2,0,0)` on the four perfect matchings, TV distance 1/2 from uniform.
- On nonregular P4 with only edge (2,3) occupied, L={0,2} vacancy 0 cannot
  reach 2 while the R vacancy 1 stays fixed. This refutes the intermediate
  fixed-vacancy reachability claim without regularity; it does not claim
  that every nonregular graph violates final uniform selection.
- A positive asymmetric extra conservative rate on C4 can change the rare
  full law to `(3/5,2/5)`. Giving one vacant birth edge twice the others'
  rate produces the same bias. Symmetry and equal per-edge birth rates do
  actual work in the theorem.
- Zero slides complete a near-perfect C4 matching deterministically.
  Sending beta and kappa to zero with beta/kappa=1 retains probability 3/5,
  not 1/2. A full initial state remains its initial first-full point mass.

The independent cube harmonic reconstruction gives exactly

    (6 b^3+77 b^2+308 b+308)/[7(b+6)(3 b^2+19 b+22)],

including 699/2156 at b=1, 1/3 as b decreases to zero, and 2/7 as b increases
without bound. A separately generated ten-state automorphism quotient is
verified on every one of the 108 matching states, and the lifted symbolic
solution satisfies all 99 original transient harmonic equations. Its
difference from 1/3 is

    -b(3 b^2+28 b+28)/[21(b+6)(3 b^2+19 b+22)] < 0.

For the distinct endpoint kappa=nu=0 on this cube, exact deposition recursion
gives full-packing probability 17/21, unconditional columnar probability 2/7,
and columnar probability conditional on full packing 6/17. The equality of
one unconditional numerator with the fast-motion-separated limit does not
identify the laws: the no-slide process has positive jamming probability.

All independent runs in this unit passed on their first attempt; full
stdout/stderr and command/source receipts are preserved. No source fix was
made. Beyond F1, no unresolved defect has been found before author comparison.
