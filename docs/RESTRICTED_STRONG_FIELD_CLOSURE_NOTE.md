# Restricted Static-Conformal Finite-Box Closure on the `O_h` Shell Class

**Date:** 2026-04-13; self-contained arbitrary-source repair 2026-07-12
**Type:** bounded_theorem
**Claim boundary:** exact finite-dimensional closure of the scalar
Hamiltonian-plus-static-trace equation system on the full local `O_h`-invariant
seven-star source space. The theorem does not derive a physical gravity action
or stress tensor from the framework axioms and is not full nonlinear GR.
**Status authority:** independent audit lane only. This source note proposes no
audit verdict.
**Primary runner:**
[`frontier_restricted_strong_field_closure_packet.py`](../scripts/frontier_restricted_strong_field_closure_packet.py)

## The theorem

Let `V` be the interior of the centered `15^3` box with zero Dirichlet outer
boundary, and let

```text
H = 6 I - A
```

be its nearest-neighbor negative lattice Laplacian. Let `P : R^7 -> R^V`
inject the centered seven-site star

```text
S = {0, +/-e_x, +/-e_y, +/-e_z}.
```

The complete `O_h`-invariant source subspace on `S` is

```text
q = (q_0, q_s, q_s, q_s, q_s, q_s, q_s),
```

with independent coefficients `(q_0,q_s)`. For any such `q`, define the
microscopic field by the independent source equation

```text
H phi = P q.                                                (1)
```

Fix `R=4`, let `Pi` set a field to zero on `r <= R`, and construct

```text
phi_ext = Pi phi,
sigma = H phi_ext.                                         (2)
```

Assume only the nondegenerate bridge-domain condition

```text
||phi_ext||_infinity < 1.                                  (3)
```

Then all of the following are consequences, not additional fitted inputs.

1. `sigma` is supported on the nearest-neighbor sewing band `3 < r <= 5`,
   carries total charge `sum sigma = sum q`, and is `O_h` invariant.
2. The two affine Dirichlet problems

   ```text
   H(psi-1) = sigma,       H(chi-1) = -sigma               (4)
   ```

   have the unique solution

   ```text
   psi = 1 + phi_ext,      chi = 1 - phi_ext.              (5)
   ```

   Thus `alpha = chi/psi` is also uniquely fixed and nonzero.
3. On the restricted static-conformal finite-lattice sector

   ```text
   H(psi-1) =  2 pi psi^5 rho,
   H(chi-1) = -2 pi alpha psi^5 (rho + 2 S),                (6)
   ```

   the source readouts are the unique pointwise solution

   ```text
   rho = sigma / (2 pi psi^5),
   S   = 0.5 rho (1/alpha - 1).                            (7)
   ```

4. Let `Gamma` be the first exterior layer adjacent to `r <= R`, let `B` be
   the remaining exterior bulk, and retain the zero outer boundary. With the
   corresponding block decomposition of `H`, define

   ```text
   Lambda = H_GG - H_GB H_BB^-1 H_BG.                      (8)
   ```

   If

   ```text
   f = phi_ext|Gamma,       j = sigma|Gamma,                (9)
   ```

   then `j` is fixed by the microscopic source construction before any
   boundary variation is performed, and

   ```text
   Lambda f = j.                                           (10)
   ```

   Consequently `f` is the unique global minimizer of

   ```text
   I(g;j) = 0.5 g^T Lambda g - j^T g.                      (11)
   ```

This is a genuine algebraic closure over the independent inputs `(H,P,q,Pi)`
and the explicitly stated restricted sector (6). It is not a status-package
declaration and it does not use the formerly scanned benchmark coefficients.

## Proof from the finite-box primitives

### 1. Positivity and the independent microscopic solve

For a zero-boundary vector `v`, the graph energy identity gives

```text
v^T H v
  = sum_{unordered interior edges {x,y}} (v_x-v_y)^2
    + sum_{interior-to-boundary edges (x,b)} v_x^2.         (12)
```

Every term is nonnegative. If the sum is zero, `v` is constant along the
connected interior and zero at every site adjacent to the boundary, hence
`v=0`. Therefore `H` is symmetric positive definite. Equation (1) has one and
only one solution for every `(q_0,q_s)`.

No numerical source profile has been selected here. The center orbit and the
six-arm orbit form a basis of the full invariant source space, so the theorem
holds for arbitrary signed linear combinations of those two basis vectors.

### 2. Shell localization and charge

Away from the seven-site source, (1) says that `phi` is lattice harmonic.
Inside `r <= R`, `phi_ext` is zero; outside that set, it equals `phi`. Since
`H` has nearest-neighbor range, `H phi_ext` can be nonzero only at cells within
one edge of the cutoff interface. On this centered lattice that support is
exactly contained in

```text
R-1 < r <= R+1,  or  3 < r <= 5.                           (13)
```

To see charge preservation, write `d=phi-phi_ext`. The field `d` is supported
strictly away from the outer boundary. Summing a graph Laplacian of such a
compactly supported field cancels edge by edge, so `sum H d=0`. Hence

```text
sum sigma = sum H(phi-d) = sum H phi = sum Pq = sum q.      (14)
```

Signed coordinate permutations preserve the centered box, the star, the
cutoff, and nearest-neighbor adjacency. Thus their actions commute with `H`,
`P`, and `Pi`. Uniqueness of (1) then propagates `O_h` invariance from `q` to
`phi`, `phi_ext`, and `sigma`.

### 3. The bridge is solved, not assigned

Let `u` be obtained by solving the independently sourced Dirichlet problem

```text
H u = sigma.                                               (15)
```

Equation (2) shows that `phi_ext` satisfies the same equation and the same
zero boundary condition. Positive definiteness of `H` gives

```text
u = H^-1 sigma = phi_ext.                                  (16)
```

Solving the two affine problems (4) therefore gives (5). Condition (3) makes
both factors strictly positive, so division by `psi` and `alpha` below is
well-defined. This is the exact scope of the phrase “same-source bridge” in
this theorem: the two signed affine channels are the unique solutions sourced
by the already constructed pair `(+sigma,-sigma)`.

### 4. Explicit continuum equations and finite-lattice sector rule

The continuum equations used here are supplied GR starting equations, not
consequences of the four framework axioms. Their conformal reduction can be
derived without importing a target value. Start with the time-symmetric
conformally flat static ansatz

```text
ds^2 = -alpha^2 dt^2 + psi^4 delta_ij dx^i dx^j,
K_ij = 0,
rho = T_nn,
S = gamma^ij T_ij.                                        (17)
```

The Christoffel symbols of `gamma_ij=psi^4 delta_ij` are

```text
Gamma^k_ij = 2 psi^-1
  (delta^k_i partial_j psi + delta^k_j partial_i psi
   - delta_ij partial^k psi).                              (18)
```

Direct contraction gives

```text
R^(3) = -8 psi^-5 Delta psi.                               (19)
```

The time-symmetric Hamiltonian equation `R^(3)=16 pi rho` therefore reduces
to

```text
-Delta psi = 2 pi psi^5 rho.                               (20)
```

The static trace evolution equation is

```text
D^2 alpha = 4 pi alpha (rho+S).                            (21)
```

For the same conformal metric,

```text
D^2 alpha = psi^-4
  (Delta alpha + 2 psi^-1 grad(psi).grad(alpha)).           (22)
```

Set `chi=alpha psi`. Combining (20)--(22) yields

```text
Delta chi
 = alpha Delta psi + psi Delta alpha
   + 2 grad(alpha).grad(psi)
 = 2 pi alpha psi^5 (rho+2S),                              (23)
```

or

```text
-Delta chi = -2 pi alpha psi^5 (rho+2S).                   (24)
```

Equation (6) is a supplied, non-chain-satisfying finite-lattice sector rule:
it uses the positive graph operator `H` for `-Delta` on affine deviations from
the unit outer boundary. The runner and theorem do not claim that this rule,
the Einstein equations, or the physical identification of `(rho,S)` follows
from the framework's four minimal axioms. They are explicit inputs bounding
this sector.

Within that sector, however, the inverse scalar-equation problem is not
definitional freedom. Substitution of the independently constructed bridge
into (6) gives

```text
sigma = 2 pi psi^5 rho,
sigma = 2 pi alpha psi^5 (rho+2S),                         (25)
```

and nondegeneracy makes the triangular solution (7) unique. There is no free
shell density, stress trace, normalization, branch selector, or fitted target
left in this solve.

### 5. The Schur source is fixed before trace variation

Restrict `phi_ext` to the exterior variables `(f,u_B)`. The shell source
vanishes on the harmonic bulk `B`, so the bulk block of (2) is

```text
H_BG f + H_BB u_B = 0,
u_B = -H_BB^-1 H_BG f.                                    (26)
```

The trace block uses the source already constructed in (2):

```text
j := sigma|Gamma
   = H_GG f + H_GB u_B
   = (H_GG - H_GB H_BB^-1 H_BG) f
   = Lambda f.                                             (27)
```

This order matters. The proof does not define `j=Lambda f` to force a desired
stationary point; it restricts the previously computed microscopic source
`sigma` and then proves equality (27).

Because `H` is positive definite, its principal block `H_BB` and Schur
complement `Lambda` are positive definite. For any trial trace `g=f+delta`,

```text
I(g;j)-I(f;j) = 0.5 delta^T Lambda delta,                  (28)
```

which is strictly positive for every nonzero `delta`. Thus the microscopic
source selects `f` uniquely.

## Self-contained runner certificate

Run

```bash
python3 scripts/frontier_restricted_strong_field_closure_packet.py
```

The primary runner constructs every load-bearing matrix and source locally.
It imports `numpy` and `scipy`, but no frontier/helper module. It checks the
two basis directions spanning the invariant source space and three signed
mixtures. The current result is

```text
finite H:       min eigenvalue = 1.504325269e-01
Schur Lambda:   trace=186, bulk=1754,
                min eigenvalue = 2.045426696e+00
shell band:     [3.162278,5.000000]
max charge error                         5.551e-17
max bridge reconstruction error          3.469e-18
max static-conformal residual            1.908e-17
max harmonic-bulk source                 1.041e-17
max microscopic-source/Schur-flux error  6.939e-18
max Schur minimizer reconstruction error 4.554e-18
PASS=13 FAIL=0 TOTAL=13
```

The earlier component runners remain useful regression probes of the old
scanned benchmark and broader finite-rank examples, but none is a proof input
to this theorem.

## Claim-state firewall

What is closed here is narrow and exact:

```text
arbitrary local O_h source (q_0,q_s)
  -> unique microscopic field phi
  -> derived sewing source sigma
  -> unique signed affine bridge (psi,chi)
  -> unique inverse-equation readouts (rho,S) in the stated sector
  -> source-first Schur variational reduction with unique trace minimizer.
```

The following are not consequences of this theorem:

1. derivation of the Einstein equations or a physical stress tensor from the
   Lattice, Qubit, Admissibility, and Record axioms;
2. a tensor-valued or fully pointwise Einstein/Regge completion;
3. unrestricted non-`O_h` or continuum strong-field closure;
4. black-hole, horizon, echo, or other astrophysical consequences;
5. derivation of any formerly scanned benchmark source coefficients.

Accordingly, “strong-field” in the historical filename identifies the repo
lane. The auditable theorem in this note is the bounded finite-box
static-conformal closure stated above.
