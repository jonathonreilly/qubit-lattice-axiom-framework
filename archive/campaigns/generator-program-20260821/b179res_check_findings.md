# B179 B4 residue adversarial check

Scope: exact-arithmetic audit of `B4 PARTIAL` and `B4 CARRIER-MAP RESIDUE` only.
Fixture: `RULES["const"] = lambda t,x: Rational(7,5)` at `Width(6,"const")`.
Method: reconstruct the stated Fourier vectors and restrictions from the exact `Q` matrix exposed by `Width`; do not trust prose numerals.

## C1 — orientation

Let `omega=(-1+sqrt(3) i)/2` and `f_k=3^(-1/2)(1,omega^(-k),omega^(-2k))^T` on `(t,x)=(0,0),(0,2),(0,4)`.
Exact extraction gives `Q_orb=(3193/2240) I_3`, hence
`f_1^*Q_orb f_1=f_2^*Q_orb f_2=3193/2240` and `f_1^TQ_orb f_1=f_2^TQ_orb f_2=0`.
Attack: this is **forced/trivial**, not a contentful orientation result.  Since `f_2=conj(f_1)`, any real-symmetric orbit block has equal real Rayleigh quotients for the conjugate pair; here scalarity is stronger still.
**VERDICT C1: numbers CONFIRMED; “orientation-independence theorem” is algebraic tautology after the real-symmetric restriction, so no independent selector residue was solved.**

## C2 — multiplicity

The two parity-orbit copies at `t=0` each give `3193/2240`; those at `t=3` and `t=4` each give `1817/1120`, exactly as stated.
The full 12-copy diagonal table is: `t=0:3193/2240`, `t=1:43/35`, `t=2:3193/2240`, `t=3,4,5:1817/1120`, twice at each level (parities 0,1).
Thus `1817/1120` does fit the landed level structure (the bulk free-level class), but the prose's two-value sample omits the read level `43/35` and the return of `3193/2240` at `t=2`.
For the explicit `(t,parity)=(3,0)` copy, `f_1^*Qf_1=1817/1120` and `f_1^TQf_1=0`; with `phi=z f_1`, `phi^*Qphi=(1817/1120)|z|^2`, with no `z^2` term.  Slot typing is CONFIRMED.
But the rank-12 isotype block is not diagonal (the `(3,0)` row couples to five other copies), so these are not 12 factorized scalar Gaussian cells.
More decisively, the cited fork uses `r_from_slot_count(n)=n/2`: retaining all 12 holomorphic copies gives `r=6`, `Q=(1+2r)/3=13/3`, not `r=1/2`, `Q=2/3`.
Copywise type-independence cannot select/count one copy; a selector, quotient, or theorem that the multiplicity is external base-space degeneracy is still required.
**VERDICT C2: local coefficients and holomorphic typing CONFIRMED; claimed multiplicity dissolution REFUTED.**

## C3 — carrier map

On the natural orbit basis `(e_0,e_2,e_4)`, `U_orb=[[0,0,1],[1,0,0],[0,1,0]]=P_3`, with `U_orb^3=I`, exactly the stated 3-cycle.
The exact orbit block is `A=(3193/2240)I_3`.  With `P_s=(I+P_3+P_3^2)/3`, `P_d=I-P_s`, one has `A=alpha P_s+beta P_d` at `alpha=beta=3193/2240`.
All three character eigenvalues are therefore `3193/2240`; this is the degenerate `alpha=beta` point, not a nondegenerate singlet/doublet metric split.
`det_R A=alpha beta^2=beta^3=32553430057/11239424000`, exactly; eigenvalue degeneracy is not determinant singularity.
What transfers: for one chosen orbit copy, the `C_3` module, its `R (+) C` representation typing, and—after choosing `J`—the algebraic `2 real slots <-> 1 complex slot` determinant-exponent comparison.
What does not transfer: any nontrivial `alpha/beta` metric ratio, hierarchy, metric-selected `J`/orientation, uniqueness of the carrier, the full rank-12 count, record-write observables, or `hw>=2` ambient sectors.
Because `A` is scalar, its “metric-preserving” leg is basis-vacuous; only `U_orb=P_3` carries representation content.  Thus this is an equivariant one-orbit module map, not yet a physical observable-preserving carrier map.
**VERDICT C3: arithmetic and per-copy slot typing CONFIRMED; broad “carrier map exhibited” claim is only true at representation scope and is REFUTED at metric/physical scope.  Degeneracy itself does not spoil per-copy counting, but C2 blocks promotion to the unselected rank-12 carrier.**

## C4 — remainder completeness

The listed record-write, `hw>=2` ambient, and metric-ratio remainders are genuine, but the list is incomplete.
Missing M1: the rank-12 multiplicity selector/fiber-normalization theorem from C2; copywise identical type does not reduce the total slot count to one.
Missing M2: an actual `M_2(C)` algebra embedding (injective unital `*`-map preserving products/adjoints) is not supplied by identifying “content-writes” with shear pins; record-write matching is weaker.
Missing M3: a non-vacuous observable-preservation/physical-generator bridge.  Equality of two regular-representation 3-cycles plus preservation of a scalar metric proves module equivalence, not that the physical generators/observables coincide.
Outside this carrier-map sublist, the imported authority `Q=(1+2r)/3` also remains imported, as previously disclosed.
**VERDICT C4: REFUTED — at least M1 and M2 are missing; M3 is the unclosed physical content of the advertised carrier map.**

## Eight-line summary

- C1: `f_1` and `f_2` restrictions both equal `3193/2240` exactly.
- C1: equality is forced by conjugacy plus a real-symmetric orbit form; it is not new selector content.
- C2: sampled copy values and the explicit `t=3` pure `|z|^2` restriction are exact.
- C2: rank 12 is not dissolved—raw fork counting gives `r=6`, `Q=13/3` absent a selector/fiber theorem.
- C3: `Q_orb=(3193/2240)I_3`, `U_orb=P_3`, and `det_R=32553430057/11239424000` are exact.
- C3: `alpha=beta` preserves per-copy type but transfers no nontrivial metric ratio or metric-selected structure.
- C4: the remainder list omits multiplicity, the `M_2(C)` algebra embedding, and non-vacuous physical observable preservation.
- Overall: the arithmetic survives; the claimed B4 residue dissolution/carrier-map completion does not.
