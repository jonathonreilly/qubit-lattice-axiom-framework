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
grammar. That equality must not be attributed to the cubic stabilizer.

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

## 3. Full complement symmetry is stronger than spatial symmetry

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

## 4. Exact-return pure-catalyst control

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

## 5. Append channels are nonunital

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

## 6. Two-use memory discriminator

Let `U_r` act on a fresh target pointer and the same bath, with profile `r`.
After the first use, the bath conditional state can depend on `r` and the
written outcome. The second reduced channel is

```text
T_(r2 | r1,outcome1).
```

A Block19 Markov claim requires this to equal `T_r2` for every first profile
and outcome. Equality only after averaging a selected first-use ensemble is
not enough. If dependence remains, the result is a memory process and the
Block19 finite-history/Harris proof cannot be imported unchanged.

Passing two uses is only a pre-gate. A fixed finite-bath positive claim must
also address arbitrary reuse; an extensive reservoir claim must instead
account for its growing/outgoing degrees of freedom and process limit.

A finite bath preloaded with `N` independent ready factors may pass `N` uses,
but this is a finite reservoir stock. It does not prove exact indefinite reuse
of one bath degree of freedom.

## 7. Thermal and spectral relocation test

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

## 8. Extensive reservoir exit

An infinite translating or chiral reservoir can carry outcome information
away while continually presenting a stationary incoming local state. This
may be a valid autonomous open-system mechanism even though the global bath
does not return to its initial state. It remains live unless the campaign
explicitly constructs and tests it.

The route must expose the boundary state, transport law, outgoing archive,
coupling ratios, locality, and process limit. Calling incoming temporal modes
"the same reset bath" is insufficient.

## 9. Frozen execution matrix

The primary and independent implementations must separately evaluate:

1. all 24 proper-cubic rotations and the fixed-`f` orbit partition;
2. the invariant diagonal response dimension;
3. the Block19 pair-factor slice and the exact complement-blind projection;
4. at least two distinct positive beta rays allowed before complement
   blindness is licensed;
5. the exact-return pure-catalyst inner-product control;
6. the append-channel nonunitality identity;
7. a declared finite two-use bath model and the exact indefinite-repeatability
   entropy bound with its hypothesis matrix;
8. KMS/spectral parameter relocation; and
9. the `Z=9,10,12` beta discriminator without fitting.

If an item is not executed, its resolution line must say so. No failed finite
bath grammar may be promoted into a universal bath no-go.
