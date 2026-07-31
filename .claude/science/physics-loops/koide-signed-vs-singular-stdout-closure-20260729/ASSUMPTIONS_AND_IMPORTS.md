# Assumptions and imports

## Import ledger

No framework, observation, literature value, fitted selector, unit convention,
or same-surface family argument is load-bearing. The mathematical inputs are:

- `a>0`, `theta` real, and the displayed real circulant spectrum;
- `r=1/2` only for the specialized boundary;
- root-of-unity/trigonometric identities, equality in the real triangle
  inequality, and exact symbolic arithmetic;
- SymPy as an implementation of those checks, not as a premise.

`2/3` is both an exactly derived value of the signed readout at `r=1/2` and the
stated phenomenological comparator; no observed mass is used.

## Counterfactual pass

| Choice | If changed | Effect |
|---|---|---|
| signed readout `lambda_k` | replace by `|lambda_k|` | this is the theorem's compared branch; numerator stays fixed and denominator changes |
| `r=1/2` | allow arbitrary `r` | the general conclusion narrows to `Q(V)<Q(S)`; `Q(V)<2/3` is no longer universal |
| closed zero-mode boundary | exclude `theta=pi/12` | incorrectly turns the equality set into an open window |
| exact symbolic checks | use float-only samples | supports examples but does not prove the identities or exact boundary |
| verbose transcript | compact successful details | scientific assertions are unchanged; complete transport becomes possible |

No counterfactual opens a missing physics route because this cycle repairs
evidence transport, not the theorem's scientific premises.
