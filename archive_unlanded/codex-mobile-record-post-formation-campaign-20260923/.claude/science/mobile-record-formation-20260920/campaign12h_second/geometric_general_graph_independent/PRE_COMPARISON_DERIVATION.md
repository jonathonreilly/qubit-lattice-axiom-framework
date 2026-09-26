# Independent reconstruction before the author checker

Only the complete frozen candidate GEOMETRIC_TWO_VACANCY_GENERAL_GRAPH.md has been opened for this new unit, together with unchanged previously checked geometric-model/rare-birth/clock premises. The author runner has been hashed but not read or executed; its results and the separate mixing comparison remain unread. This is an independent scrutiny of the supplied construction, not production authorship.

## Elementary and virtual steps

A legal slide is the triple (a,b,c), where a is vacant, bc is a present dimer and ab is an edge. It replaces bc by ab. If the immutable record labels at b,c are R,S, their new positions are a,b: R moves b->a, S moves c->b, and c becomes vacant. The inverse (c,b,a) restores both records. This is the same supplied two-record turning move, with its arguments written from the vacant end.

Fix any reference perfect matching F. Contract its edges; connectedness of G implies connectedness of that quotient, regardless of odd cycles or bridges. If the holes form an edge e=aa' in F and ab connects e to f=bb', the two slides (a,b,b') then (a',a,b) turn F-e into F-f. The second operation moves the two records currently on ab onto aa'; it does not insert an absent reference pair. The actual count remains K-1 throughout. A simple quotient path gives at most 2(K-1) slides between any two missing reference edges.

For an F-alternating cycle v0,...,v(2r-1), orient it so its F edges are v(2j)v(2j+1). After transferring the missing edge to v0v1, apply (v(2j-1),v(2j),v(2j+1)) for j=1,...,r-1. Each first argument is the current vacancy. The resulting matching is F' minus v(2r-1)v0, with F'=F symmetric_difference C. The actual records are transported, never created/deleted; only the proof's full reference changes. This requires r-1 slides, not a prohibited whole-cycle update.

## Arbitrary endpoints

For any near-perfect M and any fixed perfect P, M symmetric_difference P has degrees zero/two except the two holes, which have degree one. Thus it contains a single path joining the holes, plus even alternating cycles. The path begins/ends with P and has 2r+1 edges, r<=K-1. Slide from one vacant end successively across its r present M edges. This yields a near-perfect U with adjacent holes; U plus their last P edge is a virtual perfect F. The other symmetric-difference cycles need not be touched.

Do the same to the target T, obtaining F'-e' and a recorded target slide path. The full references F,F' differ by vertex-disjoint alternating even cycles; odd cycles in G do not change this fact. Transfer the hole edge to each such cycle and implement its flip as above. Finally move the missing reference edge to e', then reverse the target path. This reaches the target *geometry*. It does not assert that arbitrary prescribed final immutable labels can be reached.

If c is the number of nontrivial alternating cycles and their lengths are 2r_j, simplicity gives c<=floor(K/2) and sum r_j<=K. The two endpoint preparations and final missing-edge placement cost at most 4(K-1). Transfers before cycles cost at most 2(K-1)c, and cycle interiors cost sum(r_j-1)<=K. Consequently the full length is at most K^2+4K-4, hence certainly K^2+4K. For K=1 there is one geometric near-perfect state. These are construction/diameter bounds, not mixing estimates.

## Killed-chain inheritance

The geometric slide generator Q is finite, symmetric and now irreducible on Omega, hence has invariant pi=uniform. For a simple graph, the two holes permit either no birth or a single vacant edge. Write h in {0,1} for that eligibility and R(M,F)=1 if inserting that edge produces F. Each perfect F has exactly K distinct deleted-edge predecessors. Thus p=pi h=K Z/|Omega|>0 and (pi R)(F)=K/|Omega|=p/Z.

For beta->0 with fixed graph and fixed positive conservative rates, finite-state averaging gives joint Laplace transform

  E_M[exp(-s beta tau) 1_{exit=F}]
    = [beta (s beta I-Q+beta diag(h))^{-1} R](M,F)
    -> [p/(s+p)] / Z,  s>=0.

The limiting scaled clock is Exp(p), independent of the uniform full exit. The finite inverse/Poisson calculation already checked for the clock gives beta E_M tau->1/p uniformly over the finite entrance set. The earlier augmenting-path filling proof guarantees that any initially nonfull matching eventually enters this last level at each beta>0; the strong Markov property and uniform-over-entrances limit give the first-full law. This says nothing about the *total* scaled empty-start time law. Additional fixed geometric conservative channels with symmetric aggregate rates preserve uniformity/irreducibility; arbitrary marked channels that fail to give that geometric generator are not silently included.

The count |Omega|=sum_unordered{u,v} Z(G-{u,v}) follows by classifying each matching by its unique holes. On a bipartite graph holes must lie in opposite sides because equal sides are forced by a perfect matching. Translation averaging/fixed-origin formulas and thermodynamic literature assumptions are not inherited on arbitrary graphs.

## Deliberate countercontrols and an exact nonbipartite example

Disconnectedness can freeze already full components and destroy both slide connectivity and the uniform first-full conclusion. A connected graph without a perfect matching has no full exit: the four-vertex star already has near-perfect states whose two holes are never adjacent. The path on four vertices has a connected three-state geometric near-perfect space but two marked components if one prescribed oriented immutable pair is tracked. These distinguish the theorem's hypotheses and its geometric scope.

For the four-vertex diamond with edges 01,02,12,03,13, Omega has five one-edge matchings and there are two perfect matchings. The central edge 01 is a dark state (nonadjacent holes 2,3); the other four states have birth hazard beta. The slide graph is the line graph of the diamond. At unit kappa, p=4/5. Lumping dark versus bright gives

  E_bright tau = 5/(4 beta),
  E_dark tau = 5/(4 beta)+1/4.

Within the four bright states, those leading to either perfect exit form the two colors of a 4-cycle. The final-exit contrast from a bright state has magnitude beta/(beta+5), and the dark state has uniform exit. Therefore finite beta is generally nonuniform, while every entrance tends to probability 1/2 for each exit. The joint scaled Laplace limit for each exit is 2/(5s+4). The independent symbolic checker will reconstruct these facts directly from its own matching/sliding enumeration, rather than use them as input constants.
