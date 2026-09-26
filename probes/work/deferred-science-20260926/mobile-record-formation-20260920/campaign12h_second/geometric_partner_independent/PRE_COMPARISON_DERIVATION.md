# Independent reconstruction before author-checker access

This is a bounded mathematical check of the supplied conditional construction,
not authorship of a new process or a retention/audit decision. The complete
183-line source note has been read. Its SHA-256 is
`1bc76bc39c672c7eec318fb4e999dc6e2b1f80aad9a058683dbeb7f7ae247969`.
The parent supplied commit `b711317bab78df9e344dc9de0c18526d6e9dec4d`;
no Git command was used to authenticate that commit. The author checker,
its results/logs, and the ongoing production diagnostic remain unopened.

## 1. State domain and local formation

Treat projectors as classical content values. A configuration is a matching
whose edge carries an unordered antipodal class, distinct from every other
edge's class. It can equivalently be represented by the site contents:
each occupied site has exactly one antipodal site, which is adjacent.
Given a past with countably many keys, the forbidden marks form a countable
subset of the sphere. The new mark has an absolutely continuous law, so it
avoids that set almost surely. Taking the countable union over births
preserves this domain without an implemented nonlocal rejection. In finite
volume there are at most |V|/2 births from empty; bounded rates also rule out
explosion. A countable-history statement does not itself construct an
infinite-volume process, and the note does not claim that theorem.

For an edge oriented temporarily by d, its density integrates to one because
the spherical mean of n vanishes. It is bounded below by
(1-|epsilon|)/(4 pi)>0. Reversal gives f_{-d}(-n)=f_d(n). Proper rotations
preserve n.d, giving exactly the stated supplied proper-cubic covariance.
No claim about spatial reflections is needed.

At a currently vacant site x, each available edge has integrated rate beta.
Thus the total instantaneous site-birth hazard is beta r_x and, conditional
on that event and the current pre-event configuration, its mark density is

    p_x(n) = [1+epsilon n.(sum_{d in D_x}d)/r_x]/(4 pi).

This is an event kernel, not the distribution of the eventual first birth
at x conditional only on an earlier configuration. Its first moment is
epsilon sum_D d/(3 r_x), using the exact spherical second moment I/3.
At r_x=0 the hazard is zero and a convention for the unused conditional law
has no probabilistic consequence. The density is not asserted to arise from
a Born measurement of an unknown input.

## 2. Marked moves and conservative reversibility

On a path (a,b,c), with antipodal partners at a,b and c vacant, move the
record at a to b and the record at b to c. Both old contents and identities
survive, both steps are edges, and the pair remains adjacent. In the target,
the path (c,b,a) performs the exact inverse at the same rate. Acceptance
requires only these three sites once the unique-partner domain is assumed;
the rule need not search elsewhere to identify the partner.

On a fully occupied square with opposite paired edges, either one-corner
rotation moves every old record exactly one edge. The rotations are distinct
marked transitions, they give the same unmarked geometric flip, and their
opposite rotations are exact inverses. The projected rate is therefore
2 nu, not nu. Local marked examples with rational unit-vector contents
confirm departure, reformation at the old site, turning, and both inverses.
These are supported marked configurations; any prescribed exact spherical
mark has probability zero. Integrated geometric histories have positive
probability because their relevant rates are positive.

The geometric matching projection is strongly lumpable: event validity and
all integrated rates depend only on the matching, not the distinct keys.
Its slide/flip generator has symmetric off-diagonal rates, by the inverse
channel bijection. Hence counting measure, normalized separately in each
finite communicating component of fixed cardinality, is reversible when
births are removed. This does not determine a formation-selected final law.

## 3. Filling theorem, independent of finite enumeration

Fix any finite simple graph with a perfect matching P and any partial
matching M. In M triangle P, a vertex unmatched in M has degree one and its
incident edge is a P edge. Following alternating edges cannot enter a cycle:
every internal vertex has degree two, while the initial vertex has degree
one. The component is a path with both endpoints unmatched in M. Writing it
v_0,...,v_{2 ell+1}, its P edges have even starting index and its M edges
have odd starting index. This reasoning does not need bipartiteness or
connectedness of the graph.

Successively perform slides (v_{2j+2},v_{2j+1},v_{2j}) for j=0,...,ell-1.
At each step the first two sites are the old pair and the last is the current
vacancy. The vacancy advances by two vertices. The last two vertices are
then vacant and adjacent; one birth increases the pair number. No old pair
key is destroyed. The sequence length is ell+1<=|V|/2. A fixed perfect
matching is only a proof certificate, not data read by the dynamics.

The projected chain is finite and has finite rates. Pair count is monotone,
so every communicating class has a fixed count. A nonfull class cannot be
closed: the constructed positive-rate path reaches a larger count. All
closed classes are full. Standard finite-chain reasoning now gives almost
sure finite hitting time of the full set, with finite expectation. For
example, uniformize the finite chain; each transient state has a bounded
length positive-probability path to the full set, and the minimum of those
finitely many probabilities is positive. A geometric tail in blocks follows.
The full *set* is absorbing; an individual full matching can still flip.

The abstract-graph assertion concerns these geometric beta/kappa rules. Its
continuous marked lift needs only fresh nonatomic antipodal keys. The
cubic directional density f_d and the staggered geometric readout keep
their separate lattice hypotheses; there is no coordinate-vector or Gauss
claim on an arbitrary abstract graph. Finite expected filling time is not a
uniform bound as the graph grows. Positive beta and kappa are required for
the stated general guarantee; nu can be zero. Full-state irreducibility,
infinite-volume filling and a phase/wave limit do not follow.

On an empty translation-invariant finite torus, the total number of created
records at full packing is exactly |V|, and translation symmetry makes the
expectation of the number created at each site equal to one. This is a
statement about cumulative births at that site, not a one-birth-per-site
pathwise bound.

## 4. Geometric Gauss and operational boundary

On the cubic lattice, or a periodic cubic torus with even periods, staggered
sigma changes sign on every edge. Therefore

    sum_i [B_i(x)-B_i(x-e_i)]
      = sigma_x [sum_i(n_i(x)+n_i(x-e_i))-1]
      = -sigma_x 1_{x vacant}.

The site degree in a matching is zero or one. This is a derived matching
field. On a reflecting boundary the same 1/6 background formula needs its
boundary treatment; on an odd periodic torus sigma is not well defined as
the required staggered function. The note's preceding even-torus setting
and its established-readout reference supply the relevant periodic scope.
Turns change geometric direction counts, so the old direction-locked
permanence hypothesis no longer applies. Our cube control changes the old
axis counts (1,1,1) to (2,0,1), then fills to (2,0,2), without changing an
old content. The earlier direction-tag counterexample is not invalidated.

Exact antipodality of classical content descriptors is extra input. As a
local quantum countercontrol, P_z tensor P_{-z} and P_z tensor P_x have
overlap trace 1/2. No operation can perfectly and deterministically
distinguish these unknown physical-input alternatives without additional
information. Thus permanence and local classical acceptance do not by
themselves supply the promised physical quantum recognition operation.
This is the gap already stated in the note, not a new universal impossibility
claim. Preparing a chosen classical pair is also different from copying an
unknown parent's state.

## 5. Independently assembled controls and countercontrols

`independent_check.py` imports no author implementation. It uses recursive
matching enumeration, graph-edge channels, a separately implemented
alternating-path construction, and exact SymPy generators. It checks:

- All 37 labeled four-vertex simple graphs with a perfect matching, plus
  K6, K3,3, a triangular prism, triangle with three leaves, a ten-cycle, a
  2-by-5 ladder, the reflecting cube, and a disconnected edge plus six-cycle.
  Every partial matching reaches a full one; every conservative slide has
  the exact reversed channel. Nonbipartite and disconnected cases are included.
- Six rational Bloch projector fixtures, all 24 proper signed-permutation
  rotations, exact spherical first/second moments, and all 63 nonempty
  subsets of the six vacant-neighbor directions.
- Marked site reuse and turns, the two distinct marked square rotations
  with the same geometric target, and the old cube cage's one-turn escape.
- On path P4 at arbitrary positive beta,kappa, exact full-packing probability
  one and mean time from empty `11/(6 beta)+1/(6 kappa)`. At kappa=0 the
  full-packing probability is only 2/3; the center-edge deposition traps the
  other 1/3. A three-vertex path has no perfect matching and cannot fill.
- Expected cumulative site birth counts on P4 are
  `(5/6,7/6,7/6,5/6)`; on transitive C4 they are all one. This directly
  tests the symmetry qualification for the per-site statement.

The first run failed at an unsimplified structural SymPy equality for
complex projector entries. Its source, receipt and full logs are preserved.
Replacing that structural test by exact entrywise symbolic simplification
made the checker pass; no tolerance, parameter, or expected value changed.
The analogous rational absorption comparison was normalized symbolically.
Run 02 exits zero, with full results and stdout/stderr on disk.

Provisional disposition before author-code comparison: no unresolved
mathematical defect found in the supplied claims at their stated classical,
finite-volume and proper-cubic scope. The construction does not close its
explicit quantum, formation-selected-state, wave, or infinite-volume gaps.
