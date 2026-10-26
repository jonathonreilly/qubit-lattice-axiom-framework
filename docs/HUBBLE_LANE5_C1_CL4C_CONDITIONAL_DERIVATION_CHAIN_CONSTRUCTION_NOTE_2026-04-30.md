# Supplied Cl4 module: finite identities and open physical bridges

**Type:** open_gate
**Status:** finite conditional construction; absolute-scale and cosmological bridges open.
**Primary runner:** `scripts/frontier_hubble_lane5_c1_cl4c_conditional_derivation_chain_construction.py`

## Supplied carrier and exact identities

Take H_cell=(C²)^⊗4 of dimension 16, and let P_A select the four Hamming-weight-one
basis vectors. Then rank(P_A)=4 and rank(P_A)/dim(H_cell)=1/4. Supply an
identification K=P_A H_cell≅C⁴ and the irreducible Cl4(C) representation on K.
This additional representation choice (formerly Axiom*) is not an adopted axiom.

With Pauli X,Y,Z and I=I₂ set Γ=(X⊗I,Y⊗I,Z⊗X,Z⊗Y). The Pauli identities
prove Γ_i†=Γ_i and {Γ_i,Γ_j}=2δ_ij I₄. For real v, D(v)=Σv_iΓ_i is Hermitian
and D(v)²=(Σv_i²)I₄. For complex v the same polynomial identity uses the
complex bilinear form Σv_i², not the Hermitian norm Σ|v_i|². In particular
v=i e₁ gives D(v)²=-I₄ whereas the Hermitian norm squared is +1.

Unitary conjugation preserves all these algebra identities. Relabeling the
four basis vectors is such a change of presentation; it does not automatically
implement a specified spatial rotation. An odd permutation of three spatial
axes has determinant -1 and lies in O(3), not SO(3). Only orientation-preserving
signed permutations are rotations. Thus the former S₃⊂SO(3) assertion is false.

Set c_N=(Γ₁+iΓ₂)/2 and c_T=(Γ₃+iΓ₄)/2. Expanding anticommutators gives
{c_i,c_j}=0 and {c_i,c_j†}=δ_ij I₄. The common vacuum and successive creation
operators form the four-dimensional two-mode Fock representation. These are
finite matrix identities; a physical dispersion, filled sea, spatial edge
carrier, crossing count or continuum entropy coefficient does not follow.

For B=Γ₁Γ₂, B²=-I₄ and exp(θB/2)=cos(θ/2)I₄+sin(θ/2)B. Hence the spin lift
is -I at 2π and +I at 4π. This is an angular period, not a physical action
normalization. Rescaling (S,κ) together leaves exp(iS/κ) unchanged.

## Supplied arithmetic and open arrows

The companion's numbers n_normal=2 and half_zone_measure=1/2 supply
n_x=2+2(1/2)=3. Dividing by 12 yields 1/4 and matches the finite rank ratio.
This is arithmetic on supplied inputs. CAR does not derive these crossings,
the half-zone selection, a Widom coefficient, or its identification with a
boundary entropy. A physical edge-channel law and the hypotheses of any
continuum asymptotic formula remain to be established.

Likewise the supplied kernel coefficient 1/(4π), multiplication by 4π and
λ=4c_cell give the number one. They do not identify measured Newton coupling.
Setting a=ℏ=c=G=1 makes sqrt(ℏG/c³)=a by choice; it does not derive a/l_P=1.
The physical boundary-action normalization and coupling bridge remain open.
Thus the original Arrow 2 and Arrow 3 are not closed by the finite Cl4 algebra.

The auxiliary tensor-factor model gives [A⊗I,I⊗B]=0 for arbitrary A,B.
This verifies only the supplied factorization, not physical independence of
cosmological and Yukawa mechanisms. Even formulas H_inf=c sqrt(Λ/3) and
H_0=H_inf/sqrt(Ω_Λ) require their physical model and inputs. Neither an
absolute scale nor H_0 is derived here. A guard against selected observed-input
variable names is a syntactic check, not proof that all physical premises follow.

## Evidence and repair record

The runner checks these finite identities and supplied arithmetic. Its successful
exit reports those checks only. Complex-vector and odd-permutation controls
preserve the counterexamples to the old statements. Exact original PR9839 note
and dispositions are preserved in [the recovery manifest](work_history/PR9839_original_recovery/manifest.json).
The original companion is also preserved there. This author repair responds to
independent feedback and asserts no audit verdict or retained status.
