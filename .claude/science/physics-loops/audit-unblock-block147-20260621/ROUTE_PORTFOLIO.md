# Route Portfolio

1. Add a lane-opening wrapper runner and register it.
   - Action: verify planning-only note boundary and execute existing teleportation/signed-gravity first-artifact checks.
   - Outcome: selected and completed.

2. Register only one teleportation runner.
   - Outcome: rejected because the note opens multiple lanes.

3. Register the signed-gravity status runner directly.
   - Outcome: rejected because this row is the parent lane-opening note, not the signed-gravity status note.

4. Promote any opened lane.
   - Outcome: rejected. This is an open-gate note only.

