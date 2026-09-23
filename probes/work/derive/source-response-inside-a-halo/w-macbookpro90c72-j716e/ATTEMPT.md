# J:derive:source-response-inside-a-halo:a5

Worker `w-macbookpro90c72-j716e` (claude-opus-5-5). This is attempt 5 of 5. I formed my plan before reading attempt a3 (`w-jonathonsmac4f50-jf032`, claude-opus-5, unrefereed); it is the only earlier attempt with files.

**Overlap with a3.** a3 found:
- the first-order drift of a free record under heat-bath acceptance;
- that it is negative at the neutral scale, which refutes the unit's part (b);
- the reversal scale `c*`;
- (c) and (d) by scaling, with a capture constant `κ`.

My first-order heat-bath formula agrees with a3's closed form at all four triples. **New here:**
1. the dependence on the acceptance, which block 39 leaves free;
2. all orders in the gas density;
3. an exact formation moment for part (c);
4. (d) re-read in that light.

Definitions come from blocks 39, 40 and 41 (open PRs #8530, #8546, #8547) and the unit text.

## (1) Exact statement

### The model

- **Weights (blocks 39–41).** A site is empty or holds one record, whose content is one of six axes. A record–record bond weighs `W = cω`, with `ω = p, q, r` for equal, opposite and orthogonal contents; a bond with an empty end weighs 1.
- **Transit (block 39).** Each bond with exactly one occupied end is visited at rate 1. The record moves with probability `A(w_x, w_y)`, where `w_x` and `w_y` are the products of its pair weights at `x` and at `y`. Any `A` with `A(w_x, w_y)/A(w_y, w_x) = w_y/w_x` is admitted; heat bath `w_y/(w_x + w_y)` and Metropolis `min(1, w_y/w_x)` are two such.
- **Gas.** This is an assumption, stated plainly. Sites are independent, with occupancy `ρ(v) = ρ₀ + g v_x`, and contents are uniform on the six axes and independent of occupancy. It is an imposed non-equilibrium product state, not the halo's own correlated state.
- **Drift.** The instantaneous mean velocity of a test record at 0 is `v = Σ_e e (1 − ρ(e)) E[A(w_x, w_y)]`.

### (a) The drift

1. **First order in the density, any acceptance:**

   `v/g = 12 Ā_in − 2 Ā_out − 12 A₁₁`, with `A₁₁ = A(1,1)`, `Ā_in = E_s A(1, W)` and `Ā_out = E_s A(W, 1)`.

   The `−2A₁₁` part is the blocking of the target.
   - **Heat bath:** `14δ − 1`, with `δ = E[(W−1)/(2(W+1))]`. This is a3's closed form: −52/45 at (3,1,2), −21002/9207, −13866/12455, −79/72.
   - **Metropolis:** −26/9, −3337/504, −974/345, −284/105. That is −1.44 to −3.31 per free hop rate, against −2.19 to −4.56 for heat bath.
2. **The sign above the neutral scale depends on the acceptance.**
   - Heat bath turns up the gradient above `c*` = 0.702965, 0.597174, 0.361617, 0.275496, which is 1.38–2.09 times `c₀`.
   - **Metropolis never does.** There `Ā_in = E min(1, W) ≤ 1 = A₁₁`, so `v/g ≤ −2E min(1, 1/W) < 0` at every `c`.

   So "drift towards higher density" is not a consequence of the static law. It is decided by the kinetic rule.
3. **All orders in the density, first order in `g`.** `v/g` is an exact polynomial in `ρ₀`, of degree 9 or 10:
   - (3,1,2): `−52/45 + (317/1755)ρ₀ + …`;
   - (12,1,2): `−2.2811 + 2.7325ρ₀ + …`.

   At the neutral scale it stays negative on all of `(0,1)`, for all four triples, under both acceptances. The down-gradient sign survives to clumping densities (block 39's onset is near 0.3) — within the independent-site gas.

**(b)** A single test record does **not** have zero drift at the neutral scale; it drifts down the gradient (a3). The first non-vanishing order is the first: blocking gives `−2A₁₁`, and the weight asymmetry adds a term of the same sign at `c₀`.

**(c) Accretion by formation at `c₀`.** Take a held cube of side `m` (records fixed).
- Every site in its first shell has exactly one cube neighbour.
- At `c₀` a row of `W` sums to 6, and each independent gas neighbour multiplies `Z` by `E_s W(a, s) = 1`, so `E[Z] = 6` at every shell site and every gas density. A site forms only when empty, at rate `z Z (1 − ρ(x))` on average.
- The first moment of the formation rate is therefore exactly `d(Σx)/dt = −z g m²(m+1)(5m+1)`.
- If the formed records join the lump, its centre moves at `−z g (m+1)(5m+1)/m`: **down** the gradient, about `−5zgm` for large `m`.

This mechanism opposes a3's capture model (`+κgm/2`). The net sign depends on whether arriving records are retained, which at `c₀` happens only where the lump's surface closes a cycle.

**(d) B inside A's halo.** Block 41's halo is `u = Q_A G/κ`, and `G ≈ 1/(4πR)` gives a gradient of magnitude `Q_A/(4πκR²)` at `B`. With (a) and (c), `v_B = −K_B Q_A/(4πκR²)` along `R̂` (away from A), where `K_B > 0` at `c₀`:
- `K_B = |v/g|` for a free record;
- `K_B = z(m+1)(5m+1)/m` for a lump growing by formation alone.

So the law is **repulsive** at the neutral scale, and goes as one over `R²`. Because `v_B ∝ Q_A K_B` and `v_A ∝ Q_B K_A`, it is symmetric only if production is proportional to the response for every body. The coefficient's sign, and even its existence above `c₀`, depends on the acceptance and on the retention rule.

**It is not a force law with inertia.** The velocity is set by the local gradient, with no memory. Inertia needs a conserved momentum-like density, and block 41 (1) says the occupancy is the only local additive invariant. That would be new content, not a consequence.

## (2) Steps

1. **PROVED (first-order formula).**
   - To first order only one gas record matters.
   - The sets `N(0)\{e}` and `N(e)\{0}` are disjoint on `Z³`: `x` and `y` have no common neighbours.
   - `Σ` over `N(e)\{0}` of `ρ` is `5ρ₀ + 6g e_x`, and over `N(0)\{e}` it is `5ρ₀ − g e_x`.
   - Summing `e_x(·)` gives the formula.
   - **CHECKED (A1):** exactly, against the all-orders polynomial at `ρ₀ = 0` and against a3's values.

2. **PROVED (Metropolis never reverses; the heat-bath reversal).** See above. **CHECKED (A2):** a3's `c*` values for heat bath; the Metropolis coefficient is negative for `c` from 0.001 to `10⁶`.

3. **PROVED (all orders in density).**
   - `w_x` depends only on the number of gas records on `N(0)\{e}` and on their content classes (1, 1, 4 of 6); likewise `w_y` on `N(e)\{0}`.
   - Hence `E[A] = Σ_{n_x, n_y} P_X(n_x) P_Y(n_y) Ā(n_x, n_y)`, with Poisson-binomial `P` from `Π(1 − ρ_v + ρ_v t)` and `Ā` by exact multinomial averaging.
   - **CHECKED (B1):** sympy, exact rationals.
   - **CHECKED (C1):** an explicit Möbius expansion over every one- and two-record configuration of the 24 sites that touch a hop reproduces the first two coefficients, −52/45 and 317/1755.

4. **PROVED (c).** See above. **CHECKED (D1):** the general symbolic sum, and explicit shells for `m = 1..4`, confirming one cube neighbour per shell site.

5. **DERIVED (d).** From (a), (c) and block 41 (5), as stated.

### ASSUMED

- The independent-site gas, stated plainly.
- For (c): that formed shell records join the lump.
- For (d): block 41's halo form and its `κ`.

## (3) Where the route fails

- **The unit's part (b) is false.** The drift at `c₀` is nonzero and negative, as a3 found.
- **"Up the gradient" (part (a)) is not decided by the static law.** One admissible acceptance (heat bath) reverses above `c*`; another (Metropolis) never does.
- **Accretion (c) has two first-order mechanisms of opposite sign:** formation blocking (down, exact here) and capture (up, a3's model). Retention at `c₀` needs cycles, and is not computed.
- **Not done:** bound clusters (a3's open item). A cluster bound only by cycles at `c₀` has no distinguished bound state to average over.

## (4) What would finish it

- A clause that fixes the acceptance, or a physical reason to prefer one.
- A retention rule at the lump's surface, which would give the net sign of (c).
- The drift in block 41's actual correlated halo rather than an imposed product state.
- Another model family's check. blocks 39–41, a3 and this attempt are one family.
