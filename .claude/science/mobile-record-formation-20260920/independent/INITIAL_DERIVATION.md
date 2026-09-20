# Independent check: third birth on the six-site ladder

Initial independent derivation, 2026-09-20. Computation and final evidence are
pending below; the primary agent's `probe.py`, `probe.json`, and `CHECKPOINT.md`
have not been read. This file was first written before any comparison with the
primary agent's result.

## Analytic result derived before implementation

Let `g(s)` be the product of occupied-edge weights and let
`b(s;x,a) = g(s + (x,a))/g(s)`. Write `B(s) = sum_(x,a) b(s;x,a)`.
On a finite irreducible motion component `C`, motion has stationary law
`pi_C(s) = g(s)/Z_C`. The state immediately before a rare birth is instead

```
nu_C(s) = pi_C(s) B(s) / <B>_pi_C.
P(prestate=s, birth=(x,a)) = pi_C(s) b(s;x,a) / <B>_pi_C.
```

For a component entrance law `alpha`, the exact finite-epsilon joint law is
`epsilon [alpha (epsilon diag(B) - Q_C)^(-1)](s) b(s;x,a)`.
The rare-event expression follows because any subsequential limit of
`epsilon alpha (epsilon diag(B) - Q_C)^(-1)` is stationary for `Q_C`, while
its product with `B` has mass one. Positivity and finiteness bound the vector,
and irreducibility identifies the unique limit as `pi_C/<B>_pi_C`.

With one record, `B=30` and sites are uniform. The second record agrees with
the first with probability `(5 + (1/2)(14/6))/30 = 37/180`.

For two identical records, the pair placement partition sum is
`Z_aa = 7(3/2) + 8 = 37/2`. Of the eight nonadjacent pairs, two have one
common neighbor, four have two, and two have none. Adjacent pairs have no
common neighbor. Thus `B(s)=24 + m(s)/2` and

```
sum_s g(s) B(s) = 24(37/2) + (1/2)(2 + 8) = 449.
```

The 20 three-site subsets have respectively 0, 1, and 2 occupied edges with
multiplicities 2, 8, and 10. Hence `Z_aaa = 2 + 8(3/2) + 10(3/2)^2 = 73/2`.
Each all-identical triple can be reached by three deletions, giving
`sum_s g(s) sum_x b(s;x,a) = 3 Z_aaa = 219/2`. Therefore

```
P(all three identical immediately after third birth, epsilon -> 0)
  = (37/180) (219/898)
  = 2701/53880.
```

For the static law conditioned on three occupied sites, every induced graph
is a forest and every row of `W` sums to six. Summing over the leaf content
successively therefore gives 216 per occupied triple. The total partition
sum is `20*216=4320`; the identical-content weight is `6*(73/2)=219`.
Consequently the static probability is `73/1440`, and the dynamic/static
ratio is `444/449`.

These are candidate exact calculations awaiting the separate enumeration
and finite-epsilon resolvent checks. Connectivity by content counts on the
needed levels will be checked exhaustively rather than presumed.
