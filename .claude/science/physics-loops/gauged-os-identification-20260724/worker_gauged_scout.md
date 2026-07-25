# Source scout — lifting the free 3+1 reflected-Gram theorem to a fixed gauge background

Worker report. Read against `origin/main` at `e6d1070adf`; all seven target files
in the worktree are byte-identical to `origin/main` (checked with `git diff --stat origin/main -- <file>`,
empty for all seven).

Nothing here sets, predicts, or reads an audit verdict. No repo file was edited.
Three throwaway probe scripts were written **outside the repo** in the session
scratchpad (`.../scratchpad/complex_hop_probe.py`, `gauged_hop_probe.py`,
`probe3.py`); they are scratch evidence for section (b), not repo runners and not
audit evidence.

**Headline for the supervisor, up front:**

1. The gauged reflected Gram is **not** already landed (section d). File 4 proves
   something structurally different: RP of an *observable* Gram *after* Haar
   integration, and it explicitly disclaims a fixed-holonomy theorem and any
   transfer operator. The proposed lift is not redundant.
2. The free note's operator identity **does not survive verbatim** for a complex
   hop, and the note says so itself in a parenthetical — but the parenthetical is
   **incomplete**: it repairs the frames and silently leaves Theorem 3's
   transfer intertwiner broken. Corrected statement: the Gram at background `U`
   is intertwined with the two-step transfer at `conj(U)`, not at `U`
   (section b, items B2/B3, numerically decisive).
3. A hidden hypothesis has to be added: the background must be **static**
   (time-independent spatial links in temporal gauge). At a time-dependent fixed
   background the reflected Gram is not even Hermitian, and its Hermitian part
   has a negative eigenvalue (section b, item B9).
4. Even fully repaired, the lift does **not** discharge the microcausality note's
   `Gamma(t[U])` open problem: it produces matrix elements, not the canonical
   creation intertwiner that note names as "the pin" (sections f, g).

---

## (a) The 07-12 free reflected-Gram note — verbatim theorem statements, carrier, hypotheses, open list

File: `docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md`
Runner (from its header, lines 7-8):
`scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.py`
Cached output (lines 9-10):
`logs/runner-cache/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.txt`

### a.1 Carrier, conventions, hypotheses (verbatim)

Scope sentence, lines 22-26:

> "This note closes that bridge for the free massive family at fixed lattice
> spacing on the **infinite temporal lattice** and a **finite even 3D spatial
> torus**."

Conditionality, lines 28-33:

> "The theorem is conditional on the CAR/Grassmann branch and on the displayed
> free staggered action. It does not select CAR, does not select the physical
> carrier or one taste, and does not recover the interacting Standard Model or
> GR. Barred-field reciprocal-pole/contact-term reconstruction, finite temporal
> thermal/image corrections, gauge interactions, and the continuum joint limit
> remain separate."

Setup, lines 52-76:

> "Let `h` be the one-particle space of the finite even spatial torus and let
>
> ```text
> H^dag=-H,             M>0,
> R=(M^2-H^2)^(1/2)>0,
> E=asinh R,
> Z=e^(-2E),            0<Z<I,
> B=(M+H)R^(-1).
> ```
>
> All functions are finite-dimensional spectral functions. Since `H` commutes
> with `R`,
>
> ```text
> B^dag B=(M-H)(M+H)R^(-2)=I,
> ```
>
> so `B` is unitary. On an eigenline `H=i lambda`, write
>
> ```text
> r=sqrt(M^2+lambda^2),
> e=asinh r,
> z=e^(-2e),
> b=(M+i lambda)/r,     |b|=1.
> ```"

**The reality hypothesis, verbatim, lines 78-85 — this is the single most
important paragraph in the file for this campaign:**

> "For the canonical free 3D staggered action, `H` is the spatial hop with the
> three staggered phases. The mode-level identities below need only finite
> dimension and `H^dag=-H`. The operator-level reflected-Gram identities
> additionally use that the hop is **real in the site basis** (`H*=H`, so
> complex conjugation maps `H=i lambda` eigenvectors to `H=-i lambda`
> eigenvectors); for a complex anti-Hermitian hop the same formulas hold with
> `H` replaced by `conj(H)` in the frames. The canonical torus supplies finite
> dimension, anti-Hermiticity, and realness."

The same condition is re-declared in the N3 phrase scan, line 441:

> "| real staggered hop (`H*=H`) | load-bearing carrier condition | required for
> the conjugate-eigenline operator binding; the canonical staggered hop is real,
> and a complex anti-Hermitian hop gets the `conj(H)` frames instead |"

Sign/reflection convention, lines 286-288:

> "Here reflection acts antimultiplicatively on Grassmann generators with the
> Osterwalder--Seiler sign convention `Theta(chi_t)=-bar-chi_(theta(t))`, as
> displayed in `scripts/mixed_os_transfer_representation_2026-05-30.py:241-263`."

The reflection itself is `theta(t)=-1-t` (line 107).

### a.2 Theorem statements, numbered as the note numbers them

**"### 1. Exact pole residue and reflected two-slice Gram"** (line 89). Lines 92-138:

> "In time-cell coordinates `(chi_even,chi_odd)` with coarse Bloch multiplier
> `zeta=e^{iQ}`, the same action has
>
> ```text
> D_lambda(zeta)
>  = [[M+i lambda,          (1-zeta^(-1))/2],
>     [(zeta-1)/2,          M-i lambda       ]],
>
> Delta_lambda(zeta)
>  = r^2+(2-zeta-zeta^(-1))/4
>  = -(zeta-z)(zeta-z^(-1))/(4 zeta).
> ```
>
> The inside pole is `z=e^{-2e}`. Taking the cell-separation-one Fourier
> coefficient of `D_lambda(zeta)^(-1)` and applying the Osterwalder-Seiler
> two-slice reflection `theta(t)=-1-t` gives the exact Gram on the block fields
> `(chi_0,chi_1)`:
>
> ```text
> K_lambda
>  = (2z/(1+z))
>    [[1,             sqrt(z) b],
>     [sqrt(z) b*,    z        ]]
>  = 2z v_lambda v_lambda^dag,
>
> v_lambda=(1+z)^(-1/2) [1, sqrt(z)b*]^T.
> ```
>
> Therefore
>
> ```text
> K_lambda>=0,
> rank K_lambda=1,
> spec K_lambda={0,2z},
> P_OS,lambda=K_lambda/(2z)=v_lambda v_lambda^dag.
> ```
>
> This proves analytically that the unrescaled two-time-cell convention has
> `c_block=2`, independent of mode and mass. Rescaling the block field by
> `1/sqrt(2)` removes the factor; it is a basis normalization, not a physical
> constant.
>
> At a separation of `n>=1` two-step cells, the same residue acquires
> `z^(n-1)`, hence
>
> ```text
> K_lambda,n=2 z^n P_OS,lambda.
> ```"

**"### 2. Basis-independent OS quotient and positive transfer"** (line 140). Lines 142-198:

> "Reading the reflected Gram as an operator kernel (row index = reflected
> first argument) places each mode Gram `K_lambda` on the **conjugate**
> carrier eigenline: the staggered hop is real, so complex conjugation maps
> an `H=i lambda` eigenvector to an `H=-i lambda` eigenvector, and
> `K((a,x),(b,y)) = G((t_b,y),(theta(t_a),x))` dresses `K_lambda` with the
> conjugated mode. On the eigenline `H=-i lambda` the unitary `B` acts as
> `b*`, so the support column `[1, sqrt(z) b*]^T` of `K_lambda` is exactly
> the value of the pole-frame isometry
>
> ```text
> U_pole = [ I ; Z^(1/2) B ] (I+Z)^(-1/2),
> U_pole^dag U_pole=I.
> ```
>
> Then the full reflected Grams are
>
> ```text
> P_OS=U_pole U_pole^dag,
> K_n=2 U_pole Z^n U_pole^dag.
> ```
>
> Equivalently, with the coisometry `W=U_pole^dag` and one-particle
> contraction `C=Z`,
>
> ```text
> K_n = 2 W^dag C^n W.
> ```
>
> The positive OS quotient map at one block is
>
> ```text
> A=sqrt(2) Z^(1/2) U_pole^dag,
> K_1=A^dag A.
> ```
>
> Its nullspace is exactly the orthogonal unphysical block-field combination;
> its rank equals `dim h`. The quotient isometrically identifies with `h` through
> `A`, and
>
> ```text
> K_n=A^dag Z^(n-1) A.
> ```
>
> Separately, `U_pole` is an orthonormal frame for the support of `K_1`, and
> the unweighted boundary-insertion frame `sqrt(2)U_pole^dag` sees the
> one-block transfer `Z`:
>
> ```text
> U_pole^dag P_OS U_pole=I,
> U_pole^dag (K_1/2) U_pole=Z.
> ```
>
> Thus the residue is not merely spectrally compatible with the transfer: it
> gives the exact OS support and quotient factorization. `P_OS` is a support
> projector of the reflected Gram, not a derivation of the original lattice
> fields' equal-time CAR anticommutator; that stronger claim requires the barred
> fields and contact terms left open below."

**"### 3. Pole, parity-image, and stable-transfer frames on the canonical 3D carrier"** (line 200). Lines 202-259:

> "The parity-image frame and normalized stable-transfer frame are
>
> ```text
> V = [ I ; Z^(1/2) B^dag ] (I+Z)^(-1/2),
> W_stable = [ Z^(1/2) ; B ] (I+Z)^(-1/2).
> ```
>
> For `T_2=T_even^dag T_even`,
>
> ```text
> T_2 W_stable = W_stable Z.
> ```
>
> The time-cell-to-transfer map of the preceding block now has the polar form
>
> ```text
> J_Z=diag(I,Z^(-1)),
> J_Z U_pole = W_stable Z^(-1/2).
> ```
>
> The operator reading of the reflected Gram conjugates the mode dressing
> (`H` to `-H` on mode labels), which is why the OS support frame is the
> pole frame `U_pole` containing `B`, while the parity-image frame `V`
> contains `B^dag`. On the canonical even staggered torus the parity
> involution
>
> ```text
> (Pi psi)(x)=(-1)^(x_1+x_2+x_3) psi(x)
> ```
>
> obeys `Pi H Pi=-H`, `Pi Z Pi=Z`, and `Pi B Pi=B^dag`. With
> `boldPi=diag(Pi,Pi)`,
>
> ```text
> V=boldPi U_pole Pi,
> ```
>
> so `V` is the OS support frame of the parity-transformed carrier, not of
> the carrier itself.
>
> The partial unitary
>
> ```text
> L=W_stable U_pole^dag
> ```
>
> maps the OS quotient onto the stable transfer space and intertwines
>
> ```text
> L (K_1/2) = T_2 L.
> ```
>
> This is the exact finite-`a` reflected-Gram/OS-quotient/stable-transfer
> identification on the actual free 3D staggered carrier, conditional on the CAR
> branch. The paired runner verifies these operator identities directly against
> a dense inverse of the actual 3+1 chain operator, where the conjugate-eigenline
> binding is decisive: the `V`-frame variant of the same formulas fails on the
> actual carrier by an order-`10^-2` residual."

**"### 4. Multitime Gaussian Wick hierarchy equals CAR-Fock exterior products"** (line 261). Lines 263-312:

> "Let `f_1,...,f_q` and `g_1,...,g_q` be arbitrary two-slice block one-particle
> vectors placed at arbitrary nonnegative positive block times `r_i` and `s_j`.
> Reflection makes the cell separation of the `(i,j)` pair
> `r_i+s_j+1`, so
>
> ```text
> K_ij=2 U_pole Z^(r_i+s_j+1) U_pole^dag
>     =A^dag Z^(r_i+s_j) A.
> ```
>
> Define the canonical OS quotient states
>
> ```text
> xi_i=Z^r_i A f_i,
> eta_j=Z^s_j A g_j.
> ```
>
> Then
>
> ```text
> <f_i,K_ij g_j>=<xi_i,eta_j>.
> ```
>
> [... OS sign convention paragraph ...]
>
> ```text
> G_Berezin=det[ <xi_i,eta_j> ]
>           =<xi_1 wedge ... wedge xi_q,
>              eta_1 wedge ... wedge eta_q>_Fock.
> ```
>
> This is the canonical OS-isometric quotient factorization. For two clusters at
> common block times `r` and `s`, it is equivalently a `q`-particle matrix element
> of `Gamma(Z)^(r+s)`. There is also a distinct but algebraically equivalent
> boundary-insertion normalization
>
> ```text
> phi_i=sqrt(2)U_pole^dag f_i,
> psi_j=sqrt(2)U_pole^dag g_j,
> <f_i,K_ij g_j>=<phi_i,Z^(r_i+s_j+1)psi_j>.
> ```
>
> The extra power of `Z` distinguishes this frame from the quotient map `A`.
> Thus every finite multitime reflected Wick Gram generated by the positive-time
> unbarred two-slice fields is exactly a CAR-Fock exterior inner product. The
> claim is algebraic for arbitrary finite `q`, not only the grades sampled by the
> runner."

**"### 5. Full 3D lift and multiplicity"** (line 314). Lines 316-329:

> "The canonical 3D spatial hop is normal and anti-Hermitian, so a unitary modal
> transform diagonalizes it. Applying the preceding identities per mode — with
> each mode Gram bound to the conjugate eigenline as in Theorem 2 — and
> conjugating back proves the full position-basis statement, including every
> cross-mode contraction. No one-spatial-axis assumption remains. The paired
> runner checks this lift both analytically and against a dense inverse of the
> actual 3+1 chain operator.
>
> For each reduced spatial momentum the staggered cell has dimension `8`; the
> OS projector, pole projector, and stable transfer projector therefore each
> have rank `8`. The algebraic rank is unconditional. Its reading as four tastes
> times two positive-energy spin states is conditional on the supplied
> CAR/Dirac interpretation; this note does not select that interpretation or a
> single taste."

Arena boundary (lines 333-339):

> "The theorem uses the vacuum/infinite temporal lattice, where the inside-pole
> residue is exact. On an open temporal chain of length `2N`, the central seam
> Gram converges exponentially to `K_lambda`; it is not exactly equal at finite
> `N` because of boundary images. On a finite temporal circle, thermal winding
> images similarly modify the vacuum Gram."

### a.3 Its own "Still open:" list, verbatim (lines 358-368)

> "Still open:
>
> - derivation or physical selection of the CAR/Grassmann branch, the staggered
>   carrier, and a taste/family rule;
> - reciprocal barred-field pole, contact/time-ordering terms, and a complete
>   all-field generating-functional identification beyond the positive-time
>   unbarred OS algebra proved here;
> - massless uniformity and infinite spatial-volume control;
> - interacting gauge-plus-fermion representation, renormalized SM continuum,
>   and anomaly/chirality/taste control;
> - dynamical geometry/GR and its joint compatibility with the matter limit."

And the honest-status closer, lines 572-577:

> "It does not derive the original fields' equal-time CAR anticommutator and does
> not close the reciprocal barred/contact all-field functional, select the
> physical category/carrier/taste, or establish the interacting SM/GR continuum."

### a.4 What the runner actually computes (relevant to (b))

`scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.py`:

- `spatial_hop_3d(L)` (lines 148-161) builds the hop with `eta = (-1) ** sum(x[:mu])`
  and **real** entries: `H[site, xp] += 0.5 * eta`, `H[site, xm] -= 0.5 * eta`.
  Dtype is complex but the matrix is real; every test in the file uses this one
  carrier.
- `test_actual_chain_operator_gram` (lines 362-433) is the load-bearing check. Its
  Gram extraction is `K[:, b*n3:(b+1)*n3] = X[tgt_row*n3:(tgt_row+1)*n3, :].T`
  (line 411) — an unconjugated **transpose** in the spatial index.
- Expected scorecard (note line 565): `SCORECARD: PASS=26 FAIL=0`.

---

## (b) THE CRITICAL AUDIT — every place reality of the hop is used

Method: I re-derived each step symbolically and then ran the note's own
construction with (i) a real antisymmetric hop, (ii) a generic complex
anti-Hermitian hop, and (iii) the actual gauged 3D staggered hop with random
`SU(3)` links at `L=2`, `N_c=3` (`n=24`), extracting the Gram from a dense
inverse of the actual chain operator exactly as the runner does. Numbers below
are from those scratch probes (open chain `Nt=20..24`, exponentially converged;
`M=0.7`/`0.8`; inf-norm residuals; signal scale is `O(1)`).

First, the structural fact that organises everything:

> The kernel reading `K((a,x),(b,y)) = G((t_b,y),(theta(t_a),x))` is a
> **spatial transpose**, not a complex conjugation. Every block of `G=D^{-1}` is
> a function of the single operator `h`, so `K_{ab} = g_{ab}(h)^T = g_{ab}(h^T)`,
> and `h^dag=-h` gives `h^T = -h^*= -conj(h)`.
> For the free carrier `conj(H)=H`, so transpose and "conjugate eigenline"
> coincide. For complex `h` they do not: `conj(h[U]) = h[conj(U)]` is the hop at
> the **complex-conjugate (anti-fundamental) background**.

Carrying this through the closed form gives, for any fixed static anti-Hermitian `h`,

```text
K_n = 2 U_pole[conj h] Z[conj h]^n U_pole[conj h]^dag,
U_pole[k] = [ I ; Z[k]^(1/2) B[k] ] (I+Z[k])^(-1/2),
B[k] = (M+k) R[k]^(-1),   R[k]=(M^2-k^2)^(1/2),   Z[k]=e^(-2 asinh R[k]).
```

which is the note's parenthetical, confirmed. The items below say which steps
need nothing, which need repair, and which break.

### B1. `B^dag B = I` (`B` unitary), `R>0`, `Z<I`, `Delta` factorization, residue — **survive verbatim**

Uses only `h^dag=-h` (hence `h` normal, `h^2` Hermitian, `M^2-h^2 >= M^2 > 0`)
and the commutation `[h,R]=0`. Nothing is transposed, no eigenbasis is chosen,
no symmetric-matrix or real-orthogonal diagonalization appears. The identity
`Z+Z^{-1} = 2+4R^2` (needed for `Delta_lambda(zeta) = -(zeta-z)(zeta-z^{-1})/(4 zeta)`)
is `2 cosh 2E = 2 + 4 sinh^2 E` with `sinh E = R`: pure spectral calculus over `C`.
Probe: `||B[conj h]^dag B[conj h] - I|| = 1.5e-14`, `||U_pole[conj h]^dag U_pole[conj h] - I|| = 1.6e-14`
at the gauged `SU(3)` carrier.

I also re-derived Theorem 1's closed form from the residue by hand and it is
correct: with `d = z - 1/z` the entry ratio forces `1 - z = 2 sqrt(z) r`, and
`2 e^{-E} sinh E = 1 - e^{-2E}` verifies it. `|b|=1` is `|M+i lambda| = r`. No
reality anywhere in Theorem 1.

### B2. Theorem 2's "conjugate-eigenline binding" — **stated reason is FALSE for complex `h`; the formula survives with `h -> conj(h)`**

The note's reason (line 143-147) is *"the staggered hop is real, so complex
conjugation maps an `H=i lambda` eigenvector to an `H=-i lambda` eigenvector"*.
For complex `h` that sentence is simply wrong: conjugation maps `h`-eigenvectors
to `conj(h)`-eigenvectors, and `conj(h)` is a **different operator**
(`||Z[conj h] - Z[h]|| = 3.9e-01` in the generic complex probe), even though the
two have the same spectrum (`|sort spec Z[conj h] - sort spec Z[h]| = 9.7e-17`,
forced by staggered parity `Pi h Pi = -h`).

What actually happens is the transpose, and it lands on `conj(h)`. Numbers:

| carrier | `||K_1 - 2 U_pole[h] Z[h] U_pole[h]^dag||` (note verbatim) | `||K_1 - 2 U_pole[conj h] Z[conj h] U_pole[conj h]^dag||` |
|---|---|---|
| real antisym `h`, n=6 | `5.25e-14` | `5.25e-14` (same object) |
| generic complex anti-Herm `h`, n=6 | **`9.46e-01`** | `2.59e-14` |
| gauged staggered `SU(3)`, `L=2`, `n=24` | **`1.01e+00`** | `3.63e-13` |

`n=2`: `||K_2 - 2 U_pole[conj h] Z[conj h]^2 U_pole[conj h]^dag|| = 1.40e-12` at
the gauged carrier. So `K_n = 2 W^dag C^n W`, `P_OS`, rank, `K_1 = A^dag A`,
`K_n = A^dag Z^{n-1} A` all survive **with every frame and every `Z` re-evaluated
at `conj(h)`**. Probe: `||K_1 - A^dag A|| = 3.6e-13`, `||K_2 - A^dag Z[conj h] A|| = 1.4e-12`,
`min sv(A) = 3.08e-01`, `rank K_1 = 24 = dim h` — with `A = sqrt(2) Z[conj h]^{1/2} U_pole[conj h]^dag`.

**Verdict: survives with modification.** The modification is not cosmetic — the
note's own displayed formula is *false* at a complex background by an O(1) amount.

### B3. Theorem 3's transfer intertwiner `L (K_1/2) = T_2 L` — **GENUINELY FAILS; the note's parenthetical does not repair it**

`T_2 = T_even^dag T_even` with `T_even = [[-2(M+h), I],[I,0]]` is built from `h`,
**not** from `conj(h)`. The Gram is built from `conj(h)`. So `L = W_stable[h] U_pole[h]^dag`
mixes two different backgrounds:

```text
L (K_1/2) = W_stable[h] Z[conj h] U_pole[conj h]^dag,
T_2 L     = W_stable[h] Z[h]      U_pole[conj h]^dag,
```

equal iff `Z[conj h] = Z[h]`, i.e. iff the background is `K`-real. Probe (generic
complex `h`):

```text
||L[h]      (K_1/2) - T_2[h]      L[h]||       = 5.39e-01     FAILS
||L[conj h] (K_1/2) - T_2[conj h] L[conj h]||  = 1.11e-14     holds
||T_2[conj h] - T_2[h]||                       = 1.19e+02
||T_2[conj h] - T_2[h]^T||                     = 0.00e+00     exact
```

So the correct gauged statement is: **the reflected Gram at background `U` is
intertwined with the two-step transfer at `conj(U)`, and `T_2[conj U] = T_2[U]^T`
exactly.** Same spectrum, different operator, related by an antiunitary.

This is a defect in the note's generalization clause (line 82-84): "the same
formulas hold with `H` replaced by `conj(H)` in the frames" repairs `U_pole`, `V`,
`W_stable`, `A`, `Z` — but `T_2` is not a frame, and Theorem 3's identity, the
polar relation `J_Z U_pole = W_stable Z^{-1/2}`, and the boundary-insertion
relation `U_pole^dag (K_1/2) U_pole = Z` all silently change background under it.
Anyone lifting this note must restate all three, or the lift ships a false
sentence.

Immediate consequence for the campaign: the object a fixed-background lift
naturally delivers is `t[conj U] = t[U]^T`, not `t[U]`. Either restrict to
`K`-real backgrounds (`conj U = U`) — which is exactly the class
`CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md:105-107`
already isolates — or supply an explicit antiunitary bookkeeping lemma.

### B4. Parity involution `Pi h Pi = -h`, `Pi B Pi = B^dag`, `V = boldPi U_pole Pi` — **survive verbatim, no reality used**

`Pi = (-1)^{x_1+x_2+x_3}` changes sign across every nearest-neighbour hop, so
`Pi h Pi = -h` for *any* link values; `Pi R Pi = R` follows; `Pi B Pi = B^dag`
follows because `B` and `R^{-1}` commute. Load-bearing hypothesis is the **even**
torus (so `(-1)^{|x|}` is well defined), not reality. Probe at the gauged `SU(3)`
carrier: `||Pi h Pi + h|| = 0.00e+00`, `||V[conj h] - boldPi U_pole[conj h] Pi|| = 1.02e-14`.
Caveat: the *statement* must be re-anchored at `conj(h)`, since that is where the
OS frame lives.

### B5. Theorem 4 (Wick determinant = exterior inner product) — **survives verbatim, no reality used**

The Berezin Gaussian determinant theorem and `det[<xi_i,eta_j>] = <wedge xi, wedge eta>`
are finite-dimensional linear algebra over `C`. Probe at the gauged `SU(3)`
carrier, degree 3, non-uniform block times `r=(0,1,2)`, `s=(2,1,0)`:
`||multitime Berezin pairs - <xi,eta>|| = 6.36e-15`,
`|det(pairs) - <wedge xi, wedge eta>| = 9.61e-18`. All frames at `conj(h)`.

### B6. Theorem 5's "unitary modal transform diagonalizes it" — **survives**; its **multiplicity clause does not lift**

Anti-Hermitian implies normal implies unitarily diagonalizable, over `C`. That
half lifts. But *"For each reduced spatial momentum the staggered cell has
dimension `8`; the OS projector, pole projector, and stable transfer projector
therefore each have rank `8`"* (lines 324-327) is a **translation-invariance**
statement. A general fixed background has no Bloch decomposition and no reduced
spatial momentum. What survives is only `rank K_1 = dim h` (probe: 24 of 24).
Any lift that repeats the rank-8/four-taste sentence at a background is an
over-claim.

### B7. `T_odd = T_even^dag` — **survives**, and it is already landed for arbitrary anti-Hermitian `h`

`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md:86-93` proves
exactly this from `h^dag=-h` and real `m`. No reality used.

### B8. `eta_mu` independence of `x_mu` — **load-bearing, and it is what keeps `h[U]` anti-Hermitian**

In the runner's convention the *same* site phase `eta_mu(x)` multiplies both the
forward and the backward hop out of `x` (`scripts/...2026_07_12.py:159-160`), so
`h^dag = -h` needs `eta_mu(x) = eta_mu(x - e_mu)`. Mutation control at the gauged
`SU(3)` carrier: with the canonical `eta_mu = (-1)^{x_0+...+x_{mu-1}}`,
`||h + h^dag|| = 0.00e+00`; replacing it by a phase that depends on `x_mu` gives
`||h + h^dag|| = 8.33e+00`. See section (e) for what the landed notes do and do
not say about this.

### B9. **The hypothesis nobody has written down: the background must be STATIC**

The free note's chain operator uses the *same* `H` on every time slice. A
"fixed gauge background" that is time-dependent breaks the construction at the
first step — not just the frames, but Hermiticity and positivity of the Gram
itself. Probe: two independent random `SU(3)` backgrounds `h` on even slices and
`h2` on odd slices, everything else identical:

```text
||K_1 - K_1^dag||                    = 2.27e+00      (static: 1.45e-15)
min eig of Hermitian part of K_1      = -7.897e-02   (max +3.913e-01)
```

So reflection positivity **fails outright** at a general time-dependent fixed
background. Static spatial links in temporal gauge is exactly the
reflection-symmetry condition `U_k(x,1-t) = U_k(x,t)` that
`RP_COUPLED_MULTISLICE_HALFSPACE_GAUGE_STAGGERED_OS_GRAM_NARROW_THEOREM_NOTE_2026-07-11.md:142`
carries inside its L2' proof. It is *not* stated anywhere in the fixed-background
lane (files 5 and 6). Any lift note must state it as a hypothesis.

### B10. Runner coverage of the complex case is **zero**

`spatial_hop_3d` is the only carrier in the file, and it is real. `two_step` and
`Teven` are built from the same real `H`. Both mutation controls (`V`-frame,
`e^{-E}` decay) are real-carrier controls. The note's complex-hop parenthetical
(lines 82-84) and its N3 row (line 441) are therefore **asserted and never
certified** by the paired runner. My probes above are the first check I can find
in this repo of that clause — and they show the clause is right about the frames
and incomplete about the transfer.

### B11. Things I checked for and did **not** find (so they cannot break)

No step in the note or runner uses: a real-orthogonal diagonalization; a
symmetric-matrix eigenbasis; a Pfaffian identity; a real determinant identity; a
Majorana/self-conjugacy condition; a charge-conjugation matrix. `np.linalg.eigh`
is applied only to `-1j*H` (Hermitian for any anti-Hermitian `h`) and to the
`2x2` mode Grams (Hermitian for any `h`). The single reality use is the one in
B2/B3, and it enters through the spatial transpose in the kernel reading.

### B12. Uncertainties I am flagging rather than smoothing

- My probes use the note's own untransported reflection `theta(t) = -1-t` with
  `Theta(chi_t) = -bar-chi_{theta(t)}`. At a gauge background the landed
  conventions differ: `RP_COUPLED_MULTISLICE ... :46` adds
  `theta(U_k(x,t)_(cc')) = conj(U_k(x,1-t)_(cc'))`, and the two-seam note uses a
  *transported* reflection with step phase `s_j(t)`
  (`COUPLED_PERIODIC_TWO_SEAM ... :111-123`). For a **static** background in
  temporal gauge these reduce to what I computed; for a circle or with dynamical
  temporal links they do not, and B1-B9 would have to be redone.
- I used an open temporal chain (`Nt=20,24`), not the infinite lattice; residuals
  `~1e-12..1e-13` are consistent with the note's own exponential-convergence
  control (`docs/...:333-339`), but the exact-vacuum statement is an extra step.
- I did not check the Berezin sign bookkeeping at a background (the two-seam
  note's `s_j(t)` phases). That is a real open item, not something my linear
  algebra covers.

---

## (c) The gauged lane's own scope firewalls, verbatim

### c.1 `RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md` — classical matrices only

What it establishes (lines 26-33):

> "The source claim has exactly two parts:
>
> 1. the supplied static classical recurrence has a positive-definite two-step
>    matrix; and
> 2. determinant, spectrum, and exponential trace are invariant under supplied
>    finite permutation-unitary conjugations.
>
> No quantum-transfer, reflection-positivity, dynamical-gauge, P2, or
> `AC_phi_lambda` consequence is part of the theorem."

Scope repair (lines 15-19):

> "This note proves a conditional finite-matrix theorem. Its starting data are a
> finite anti-Hermitian matrix and the explicitly stated alternating two-step
> recurrence. It does **not** claim that the framework axioms select that
> recurrence, a staggered kinetic branch, a Hamiltonian, a temporal-gauge
> carrier, a Grassmann transfer kernel, or a Fock-space second quantization."

Its supplied gauged hop (lines 132-140):

> "```text
> h[U]_{x,y} = (1/2)(U_x delta_{y,x+1}
>                          - U_{x-1}^dag delta_{y,x-1}).
> ```
>
> For every such list, the forward block and backward block are
> minus-conjugate-transposes, so `h[U]^dag = -h[U]`."

Note this is a `1d` periodic chain with no `eta` at all, and the anti-Hermiticity
is arranged by the `U_{x-1}^dag` placement, not derived from a staggered phase.

Scope firewall (lines 219-230), verbatim:

> "The theorem does not establish any of the following:
>
> - a Hamiltonian or transfer operator selected by the framework axioms;
> - a staggered KS action derived from Lattice, Qubit, Admissibility, and Record;
> - a physical temporal-gauge or time-dependent gauge carrier;
> - positivity of a Grassmann transfer kernel or its inner product;
> - a second-quantized or many-body operator `Gamma(t1)`;
> - an Osterwalder-Schrader or reflection-positivity inequality;
> - a `U`-integrated Wilson-plaquette gauge theorem;
> - P2 phase blindness, scalar additivity beyond the Record axiom, or any
>   `AC_phi_lambda` conclusion; or
> - a continuum or OS-reconstruction statement."

### c.2 `CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md` — classical matrices + a trace identity, `1+1d`, `U(1)` witnesses

Boundary (lines 14-22):

> "FIREWALL: fixed background only. This note proves (N1)--(N5) on the supplied
> corner-axis surface at a fixed spatial gauge background in temporal gauge. The
> computed witness class is arbitrary finite `U(1)` phase backgrounds at
> `L_s = 2`. The cited conditional finite-matrix theorem supplies only the
> anti-Hermitian recurrence algebra used by the finite construction; it supplies
> no physical transfer, reflection-positivity, or P2 authority. This note does
> **not** integrate over backgrounds, does **not** supply the gauge measure, does
> **not** select a species reading, does **not** select an occupancy cell, does
> **not** fix `r`, and leaves the binary untouched."

Surface (lines 32-34): *"Work with the staggered `1+1d` action at a fixed spatial
background `{U_i(x)}` in temporal gauge."* — i.e. **static**, `1+1d`, and the
positivity it inherits is the classical `T_k^2[U] = B_k[U]^dag B_k[U] >= 0`
(lines 48-55).

Its only second-quantized content is a **trace** identity, (N3), lines 82-87:

> "**(N3) Trace correspondence config-by-config.** For each fixed background,
> the finite-fermion second quantization obeys
>
> ```text
> Tr Gamma(t[U]) = det(1 + t[U]).
> ```"

Its `K`-conjugation statement, (N4), lines 96-124 — note the explicit
operator-level disclaimer:

> "`K`/CPT conjugation acts on the background as `U -> conj(U)`. The channel
> kernels obey the computed doublet-swap relation
> ...
> - On general backgrounds, the operator-level statement is the
>   conjugated-background statement: reading-1 data at `U` equal reading-2 data
>   at `conj(U)`; operator-level unitary equivalence at the same background is
>   asserted only on the `K`-invariant class."
> ...
> "Operator-level same-background equivalence beyond the `K`-real class is still
> not claimed."

"Does NOT" list (lines 144-154), verbatim:

> "- Does not integrate over gauge backgrounds.
> - Does not supply or select the gauge measure.
> - Does not prove full dynamical-gauge reflection positivity.
> - Does not select a species reading.
> - Does not select an occupancy cell.
> - Does not fix `r`.
> - Does not alter the binary.
> - Does not remove or rewrite `AC_phi_lambda`.
> - Does not claim that the U-INTEGRATED level has been handled."

### c.3 The microcausality note's own summary of these two firewalls (file 7)

`MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md:33-41`, verbatim:

> "The distinction is load-bearing. The current source tree does not
> supply `T_MB^2[U] = Gamma(t[U])` at a general fixed gauge background. The
> conditional finite-matrix recurrence in
> `RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`
> explicitly excludes a Fock-space second quantization, while
> `CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md`
> constructs classical fixed-background matrices and separately records a trace
> identity. Neither statement is an operator identification. Fixed-background
> factorization therefore remains open."

The exact `Gamma(t[U])` sentence requested, `...2026-07-18.md:143-144`, verbatim:

> "- **Fixed gauge backgrounds:** no current source identifies the classical
>   fixed-background recurrence matrix with a Fock-space `Gamma(t[U])`."

Its **full** open-problems list, `...2026-07-18.md:141-156`, verbatim:

> "## Open problems and non-claims
>
> - **Fixed gauge backgrounds:** no current source identifies the classical
>   fixed-background recurrence matrix with a Fock-space `Gamma(t[U])`.
> - **Gauge integration:** no measure over backgrounds or interacting transfer
>   is supplied.
> - **Locality and Lieb-Robinson bounds:** this note proves no spatial kernel
>   envelope and makes no open-chain or periodic-chain activity claim. A
>   one-particle locality estimate cannot be fed into a many-body bound until the
>   operator identification and boundary convention are both supplied.
> - **Matrix fibers:** if a future one-dimensional open-chain bridge supplies a
>   block-operator-norm envelope with fixed fiber dimension `n_f`, the coarse
>   activity expression carries the factor `n_f`; scalar-fiber constants do not
>   transfer to a non-Abelian block kernel.
> - **Physical interpretation:** no species choice, occupancy choice, physical
>   velocity, infinite-volume dynamics, or retained-grade status follows."

And the "pin" it names, `...2026-07-18.md:104-106`, verbatim:

> "Thus the exterior action or, equivalently, the canonical creation
> intertwiner is the pin. The trace/determinant correspondence by itself is not
> a Gaussian-factorization theorem."

---

## (d) What the SU(3)-Wilson two-seam note already establishes — **the lift is NOT redundant**

File: `docs/COUPLED_PERIODIC_TWO_SEAM_SU3_WILSON_STAGGERED_REFLECTED_GRAM_BOUNDED_THEOREM_NOTE_2026-07-12.md`.
This is the single most important question in the task, so I answer it sharply.

**The two notes prove different theorems about different objects.**

| | free 07-12 reflected-Gram note | two-seam SU(3) note |
|---|---|---|
| object | `K_{ab}` on **two-slice one-particle block fields**, from the residue of `D^{-1}` | `G^{(j)}_{i,k} = omega(theta_j(F_i) F_k)` on **arbitrary gauge-invariant polynomial observables** |
| background | free, `U=1` | `SU(3)`, but **integrated over**, not fixed |
| output | exact rank-`n` PSD kernel, explicit frames `U_pole`/`V`/`W_stable`, OS quotient `A`, `K_n = 2 W^dag C^n W`, exterior/Fock matrix elements | PSD, full stop — no frames, no spectrum, no quotient, explicitly not a transfer |
| arena | infinite temporal lattice | finite even Euclidean-time circle |

The two-seam note is a **reflection-positivity** theorem, not a representation
theorem. Its positivity comes from expanding the seam Wilson kernel into a
positive-type character Gram — an object that only exists once the seam links are
*integrated*. Verbatim, lines 240-241:

> "The Wilson factors in (4.3) are cross-configuration character Grams, not
> pointwise norm squares at one link configuration."

Its Theorem 5.1 (lines 275-286) is at the level of the full functional `omega`,
and it says so immediately after, lines 288-289:

> "The theorem integrates over the full residual Polyakov holonomy. It does not
> assert reflection positivity separately in a fixed-holonomy sector."

Its "It does not prove" list, lines 424-435, verbatim:

> "It does not prove:
>
> - a fixed-holonomy-sector theorem;
> - arbitrary charged or bare gauge-variant fields;
> - OS-null descent of `B_2`, a bounded completed-space operator, domination,
>   or contraction;
> - a finite-circle transfer, semigroup, Hamiltonian, or unitary evolution;
> - the infinite-time/thermodynamic limit;
> - a controlled interacting continuum, Lorentz invariance, QFT/Standard-Model
>   identification, or GR;
> - selection of the supplied action, spin structure, reflection, or gauge
>   group from the four axioms."

and lines 44-47:

> "Equation (0.2) does not descend automatically through the `theta_0` OS null
> space and is **not a transfer operator**. Positive-form countermodels show
> that neither null descent nor contraction follows from two-plane reflection
> positivity alone. No finite-circle semigroup, Hamiltonian, unitarity, or
> continuum result is claimed."

**Conclusion for (d): the gauged reflected Gram in the free note's sense is NOT
landed there.** The lift is not redundant. Three genuine overlaps to cite rather
than redo:

- **Anti-Hermiticity at fixed links is landed** (line 293): *"For every link
  configuration, `M_KS^dagger=-M_KS`."* Same statement at
  `RP_COUPLED_MULTISLICE...:198` and `RP_COUPLED_TWO_SLICE...:300-304`.
- **Strict normalization at fixed links is landed** (lines 292-306): `{epsilon,M_KS}=0`
  on even/open bipartite geometry, `det(mI+M_KS) = prod_a (m^2+lambda_a^2) > 0`.
- **Per-configuration Hermiticity + PSD has a numerical certificate** —
  but only on *reflection-symmetric* backgrounds and only at `d=1`, `L_s=2`, `N_c=3`,
  three backgrounds: `RP_COUPLED_MULTISLICE...:186-190`:
  *"At `d=1`, `L_s=2`, `N_c=3`, on reflection-symmetric backgrounds the
  per-configuration half-space Gram is exactly Hermitian
  (`||G-G^dagger||_F=3.9e-13`, no Hermitization applied) and PSD
  (`lambda_min=8.370126e-01`) across three independent backgrounds."*
  That is the closest landed thing to a fixed-background reflected Gram, and it is
  a numerical certificate for observable Grams, not an operator identification, and
  it carries the reflection-symmetry hypothesis my probe B9 shows is essential.

Finally: `grep -rln "U_pole\|Upole\|W_stable\|Wstable" docs/*.md scripts/*.py`
returns **exactly two files** — the free 07-12 note and its paired runner. No
gauged note anywhere in the repo reuses the pole/stable-frame machinery.

---

## (e) The staggered phase convention on the gauged carrier, and the `x_mu`-independence fact

**The convention is stated on the gauged carrier.** `RP_COUPLED_TWO_SLICE_GAUGE_STAGGERED_BEREZIN_GRAM_NARROW_THEOREM_NOTE_2026-07-10.md:17`:

> "phases (`eta_k(x,t)=(-1)^(t+x_1+...+x_(k-1))` for spatial `k`)"

Free-carrier version, `FREE_STAGGERED_3PLUS1_SAME_ACTION_TRANSFER_GAUSSIAN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-07-12.md:68-70`:

> "```text
> eta_0=1,
> eta_mu(n)=(-1)^(n_0+...+n_{mu-1}).
> ```"

Both manifestly omit `x_mu` from the exponent, so the fact is *derivable in one
line*. **But no landed note states it.** The closest is
`GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md:196-198`, which states the
sibling fact for a *different* coordinate:

> "The factor `eta_mu` is independent of `x_nu`, so
> `eta_mu(x + e_nu) = eta_mu(x)`. The factor `eta_nu` does depend on `x_mu`, so
> `eta_nu(x + e_mu) = -eta_nu(x)`."

(there `mu < nu`, and the point is plaquette orientation blindness, not
anti-Hermiticity). Greps for `eta_mu(x + e_mu)`, `independent of x_mu`, and
variants return nothing in `docs/`; the only near hit is a comment in an unrelated
runner, `scripts/cl3_g_newton_skeleton_selection_2026_05_10_gnewtonG1.py:111`
(`eta_mu(x) eta_mu(x + e_mu) = ... (KS staggered cancellation)`).

What **is** landed is the *conclusion* without the *reason*, at three places, all
one-liners:

- `COUPLED_PERIODIC_TWO_SEAM...:293` — "For every link configuration, `M_KS^dagger=-M_KS`."
- `RP_COUPLED_MULTISLICE...:198` — "At fixed links `D=mI+M_KS`, with `M_KS^dagger=-M_KS`."
- `RP_COUPLED_TWO_SLICE...:300-305` — "At fixed links write `D=mI+M_KS`. With the
  stated staggered phases and unitary links, `M_KS^dagger = -M_KS`. (5.1)"

And separately, at a `1d` chain with no `eta`,
`RP_P2...:136-140` — "For every such list, the forward block and backward block are
minus-conjugate-transposes, so `h[U]^dag = -h[U]`."

**Answer to (e):** the convention is present and manifestly `x_mu`-free; the
`eta_mu(x) = eta_mu(x ± e_mu)` step is **absent** from every landed note; the
conclusion `h[U]^dag = -h[U]` at fixed links **is** landed (three places), so a
lift can cite it rather than rederive — but it should display the one-line reason,
because the fact is load-bearing (probe B8: breaking it gives `||h+h^dag|| = 8.33`)
and no landed source carries it.

---

## (f) GAP LIST — what a fixed-background `Gamma(t[U])` identification needs that no landed note supplies

Ordered by how badly each blocks the target.

**G1. The canonical creation intertwiner (the "pin"). BLOCKING.**
File 7 names it exactly (`...2026-07-18.md:104-106`, quoted in (c.3)): trace and
functoriality do not select `Gamma`; the pin is `Gamma(A) a^dag(f) = a^dag(Af) Gamma(A)`.
Nothing at a background supplies `a^dag`. The free note explicitly refuses even
the free version: *"`P_OS` is a support projector of the reflected Gram, not a
derivation of the original lattice fields' equal-time CAR anticommutator"*
(`...REFLECTED_GRAM...:196-198`) and *"It does not derive the original fields'
equal-time CAR anticommutator"* (line 573-574). So this gap is open **already in
the free case** — the lift cannot close it by going gauged.

**G2. Barred fields, reciprocal pole, contact terms. BLOCKING, and open free.**
`...REFLECTED_GRAM...:361-364`. Without them the algebra is positive-time
unbarred only, so there is no `a`/`a^dag` pair and no many-body transfer to
compare `Gamma` against.

**G3. The conjugate-background twist (new, from B3).**
The reflected-Gram route delivers `t[conj U] = t[U]^T`. To name `Gamma(t[U])` one
needs either (i) restriction to `K`-real backgrounds — `CORNER_TRANSFER...:105-107`
already isolates that class — or (ii) an antiunitary/CPT lemma at the **many-body**
level. `CORNER_TRANSFER` supplies the conjugation bridge only for **trace** data
(N4 third bullet, lines 117-124) and explicitly refuses operator-level
same-background equivalence off the `K`-real class. No landed note supplies (ii).

**G4. The static-background hypothesis (new, from B9).**
No landed note in the fixed-background lane states that the construction needs a
time-independent background. `RP_COUPLED_MULTISLICE...:142` carries
`U_k(x,1-t)=U_k(x,t)` inside a proof step, for observable Grams; files 5 and 6 say
"fixed spatial background in temporal gauge" and never state the reflection
symmetry. My probe shows Hermiticity *and* positivity fail without it.

**G5. A `3+1` gauged carrier.** Every gauged source is low-dimensional:
`CORNER_TRANSFER` is `1+1d` with `L_s=2` `U(1)` witnesses (lines 16-18);
`RP_P2` is a `1d` periodic chain (lines 130-140); `RP_COUPLED_MULTISLICE` and
`RP_COUPLED_TWO_SLICE` exercise `d=1`, `L_s=2`. Nothing runs a gauged `3+1`
staggered chain. The free note's `3+1` lift (Theorem 5) is the only `3+1` object,
and it is free.

**G6. Multiplicity / taste at a background.** Theorem 5's rank-8-per-reduced-momentum
clause has no background-independent analogue (B6). Nothing supplies a replacement.

**G7. Gauge measure / `U`-integration.** Named open by
`CORNER_TRANSFER...:24-27` ("The U-INTEGRATED level remains the named open next
path") and `...:144-146`, and by file 7's second bullet ("no measure over
backgrounds or interacting transfer is supplied").

**G8. A stated boundary convention.** File 7's third bullet requires "the operator
identification and boundary convention are both supplied". The three candidate
arenas disagree: free note = infinite temporal lattice (`...:333-339`); two-seam
note = finite even circle with thermal images; `CORNER_TRANSFER` = unstated. A
lift must pick one and say so.

**G9. The residue/normalization at a background.** `c_block=2` is derived for the
free unrescaled convention. My probe confirms the same factor 2 survives at a
static `SU(3)` background (`K = 2 U_pole[conj h] Z[conj h] U_pole[conj h]^dag`),
but that is a claim that needs its own displayed derivation, not an inheritance.

**Not a gap (available to cite):** `h[U]^dag = -h[U]` at fixed links (three notes,
section e); `T_odd = T_even^dag` and positive-definite `C(h,m)` for arbitrary
finite anti-Hermitian `h` (`RP_P2...:86-126`); `det(mI+M_KS) > 0` config-by-config
(`COUPLED_PERIODIC_TWO_SEAM...:292-306`, `RP_COUPLED_MULTISLICE...:196-213`);
`Tr Gamma(t[U]) = det(1+t[U])` config-by-config (`CORNER_TRANSFER...:82-87`);
finite-mode functoriality/positive-log/direct-sum identities (file 7, items 1-5).

---

## (g) LIMITS — what would block or rescope the campaign

**L1. Do not frame this as "general fixed gauge background."** B9 is decisive:
at a time-dependent background the reflected Gram is not Hermitian and its
Hermitian part has a negative eigenvalue. The honest scope is
*static spatial background in temporal gauge* — i.e. exactly `CORNER_TRANSFER`'s
surface, lifted from `1+1d` to `3+1`. Note also that "static in temporal gauge" is
a genuine restriction, not a gauge choice: on a circle it excludes nontrivial
Polyakov holonomy structure, and the two-seam note's whole point is that the
holonomy stays integrated.

**L2. The deliverable is `t[conj U]`, not `t[U]`, unless you restrict to `K`-real
backgrounds.** B3 shows the note's own intertwiner is false at a complex
background. A campaign that promises `Gamma(t[U])` and delivers `Gamma(t[U]^T)`
will be read as an over-claim. Two clean framings: (i) restrict to
`conj(U) = U`, citing `CORNER_TRANSFER...:105-107`; or (ii) state the result as
`K_n[U] = 2 U_pole[conj h[U]] Z[conj h[U]]^n U_pole[conj h[U]]^dag` and name the
transpose relation `T_2[conj h] = T_2[h]^T` as part of the theorem.

**L3. The lift does NOT discharge file 7's `Gamma(t[U])` open problem.** G1+G2 are
open in the *free* case. The most a fixed-background reflected-Gram lift can
deliver is the OS-side object: reflected Gram, OS support projector, quotient map
`A`, and multitime Wick determinants equal to exterior inner products of
`Z[conj h[U]]` — i.e. matrix elements, which is precisely what file 7 says is
*not* an identification (`...:93-106`, "Why trace data do not identify the
functor"). If the loop's stated target is `T_MB^2[U] = Gamma(t[U])`, rescope it
now. A defensible target: *"fixed static background reflected two-slice Gram,
OS quotient, and multitime Wick-to-exterior identity, at the conjugate
background frames"*, with the operator identification explicitly left open.

**L4. Reflection convention risk.** The free note's `Theta(chi_t) = -bar-chi_{theta(t)}`
is untransported. The landed gauged conventions add
`theta(U_k(x,t)_(cc')) = conj(U_k(x,1-t)_(cc'))` (`RP_COUPLED_MULTISLICE...:46`)
and, on the circle, a transported step phase `s_j(t)`
(`COUPLED_PERIODIC_TWO_SEAM...:111-123`). At a static background in temporal gauge
these agree with what I computed; anywhere else the whole calculation changes.
Pick the convention in the setup section and say which landed note supplies it.

**L5. Supplier grade.** The two-seam note self-declares (line 5)
*"unaudited candidate; independent audit alone assigns retained status."*
The free note's own N6 table (lines 482-490) lists its own dependency as
"branch-local PR #5262, audit pending" and the old mixed-OS source as `unaudited`.
Check the live ledger for every cited row before the lift leans on it; do not
inherit grade from these.

**L6. Vocabulary.** `U_pole`, `V`, `W_stable`, `A`, `K_n`, `P_OS`, `c_block`,
`J_Z`, `L` exist in exactly one note+runner pair. Reuse those names verbatim in
any lift; do not mint new frame names. Per the repo's no-new-vocabulary rule,
also do not introduce a new tag for "static background" — `CORNER_TRANSFER`'s
existing phrase *"fixed spatial background in temporal gauge"* is the landed
wording, and the time-independence needs to be added as a displayed hypothesis,
not as a new class name.

**L7. A rescope that is *cheaper and sharper* than the campaign as posed.** The
single highest-value shippable increment I can see from this scout is not the full
lift but the **defect + repair**: the free note's generalization clause (lines
82-84) is incomplete, and Theorem 3's intertwiner, the polar relation, and the
boundary-insertion relation are false at a complex background as written. That is
a bounded, numerically decisive, self-contained finding (B2/B3, residuals
`9.5e-01`/`1.01e+00`/`5.4e-01` against `2.6e-14`/`3.6e-13`/`1.1e-14`), it needs no
new gauge input beyond `h[U]^dag = -h[U]` which is already landed, and it is a
prerequisite for any lift. Doing the lift without it would ship the false
sentence.
