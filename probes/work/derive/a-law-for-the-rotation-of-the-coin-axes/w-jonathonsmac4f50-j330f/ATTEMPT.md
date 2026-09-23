# A law for the rotation of the coin axes — attempt 2

Worker `w-jonathonsmac4f50-j330f`, model `claude-opus-5-5`. Task `J:derive:a-law-for-the-rotation-of-the-coin-axes:a2`.

**Provenance.** Blocks 54 and 62 to 65 (#8570, #8592, #8593, #8595, #8596) were written by the same model family (Claude Opus). They are open and unrefereed; I restate what I use. The referee should come from another family. No attempt had been delivered at claim time.

**Relation to block 65 (#8596).** Block 65 appeared after this task was written. It treats (a) to (c) at **first order around the identity frame**. Its scope explicitly does not claim "a walk blind beyond first order or around a frame that is not the identity (that needs a rotation carried along each bond, not constructed)". This attempt constructs that object and works **to all orders, for every frame**. My plan was fixed before reading block 65; I read it to place the result.

**Scope.** This works within the supplied clauses of blocks 54 and 62. Nothing is adopted. The one-site algebra (parked decision 4) is untouched: every object below acts on the existing qubit coin. No gravitational claim is made. The comparator (tetrads, spin connections, Belinfante, Einstein–Cartan) is named for orientation only.

## 1. The exact statement attempted

**Setting.**
- Block 62's generator is `H[E] = (1/2) Σ_j {E^j(x)·σ, S_j}`, with `S_j = (T_j − T_j†)/(2i)`.
- Equivalently, bond `b = (x, y = x + e_j)` carries `ψ_x† (B_b/(2i)) ψ_y + h.c.` with `B_b = Ē_b·σ` and `Ē_b = (E^j(x) + E^j(y))/2`.
- A local coin rotation is `U(x) ∈ SU(2)`, with `R(x)` defined by `U(v·σ)U† = (Rv)·σ`.

**(a) Not a conjugation (PROVED; CHECKED 1.1–1.3).**
- `U H[E] U†` has bond matrix `U_x (Ē·σ) U_y†`.
- It differs from `H[RE]`'s bond matrix by `(1/2)[U_x (E_x·σ)(U_y† − U_x†) + (U_x − U_y)(E_y·σ) U_y†]`: a coupling to the differences of `U` along the bond, exact to all orders.
- The transformed bond matrix has a coin-scalar part `−i (R_x Ē)·w`, where `w` is the vector part of `U_x U_y†`. No frame generator has one, so `U H[E] U†` is not `H[E']` for any `E'`.
- At first order this is block 65 T1: the bond-averaged frame rotation plus the twist hop `(i/2)(θ_y − θ_x)_j`.

**(b) The object that restores the symmetry (PROVED; CHECKED 2.1–2.4).**
- An `SU(2)` link `W_b` on each bond, with bond matrix `B_b = (1/2)(E_x·σ W_b + W_b E_y·σ)`, makes `ψ → Uψ`, `E → RE`, `W_b → U_x W_b U_y†` an exact symmetry.
- It reduces to block 62 at `W = 1`.
- No generator built from the frame alone is covariant: `U = −1` rotates nothing but flips every bond matrix.
- Given a lift sign at each site (a unitary `ψ_x → ±ψ_x`), the links the frame can fix are exactly `W_b = Û_x f(S_x, S_y) Û_y†`, with `E = R_E S` the polar decomposition and `f` any rotation-invariant rule on the two stretches.
- With `f = 1` (flat), `H[E, W(E)] = Û H[S, 1] Û†`: **the walker sees only `S = √g`**.
- Links with holonomy need a supplied `f` or a new field. The comparator's connection is fixed by the tetrad; here nothing but the flat part is.

**(c) The torque identity (PROVED; CHECKED 3.1–3.6).** For every state, frame and link field, at every site `x` and axis `c`:

`(Σ_j E^j × Θ^j)_c(x) + Λ_c(x) = (1/2) d⟨ψ†σ_cψ⟩(x)/dt`,

where `Θ_a^j(x) = ∂⟨H⟩/∂E_a^j(x)` and `Λ_c(x)` is the links' response to a rotation at `x`. On stationary states the frame torque therefore vanishes iff `Λ` does:
- with `W = 1` (block 62) it does not;
- with flat links fixed by the frame, the total torque vanishes;
- with links as a field in equilibrium under an energy that is invariant by itself (e.g. plaquettes), the frame torque vanishes.

## 2. Steps

### Step 1 — (a) (PROVED; CHECKED 1.1–1.3)
- **The transformed bond matrix.** `(U H U† ψ)_x` contains `U_x (B_b/(2i)) U_y† ψ_y`, so the bond matrix becomes `U_x (Ē·σ) U_y†`. `H[RE]` has `((R_x E_x + R_y E_y)/2)·σ = (1/2)(U_x E_x·σ U_x† + U_y E_y·σ U_y†)`. Subtracting gives the stated extra term (1.1). It vanishes for every `E` iff `U_x = U_y` on every bond, that is, for a uniform rotation (block 62 T1).
- **The coin-scalar part.** Write `W = U_x U_y† = w₀ − i w·σ` and `n = R_x Ē`. Then `U_x (Ē·σ) U_y† = (n·σ) W = w₀ n·σ + (n × w)·σ − i (n·w)`. The scalar `−i(n·w)` gives the real, coin-independent hop `−(n·w)/2` on the bond. Frame bond matrices are traceless. So no `E'` gives `U H[E] U†` unless `n·w = 0` on every bond (1.2: an exact instance has trace `15724i/5859`).
- **First order (1.3).** With `U = 1 − (i/2)θ·σ + O(θ²)`: `U_x σ_j U_y† = σ_j + ((θ_x + θ_y)/2 × e_j)·σ + (i/2)(θ_y − θ_x)_j + O(θ²)`. This is block 65 T1's frame rotation and twist hop.

### Step 2 — (b) (PROVED; CHECKED 2.1–2.4)

**2.1 Covariance.**
- `B[R_x E_x, R_y E_y, U_x W U_y†] = (1/2)(U_x E_x·σ U_x† U_x W U_y† + U_x W U_y† U_y E_y·σ U_y†) = U_x B U_y†`.
- The generator `Σ_b ψ_x†(B_b/(2i))ψ_y + h.c.` is hermitian and nearest-neighbour.
- Its bond matrices transform as `U_x · U_y†`, so `H[RE, UWU†] = U H[E, W] U†` exactly. At `W = 1` it is block 62's generator (2.2).

**2.2 A link is needed (PROVED).**
- Suppose the bond matrix were a function `F(E_x, E_y)` of the frame alone. `U_x = −1` gives `R_x = 1`, so covariance forces `F = −F`, hence `F = 0`.
- So local `SU(2)` covariance needs a bond field transforming as `U_x · U_y†` (or a spinor-valued site field, which the task does not ask for).
- An `SU(2)` link is the smallest such object: 3 numbers per bond.

**2.3 What the frame can fix (PROVED; CHECKED 2.3, 2.4).**
- Let each frame `E(x)` (the 3 × 3 matrix with columns `E^j`) be invertible, with polar decomposition `E = R_E S`, `S = √(EᵀE) = √g`.
- Choose a lift `Û_x` of `R_E(x)`. The choice is a sign per site, the unitary `ψ_x → ±ψ_x`, which leaves the spectrum unchanged (2.4).
- *Classification.* Let `W_b = F(E_x, E_y)` be covariant for this lift. Put `f := Û_x† W_b Û_y`. Covariance makes `f` invariant under independent rotations at both ends. The orbits of `(E_x, E_y)` are labelled by `(S_x, S_y)`, since the polar decomposition is unique. So `f = f(S_x, S_y)` and `W_b = Û_x f(S_x, S_y) Û_y†`.
- *The flat choice `f = 1`.* Bond by bond, `B = Û_x B[S_x, S_y, 1] Û_y†` (2.3). So `H[E, W(E)] = Û H[S, 1] Û†` (checked on the `4³` torus in 3.4 with `S = 1`). The frame's rotation part is invisible, and the walker sees only `√g`.
- *Holonomy.* Around a plaquette it is `Û_x (f f f f) Û_x†`. Curvature needs `f ≠ 1`, that is, a supplied rule on the stretches (the lattice analogue of a torsion-free condition, not constructed) or a new field.

### Step 3 — (c) (PROVED; CHECKED 3.1–3.6)

**3.1 The identity.**
- Let `G = σ_c/2` at site `x`, and `U = e^{−iαG}`.
- By 2.1, `H[R(U)E, W^U] = U H U†`. Differentiate `⟨ψ|H[R(U)E, W^U]|ψ⟩` at `α = 0`.
- The right side gives `i⟨[H, G]⟩ = d⟨G⟩/dt`.
- The left side is the sum of two responses:
  - the frame's, `Σ_j Θ^j·(e_c × E^j)(x) = (Σ_j E^j × Θ^j)_c(x)`;
  - the links', `Λ_c(x)`: `W_b → −(i/2)σ_c W_b` on bonds leaving `x` and `W_b → (i/2)W_b σ_c` on bonds entering `x`.
- This holds for every state, frame and link field. It is checked exactly on a `3³` torus with random rational frames, rational unit-quaternion links and Gaussian-rational states: 81 identities, every term non-zero (3.1).

**3.2 With `W = 1` (block 62).**
- `Λ_c` is the twist-hop bond term of blocks 63 and 65.
- On the exactly stationary state of the `4³` torus, `Σ_j i^{x_j} c_j` with `c = (1,1), (1,i), (1,0)` and energy `+1` (3.2), the frame torque is non-zero at 136 of 192 (site, axis) pairs and equals `−Λ` (3.3). This is block 62 N1.2's non-zero antisymmetric response, now with its exact partner.

**3.3 Flat links fixed by the frame.**
- Rotating `E` at `x` moves `W(E)` by exactly the gauge variation, so the **total** response is the left side of 3.1. It vanishes on stationary states.
- Checked with `E = R_E(x)` random rational rotations and the state `Ûψ₀`: an exact eigenstate (3.4); the total torque is 0 at all 192 pairs, while the frame part alone is non-zero at 180 (3.5).

**3.4 Links as a field.**
- Supply a link energy `F_W` invariant under `W_b → U_x W_b U_y†` alone, for instance `Σ_p Re tr W_p` (checked invariant under an exact finite local rotation, 3.6). Supply also the rule that the links sit at equilibrium, `∂(⟨H⟩ + F_W)/∂W = 0` along `SU(2)`.
- Then `Λ_c(⟨H⟩) = −Λ_c(F_W) = 0`, since `F_W` is invariant.
- So on stationary states `(Σ_j E^j × Θ^j)_c = 0` at every site. **The antisymmetric frame response vanishes, for every frame, to all orders.**

**3.5 What would have to be supplied, in order of economy.**
1. A lift sign per site (unitarily trivial), plus links fixed by the frame with `f = 1`. This costs nothing new. The frame's rotation part then becomes unobservable, and the walker sees only the metric through `√g`.
2. A rule `f(S_x, S_y)` for the stretches, if a connection with holonomy is wanted from the frame alone.
3. Links as an independent field (3 numbers per bond) with an energy of their own and an equilibrium rule.

None is adopted.

## 3. Where the route stops

There is no failing step. Not done:
- a lattice rule fixing `f` from the stretches (a discrete torsion-free condition);
- block 64 T5's torque, which belongs to a rotation of a site's bonds, not of its coin axes;
- the dynamics of the links;
- how the six symmetric numbers on the bonds and the three rotations on the sites combine (the sibling problem "one set of variables").

## 4. What would finish it

1. A discrete torsion-free condition giving `f(S_x, S_y)` at nearest-neighbour range, and the curvature it carries around plaquettes, compared with block 60's curvature member.
2. The static law of links in equilibrium with the walker's link current. Step 3.4 shows the frame torque then vanishes; what the links look like around a source is not computed.
3. An owner's decision between the three supplements of 3.5.
