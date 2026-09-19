# formation-clauses-in-level-time, attempt 3 (worker w-macbookpro90c72-j8dec, model grok-4.6)

Independent of attempt 2 (same model family, not used as a lemma). Route: closed-form noise maps for each recorded clause, a structural criterion for when the Z^3 law is a north-east-centre noisy majority, and exact all-+x probabilities on the 2×2×2 cube and the 3×3×2 slab as functions of the recorded-neighbour count histogram.

Definitions from PR #8146 (block 12, S0–S1), #8148 (block 14, clocks / jump chain), #8149 (block 15, sequential vs joint units), #8158 (block 24, free window vs integrated exterior). Menu `{±e_1, ±e_2, ±e_3}` labelled `0…5` with antipode `a^1`; rule `φ(a,a)=p`, `φ(a,−a)=q`, `φ(a,b⊥)=r`. One-site kernel given recorded neighbours `n_1,…,n_k`:

    r(s | n) ∝ ∏_j φ(s, n_j)     (k=0: uniform 1/6).

## (1) The statement attempted

Among the recorded clause candidates, the three-dimensional strong-coupling law reduces to a north-east-centre noisy majority automaton in level time if and only if records form one site at a time, in monotone level order, with the free-window (records-only) kernel. Its noise map is block 12 S1, exactly

    ε₂ = 1 − p³/(p³+q³+4r³),
    ε₁^⊥ = 1 − p² r / (r(p²+q²) + r²(p+q) + 2r³),
    ε₁^− = 1 − p² q / (pq(p+q)+4r³).

Every other recorded clause breaks at least one of the three NEC hypotheses (independent sites; exactly the three previous-level neighbours recorded; unrecorded sites contribute no factor), and therefore is not that automaton. The six constant configurations remain exchangeable under every covariant clause. The Toom-type leading behaviour (majority of three, island erosion, noise O(1/p)) holds only for the NEC clause; seeded growth is a one-neighbour copy `p/(p+q+4r)` and is not an eroder. The unique order-independent clause is joint formation of the whole window (the static Gibbs law). Exact witnesses: four distinct all-+x probabilities on the cube; k-histogram dependence on the 3×3×2 slab; positive total variation between joint and independent NEC on a same-level pair.

## (2) Steps

**Step 1 — S1 noise map (PROVED; CHECKED S1).** For a triple of recorded neighbours the kernel is the product of three `φ`. Unanimous `(a,a,a)`: `P(a)=p³/(p³+q³+4r³)`. Two-one orthogonal `(a,a,b⊥)`: `P(a)=p² r / (r(p²+q²)+r²(p+q)+2r³)`. Two-one antipodal `(a,a,−a)`: `P(a)=p² q/(pq(p+q)+4r³)`. Three positive axes `(+x,+y,+z)`: `P(+x)=p/(3(p+q))`. These are the majority probabilities of the NEC automaton; the complementary probabilities are `ε₂, ε₁^⊥, ε₁^−`. At `(3,1,2)`: `ε₂=11/20`, `ε₁^⊥=17/26`, `ε₁^−=35/44`. At `(10,1,2)`: `ε₂=33/1033`. Every one of the `6³` kernels is a probability (CHECKED S1.6). Majority is the mode iff `p>max(q,r)` (block 12 S1; used here only at `(3,1,2)` and `(10,1,2)` where it holds by the closed forms).

**Step 2 — NEC reduction criterion (PROVED).** Project `Z^3` onto levels `t = x_1+x_2+x_3`. A site at level `t` has three neighbours at level `t−1` and three at level `t+1`. The update at level `t` is a product, over sites of the level, of independent kernels of the three `t−1` neighbours, if and only if:

(N1) sites of the level form independently (sequential sites, not a joint unit);
(N2) when a site forms, its recorded neighbours are exactly those three (monotone level order; no same-level record yet, no missing predecessor);
(N3) unrecorded neighbours contribute no factor (free window / records-only).

This is block 12 S0, re-stated as a criterion. The noise parameters of Step 1 then apply, and S2–S3 of block 12 (eroder; domination by a binary noisy majority with `ε = max(ε₂,ε₁^⊥,ε₁^−)`) apply unchanged.

**Step 3 — seeded and uniform clocks fail (N2) (PROVED; CHECKED S1.13–14, N.1–2, C.2–5).** A covariant clock (block 14 R1) draws the next empty site with probability `λ_x/∑λ`. The seeded law (`λ_x=1` iff `x` has a recorded neighbour, else 0 after the first site) produces a connected growth: the typical interior step of the growth has `k=1` recorded neighbour, kernel `P(copy)=p/(p+q+4r)`. At `(3,1,2)` this is `1/4`, not `P(a|aaa)=9/20`. A one-neighbour copy is not a majority vote: a dissenting recorded neighbour is copied with probability `p/Z_1 → 1` as `p→∞`, so a finite island is not eroded. S2 fails. The uniform clock (`λ_x=1` on every empty site) mixes in extra `k=0` seeds and extra `k=2,3` closings; it is a mixture over orders, not a synchronous NEC product.

On the cube, the all-+x probabilities at `(3,1,2)` are four distinct rationals (CHECKED C.1–C.8):

| clause | `P(all +x)` |
|---|---|
| monotone sequential | `2187/44994560` |
| seeded jump chain | `84807/1799782400` |
| uniform-clock mixture over `8!` orders | `338229/7997080000` |
| joint (static Gibbs) | `p^{12}/Z` with `Z=6982520832`, i.e. `59049/775835648` |

So the rate clause changes the finished law on the cube, in agreement with block 14 R2 (different clocks, different laws) and extending it to the all-+x observable and to the joint comparator.

**Step 4 — joint units fail (N1) (PROVED; CHECKED U).** Two sites on the same level that are neighbours (a fork `e_i−e_j`) are independent under NEC and coupled by `φ` under joint formation of the pair, with three frozen +x predecessors each. At `(3,1,2)` the total variations on this 6×6 law are exact:

- joint vs independent NEC: `360383/3544200`
- sequential (first then second) vs joint: `1989/39380`
- sequential vs independent NEC: `527573/6175800`

and `P(both +x)` is `2187/7876` (joint), `81/400` (NEC), `729/2920` (sequential). The extra same-level bond is absent from the NEC product, so joint formation of a connected unit (in particular of a whole level, or of the window) is not the NEC automaton. Block 15 U2 is the finite-window criterion: sequential equals joint iff no site records an inside neighbour together with a second; a same-level neighbour is exactly such a second, so U2 fails for any joint unit that contains a fork.

On the cube, `TV(monotone sequential, joint) = 1182193085/23402354976` (CHECKED C.10).

**Step 5 — unrecorded exterior fails (N3) when a component touches two recorded sites (PROVED; CHECKED Q).** Block 24 Q3: an unrecorded site attached to two recorded sites `a,b` contributes the matrix `M_{ab} = ∑_s φ(s,a)φ(s,b)`, equal to `p²+q²+4r²` on the diagonal, `2pq+4r²` on antipodes, `2r(p+q)+2r²` on orthogonals. At `(3,1,2)` these are `26, 22, 24`, not constant. On a recorded pair with no direct bond, the free-window law is uniform (`1/36`); the integrated-exterior law is `M/∑M`; their TV is `1/72`. So adopting the integrated-exterior clause as a factor in the formation kernel changes the kernel whenever an unrecorded component touches two recorded sites. In monotone level order the three future neighbours of a site each touch that site and two other current-level sites (once those exist), so the clause is live after the first level. The free-window reading is (N3).

**Step 6 — six constants and the threshold's leading behaviour (PROVED; CHECKED N.3).** Every kernel that is a function of neighbour values only, covariant under the signed permutation group of the axes, treats the six constant configurations symmetrically: `r(a|a,…,a)` is independent of which axis `a` is (CHECKED N.3). The six constants remain exchangeable invariant candidates under every recorded covariant clause. What changes is the *mechanism*:

- NEC (three-neighbour majority, noise `O(1/p)`): block 12 S2–S3, Toom eroder, S6 obligation.
- Seeded `k=1` copy, noise `(q+4r)/(p+q+4r) = O(1/p)` but *no majority*: errors are copied along the growth tree; no island erosion (CHECKED N.2). The S6 obligation does not apply. This is the two-dimensional phenomenon of block 12 S5 (two predecessors, no error correction), realised in 3d by a rate clause.
- Joint / static: block 19's infrared bound on the sphere, or block 17's discrete order on six-axis; not a level automaton at all.

**Step 7 — order-independence (PROVED; CHECKED L, C).** A clause is order-independent when the finished law does not depend on which linear extension of “records form” is used.

- Joint formation of the whole window is the unique Gibbs field with the rule as one-site conditionals (block 15 U1). There is no order. This is the static law. It is order-independent by construction.
- Sequential laws: on any window whose graph has a cycle, different orders can produce different k-histograms for the all-+x event, hence different probabilities. On the 3×3×2 slab at `(3,1,2)`, monotone connected growth from a corner has k-histogram `(0:1, 1:5, 2:8, 3:4)` and `P(all +x)=94143178827/68428452520263680000`; an order that plants a second seed has histogram `(0:2, 1:3, 2:9, 3:4)` and a strictly smaller probability `282429536481/222392470690856960000` (CHECKED L.2–L.5). On the cube the uniform mixture over `8!` orders is not the monotone law (CHECKED C.3).
- Seeded growth is a mixture over connected orders only; it still depends on the clock (seeded ≠ uniform ≠ monotone on the cube).
- Trees: sequential equals joint for every order that never records an inside neighbour with a second (U2, R3). `Z^3` is not a tree.

So among recorded clauses, only joint-whole-window is order-independent on `Z^3`.

## (3) Where the route stops

The NEC criterion is for the recorded candidates, not a classification of every conceivable clause. Clock laws other than uniform and seeded (attracting, value-dependent) are not given new cube numbers here; block 14 already separates them on the 2×3 rectangle and the plaquette. The 3×3×2 joint partition function is not computed (`6^{18}`). The Toom stability theorem is not re-proved (block 12 S6 remains an obligation, and applies only to the NEC clause). Discrete-menu long-range order under joint/static is block 17, not this note.

## (4) What would finish it

A attracting-clock all-+x number on the cube; the 3×3×2 joint `Z` by a 3×3 transfer (six-axis `6^9` is heavy but finite); a proof that every connected growth order from a given corner of a rectangle has the same k-histogram (observed here for several orders, not proved); the S6 re-proof restricted to the NEC clause, with the exact `(ε₂,ε₁^⊥,ε₁^−)` of Step 1 as input.
