# Supporting mathematical source

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_KINK_FOURTH_CHECK.md`, SHA256 `b5d0a2aa0107b92e37f5513cd9882e558386634d86e34b86348363133dcaf1df`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Focused fourth-order kink side-state check

Exact value -73/192 and independence for ALL L>=8 remain numerical/conjectural unless accompanied by a separate exact local-count proof. No root files edited or formal audit; root retains authorship.

Let A=PVP=K1, R=Q(8-H0)^(-1)Q, K2=PVRVP and N2=PVR²VP, with K2 here the ABSOLUTE-band coefficient. The side state is normalized and satisfies A|d>=0, explicitly asserted. Intermediate-normalization Bloch recursion gives b4=PVRVRVRVP minus terms ending in A, minus N2K2, plus a term ending in A². Canonical similarity contributes [N2/2,K2] and a commutator with A. All terms with A at an endpoint vanish in the d,d element. Thus the surviving real canonical diagonal is

<d|PVRVRVRVP|d> - Re<d|N2 K2|d>.

This justifies the code's term1-folded even though PVP is nonzero elsewhere in this excited band. It is NOT a general full-matrix fourth-order formula for this band; omitted A terms would matter for other matrix elements.

The source computes w=R V d and y=Vw over the full computational configurations, then term1=<y,Ry>. The R exclusion of energy8 is the complete P exclusion previously proved. V(y) destinations are not restricted to Q1: all two-hop configurations are present, including Q2 states reachable only after a second hop. Summing each destination amplitude BEFORE its absolute square retains interference between paths. The folded term uses bd=(H2-L/2) d=K2 d and wb=R V bd, so <w,wb>=<d|N2 K2|d>. No absolute-square substitution, half-factor or cross-path omission was found.

Ground subtraction is also correct for these L>=6 samples: the aligned ground band has scalar second order E2=-L/2 and no earlier nonconstant coupling at order4. With w0=R0 V vac, its canonical E4 is <Vw0,R0 Vw0>-E2||w0||², exactly the implemented plus(L/2) term. The uniform eight-vacuum state is sufficient for this scalar coefficient; the first distinct aligned-column tunneling appears at orderL. Extending this scalar-ground premise to shorter chains would require checking their earlier tunneling.

## Independent controls

Built full computational vectors on all8^6=262144 states and applied V by independent tensor-axis contractions, using a full diagonal H0 energy array rather than dictionary Q-support assembly. A direct Bloch-column recursion through order3 and final V contraction reproduces absolute K4=-.5364583333333339 for L6,q0 and-.3958333333333336 for q1,q2, ground E4=-.0625. Ground-subtracted values are-.4739583333333339 and-1/3, respectively, agreeing with root within1.3e-13. This verifies the real wrapping exception independently of the compressed formula.

Also reran the L8 dictionary algorithm with ALL eight momenta and all amplitude pruning removed. Every value is-.38020833333360..., agreeing with-73/192 to2.8e-13. This tests numerical support pruning and momentum coverage, but it reuses the inspected dictionary algorithm and is not claimed as an unrelated exact proof. The root L8,10,12 samples support the proposed stable coefficient. Floating operations, amplitude thresholds in the original, and a finite L list do not establish an exact all-L identity by recognizing a rational number. A bounded-local-support enumeration/linked-cancellation proof or exact arithmetic would be needed for that stronger formulation.

The result is a single bare side-state diagonal coefficient in a specified canonical band. Off-diagonal fourth-order terms and virtual mixing WITHIN the retained band remain relevant to actual eigenenergy/pole shifts. This diagonal alone is not a resonance position or width certificate. Full-H higher-order remainder and uniform thermodynamic limits remain separate; no physical scalar or detector claim follows.

## Exact finite certificate and full K4d follow-up

The earlier exactness limitation is now discharged for L8 and L10 at EVERY allowed momentum, but not for arbitrary L. An independent Fraction-arithmetic implementation uses integer native h matrix elements, integer unnormalized side configurations and exact rational resolvents. No floating normalization, energy cutoff or amplitude pruning is used. A transient Fraction-to-JSON serialization error was corrected in this reviewer's own script; the mathematical assertions had already passed and all final outputs were regenerated.

For the uniform q0 side vector the squared norm is16L. Exact results are:

L8: absolute K4=-89/192, ground E4=-1/12, gap K4=-73/192.
L10: absolute K4=-31/64, ground E4=-5/48, gap K4=-73/192.

A stronger finite control constructs a localized side vector d0 with integer amplitudes and norm²16, and computes all matrix elements to translated side vectors dj. The direct term uses full two-hop dictionaries and the same complete signed interference; the folded cross term is symmetrized as -( <w_j,wb_0>+<wb_j,w_0> )/2. After ground subtraction, the EXACT translation kernel is[-73/192,0,...,0] at BOTH L8 and L10. Fourier transformation therefore proves momentum independence and coefficient-73/192 exactly for those finite sizes. This is stronger than checking a few roots of unity, but still not an all-L proof. No general connected-support cancellation argument has been established by this follow-up.

### Full column formula

The newly supplied neutral_kink_fourth_leak.py uses the correct canonical K4 action for K1d=0. Define N2=PVR²VP, N3=PVR³VP and M=PVR²VRVP+PVRVR²VP. The full canonical fourth coefficient can be arranged as

A4-(1/2){M,K1}+(1/2){N3,K1²}-(1/2){N2,K2},

with A4=PVRVRVRVP and K2 the absolute second-order coefficient. Acting on d removes only the RIGHT-end K1/K1² terms. The surviving terms are precisely

A4d-(1/2)K1 Md+(1/2)K1²N3d-(1/2)(N2K2d+K2N2d).

The script retains these left-end contributions and correctly removes the L/2 ground shift when using H2. Its md, n3, n2 and n2b contractions match this expression. Thus using the scalar dd formula for the entire K4d would have been wrong, but the new leak script does not make that mistake.

Its outside norm uses W W† as a projector, so it presumes the host Krylov columns and the chosen physical d are mutually orthonormal. The host is twice reorthogonalized and d is dark to H1; this holds in the inspected nonzero-source cases, but explicit W†W checking is a useful robustness assertion if extended. At momenta where the source vanishes, a different basis construction would be required; the current tested modes are not a general all-momentum guarantee of that code path.

The exact dd certificate establishes only the projected matrix element. Root reports nonzero coupling at L8q0 into additional H1-dark, H2=-2 channels. Such degenerate channels can alter the physical effective eigenvalue/resonance after diagonalization even when every dd is identical. Neither the rational coefficient nor source-family closure through lower orders removes that issue. Higher-channel mixing and any special wrapping terms remain separate required checks before a standalone native pole claim.

Follow-up files/hashes:

- `/private/tmp/neutral-kink-fourth-rational.py`: `28c1b129a7fe4a69f482c144c342e337b1d25a2645f8cf93c9ed5a1d5f563fcb`
- `/private/tmp/neutral-kink-fourth-rational.json`: `75a059547934a773db17b17656c9ac4bb0d65ec29e57dc7487f578f9dcecef4e`
- `/private/tmp/neutral-kink-fourth-rational-kernel.py`: `6dde3e707fce578a48464ab26e7013188c4c33aa23eceb4c0c26b27abea12d5d`
- `/private/tmp/neutral-kink-fourth-rational-kernel.json`: `75f2aadc206b2e1492f1923d4549191c7acd9378e2a6e660132d97991c2694cb`
- `/private/tmp/neutral_kink_fourth_leak.py`: `4e41df1e1ffa05a8f16fa0a998bfbd36dcfd44ea565978f353dc2492b30fecc8`
