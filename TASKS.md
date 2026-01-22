# TASKS.md

## Current Session: Add Date Picker

**Goal:** Allow users to select a specific date for meeting planning instead of always using "today"

### AI Coding Agent Tasks
- [x] Add date input field to the form in `main.py` (default: today's date)
- [x] Update `/convert` endpoint to accept `date_input` parameter
- [x] Modify `convert_time()` function to use selected date instead of `datetime.now().date()`
- [x] Fix day indicator logic to compare against selected date, not today
- [ ] Update SPEC.md — move "Date selection" from Out of Scope to Core Features, update Implementation Status
- [ ] Update README.md — add date picker to features list

### Human Developer Tasks
- [ ] Test: Select tomorrow's date → verify day indicators still make sense
- [ ] Test: Select a date far in the future → verify conversions are correct
- [ ] Test: Verify HTMX updates work when changing date

### Acceptance Criteria
- [ ] User can pick any date from the date input
- [ ] Time conversions use the selected date for DST calculations
- [ ] Day indicators show relative to selected date (not today)
- [ ] Default is today's date on page load
