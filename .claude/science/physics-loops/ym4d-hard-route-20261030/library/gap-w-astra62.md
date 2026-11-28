## Repo search

**Step 1 · Source check (argued as a search record).** Codex research draft for row 1127, queued as `gpt-6.2-astra max`, at `c638f8daa368`. The target-specific prior note was absent. The lead's November 8 digest searched main and PRs 10114, 10133, 10134 and 10141. I checked the closest soft-route hits. PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 103–149, supplies the fundamental convolution coefficient and a positive one-time-step plaquette witness. Its block estimate loses cutoff control. PR 10133 assumes crossover clustering, and PR 10134 requires a common trajectory and matched reconstruction to transfer it. Neither supplies the order-one inequality.

The two main-branch hits use a finite-clock Villain measure or a Dirichlet Maxwell measure. PR 10141 contains recovery copies of this project's work. The registry search found no competing owner. I also searched the named refs and PR 10144 for nonorientable sheets and for a quantitative Wilson crosscap obstruction. No outside-lane match in the searched paths supplied (3) below. The in-lane antecedents found during Phase 2 are credited there. See [November 8 search digest](prior/repo-search-2026-11-08.md), PR 10133's `MASS_GAP_CROSSOVER_REDUCTION.md` opening paragraph, PR 10134's `mass-gap-interface.md` lines 25–27, and the September 14 finite-clock and massive-Wilson-loop notes on main `8b11ae2bb9`, lines 4, 79–94 and 120–145 respectively.

## Initial plan

1. Check the prior-work record, the repository search, and the scope of the assigned row.
2. State the continuum target and its lattice reduction, and locate the ultraviolet input in the indexed sources.
3. Build a proof tree from the target and attack its first open leaf analytically.
4. Compare the tree with the lane, classify its leaves, and apply any counterexamples as constraints.
5. Verify the resulting proof or obstruction, its quantifiers, and its limits.
6. Record the result and the remaining Yang–Mills obligation.

## Phase 1 · Target before comparison with the gap lane

**Step 2 · Open (Jaffe–Witten).** Construct nontrivial pure four-dimensional SU(2) Yang–Mills theory on $\mathbb R^4$, with Euclidean correlation functions satisfying the Osterwalder–Schrader axioms and their regularity requirements for reconstruction. In a vacuum representation the physical Hamiltonian must have a $\Delta>0$ with $\operatorname{spec}H\subset\{0\}\cup[\Delta,\infty)$. Clustering in a vacuum component by itself gives no positive value of $\Delta$.

**Argued (lattice route).** Use normalized link Haar measure and the periodic Wilson weight $\prod_p\exp[(\beta/2)\operatorname{Tr}U_p]$. Send $a\downarrow0$ along an asymptotically free trajectory. Keep each comparison box at its specified physical side $L$, with $L/a$ lattice intervals, and double the physical box on the same trajectory. Both the infinite-volume and continuum passages, and the transfer of the gap to the reconstructed theory, are obligations. The local fixed-$\beta$ calculation below tests a proposed inequality on the ordinary homogeneous Wilson measure in the window $23/10\le\beta\le13/5$.

**Argued (source input, conditional as stated).** The ultraviolet route is Tadeusz Bałaban's renormalization group, as developed in the text by Ethan Sussman and Levent Alpoge with Claude and Codex, revision `31a47c543775`. The outline, lines 66–77, 118–151, describes the volume-first scalar $\operatorname{tr}(F^2)$ sector. Lines 3711–3720 retain a polynomial remainder. Lines 4195–4206 require an admitted flow. CA-I 3533–3569, 3636–3698 and 56419–56460 identify the precise ultraviolet input. Given the extension and two-sided drift premises, first passage puts $g^{-2}<x_K=g_K^{-2}\le g^{-2}+B_\sharp$. The lattice application assumes (H1)–(H6), the listed one-step and large-field inputs, and the earlier effective-density representations. CA-I 56426–56430 expressly identifies incomplete inputs. CA-I 2697–2712, 3212–3223 and 56632–56647 delimit the reconstruction and flow conclusions. Matching the terminal small-$g$ effective measure through the $\beta=2.3$–$2.6$ Wilson window and estimating the twist there are **open**. Source locators are index chunks 01, 03 and 04, the spectral-gap and E1 entries of `obligations.md`, and CA 4.12–4.19 chunk 11.

**Open (the selective step).** From the last small periodic box to the first good box, the box free energy must shrink by a fixed factor on each required doubling, uniformly in the fine cutoff. In the requested notation one needs a finite doubling-defect pair $(L_0,D_0)$ and physical $L\ge4L_0$ with $z^-(L)>256D_0+30$. The twist free energy and the even thermal excited trace are candidate readouts for this program. Their sector comparison has to carry its own assumptions. **Guide.** A massless mode with $E(L)\le c/L$ already contributes at least $e^{-c}$ to the thermal trace at time $L$ in its sector. Weak-coupling compact U(1) and a massless spectator test selectivity. The reported freezing locations of $Q_8$ near $1.15$ and the binary tetrahedral group near $2.15$ are guides only.

### Step 3 · Proof tree and first open leaf

**Argued (proposed route, written before opening the lane).** Read center parity in the exact character expansion. If the winding part were a positive measure on occupied surfaces, its probability of crossing the doubled box could be compared with that in the original box. This would give a group-dependent object on which to try a contraction. The proposed dependency tree has two ways to state the finite-volume obligation.

- The continuum target consumes the OS and limit input C together with a physical periodic seed.
  - In the gap-and-defect formulation the seed consumes the two estimates in D.
  - In the thermal formulation the seed consumes a small neutral excited trace G and small required electric twist deficits at the same box.
    - The charged branch tests P first, then needs the contracting estimate B on the full ensemble.
    - Using a fixed-window estimate on the actual trajectory requires M from U. Both the charged and neutral branches need this matching if they start from an ordinary Wilson window.

The table records the leaves. The first mathematical test of the proposed surface method is P.

| Leaf | Statement and Phase 1 disposition |
|---|---|
| P | **Open candidate attacked first below.** At homogeneous Wilson coupling, the odd twist numerator is a positive measure on winding surfaces, still positive when all representation labels are forgotten but the occupied plaquettes are recorded. This is needed only by the proposed probabilistic comparison. It can be tested before M. |
| U | **Argued, supplied conditionally by the account.** Admitted first-passage flow and cutoff data as in Step 2. |
| M | **Open.** Match the stopped effective measure to a measure with a proved order-one inequality, with the errors required in both volumes and both sectors. |
| B | **Open.** On the actual ensemble, bound the change of the odd/even sector ratio under doubling by a fixed contracting factor through entry. A positive representation, if available, would still need this estimate. |
| G | **Open.** Suppress the neutral excited trace at the same physical size. |
| D | **Open.** Bound the cutoff-uniform defect and reach the threshold at a physical $L\ge4L_0$. |
| C | **Open as a whole.** Connect the chosen twist sector to the even excited trace, propagate the finite-box criterion, construct the OS limit and carry the spectral separation into it. |

**Proved (finite-volume test of P).** Let $\omega_p\in\{0,1\}$ indicate a fixed center twist on a coclosed stack of plaquettes. Write $Z_\omega$ for the corresponding homogeneous Wilson partition function, $c_0=\int e^{\beta\operatorname{Tr}U/2}\,dU$, $f(U)=e^{\beta\operatorname{Tr}U/2}/c_0$, and $h=f-1$. For every subset $S$ of the plaquettes define the real number

```math
 w_\omega(S)=\frac12\int\!\left[\prod_{p\in S}h(U_p)-
                 \prod_{p\in S}h((-1)^{\omega_p}U_p)\right]\prod_e dU_e .
```

Expansion of the finite product gives $(Z_0-Z_\omega)/(2c_0^{\#p})=\sum_S w_\omega(S)$. This is a decomposition of one pair of Wilson integrals at one constant $\beta$. At fixed $S$ only the support is recorded. The coefficient includes the link integrations and all representation labels on it. Denominator normalization by any common positive constant preserves its sign.

**Proved (sheet formula).** Let $S$ be a connected, closed, embedded plaquette surface with exactly two of its faces at every edge of $S$. Suppose it is obtained from a sphere by adding $h_0$ handles and $k$ crosscaps (a crosscap is a projective-plane summand). Write $F=\#S$, $\chi=2-2h_0-k$ and $p(S)=\sum_{p\in S}\omega_p\bmod2$. With $d$ the dimension of the irreducible SU(2) representation, put $a_d=d^{-1}\int f\chi_d$. Then

```math
 w_\omega(S)=
 \begin{cases}
  0, &p(S)=0,\\[2pt]
  (-1)^k\displaystyle\sum_{d=2,4,6,\ldots}d^\chi a_d^F, &p(S)=1 .
 \end{cases}                                                       \tag{1}
```

In particular the sign, including after loss of the spin labels, has an exact topological criterion.

**Proof.** A class angle $\theta$ on unit quaternions has normalized Haar density $2\sin^2\theta/\pi$ on $[0,\pi]$. The characters $\chi_d=\sin(d\theta)/\sin\theta$ of the symmetric powers of the defining doublet obey $\chi_d(-U)=(-1)^{d-1}\chi_d(U)$. Expanding the two exponentials in $e^{(\beta/2)(v+v^{-1})}$ gives the Fourier coefficients

```math
 I_j=\sum_{\ell\ge0}\frac{(\beta/2)^{2\ell+j}}{\ell!(\ell+j)!},\qquad j\ge0 .
```

Multiplying the sines in the Haar integral gives $I_{d-1}-I_{d+1}=2d I_d/\beta$, the last equality by matching powers. Thus $a_d=I_d/I_1>0$ and $h=\sum_{d\ge2}d a_d\chi_d$. The series converges absolutely and uniformly since $I_d\le(\beta/2)^d e^{\beta^2/4}/d!$ and $|\chi_d|\le d$. Also $a_d<1$ for $d>1$, by integration against the strictly positive $f$ and the strict character bound off the center except on a Haar-null set.

At an edge incident on two faces, the Haar integral pairs equal irreducibles and annihilates unequal ones. To see the normalization, averaging matrices $R_d(u)X R_{d'}(u)^{-1}$ gives zero for inequivalent irreducibles and $(\operatorname{tr}X/d)\mathbf1$ for equal ones, by invariance and trace. In particular
$\int\chi_d(Au)\chi_{d'}(u^{-1}B)\,du=\delta_{dd'}\chi_d(AB)/d$.
A face may be reversed since its character is real and invariant under inversion. Connectedness of the face adjacency graph thus forces one common dimension. The twist difference keeps precisely $p(S)=1$ and even $d$. It remains to integrate $\prod_{p\in S}d\chi_d(U_p)$ at this fixed $d$.

Splitting a disk face by a diagonal preserves its character integral by the identity just proved. Subdividing an edge preserves normalized Haar on its product. To compare with a cut polygon, draw its piecewise-linear cuts on the surface, subdivide at crossings with the face edges, and triangulate the resulting pieces inside each face. This refines both disk decompositions by these operations, with $a_d^F$ held outside. Equivalently one can join faces along a dual tree and gauge the vertex tree to the identity by successive Haar translations. Each handle supplies a commutator $[x,y]$ around the polygon, and the two sides of a crosscap are traversed in the same direction, supplying $u^2$. The residual polygon carries $d\chi_d$. Integrating $x$ by conjugation and then using matrix orthogonality for $y$ gives $\int R_d([x,y])\,dx\,dy=d^{-2}\mathbf1$. The average of $R_d(u^2)$ is $(\nu_d/d)\mathbf1$ by conjugation, where $\nu_d=\int\chi_d(u^2)\,du=(-1)^{d-1}$. Indeed $\chi_d(u^2)=\sum_{j=0}^{d-1}\exp(2i(d-1-2j)\theta)$. Paired frequencies are cosines. Under the Haar density only the constant and $\cos(2\theta)$ have nonzero means, $1$ and $-1/2$ respectively. Odd $d$ has one constant and even $d$ has the pair of frequencies $\pm2$. Independent polygon letters therefore give $d^{2-2h_0-k}\nu_d^k$. This proves (1). This calculation is the SU(2) surface character calculation with its Frobenius–Schur indicator. Step 4 records its antecedents.

**Proved (a connected twist-odd witness on the ordinary four-dimensional cubic lattice).** Here is an explicit cubical crosscap so that (1) can be used on an actual Wilson support. Use coordinates $(x,y,z,w)$. In the first plane put $B=[-2,2]^2$, $b=(0,0)$, $v_\pm=(0,\pm2)$, $r_\pm=[b,v_\pm]$. In the second put $Q=[-1,1]^2$ with its four side midpoints $E,N,W,S$ in cyclic order. “Arc $EN$” denotes the two unit edges of $\partial Q$ from $E$ to $N$. The quadrant between their radii is one square. All the following products are tiled with unit plaquettes.

1. Over the left half of $\partial B$ take the strip with fibre the diameter $WE$. Over the right half take the strip with fibre $SN$. At $v_+$ insert the two quadrants $EN,WS$ and at $v_-$ insert $NW,SE$. This is a Möbius band. Each joint matches the two halves of an interval by two quadrants. At its central vertex the two incoming-strip edges of the link, the two outgoing-strip edges and the two quadrant edges form one six-cycle. Following the endpoint $E$ around the base gives $E\to N\to W$. A cut across either strip gives a band with the endpoints reversed on regluing. Its one boundary lies on $\partial B\times\partial Q$.
2. Cap that boundary by a disk. Start with $\{b\}\times Q$. For each of the four arcs $I$ just listed attach $r_\pm\times I$, using the sign of its joint. These four rectangles attach along consecutive boundary arcs of the disk, with successive rectangles meeting only at the common attachment endpoint. At each cardinal point the resulting boundary contains the diameter from $v_-$ through $b$ to $v_+$. Attach along that diameter the left half of $B$ at $E,W$, and the right half at $N,S$. Each attachment is a disk along a single boundary arc. Its free arc is the corresponding half of $\partial B$. Thus the cap is a disk, and it meets the band exactly in their common boundary. Their union is a cubical projective plane with $32+4$ band squares and $4+16+32$ cap squares.
3. On an even periodic torus of side $n\ge16$, put the flat $yw$-torus at $x=4,z=0$. The band has a face at $x=2,z=0$ over $0\le y,w\le1$. Remove that face and its translate on the flat torus and join the two square boundaries by the eight side plaquettes along $2\le x\le4$. The open tube is disjoint from both surfaces. This is their connected sum, a torus with one crosscap, with $F=n^2+94$, $\chi=-1$. Use the coclosed stack of $yw$-plaquettes based at $y=w=6$ and arbitrary $x,z$. It meets the new surface just once. All coordinates in the construction fit in the stated period.

**Proved (counterexample to P).** On this connected winding support, for every real $\beta>0$,

```math
                    w_\omega(S)=-\sum_{d\ {\rm even}}\frac{a_d^F}{d}
                         \ \le\ -\tfrac12 a_2^F<0.                 \tag{2}
```

In particular this holds throughout the specified order-one interval. Nonnegative auxiliary weights with any choice of auxiliary space, local or nonlocal, cannot integrate to $w_\omega(S)$ on each recorded support. The event “all occupied plaquettes lie in this surface” has the same negative weight. Every proper nonempty subset has an edge adjoining one occupied and one unoccupied face by connected face adjacency. Integration over that edge gives zero. The empty subset has zero twist difference. No detached vacuum bubble was used. The crosscap is attached to the winding sheet.

## Phase 2 · Comparison and one return to Phase 1

**Step 4 · Argued (lead rule CL).** Rows 845, 852, 895, 896 and 1118–1122 distinguish one-sample means, two-sample mixing tests and uniform exterior bounds. Check 1123 limits the product and uniqueness conclusions. This attack uses an exact expansion at a single homogeneous Wilson coupling. Its coefficients are signed integrals. There is no cell-response hypothesis of any of those three kinds. The supremum over tilts in row 977, the coupling-field hypothesis in 996 (with its SU(2) correction), the background-uniform layer ceiling in 849/857, and the independent-replica junction in 1121 play no part.

**Proved in the lane, conditional where indicated (the consumer).** Theorem S (checks 698–699) propagates a small *full* excited trace on one box. Identity FL of row 708, checked in 709, reads $1+S=(1+S_0)/(1-U)$, where $S_0$ sums excited states in the zero-electric-flux sector and $U$ is the average of the electric twist deficits over center characters. For the threshold $t$ on that box, $S<t$ is equivalent to $S_0+(1+t)U<t$ since $1-U>0$. The basic Theorem S threshold is $t=1/5041$. For example, tensoring by a center-neutral spectator multiplies both twisted and untwisted partition functions by its partition function, preserving their ratio while adding its excitations to the thermal sum. A single twist estimate leaves the even trace open. Rows 1052, 1054 and 1055 give the flux consequence of (W) in the forward direction. The matched local-gap and OS conclusions require the indicated continuum hypotheses. A converse from a local Clay gap on $\mathbb R^4$ is open.

**Proved in the lane, given the named inputs (exact price).** Put $D_j(n)=\log Z_j(n^4)-f_j n^4$, with $f_j$ the bulk log-partition density, and $m_j(B)=\log(\lambda_{0,j}(B)/\lambda_{1,j}(B))$ in lattice units. On the admissible physical dyadic set $\mathcal P=\{2^i\ell_1:i\ge0\}$, with $\ell_1/(4a_j)$ integral and at least 3 eventually, write $n_j=L/a_j$, $D^+(L)=\limsup_jD_j(n_j)$, $z^-(L)=\liminf_j n_jm_j(n_j^3)$. Row 720, Theorem ZD-c, with the domain repair recorded in `parts/gap.md` lines 18–23, identifies (W) with a bounded $D^+$ on a tail and an unbounded $z^-$ on every tail. Row 708's (CAS) and an extensive base are sufficient. A fixed contraction for $D$ in the band would supply the missing factor. Row 998 §§6b, 6c, 7.5, 9.6 and the route registry, test table, exact price, method 34 and lead rule CL in `parts/gap.md` supply this comparison.

| Leaf | Disposition after comparison |
|---|---|
| U | **Supplied by the account, conditionally.** CA-I 4.2 and 4.19 in Step 2. The exact Wilson character eigenvalues and adjacent-coefficient bound are also supplied, in the Sussman–Alpoge outline with Claude and Codex, GL3–GL4, lines 2195–2243 (index chunk 02, rows 89–92). Their common $e^{-\beta}$ cancels from $a_d$. |
| M | **Open** on the Wilson trajectory. Rows 837, 846, 850, 861 and 877 distinguish first passage, a conditional hand-off and the missing order-one comparison. Row 868 supplies a conditional cylinder port for a different input. |
| P | **Refuted.** Generic termwise positivity was already refuted by row 737, §2.4, `gap-means-max.md` lines 69, 74–98, checked in row 744, `gap-means-max-check.md` lines 249–265, 395–419. Its 92-face surface is in class zero. Row 878, `gap-crux-exercise2-max.md` lines 268, 340, already gives the general Frobenius–Schur sign as an argument. Equations (1)–(2) apply it to a connected twist-odd support after summing its spins. Credit row 737 and its checker for the sign obstruction. Their cited antecedents are Drouffe–Zuber's nonorientable diagrams and Witten's two-dimensional surface calculation (`prior/gap-lit-assoc.md` lines 328–340). The negative sign alone is prior work. |
| B | **Open.** The parity identity in rows 860, 864, 866 and 870, and the strong-coupling surface estimates in 822–823, 826–827, 830, 833 and 847 have different hypotheses. The real response criterion of 871/874 still requires a relative estimate. Its true order-one value is untouched here. |
| G | **Open.** Rows 895–896 and 1125 locate the neutral mass and state-count estimates at the periodic seed size. |
| D | **Open.** The conditional equivalence and propagation are **proved in the lane** (708, 720). Uniform bounded defect and threshold entry for actual SU(2) remain open (998, 1122, 1125). |
| C | **Proved in the lane in conditional parts** (708, 720, 892–893, 1054–1055). **Open** at the periodic glue and flux inputs and any unprovided continuum datum. Rows 895–896 correct the extent of the even/flux separation. Rows 1115–1126 supply no positive order-one step. |

**Argued (discard tests).** This is a fixed-window test of a representation, on the actual SU(2) group. No extrapolation to first-passage data follows. The pseudoreality sign is shared by the defining doublet of $Q_8$ and $2T$, so it alone could not select the periodic seed. The order-one freezing estimates are **guide**, while the frozen-limit center-even obstruction is recorded in 884. Compact U(1) at very weak coupling and a massless spectator constrain claims about the full spectrum. The sharply peaked $w_p$ test of row 712's Proposition V concerns sufficiently large $p$ at its own transition. The Wilson action here has $p=1$. K7 at an order-one coupling is a **guide**. No statement about those transitions is used in (1) or (2). The comparison covered the requested FINISH results 708, 720, 821–896, 977, 996, 1052–1055 and 1115–1126.

**Return 1 · Open candidate to test.** Row 744 lines 415–419 require testing regroupings explicitly before drawing a conclusion about a full homology weight. Replace P by a weaker, quantitative leaf. Could an absolute sum over groups of occupied supports stay bounded with the *actual Wilson partition function* in the denominator? Test first the family that can still tell whether a specified winding plane is isolated and the parity of the number of isolated crosscaps in specified disjoint cells. Signs inside each group are summed exactly. The proof tree for this leaf consists of (i) the signs of the full local weights with all spins summed, (ii) an exact resummation of every unrestricted exterior, and (iii) a comparison with the positive full partition function. Then test connected winding surfaces after disconnected vacuum pieces have been removed. Row 866 and check 870 leave general relative resummation open. The targeted lane search found no volume-rate obstruction with these observations.

## Step 5 · An obstruction with the full Wilson denominator

**Proved (research argument, independently unchecked).** Fix any $\beta\in[23/10,13/5]$, any even $n\ge16$, and the electric twist in Step 3 on the periodic $n^4$ lattice. Put $r=\lfloor n/16\rfloor$. Let $\mathcal Z=Z_0/c_0^{\#p}$. On the finite set of occupied plaquette supports put $\mu(B)=w_\omega(B)/\mathcal Z$. Its total is $X=(Z_0-Z_\omega)/(2Z_0)$, with $0\le X<1/2$. Indeed the temporal twist inserts a commuting unitary center involution $C$ into the trace of the positive Wilson transfer power. Its absolute trace is bounded by the untwisted trace, and the twisted link integral is strictly positive. This is the electric-twist trace identity used by row 708. The observation below is a function of the formal support label $B$. The physical twist free energy is $-\log(1-2X)$.

There is an explicit **single binary observation** $\mathcal E$ of this support for which

```math
 -\mu(\mathcal E)\ \ge\
 \frac14\, b_*^{\,n^2}\big[(1+\eta)^{r^4}-1\big],                 \tag{3}
```

where, uniformly on the entire interval,

```math
 K=e^{13/5},\qquad a_*=\frac{23}{40}e^{-13/5},\qquad
 b_*=a_*K^{-24},\qquad \eta=2a_*^{88}K^{-2112}>0 .
```

Consequently every method which first groups the supports, keeps enough information to decide $\mathcal E$, and then adds nonnegative upper bounds for the groups, pays at least $X+|\mu(\mathcal E)|$. The least sum of **absolute** group weights over such partitions is exactly $X+2|\mu(\mathcal E)|$. In particular taking absolute values at fixed support, even after summing every spin assignment and dividing by the actual partition function, cannot give an upper estimate of this twist deficit that is uniform in $n$. The logarithm of the minimum absolute sum grows on the scale $n^4$.

**Proof, local signs.** In the notation of (1), GL4 gives $a_{d+1}/a_d\le\beta/[2(d+1)]\le q=13/30<1/2$ for $d\ge2$, directly by comparing the positive series term by term. Also $c_0=2I_1/\beta$, $I_2\ge\beta^2/8$, $1\le c_0\le e^\beta$ (Jensen and the pointwise bound). Thus $a_2\ge\beta/(4c_0)\ge a_*$ and $0<f\le K$. For a surface $C$ let $A_C^0=\int\prod_{p\in C}h(U_p)$, and let $A_C^\omega$ denote the integral with the twist. The same polygon calculation before the odd projection gives the following three signs.

* On the 88-face embedded projective plane $P$ of Step 3, with zero twist intersection, both weights equal $\alpha=\sum_{d\ge2}(-1)^{d-1}d a_d^{88}$. The absolute summands strictly decrease, since their consecutive ratio is at most $(3/2)q^{88}$. Pairing consecutive terms after the first two gives $\alpha\le-2a_2^{88}+3a_3^{88}\le-a_2^{88}$.
* On the flat winding $yw$-torus $T$ at $x=4,z=0$, $A_T^0=\sum_{d\ge2}a_d^{n^2}\ge a_*^{n^2}$. Its twisted value $A_T^\omega=\sum_{d\ge2}(-1)^{d-1}a_d^{n^2}$ is strictly negative by the same pairing. These signs hold with all nontrivial representations included in each occupied face.

**Proof, binary observation and exterior.** Let $N(C)$ consist of every plaquette containing an edge of $C$, including $C$. Write $E_C$ for the support condition $B\cap N(C)=C$. It isolates $C$ in the support and leaves all other faces free. In four dimensions a link belongs to six plaquettes, so $|N(C)|\le24\,\#C$. Place $m=r^4$ copies $P_i$ of the projective plane by translating its coordinates by $8+16j$ in each direction, $0\le j<r$ in each coordinate. The plaquette collars $N(P_i)$ are pairwise disjoint and each is disjoint from $N(T)$. Indeed each copy has half-widths $2,2,1,1$ and a collar extends a coordinate by at most one further lattice unit. Consecutive centers are separated by at least 16 even across a periodic boundary. The $z$-coordinate of each is at distance at least seven from $z=0$ before adding collars. No copy contains a plaquette of the twist stack at $w=6$. The observation is

```math
 \mathcal E=\{\,E_T\text{ holds and an odd number of the }E_{P_i}\text{ hold}\,\}.
```

For $J\subseteq\{1,\ldots,m\}$, remove the collars of $T$ and of the $P_i$ with $i\in J$ from the plaquette list. Let $R_J^0,R_J^\omega$ be the integrals of the ordinary products of $f$ on the remaining list. The twisted product uses the original factors $f((-1)^{\omega_p}U_p)$. Both integrals are strictly positive. Summing every unrestricted support choice uses $1+h=f$. No remaining face uses any edge of an isolated surface, so the independent link Haar integrals give the exact identity

```math
 2\mathcal Z\,\mu\!\left(E_T\cap\bigcap_{i\in J}E_{P_i}\right)
    =\alpha^{|J|}\big(A_T^0 R_J^0-A_T^\omega R_J^\omega\big).       \tag{4}
```

This keeps the unrestricted exterior in both twist sectors. Pointwise multiplication by the removed positive $f$'s gives
$\mathcal Z\le K^{24n^2+2112|J|}R_J^0$. Equation (4) obtains the deleted factors by exact summation at the original homogeneous coupling.

Use the exact indicator identity

```math
 -2\mathbf1_{\mathcal E}
 =\mathbf1_{E_T}\left[\prod_{i=1}^{m}(1-2\mathbf1_{E_{P_i}})-1\right].
```

In its integral against $\mu$, each nonempty $J$ contributes $(-2)^{|J|}$ times (4) divided by $2\mathcal Z$. Every contribution is positive since $-2\alpha>0$ and $A_T^0R_J^0-A_T^\omega R_J^\omega\ge a_*^{n^2}R_J^0$. Summing the binomial expansion gives (3). No sign or independence of the unrestricted exterior coefficients has been assumed.

**Proof, sharp scope of the bound.** Every partition that decides $\mathcal E$ refines $\{\mathcal E,\mathcal E^c\}$. Its positive upper bounds alone must pay the positive total $\mu(\mathcal E^c)=X+|\mu(\mathcal E)|$. The triangle inequality on both bins gives $X+2|\mu(\mathcal E)|$ for absolute values, attained on the two-bin partition. The same lower bounds apply to any auxiliary refinement with these exact marginals. In particular

```math
 \liminf_{\substack{n\to\infty\\2\mid n}}
 \frac1{n^4}\log\!\big(X+2|\mu(\mathcal E)|\big)
 \ \ge\ 16^{-4}\log(1+\eta)>0
```

uniformly in $\beta$ in the window. Conversely $|h|\le K$, $f\ge e^{-26/5}$, and $\#p=6n^4$ give
$\sum_B|\mu(B)|\le[(1+K)e^{26/5}]^{6n^4}$. These inequalities establish the volume order. Pooling both bins gives exactly $X$. Any method that exploits their cancellation before taking upper bounds lies outside the theorem.

### What survives for connected winding supports

**Proved (relative cost with no detached components).** The volume estimate (3) uses isolated vacuum components. There is a distinct, exactly summable test involving only connected sheets. For the connected-family test take $n=16r$. On $T$ mark $s=r^2$ disjoint squares by translating the surgery in Step 3 in $y,w$ by multiples of 16. For $A\subseteq\{1,\ldots,s\}$ perform the surgery at precisely the marked squares in $A$. These are distinct connected supports $S_A$, each meeting the twist stack once. Each surgery adds one crosscap and $88-2+8=94$ plaquettes. Thus, for $F_0=n^2=256s$ and $t_d=a_d^{94}/d$,

```math
 w_\omega(S_A)=(-1)^{|A|}\sum_{d\ {\rm even}}a_d^{F_0}t_d^{|A|},\qquad
 P_{\rm sum}:=\sum_A w_\omega(S_A)=\sum_{d\ {\rm even}}a_d^{F_0}(1-t_d)^s>0.        \tag{5}
```

Suppose a grouping keeps the surgery choices at $b$ specified sites, $0\le b\le s$. The least absolute sum relative to $P_{\rm sum}$ is attained by summing all remaining choices at each fixed pattern of the $b$ bits. For a pattern of weight $k$, its signed sum has sign $(-1)^k$, since the remaining factor is $(1-t_d)^{s-b}>0$ for every $d$. Thus the optimal ratio is exactly

```math
 R_b=
 \frac{\sum_{d\ {\rm even}}a_d^{F_0}(1-t_d)^{s-b}(1+t_d)^b}
      {\sum_{d\ {\rm even}}a_d^{F_0}(1-t_d)^s}.                    \tag{6}
```

It is an average of $\rho_d^b$, $\rho_d=(1+t_d)/(1-t_d)$, with the positive weights in the denominator. Since $a_d$ decreases for $d\ge2$, $\rho_d\le\rho_2$. Relative to $d=2$, the sum of all higher even-dimensional denominator weights is at most
$\epsilon_s=2^s q^{2F_0}/(1-q^{2F_0})$, using $t_2<1/2$ and $a_d/a_2\le q^{d-2}$. Hence

```math
             \frac{\rho_2^b}{1+\epsilon_s}\ \le R_b\le \rho_2^b.  \tag{7}
```

Here $\epsilon_s\to0$ uniformly, and $(1+a_*^{94}/2)/(1-a_*^{94}/2)\le\rho_2<3$. For this family the optimal relative cost stays bounded **if and only if** the number of surgery choices kept separate stays bounded. For a positive density of remembered choices the loss is exponential in the sheet area. Setting $b=0$ gives exact cancellation with ratio one. Equation (7) compares a specified family with its own signed sum. It gives no lower bound on the fraction of the full Wilson twist numerator carried by this family.

## Step 6 · Disposition

**Proved here, pending independent review.** The three leaves of the return are the all-spin local signs from (1) and GL4, the exact exterior identity (4), and the positive ordinary-partition comparison that yields (3). For one crosscap the signed mass in (4) is negative. For several crosscaps the odd-parity indicator makes *every* nonempty-subset contribution to its negative mass positive. This accounts for the volume exponent after arbitrary exterior resummation. Equations (5)–(7) give the separate connected-sheet calculation.

**Argued (relation to earlier barriers).** Row 809, `gap-expose-astra.md` lines 276–315, 530–573, excludes a layerwise operator-norm budget and shows that a particular branched counting majorant is too large. Row 866, `gap-z2parity-astra.md` lines 364–375, identifies an extensive cost in a binomial *upper* estimate and the need to cancel vacuum pieces. Equation (3) lower-bounds the magnitude of an actual negative bin after division by the full Wilson partition function, even if the only retained information is its one Boolean label. Here vacancy means the trivial character. Row 737 uses the $\sinh/\cosh$ parity expansion. Grouping the exterior solely by center parity sums trivial and nontrivial integer spins together. Such a grouping can erase the observation, as can pooling terms across its two bins. The rate in (7) concerns the connected test family only.

**Open (the physical question).** The upper estimate on the true twist deficit $X$ still comes from transfer positivity. A small upper bound on the neutral excited trace $S_0$ at the required size also remains open. A certificate at one particular finite box could use cancellations before taking absolute values. To prove (W), a cutoff-uniform estimate must still reach $z^-(L)>256D_0+30$ for some admissible $L\ge4L_0$ with the tail bound on $D^+$. The fixed-window obstruction does not transport the stopped effective law or establish that estimate. All proof steps above are written arguments. No numerical run was used.

RESULT: Row 1127 proves a volume-exponential obstruction to nonnegative upper sums that distinguish the specified single support event in the homogeneous Wilson SU(2) twist expansion throughout $\beta\in[2.3,2.6]$, with the full Wilson denominator. The optimal cost for the connected test family is given by (6). The selective doubling estimate (W) and the continuum mass gap remain open. Research text, independently unchecked, no status granted.
