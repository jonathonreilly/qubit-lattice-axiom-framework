# Assumptions and imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Open 3D Wilson lattice and displayed numerical parameters | Defines the sampled model | admitted finite-model specification | primary/helper runner source | yes | yes | keep explicit; bounded theorem only | declared |
| Shared-minus-self centroid observable | Defines the sampled mutual channel | admitted observable definition | runner source | yes | yes | alternate observables remain outside scope | declared |
| Five-value distance grid | Defines the finite calibration | computed lattice input | sweep runner/cache | yes | yes | complete SHA-pinned cache | pending |
| Both-masses pass thresholds | Defines only a finite diagnostic, not a theorem of nature | admitted diagnostic convention | both-masses runner | no for the positive sweep; yes for the diagnostic wording | only if diagnostic retained | print criteria and nonpass explicitly | pending |
| Registered framework primitives | No role in this finite computation | not applicable | primitive-registry check | no | no | none | not invoked |

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| Centroid shared-minus-self is the useful mutual readout | It may mix mutual response with common propagation effects | local momentum flux | could establish action-reaction on another observable | live, outside scope | 2 |
| Fixed side/G/d grid captures a universal law | It does not | larger-volume/continuum sweep | tests robustness but cannot change this finite certificate | live, outside scope | 1 |
| Both-masses diagnostic thresholds define Newton closure | They do not define a universal theorem | derive a continuum Ward/flux criterion | could support a stronger theorem | live, outside scope | 2 |
