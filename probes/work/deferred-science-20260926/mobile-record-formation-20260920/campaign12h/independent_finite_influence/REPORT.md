# Independent finite-perturbation influence check

**Result.** For every initial-pair law in the supplied class, the set of sites whose occupation/content trajectories ever differ is almost surely finite. Its expected size is bounded by a constant times |K|, and its maximum distance from K has an explicit exponential tail. No spatial independence of the initial pair is needed. The result allows newborn records to relay discrepancies.

The radius is random and has no universal deterministic bound: an explicit positive-weight, zero-hopping example relays a discrepancy through arbitrarily many newborn records with positive probability. Finite spatial response does not erase the perturbation and does not by itself provide an exact finite coding or last-update stopping certificate.

No new primary influence calculation or source was read before this report and its evidence were sealed.

## 1. Model and the local estimate used

There are six immutable contents, vacancy bond weight one, positive symmetric pair weights W, insertion rate epsilon times the occupied-neighbor product at each vacant site, and rate-kappa proposals on each nearest-neighbor undirected edge with the supplied heatbath vacancy-hop acceptance. Fix epsilon>0, finite kappa≥0 and dimension d≥1. Use the checked common graphical construction: site proposals have rate beta, choose one of the six contents uniformly, and use a shared acceptance uniform; edge proposals and their acceptance uniforms are also shared.

Write z=2d and

\[
\ell=\min(1,\min W),\quad u=\max(1,\max W),\quad
\alpha=6\epsilon\ell^z,\quad\beta=6\epsilon u^z,\quad\lambda=z\kappa,
\]
\[
\gamma=\alpha/2,\qquad A=(1+4\lambda/\alpha)^d,
\qquad C=\frac{(\beta+2\lambda)A}{\gamma}.
\tag{1}
\]

For any initial configuration or law independent of future clocks, the checked estimates imply, uniformly in x,

\[
\Pr(x\text{ vacant at }t)\leq Ae^{-\gamma t},\qquad
E[J_x(t,\infty)]\leq Ce^{-\gamma t}.
\tag{2}
\]

Here J counts actual accepted births and hops that update x. The estimates are for v_*=1, so they remain valid after conditioning on any allowed initial pair. One way to obtain (2) labels each initial vacancy: its killing rate is at least alpha and its hop rate at most lambda. For lambda>0, choosing exp(delta)=1+alpha/(2lambda) bounds its surviving weighted hop count by exp(−gamma t). Summing exp(−delta distance) over starting sites gives A. The total update intensity at x is bounded by beta times its vacancy indicator plus kappa times the vacancies at both endpoints of each incident edge; integration gives C. For lambda=0 the direct vacancy bound exp(−alpha t) is stronger, so (1)–(2) still hold as written.

Let the two copies be sigma and tau, agreeing initially outside a fixed finite K, k=|K|. Define the actual trajectory-disagreement set and its radius by

\[
\mathcal D=\{x:\exists t\geq0,\ \sigma_t(x)\ne\tau_t(x)\},
\qquad R_*=\sup_{x\in\mathcal D}\operatorname{dist}(x,K).
\tag{3}
\]

Use R_*=0 when the disagreement set is empty. If K is empty, common-clock pathwise uniqueness gives an empty disagreement set. The remainder assumes k≥1. These are occupation/content trajectories, not a syntactic graph of every possible dependency or an additional unobserved genealogy label.

## 2. Forward dependence has its own footprint count

A birth mark centered at v reads the closed radius-one neighborhood of v and can write v. An edge mark on {v,w} reads the two closed neighborhoods and can write both endpoints. Accordingly, a potential forward arrow goes **from a pre-mark input site to a post-mark output site**. Its graph length is at most two.

For a fixed affected input site y, possible birth centers number at most z+1. Possible edge clocks have an endpoint in the closed neighborhood of y, so at most z(z+1) such edges suffice as an overcount; each has two possible outputs. Thus the total rate weighted by possible forward outputs is at most

\[
\Lambda=(z+1)(\beta+2z\kappa).
\tag{4}
\]

This happens to equal the earlier conservative backward-footprint bound, but the counting arguments are different. A forward edge event need not be incident to y: in one dimension, the event on {1,2} can read a discrepancy at 0 and write site 2. Counting only edges that update y would miss it.

Let P_n(T) count all chronological potential forward paths of n arrows, starting in K at time zero and ending by time T, including every possible endpoint. Poisson factorial moments over the ordered time simplex give

\[
E[P_n(T)]\leq k\frac{(\Lambda T)^n}{n!}.
\tag{5}
\]

Repeated visits to a site or clock are permitted, at distinct increasing times; paths need not be independent. The update maps in the two replicas are identical. Tracing any first actual discrepancy backward through those maps reaches an initial discrepancy in K. Thus every actual discrepancy has a potential chronological path from K. This uses the path bound at finite times; the unbounded-time potential graph itself is not claimed to be finite.

## 3. Bounds for the supremum over all times

For integer r≥1, let D_r be the number of sites in the disagreement set at distance exactly r from K. Put

\[
m_r=\lceil r/2\rceil,\qquad T_r=\frac{m_r}{2e\Lambda},\qquad
\eta=\frac1{1-(2e)^{-1}},\qquad a=\frac{\gamma}{4e\Lambda}.
\tag{6}
\]

Every site counted before T_r requires a path of at least m_r arrows. Distinct first-discrepancy sites have distinct ending paths, so their number is bounded by the total number of such potential paths. Consecutive terms in the series in (5), for n≥m_r, have ratio at most 1/(2e). Also m!≥(m/e)^m. Hence

\[
E[\#\{\text{distance-r sites that disagree by }T_r\}]
\leq k\sum_{n\geq m_r}\frac{(\Lambda T_r)^n}{n!}
\leq k\eta\,2^{-m_r}.
\tag{7}
\]

A site that first disagrees after T_r must have an actual accepted update after T_r in at least one copy. This is the step needed for the supremum over all times; a fixed-time disagreement probability alone would not suffice. Applying (2) to both copies requires no independence between them.

Let s_d(r) be the number of Z^d sites at L1 distance r from the origin. The distance-r shell about K has at most k s_d(r) sites. Since exp(−gamma T_r)≤exp(−ar),

\[
\boxed{E[D_r]\leq k\eta\,2^{-\lceil r/2\rceil}
 +2Ck\,s_d(r)e^{-ar}.}
\tag{8}
\]

Define the elementary geometric sum

\[
G_d(b)=\sum_{x\in\mathbb Z^d}e^{-b|x|_1}
=\left(\frac{1+e^{-b}}{1-e^{-b}}\right)^d.
\]

Using sum_{r≥1}2^{−ceil(r/2)}=2 and sum_{r≥1}s_d(r)e^{−ar}=G_d(a)−1 gives

\[
\boxed{E[|\mathcal D|]\leq
k\{1+2\eta+2C[G_d(a)-1]\}<\infty.}
\tag{9}
\]

In particular, an infinite ever-disagreement set has probability zero. For integer R≥1, summing (8) from R onward gives a convenient explicit tail:

\[
\boxed{\Pr(R_*\geq R)\leq
\min\{1,\ k[4\eta+2C G_d(a/2)]e^{-aR/2}\}.}
\tag{10}
\]

Indeed, the geometric first-term tail is at most 4·2^{−ceil(R/2)}, and the second is at most exp(−aR/2)G_d(a/2). Here a<log 2, as follows from gamma≤beta≤Lambda. These constants are conservative and may be very large.

All estimates are uniform over the initial-pair law, conditional on its allowed configuration values, because (2) is uniform. Arbitrary spatial correlations and correlations between the two initial replicas are allowed. The quantifier is: for each such initial-pair law independent of future clocks, the conclusion holds almost surely. Uniform bounds do not authorize an uncountable intersection over all backgrounds selected with knowledge of those future clocks.

Both terminal fields therefore differ only on a finite random set. They can remain unequal on that set forever; this is finite spatial response, not eventual equality of the two fields. Tagged-record fixation was not used to prove (8)–(10).

## 4. No deterministic radius: an explicit newborn relay

Take d=1, kappa=0, epsilon>0, and the positive six-axis weights W(a,b)=1+j v_a dot v_b with 0<j<1. Initially the two copies differ only at 0: one contains +e1 and the other −e1. All other sites are vacant. Let the desired proposal content be +e1. Put u=1+j and beta=6epsilon u².

For any n≥1, impose the following finite positive-probability clock event in the guard interval {−1,0,...,n,n+1} during [0,T]. There is exactly one proposal at each site 1,...,n, in that order, and no other guard-site proposal. All n proposed contents are +e1. At site 1 choose the shared acceptance uniform strictly between (1−j)/u² and (1+j)/u². At each later site choose it between 1/u² and (1+j)/u².

The first copy accepts every proposal and the second rejects every one. Site n has differing trajectories, although the original record never moves. The probability of this sufficient event is exactly

\[
\boxed{\frac{2(\epsilon jT)^n}{n!}
       e^{-(n+3)\beta T}>0.}
\tag{11}
\]

To obtain (11), the ordered specified-clock events contribute exp(−(n+3)beta T)(beta T)^n/n!, the content marks contribute 6^{−n}, and the uniform intervals contribute (2j/u²)(j/u²)^{n−1}. Outside events cannot alter the guarded vacant neighbors when kappa=0. Thus no deterministic finite radius can be asserted uniformly for this fixed model and initial pair. This is compatible with the almost surely finite radius and its tail. The example concerns ever-differing trajectories; later content agreement would not erase the earlier discrepancy.

There are simpler special cases: when kappa=0 and W=1, sites evolve independently under this coupling and the disagreement set stays inside K. With positive hopping, even W=1 permits a changed initial record to travel an arbitrarily prescribed finite distance with positive probability before competing births block it. The relay above shows why transport of the original tag is not the only mechanism that must be controlled.

## 5. What this does and does not certify

The finite random radius in (10) is a property of the completed coupled trajectories. The estimates do not turn it into a deterministic cutoff, exhibit a finite stopping rule certifying no future discrepancy, or guarantee stability against arbitrary infinite changes outside an observed input ball. A last-update time can be finite almost surely without being a stopping time. Forward response to a fixed finite initial change and backward determination of a terminal output from a finite input region are different obligations.

A concrete distinction already occurs for W=1, kappa>0 and an empty initial lattice. At every finite time there are almost surely vacancies somewhere: infinitely many separated sites have received no site or incident-edge proposal, and intersecting this property over integer times covers all finite times. At any finite stopping time, if a queried site is occupied, choose a closest vacancy and a shortest path to it. The interior path is occupied. There is positive conditional probability that a prescribed finite sequence of accepted swaps brings that vacancy to the queried site before births intervene. If the queried site is vacant, it also has positive probability of a later update. Therefore no finite stopping time in the natural history filtration can certify that this site has had its last accepted update. This holds even if the entire current configuration is available.

That is a statement about last-update certificates, not a classification of every possible finitary coding representation. Conversely, when kappa=0 a site's first accepted birth, or time zero if initially occupied, does certify its terminal content. The present argument establishes no general impossibility theorem for exact coding, and (9)–(10) alone do not supply one.

Finite perturbation response also does not force terminal spatial clustering under correlated initial laws. A fully occupied configuration with a shared random global choice of +e1 or −e1 is fixed. Changing finitely many contents changes only those trajectories, while the unperturbed field has first-coordinate covariance one at every separation. Product-law assumptions used for separate correlation theorems cannot be inferred from finite perturbation stability.

The hypotheses held fixed here are a positive uniform insertion floor, finite proposal-rate bounds, finite-range read/write maps, polynomial lattice geometry, common marks, and initial-pair independence from future clocks. The constants are not uniform as the formation or weight floor tends to zero at fixed mobility. Vanishing formation, loss of the weight floor, unbounded mobility, different motion rules or altered information/coding resources are outside this claim.

## 6. Independent controls and provenance

`check.py` imports no primary source. It enumerates forward and backward footprints in d=1,2,3, including edge clocks not incident to the changed input site; counts L1 shells; checks the chronological-path series and radius-tail constants; and verifies the acceptance thresholds and exact probability (11) through six newborn relays. The numerical choice j=1/2, epsilon=1, T=2/27 gives probability 2e^{−4}/27 for the one-step relay and e^{−9}/139471376040 for six steps. The general positive-probability construction and the all-time proof are analytic, not extrapolations from these finite checks.

All controls passed on Python 3.13.5 and SymPy 1.14.0. Run `python3 check.py > RUN.log 2>&1` in this directory; `RESULTS.json` and `RUN.log` are byte-identical. The allowed prior activity/correlation report identities, the supplied-input receipt and all new evidence hashes are recorded in `SEAL.json`. No primary influence file or result was accessed before sealing, and no source outside the assigned directory was edited.
