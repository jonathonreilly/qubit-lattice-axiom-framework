# Literature Bridges

No new literature bridge is introduced.

The existing `I_S in [4,10]` literature bracket remains a supplied conditional
comparison bracket. This PR neither validates it as framework-native nor removes
it. The source-side repair prevents an invalid native-BZ route from pretending
to retire that import.
