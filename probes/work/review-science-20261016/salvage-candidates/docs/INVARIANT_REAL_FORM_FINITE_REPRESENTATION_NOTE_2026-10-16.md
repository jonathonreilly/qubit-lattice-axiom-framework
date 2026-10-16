# Invariant real forms of a finite complex representation

Claim type: bounded_theorem

Primary runner: [invariant_real_form_finite.py](../scripts/invariant_real_form_finite.py).

## Criterion

Let R be a nonzero finite-dimensional irreducible complex representation of
any group G, with complex dimension d. Its underlying real representation
has a G-invariant real subspace W of dimension d if and only if R has a
G-equivariant antilinear involution C. No unitarity or compactness assumption
is required for this criterion.

Proof. Given W, W+iW is a nonzero invariant complex subspace, hence equals R.
The intersection W intersect iW is also an invariant complex subspace: if
v=iw with v,w in W, then iv=-w is in W and also in iW. Irreducibility makes
this intersection zero or R; its real dimension is at most d<2d, so it is zero.
Every vector has a unique expression w+iu with w,u in W. Define
C(w+iu)=w-iu. This is antilinear, squares to the identity and commutes with G.
Conversely, for an antilinear involution C each v decomposes as
(v+Cv)/2 + i(v-Cv)/(2i); both displayed real components are C-fixed.
The fixed space W intersects iW trivially and has real dimension d. It is
G-invariant when C commutes with G. This proves both directions.

## Quaternionic pairing

Suppose instead that a G-equivariant antilinear map J satisfies J squared=-I.
For irreducible R there is no equivariant antilinear involution: if C existed,
JC inverse would be complex-linear and equivariant, hence scalar lambda by
Schur's lemma. Then J squared=(lambda C) squared=|lambda| squared I,
contradicting -I. The version of Schur used here follows by choosing an
eigenvalue of a complex commuting endomorphism: its nonzero invariant
kernel forces that endomorphism to be scalar on an irreducible module.

On R direct-sum R, the antilinear map F(v,w)=(Jw,-Jv) does square to I.
Its fixed space is exactly {(v,-Jv):v in R}. As a real G-module this is
isomorphic to the underlying real R, of dimension 2d. Thus the doubled
complex space admits a real form, while the original quaternionic module
does not admit a real half of dimension d. This is a statement about the
specified representation, not a ban on new carriers or physical mechanisms.

## Checks and scope

The proof is general; finite controls are not a proof by sampling groups.
The exact runner checks the real-form decomposition, quaternionic pairing,
and representative real, complex and quaternionic examples. For the
nonzero U(1) character, commuting with multiplication by i makes a real
endomorphism aI+bJ; its symmetric part is aI. For the SU(2) fundamental,
commuting with all three Pauli Lie generators has the same scalar symmetric
part after realification. Hence invariant orthogonal projectors have ranks
zero or full in these examples. Standard unitary inner products make such
projectors available for invariant subspaces. A real SO(3) representation
on C cubed has the ordinary real fixed subspace of dimension three.

Supplied representation choices and conventional complex linear algebra
are the only inputs. No local field content, physical Majorana constraint,
fermion generation count, dynamics, strain response or taste elimination is
inferred. The historical factor-only multiplicity tables are not adopted.
In particular their no-sterile SU(3)-only and SU(2)-only exclusions for every
generation number were too strong: the supplied block arithmetic permits
even generation numbers. That arithmetic is distinct from this theorem.

This extracts the representation argument from PR #9571 at commit
`6afb06951a13ca861b50f47a8faf5d5c06594109`, historical
`.claude/science/exercises/strain-hot-matter-and-twins-20261013/agents/C5_TW1_report.md`
and exercise scripts `scripts/TW1/tw1_alg.py`, `scripts/TW1/tw1_count.py`.
Historical material is recoverable on its preserved branch; the complete
proof is given here. Existing Pfaffian realification results concern
coordinate changes, a different question. No novelty or audit-grade claim
is made.

## No-Go Discipline Gate — packet HOLD

N1 — Alternative routes: ATTEMPTED exact invariant-subspace and antilinear-map proof; exact commutant examples provide controls, not five distinct attack families.
Fewer than five distinct routes have been established. Current no-go-discipline
schema therefore withholds packet PASS. This is a procedural limitation,
not evidence against the displayed finite theorem. This candidate has not landed.

N2 — Wall independence: no list of independent physical walls is asserted.
The supplied mathematical hypotheses define the theorem's domain; no wall
count or pairwise non-implication claim is made.

N3 — Hidden conditions: the complete proof was reread. Finite dimension, complex irreducibility and equivariance are explicit; Schur's lemma is proved in the text. The example projector argument separately uses the stated standard unitary inner products.
Historical provenance and comparisons are non-load-bearing context.

N4 — Residual matching: no prior no-go or campaign is cited as proof authority.
Historical paths identify origin only; the current argument is self-contained.
The contextual Pfaffian result is a coordinate identity, not an invariant-real-form obstruction.

N5 — Rhetoric: the runner checks exact matrix entries and the finite module
or cluster stated above. Its five resolution lines state executed scope and
nonexecution explicitly. No site-independent or lattice-wide physical
exclusion is asserted.

N6 — Partial closure: Doubling constructs an equivariant real form explicitly; restriction to a smaller group or removal of irreducibility changes the domain.
No approved primitive is called a missing premise, and no new axiom is required
for these finite mathematical statements.

N7 — Steelman: An opponent can double the quaternionic representation and exhibit a real fixed space. The explicit F construction proves that escape and its dimension. To refute the stated irreducible-module obstruction, the opponent must instead produce an equivariant antilinear involution on the same R despite the scalar-square contradiction.
The direct proof, rather than failure to imagine another route, supports the
mathematics. This does not waive the N1 packet shortfall.

N8 — Cross-cycle echo: the independent check compared the existing Pfaffian realification note and the historical TW1 pairing proposal; coordinate realification and doubled-carrier reality are both considered, neither silently supplies a real half of the original module.
This focused comparison is not an exhaustive campaign-ledger search. Packet
coverage remains incomplete; no overall review-loop PASS is claimed.
