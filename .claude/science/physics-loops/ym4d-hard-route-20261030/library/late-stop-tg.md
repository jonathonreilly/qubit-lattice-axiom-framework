lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T00:28Z

# late-stop-tg: statement (TG) of cov-frames at the late stop (FINISH row 647)

Provenance: Claude Fable 5.2, medium, one session, commit 3591d5adc, 2026-11-10. No numerics were run.
Not checked by another model. Source: `YM4_1400.tex` of Sussman and Alpoge (with Claude and Codex as
authors of the text), commit 2bc0658f, cited as 'Y n'; Bałaban, Comm. Math. Phys. 122 (1989) 175-202,
pp. 195-197, cited as 'B122a' (local OCR `~/ym4d-papers/cmp122a.txt`). 'Read' means: a clause of Y's
definition, quoted with its lines, not rebuilt.

## 0. Result

**Verdict: stop condition (i), with one correction to the wording of (TG).** (TG) holds in this form:

**(TG\*)** At the main step of X the tree gauge is the map `V -> u . V` on the old-slot datum, for one
function `u` on the nodes (a node is a point with its finest level: a level-q site in layer `q`). `u` is
the unit at every node outside the set `N` of nodes of `Lambda^pr minus I_h`, where
`I_h = H_{h+1}^{[a_{h+1}]}` is the *inner cut*: the box `Z''_{h+1}` less its two outer cell layers.
Every determining row with an end in `N` changes from `V(b)` to `u(b_-) V(b) u(b_+)^{-1}`; every other
row keeps its value. So the tree gauge is a site-gauge move in the sense of `library/cov-frames.md`
section 2, and by Lemma 2.2 there every tested loop is conjugated by `u` at its base corner.

What is proved and from what:

1. The rows with an end in `N` are of exactly four kinds (Lemma 2): inside one shell; across a face
   between two shells; across the outer face of `Lambda^pr`; across the inner cut `dI_h`. Proved from
   the sequence (D1) of `library/cov-x.md` and the box facts (B1), (B2) there.
2. On each kind the move is `u(b_-) V(b) u(b_+)^{-1}` with the same `u` (Theorem 4). For the first
   three kinds the row is a fluctuation bond (in `B_0`) and this is Y's definition of the tree gauge
   (clauses (T-node), (T-B0), (T-tree), read). For the fourth kind the row is not in `B_0`; Y keeps it in
   the level-h Haar stock and moves it by "a Haar translation at the endpoints of every kept link"
   (clause (T-cut), read). Lemma 3 proves that this joint action is the one that carries the integral
   before the tree gauge to the integral after it, with Jacobian one; the action on `B_0` alone does
   not (Remark 3.1).
3. `u` exists, is unique, and is the unit at the root and outside `N` (Lemma 1, proved).

**Correction to (TG) as `cov-frames` states it.** The inner boundary of the tree gauge is not the core
face (the face of `C_h = G_h`). It is the inner cut `dI_h`, one coarse cell outside the hull `H_{h+1}`
of the core (Y 71302-71310, 76459-76468, 134413-134416). A row across the core face has both ends in
`I_h`; the tree gauge does not move it (Lemma 2 (e)). The row at stake on the inner side is the level-h
row across the inner cut. No lemma of `cov-frames` changes: Lemma 4.3 (c) holds as stated, with (TG\*)
in the place of (TG), so the hypothesis "given (TG)" is removed.

**Effect on the weak-form statements (item 4 of the row): yes for every kind of loop.** At a late stop
every tested loop changes at most by conjugation; the table is in section 5. `B` is empty and a late
stop makes no plaquette fresh.

What stays open: the clauses (T-node), (T-B0), (T-tree), (T-cut), (T-inv), (T-comp) of section 2 are
read from Y, not rebuilt (they are definitions of the operation, and one invariance statement); the
second gauge of the main step (the compensating change, (T-comp)) is treated only through Y's clause
that it is a site gauge with unit at the endpoints of the rows below level `h`; no check by another
model.

## 1. Repo search

- `grep -n -i "late stop\|(TG)\|late-stop\|tree gauge\|inner cut" library/open-core.md`: no entry.
- FINISH rows: 638 (`cov-frames`, states (TG) and reduces the late stop to it), 646 (`cov-frames-check`,
  the check of that file), 647 (this row). Registry row COV names row 647 for (TG). No other row proves
  it.
- `grep -l -i "tree gauge\|frame tree\|inner cut" library/*.md library/prior/*.md parts/*.md`: hits in
  `library/cov-frames.md` (the statement), `library/cov-global.md` and its check (the move (m1) as part
  of the definition of a trajectory), and Bałaban rebuild files (`b98`, `b102`, `b119`, `a1-*`, the axial
  gauge of the small-field step). None states the action of the main-step tree on the rows across the
  faces of the shells, and none has the inner cut `I_h`.
- This checkout has the ref `origin/claude/ym4d-hard-route` only; `origin/main` and the other YM4D PR
  branches are not present, so I did not search them.

## 2. Setting and Y's definitions (item 1 of the row)

Notation of `library/cov-frames.md` section 2 and `library/cov-x.md` 2.1: X a class component of level
`t`, window from `h`, `h < k_0 <= t - 2`; `a_q = M R_q L^q`, `u_q = M L^q`; `H_{h+1}` the hull of the core
with `G_h subset H_{h+1}`, `O_h = Omega_h^c cap X subset G_h`; `Z''_{h+1} = H_{h+1}^{[3 a_{h+1}]}` (`h + 1 <= k_0`);
`Lambda^pr = Z''_t^{[u_t]}`. The moment is after `N_t` stages, so inside X the sequence is `A^t` of (D1):

`A_q = Omega_q cap X` (`q <= h`),  `A_q = X minus Z''_q` (`h < q <= t`),

with layers `Lay_q = Z''_{q+1} minus Z''_q` (`h < q < t`), `Lay_h = Z''_{h+1} minus O_h`, `Lay_t = X minus Z''_t`, and
`Lay_q subset O_h` for `q < h`. Rows: `Gamma_q` = the level-q bonds that touch `A_q` and have no endpoint
in `A_{q+1}` (Y 10555-10566); the top level is `t` (the operation of level `t` is before step `t + 1`,
(O-order) of `cov-frames`).

**Nodes.** A *node* is a point `x in Lay_q` that is a level-q site ("A top is a site
`y in T^(j) cap (Omega_j minus Omega_{j+1})`", Y 10529-10530). Both ends of every row are nodes: "Every
endpoint is a top, possibly of the preceding level" (Y 10568); the inner end of an outward row of level
`j` "is a top of level `j - 1`, even when it also happens to be a site of a coarser lattice"
(Y 10577-10579). So a point carries one node, and rows of two levels can end at it.

**Shells and the inner cut.** Shell `t` := `Lambda^pr minus Z''_t` ("this layer is the shell of level `k`",
Y 63836 (1)); shell `q` := `Lay_q` for `h < q < t`; `I_h := H_{h+1}^{[a_{h+1}]}`; shell `h` := `Z''_{h+1} minus I_h`.
`N` := the nodes in the shells = the nodes of `Lambda^pr minus I_h`. Y: "`I_h = Lambda^pr cap ((Omega''_{h+1})^{~2})^c`"
(Y 71303-71306); "The shell gauge ends at the two-cell enlargement of the prepared `Omega_{h+1}`. The
prepared inner box at `h + 1` has three cell layers around the hull of the bottom core. After the two
layers have been removed, the remaining cell layer still contains the complete bottom-core reads. The
frame tree therefore acts only on the retained shell" (Y 76459-76468); "the inner cut is one coarse
layer from the hull of the old core and two layers from the outer prepared face", the coarse layer
being `L M R_{h+1}` in level-h units, that is `a_{h+1}` (Y 134413-134416). B122a p. 196: "no gauge is
fixed in this domain", for the last domain of the sequence.

**The retained prepared datum.** "the shell of level `j` carrying the field `V_j`. Together these fields
form the datum `V''` attached to the prepared determining set `B''`" (Y 63836 (1)). On a level-t bond
with an end in `Lambda^pr` it is the old-slot variable ("the Haar refresh uses the box coins and keeps
the old variables for the prepared datum", Y 97596-97598; Y 76677-76679; (M-slot) of `cov-frames`). At a
late stop: "Use the prepared datum for the regularity comparison and the fresh outgoing field for the
later averaging rows that read it" (Y 78289-78292); "Its frame tree acts on the old shell variables"
(Y 75684-75685).

**Clauses of the tree gauge (read).**

- **(T-node)** A gauge of the datum is a function on the nodes, and it acts on each row at its two
  ends: `(u . V)(b) = u(b_-) V(b) u(b_+)^{-1}`. (Y 10594-10600: the datum is `(M^j U on Gamma_j)_j`, "Exact gauge
  covariance of the iterated average ... Its definition involves all nodes, not only the centers of
  the last lattice"; Y 10606-10608: the loops "transform by conjugation at their starting node";
  Y 69457: "A level-i site in layer `i` is a determining node"; Y 4366: "a unique `u` satisfies
  `(u . V)|_T = V_0`".)
- **(T-B0)** The fluctuation bonds are `B_0 = B'' cap (shells)` (Y 63845). "The fluctuation bonds `B_0`
  extend from the outer box to this inner cutoff. They include the bonds crossing `dLambda^pr` and
  exclude those crossing the boundary of `I_h` towards its interior" (Y 71308-71311; B122a p. 195: "bonds
  intersecting `dLambda` belong to `B_0`"). So `B_0` = the rows with an end in `N` and no end in `I_h`.
- **(T-tree)** The tree `T_0`: in each shell the union of the axial contours from one initial site to
  every site of the shell lattice (B122a p. 196; Y 63849: "axial contours which leave from a single
  initial site and go around `P_2`"); for each inner box of the nest other than `I_h`, one row crossing
  its boundary (the entrance); for the outermost box one row crossing `dLambda^pr`, whose outer end `o`
  is the *root* ("for each inner box on which a gauge is fixed, one external bond crossing its boundary
  is added, and one more is added for the outermost box. Through these extra bonds the trees of the
  shells become a single tree, and it fixes the gauge entirely, with Jacobian one", Y 63849). `o` is a
  level-t node of X outside `Lambda^pr` and is fixed ("the entrance bond has its outer endpoint in the
  component and outside the prepared core ... That endpoint is a node at the current top level ...
  They are fixed nodes", Y 69458-69468; "Put the gauge equal to the identity outside and propagate its
  values from the root along that tree", Y 84240-84241). In the summand of the frame `r in W_4` the tree
  is `r T_0` (Y 63836 (0), Y 71421; "The same component frame fixes both trees and the entrance root, so
  the tree gauge gives the same shell variables", Y 97599-97601). The tree gauge is: `u` is the function
  with `u(o) = 1`, `u = 1` off the vertices of the tree, and `(u . V'') = V_0` on the bonds of the tree,
  where `V_0` is the centre (Y 63845-63846), a function of the exterior and the frame only (Y 75689-75691;
  Y 134877-134880); the datum becomes `u . V''`. In Y's coordinates `V'' = e^{i g B} V_0`, this is `B = 0` on the
  tree: "Its tree gauge sets the tree bonds to zero and has Jacobian one" (Y 74990-74991).
- **(T-cut)** The level-h links across `dI_h` are not in `B_0`; they stay in the level-h Haar stock
  and are translated at their ends: "Its kept links, including those crossing the cut, are in the
  second Haar stock of (1.143). The gauge-nest convention excludes the crossing links from `B_0`, so
  (1.145) retains them in `dV_h`. Use this stock after the compensating change of (4c). At fixed
  exterior and frame this change is a Haar translation at the endpoints of every kept link"
  (Y 134424-134433). B122a p. 197: the change of gauge of the shell "requires the corresponding
  compensating gauge transformations of the variables `V_h`, the gauge transformation restricted to"
  the boundary sites of the last domain, "and of the variables `V'`, the gauge transformation in the
  adjoint representation. The expressions in the integral (1.76) are invariant with respect to these
  transformations."
- **(T-inv)** Before the tree gauge the integrand is invariant under the gauges of the nodes of `N`:
  "The measure and the underintegral expressions in the second integral in (1.76) are gauge
  invariant; more precisely they are invariant with respect to the gauge transformations defined on
  `B_0`" (B122a p. 195). The tests that are not invariant (the test on `B`, the last-shell test) are
  inserted after it (Y 63836 (0): "neither the test on `B` nor the last-shell test is gauge invariant.
  Each of them enters only by way of decompositions of unity performed within a single gauge-fixed
  measure").
- **(T-comp)** The main step has a second gauge, the compensating change for the mixed gauge of the
  reference `U_0`. It is a site gauge fixed by the exterior and the frame, equal to one at the
  endpoints of the rows below level `h`: "All genuine rows below level `h` of the frozen core have their
  endpoints in `Z_h`, by the no-inward convention. Choose a site gauge equal to one on those endpoints
  and the seam halo ... Use this only to change coordinates of the retained datum ... the whole
  artificial datum changes by a site gauge" (Y 71203-71220); "the exterior compensator acts by a gauge
  on the full datum" (Y 134370-134372).

The tree gauge writes no fresh-slot variable: the tree coordinates "are disjoint from the fresh Haar
pivots of the outgoing rows", "without imposing any tree condition on the fresh pivots" (Y 75692-75698).

## 3. Three lemmas

**Lemma 1 (the tree function; proved).** Let `T` be a finite tree whose vertices are nodes, with a
vertex `o` (the root), and whose edges are rows. Let `V`, `V_0` be `SU(2)`-valued on the edges. There is
exactly one function `u` on the vertices with `u(o) = 1` and `u(b_-) V(b) u(b_+)^{-1} = V_0(b)` on every edge.
Extended by one to the other nodes, `u` is one function of the node, and `u = 1` at `o` and at every
node that is not a vertex of `T`.

*Proof.* Induction on the distance `d(x)` from `o` in the tree. For `x != o` let `b` be the edge to its
parent `y`. If `b = (y, x)`: `u(x) := V_0(b)^{-1} u(y) V(b)`. If `b = (x, y)`: `u(x) := V_0(b) u(y) V(b)^{-1}`. Each
equation has this one solution given `u(y)`, and each edge is the parent edge of exactly one vertex.
`square`

**Lemma 2 (the rows at the nodes of `N`; proved from (D1), (B1), (B2) of `cov-x`).** At the moment of
the tree gauge:

- (a) No row of level `q < h` has an end in `N`, and none has an end in `X minus O_h`.
- (b) A row of level `h` with an end in `N` has both ends in `Z''_{h+1}`. Either both ends are in shell
  `h` (*inside the shell*), or one end is in `I_h` (*across the inner cut*).
- (c) A row of level `q`, `h < q < t`, with an end in `N` has both ends in `Z''_{q+1}` and an end in shell
  `q`. Either both ends are in shell `q`, or the other end is in shell `q - 1` (*across a face between
  shells*); in both cases both ends are in `N`.
- (d) A row of level `t` with an end in `N` has an end in shell `t`. Its other end is in shell `t`, or in
  shell `t - 1` (across a face between shells), or outside `Lambda^pr` (*across the outer face*; that end
  is a level-t node of `Lay_t`, not in `N`).
- (e) A row with an end in `G_h` (in particular a row across the core face) has both ends in `I_h`, so
  no end in `N`.
- (f) There is no row of level above `t`.

*Proof.* (a) `N subset X minus I_h subset X minus O_h = Omega_h cap X = A_h subset A_{q+1}` for `q < h` (`O_h subset G_h subset H_{h+1} subset I_h`,
(B1)); a row of level `q` has no endpoint in `A_{q+1}`. (b) A level-h row has no endpoint in
`A_{h+1} = X minus Z''_{h+1}`; a bond with an end in `N subset Z''_t` has its other end within `L^h` of it, in X
(`Z''_t subset O_t = X^{[-2 a_t]}`, (B1)). So both ends are in `Z''_{h+1} = (shell h) cup I_h`. (c) No endpoint in
`A_{q+1} = X minus Z''_{q+1}`, and the row touches `A_q = X minus Z''_q`: an end is in `Z''_{q+1} minus Z''_q`, shell `q`. If the
other end `y` is in `Z''_q`: it is within `L^q` of `X minus Z''_q`. For `q - 1 > h`, `dist(Z''_{q-1}, X minus Z''_q) >= u_q > L^q`
(B2), so `y in Z''_q minus Z''_{q-1}`, shell `q - 1`. For `q - 1 = h`: `dist(I_h, X minus Z''_{h+1}) = 2 a_{h+1} > L^{h+1}`, so
`y in Z''_{h+1} minus I_h`, shell `h` (Y 71321-71325: "A row of level `h + 1` ... stays on the fluctuation side of the
two-cell enlargement"). If the end in `N` is the end in `Z''_q`, the same holds with the roles exchanged.
(d) A level-t row touches `A_t = X minus Z''_t` (or `Omega_t` outside X). If its end in `N` is `x in Z''_t`, the other
end is within `L^t < u_t` of `Z''_t`, in `Lambda^pr minus Z''_t`, shell `t`, and `x` is in shell `t - 1` as in (c)
(`t - 1 > h` since `k_0 <= t - 2`). If `x` is in shell `t`, the other end is in `Z''_t` (then in shell `t - 1`), in
shell `t`, or outside `Lambda^pr`; in the last case it is in `X minus Z''_t = Lay_t`, a level-t node.
(e) The other end is within `L^h < a_{h+1}` of `G_h subset H_{h+1}` (levels `<= h`; a row of level `> h` has no end
in `G_h subset Z''_{h+1}` by (c), (d) and `dist(G_h, X minus Z''_{h+1}) >= 3 a_{h+1}`). (f) (O-order). `square`

**Lemma 3 (the tree gauge as a change of variables; proved).** Let `R` be a finite set of rows, `N` a
set of nodes, `R(N)` the rows with an end in `N`, `T subset R(N)` a tree on vertices in `N cup {o}`, `o` not in `N`.
Let `G^N` act on `SU(2)^R` by `(g . V)(b) = g(b_-) V(b) g(b_+)^{-1}` (`g := 1` off `N`). Fix `V_0` on `T`, put
`S := { W : W = V_0 on T }` with the product Haar measure `dW` of the rows not in `T`, and for `V` let
`u_V` be the function of Lemma 1 (its vertices other than `o` being all of `N`). If `F` is bounded,
Borel and `G^N`-invariant, then for every bounded Borel `phi`

`int F(V) phi(u_V . V) dV = int_S F(W) phi(W) dW`.

So the image of the measure `F dV` under the map `V -> u_V . V`, **acting on every row of `R(N)`**, is
`F dW` on the slice: the tree gauge with Jacobian one.

*Proof.* The map `Phi : G^N x S -> SU(2)^R`, `(g, W) -> g^{-1} . W`, is a bijection with inverse
`V -> (u_V, u_V . V)` (Lemma 1). It carries `dg dW` to `dV`: order `N` by tree distance from `o`. On the
tree bond `b_x` from the parent of `x` to `x`, `V(b_x)` is `g(x)` or `g(x)^{-1}` multiplied on the two sides by
elements that depend on `V_0` and on `g` at the parent only; Haar measure on `SU(2)` is invariant under
translations and under the inverse, so, integrating the `g(x)` in order of decreasing distance, `dg`
goes to the product Haar measure of the tree bonds. On a row not in `T`, `V(b) = g(b_-)^{-1} W(b) g(b_+)` is a
translate of `W(b)` at fixed `g`. Fubini. Then
`int F(V) phi(u_V . V) dV = int dg int_S dW F(g^{-1} . W) phi(W) = int_S F(W) phi(W) dW`, by invariance and
`int dg = 1`. `square`

**Remark 3.1 (the action on `B_0` alone is not the move).** Let `b = (x, y)` be a level-h row across the
inner cut, `x in N`, `y in I_h`, and let `F` read a loop through `b` and a row of `B_0` at `x` (a tested level-h
plaquette with corners on both sides of `dI_h`; Y 134424-134426 has such test boxes). `F` is invariant
under the joint action, by (T-inv), and not under the action that moves the rows of `B_0` and leaves
`V(b)`: the loop would change from `W` to a product in which `u(x)` stands at one place only. The two
candidate values on the row are `u(x) V(b)` (joint action) and `V(b)` (action on `B_0` alone). Y's formula
after the tree gauge has the same integrand as before it, with `delta_{r T_0}` inserted (Y 71421); by
Lemma 3 this is the image under the joint action. (T-cut) states the same for the kept links.

## 4. (TG\*) row by row (item 2 of the row)

**Theorem 4 ((TG\*); proved from Lemmas 1, 2 and the clauses (T-node), (T-B0), (T-tree), (T-cut)).** Let
`u` be the function of Lemma 1 for the tree `r T_0` with root `o`, the old-slot datum `V''` and the centre
`V_0`. Then `u` is one function of the node, `u = 1` at every node outside `N`, and the tree gauge changes
every determining row `b` to `u(b_-) V(b) u(b_+)^{-1}`:

| Row | Ends | In `B_0` | Value after | Clause |
|---|---|---|---|---|
| inside shell `q`, `h <= q <= t` | both in `N` | yes | `u(b_-) V(b) u(b_+)^{-1}` | (T-B0), (T-node) |
| across a face between shells `q - 1` and `q`, `h < q <= t` (level `q`) | both in `N`; the inner end is a level-(q-1) node | yes | `u(b_-) V(b) u(b_+)^{-1}`, with `u` at the inner end the value that the rows of level `q - 1` at that node get | (T-B0), (T-node) |
| across the outer face of `Lambda^pr` (level `t`, old slot) | one in `N`, one outside `Lambda^pr` | yes | `u(x) V(b)` or `V(b) u(x)^{-1}`, `x` the end in `N`; `u = 1` at the outer end | (T-B0), (T-node), (T-tree) |
| across the inner cut `dI_h` (level `h`) | one in `N`, one in `I_h` | no | `u(x) V(b)` or `V(b) u(x)^{-1}`; `u = 1` at the end in `I_h` | (T-cut), Lemma 3 |
| across the core face; inside `I_h`; level `< h`; with no end in `Lambda^pr` | none in `N` | no | `V(b)` | Lemma 2 (a), (e) |

So the tree gauge is a site-gauge move with `u`.

*Proof.* *One function, unit off `N`.* Every vertex of `r T_0` other than `o` is a node of `N`: the bonds of
the tree are rows of `B_0` and the entrance of the outermost box (T-tree), and by Lemma 2 (b)-(d) a
row of `B_0` has its ends in `N`, except the outer end of a row across the outer face; the only such
row in the tree is the entrance at `o` (the shell trees lie in their shells, and the other entrances
cross inner boxes). `o` is not in `N`. Lemma 1 gives `u` on the vertices, with `u(o) = 1`, and `u = 1` at all
other nodes: the nodes of `I_h` (the core and the layer about its hull, where "no gauge is fixed"), the
nodes outside `Lambda^pr`, and any node of `N` that the tree does not reach. A node is a point (section
2), so at a node of shell `q - 1` where a row of level `q` ends there is one value `u(y)`.

*Rows.* By Lemma 2 a row with an end in `N` is of one of the first four kinds of the table, and by
(f) there is no other level. First three kinds: the row is in `B_0` (T-B0), a variable of `V''`, and the
tree gauge replaces `V''` by `u . V''`, which by (T-node) is `u(b_-) V''(b) u(b_+)^{-1}` at its two end nodes. For
the face between shells the inner end `y` is a node of shell `q - 1`, and `u(y)` is the same element that
acts on the level-(q-1) rows at `y`; this is forced also by (T-tree): the entrance of the inner box is
such a row, and with it "the trees of the shells become a single tree" that "fixes the gauge
entirely", which holds only if the gauge of shell `q - 1` at `y` acts on it. For the outer face the end
outside `Lambda^pr` has `u = 1`, and the variable is the old slot (section 2). Fourth kind: (T-cut); the
end in `I_h` has `u = 1`. Lemma 3 with `R` = the rows of X, `F` = the integrand before the tree gauge
(T-inv): the image of the term under the joint action is the term with `delta_{r T_0}`, which is Y's
formula; so the point after the move, at which the later tests are read, is `u . V` on every row of
`R(N)`. Rows with no end in `N`: `u = 1` at both ends, and the tree gauge writes only variables at the
nodes of `N` ((M-tree) of `cov-frames`; "The frame tree therefore acts only on the retained shell",
Y 76467-76468). The determining sequence does not change (the move writes no entry). `square`

**Corollary 4.1 (the two gauges of the main step).** The compensating change (T-comp) is a site-gauge
move with a function `w` on the nodes, `w = 1` at the ends of the rows of level below `h` and outside
`Lambda^pr`. The composition of the tree gauge and this change is the site-gauge move with `w' u`,
where `w'` is `w` read at the point after the tree gauge. If the stop retains the datum before the tree
gauge (as at a sharp collar split, Y 97586-97587), the move is the site-gauge move with `u = 1`.

*Proof.* Composition of two maps `V -> u . V` is `V -> (w' u) . V`, by (T-node). `square`

## 5. Effect on the lemmas of cov-frames and on the weak form (items 3, 4 of the row)

(TG) does not fail on a row; item 3 of the row (the changed form) does not apply. The only change is
the place of the inner boundary (section 0).

**Lemma 4.3 (c) of `cov-frames`, now without hypothesis.** At a late stop: the central integration
changes no determining row ((M-slot)); the frame selection writes nothing; the tree gauge is a
site-gauge move (Theorem 4), and so is the compensating change (Corollary 4.1); the tests write nothing
((P-test)). By Lemma 2.2 of `cov-frames` every tested plaquette `p` has `W'(p) = g(x_1) W(p) g(x_1)^{-1}`, `g` the
composed function, `x_1` the base corner. `B` is empty; the late stop makes no plaquette fresh. Lemma 2.2
uses (DB) and (MC): a completed edge of level `l <= t` reads rows of level `l - 1` with both ends in
`Lay_{l-1}`, each moved by `u` at its ends (Theorem 4 covers the double blocks that meet `dI_h` or a face
between shells), so its value changes to `u(e_-) M(V)(e) u(e_+)^{-1}`.

**The weak form, by kind of tested loop (tree gauge `u`):**

| Tested plaquette | Loop after the late stop |
|---|---|
| level `< h` | the same (its corners are ends of rows of level `< h` or lie in `O_h subset I_h`; `u = 1`, `w = 1`) |
| level `h`, all corners in `I_h` (the core face included) | the same under the tree gauge; conjugate under (T-comp) |
| level `h`, corners on both sides of the inner cut | conjugate by `u(x_1)` (`u = 1` at the corners in `I_h`) |
| level `q`, `h <= q <= t`, corners in the shells; mixed plaquettes at a face between shells | conjugate by `u(x_1)` |
| level `t`, corners on both sides of the outer face (old slot) | conjugate by `u(x_1)` (`u = 1` at the outer corners) |
| level `t`, no corner in `Lambda^pr`; any plaquette outside X | the same |
| level `> t` (later moments, X standing) | not read through `B_main` (Lemma 4.5 (b) of `cov-frames`) |

In every line the answer to item 4 is **yes**: the loop changes at most by conjugation. The lines of
`cov-frames` that depend on (TG) — section 0 item 3, the table row "late stop", Lemma 4.3 (c), section 6
row "late stop", section 7 item 1 — hold with "given (TG)" deleted and "core face" replaced by "inner
cut `dI_h`". The set "tested plaquettes of levels `h, ..., t` with a corner in `Lambda^pr minus G_h`" that
`cov-frames` names as at stake is covered: those with all corners in `I_h` keep their loop, the others
are conjugated.

## 6. What a checker should test first

1. (T-cut) is quoted from a passage on the reference integral of a late last-shell drop-out, and it
   names "the compensating change of (4c)", not the tree. For the tree itself the action on the
   crossing links rests on Lemma 3 with (T-inv) (Bałaban's statement of invariance) and on the form of
   Y 71421. If a checker reads Y's tree gauge as the action on `B_0` alone, Remark 3.1 gives the row and
   the two values; the weak form would then fail exactly at the tested level-h plaquettes with an edge
   across `dI_h`, and nowhere else (Theorem 4 for the other rows does not use (T-cut)). I do not hold
   this reading: under it the integrand before and after would differ.
2. Lemma 2 uses `h + 1 <= k_0` (so `Z''_{h+1} = H_{h+1}^{[3 a_{h+1}]}`) and `t - 1 > h`; both from `h < k_0 <= t - 2`
   (`cov-x` 2.1).
3. (T-comp): I did not rebuild the compensating gauge; only its class is used.

RESULT: (TG) is proved in the form (TG*): at a late stop the tree gauge is V -> u . V for one function u of the node, unit at the root, outside Lambda^pr and on the inner cut box I_h = H_{h+1}^{[a_{h+1}]}, and every determining row with an end at a moved node (inside a shell, across a face between shells, across the outer face in the old slot, across the inner cut) changes by u at its ends; so every tested loop changes at most by conjugation at a late stop (yes for each kind), B is empty, and Lemma 4.3 (c) of cov-frames holds without hypothesis. Correction: the inner boundary of the gauge is the inner cut, one coarse cell outside the hull of the core, not the core face; rows across the core face are not moved. Open: the clauses (T-node), (T-B0), (T-tree), (T-cut), (T-inv), (T-comp) are read from Y and Bałaban, not rebuilt; the action on the rows across the inner cut rests on (T-cut) and on Lemma 3 with the invariance (T-inv); no check by another model.
