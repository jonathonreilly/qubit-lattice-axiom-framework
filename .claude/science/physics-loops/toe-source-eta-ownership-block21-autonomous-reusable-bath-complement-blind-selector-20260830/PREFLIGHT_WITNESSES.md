# Block21 preflight witnesses

## 1. Proper-cubic orbit census

Fix `f=+z`. The proper-cubic stabilizer of `f` preserves four visibly
different sectors of the seven-state pointer:

```text
blank:        {0}
same:         {+z}
opposite:     {-z}
perpendicular:{+x,-x,+y,-y}.
```

Therefore proper-cubic covariance alone permits four scalar responses
`u,a,o,p`. It cannot by itself prove `u=o=p`. The primary runner must
construct the 24 proper-cubic signed-permutation matrices, compute the fixed
stabilizer and its orbits, and verify the invariant diagonal-response
dimension directly.

Block19 additionally identified `o=p=b` inside its smaller pair-factor
grammar. That equality must not be attributed to the cubic stabilizer. A
response with `o!=p` lies outside the Block19 beta family; beta projection is
undefined there.

## 2. Complement blindness is sufficient but not yet licensed

If a physical interaction depends only on the yes/no projector `P_f`, then

```text
F_f=u(I-P_f)+aP_f.
```

After one common normalization, blank and every nonmatching Record have equal
gain. Combining this with the conditional same/nonmatch mark ratio gives
`a^2/u^2=2` and `beta=1`.

This proves sufficiency only. Defining the interaction to lie in
`span{I,P_f}` assumes the desired complement blindness unless a separate
physical mechanism excludes the independent `P_0`, `P_{-f}`, and
perpendicular-sector responses. The runner must label this as an
`ASSUMED-SELECTOR` control unless that exclusion is derived.

The source-side `G_cov` superfamily must therefore be represented before
constraints with independent positive-real `u,o,p`, a declared common phase
quotient, and `u>0`. The runner must keep a provenance ledger for constraints.
These superficially different inputs all count as assumed or relocated:

```text
u=o=p,
o/u=p/u=1,
J_blank(omega)=J_opposite(omega)=J_perpendicular(omega),
one shared coefficient assigned to the complete complement,
a basis declaration that makes the three source directions identical.
```

`DERIVED-CB` requires an independently stated physical constraint whose full
nonzero solution set forces the equality from initially independent source
directions. Testing only the final response cannot establish provenance.

## 3. One joint six-mark interaction

Six separately chosen fixed-`f` responses do not define one physical bath
interaction. A candidate must supply a single Hermitian interaction of the
schematic form

```text
H_int=sum_f (|f><0| tensor D_f tensor B_f^dagger + h.c.),
```

with one bath, common source parameters, all six `D_f`, and simultaneous
proper-cubic covariance. The displayed form is a type template, not a supplied
Hamiltonian. The runner must check Hermiticity, cross-`f` parameter
compatibility, covariance on every profile, and CP/TP of the declared reduced
channel or instrument. A lookup table of `U_r` or host-selected binary query
is `ASSUMED-SELECTOR`.

## 4. Full complement symmetry is stronger than spatial symmetry

A unitary symmetry that mixes blank with the five nonmatching occupied marks
would not preserve the pointer's Record-status decomposition: blank is
unreadable and writable, while occupied marks are readable and permanently
locked. Such a symmetry is not the supplied proper-cubic action.

An interaction can nevertheless be blind on this complement without the
states themselves being symmetry-equivalent. That is a possible physical
coupling law, not a contradiction. The campaign must distinguish:

- symmetry of the pointer states;
- covariance of the bath dynamics; and
- a restriction on the interaction observable algebra.

## 5. Exact-return pure-catalyst control

For a pure bath state `|B>` and unitary `U`, suppose every occupied mark is
fixed and the bath returns exactly:

```text
U|f,B>=exp(i phi_f)|f,B>.
```

If

```text
U|0,B>=A|0,B>+sum_f B_f|f,B>,
```

then preservation of the inner products with every `|f,B>` forces `B_f=0`.
This is a narrow control, already available before Block21. It does not rule
out a mixed, correlated, extensive, approximate-return, or outcome-carrying
bath.

## 6. Append channels are nonunital

For a one-step append channel on the diagonal pointer algebra, write

```text
T(P_0)=hP_0+sum_f p_f P_f,
T(P_f)=P_f,
h+sum_f p_f=1.
```

Then

```text
T(I)=hP_0+sum_f(1+p_f)P_f.
```

It equals `I` only when every `p_f=0` and `h=1`. Thus every nontrivial
append-only Record channel is nonunital. This identity is elementary and must
be reconstructed by both implementations.

Rybár and Ziman's Theorem 2 in *Repeatable quantum memory channels*
(Phys. Rev. A 78, 052114 (2008), arXiv:0808.3851) applies to a fixed finite
memory, fixed unitary, initially factorized input systems, and the same CPTP
channel on every individual input for arbitrarily many uses. Its entropy
argument gives

```text
n [S(rho)-S(T(rho))]
  <= S(rho_B,n+1)-S(rho_B,1)
  <= log dim(K).
```

For a nonunital channel, the maximally mixed input has strictly positive
entropy decrease, so exact indefinite repeatability requires infinite memory.
The primary and independent runners must reconstruct this inequality and
verify the append channel's entropy decrease; a citation alone is not a
certificate.

This theorem does not forbid a fixed finite number of uses, an infinite or
growing reservoir, changed input-correlation semantics, approximate
repeatability, or a memory-bearing process. It also does not select beta.

## 7. Conditional instrument and reuse discriminator

Let one joint `U` act on a fresh target pointer, quantum neighbor controls,
and the same bath. If Record outcome `y` is declared, the construction must
state a CP instrument `J_y` and the subnormalized conditional bath state.
Zero-probability branches are excluded explicitly; no measurement may reset
or replace the bath.

After the first use, the bath conditional state can depend on the first
profile and outcome. The second conditional CP map is

```text
T_(r2 | r1,outcome1).
```

A Block19 Markov claim requires the visible conditional instrument to equal
the declared `J_y` for every allowed prior visible history, including
adaptive profile choices. Equality only after averaging a selected first-use
ensemble is not enough. Bath-state dependence alone also is not a visible
no-go: different hidden states may be visibly lumpable. Compare the induced
CP maps, not only bath marginals or classical probabilities.

Passing two uses is only a pre-gate. A fixed finite-bath positive claim must
also address arbitrary reuse; an extensive reservoir claim must instead
account for its growing/outgoing degrees of freedom and process limit.

A finite bath preloaded with `N` independent ready factors may pass `N` uses,
but this is a finite reservoir stock. It does not prove exact indefinite reuse
of one bath degree of freedom.

The runner must include a two-ready-factor counterexample: one fixed memory
contains two prepared factors plus an internal cursor, implements the target
channel on uses one and two, and fails or changes it on use three. This is a
positive control proving that a two-use certificate alone cannot establish
reuse.

Existing target marks and neighbor Records must be QND on **every reachable
bath state**, not only on the initial bath state. Any reverse transition after
a prior write fails permanent lock. Block19's fresh-vacuum boundary does not
supply this stronger statement.

## 8. Thermal and spectral relocation test

A relation such as

```text
beta=exp(-theta Delta E)
```

selects beta only if `theta Delta E` is fixed by independent physical
authority. Likewise a ratio of spectral densities or coupling constants is a
selector only if that ratio is derived. Choosing a temperature, gap,
spectral density, or interaction strength to obtain beta is an
`EQUIVALENT-GAP`, not positive closure.

One common state-independent rate may remain as `c`. Profile-dependent or
mark-dependent cadence cannot be hidden in that quotient.

## 9. Extensive reservoir and lattice ownership exits

An infinite translating or chiral reservoir can carry outcome information
away while continually presenting a stationary incoming local state. This
may be a valid autonomous open-system mechanism even though the global bath
does not return to its initial state. It remains live unless the campaign
explicitly constructs and tests it.

The route must expose the boundary state, transport law, outgoing archive,
coupling ratios, locality, and process limit. Calling incoming temporal modes
"the same reset bath" is insufficient.

One finite mediator reused across lattice sites additionally needs a physical
location, transport, interaction windows, ordering, and clock; otherwise the
sequence of `uses` is an external schedule. One finite bath per site is an
infinite distributed reservoir, not one finite reusable bath. A finite
mediator plus a growing archive is likewise `G_extensive`. These ownership
classes must not be merged.

## 10. Frozen execution matrix

The primary and independent implementations must separately evaluate:

1. all 24 proper-cubic rotations and the fixed-`f` orbit partition;
2. the invariant diagonal response dimension;
3. the `G_cov` source superfamily, constraint provenance, and hostile
   reparameterizations;
4. `o=p` membership before the Block19 beta projection and at least two
   distinct positive beta rays allowed before complement
   blindness is licensed;
5. one joint six-mark interaction type with cross-mark, CP/TP, and covariance
   checks rather than six selected tables;
6. the exact-return pure-catalyst inner-product control;
7. the append-channel nonunitality identity;
8. a declared finite two-use bath model, a two-ready-factor third-use failure,
   reachable-bath QND/lock checks, and the exact indefinite-repeatability
   entropy bound with its hypothesis matrix;
9. KMS/spectral parameter relocation; and
10. the `Z=9,10,12` beta discriminator without fitting.

If an item is not executed, its resolution line must say so. No failed finite
bath grammar may be promoted into a universal bath no-go.
