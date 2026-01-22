# SPEC.md

## Current Spec

### Overview
- **App Name:** Time Zone Meeting Planner
- **Target User:** Remote workers, distributed teams, and anyone scheduling meetings across time zones
- **Problem Solved:** Quickly determine if a proposed meeting time works for participants in different cities by showing converted times with at-a-glance suitability indicators

### Fidelity
- **Current Stage:** Prototype / MVP
- **Scope:** Single-page stateless app, no authentication, no persistence

### Form Factor
- **Type:** Web app
- **Platform:** All platforms (browser-based)
- **Responsive:** Desktop (grid layout) and mobile (stacked cards)

### Core Features
1. **Time Input**
   - Dropdown to select reference timezone (default: Washington DC / America/New_York)
   - Time entry field in AM/PM format (e.g., "7:00 PM")
   - Pre-fill with current time in selected reference timezone on page load

2. **Time Zone Display**
   - Show converted times for 10-12 major world cities:
     - Americas: San Francisco, Chicago, Washington DC, São Paulo
     - Europe: London, Paris
     - Middle East/Asia: Dubai, Mumbai, Singapore, Manila, Tokyo
     - Oceania: Sydney
   - Each card displays: city name, converted time (AM/PM), day indicator (today/tomorrow/yesterday)

3. **Color-Coded Suitability**
   - Green: 9 AM – 4 PM (ideal business hours)
   - Yellow: 6 AM – 9 AM, 4 PM – 10 PM (inconvenient but possible)
   - Red: 10 PM – 6 AM (unacceptable)

4. **Instant Updates**
   - Time or timezone changes update all cards without full page reload

### Technology Choices

**Language & Framework:**
- Python (FastAPI via AIR framework)
- HTMX for frontend interactivity
- Jinja2 templates

**UI:**
- Pico CSS for styling

**Infrastructure:**
- No database required (stateless)
- No cloud services required for MVP

### Out of Scope (MVP)
- User accounts / authentication
- Date selection (always assumes "today")
- Session persistence
- Custom timezone lists
- Calendar integration

### Success Criteria
1. User can enter a time and select a reference timezone
2. All displayed times correctly reflect timezone offsets
3. Day indicators (today/tomorrow/yesterday) are accurate when crossing midnight
4. Color coding is visible at a glance for quick scanning
5. Changes update instantly via HTMX without page reload
6. At least 10 timezones spanning Americas, Europe, Asia, and Oceania are displayed

---

## Implementation Status

*Last updated: 2025-01-21*

### Core Features

| Feature | Status | Notes |
|---------|--------|-------|
| Reference timezone dropdown | ✅ Complete | 12 cities, defaults to Washington DC |
| Time input field | ✅ Complete | Uses HTML5 time picker (24h on some browsers) |
| Pre-fill current time | ✅ Complete | Loads current time in reference timezone |
| 12 timezone cards | ✅ Complete | All regions covered |
| Converted time display (AM/PM) | ✅ Complete | `format_time_12h()` in main.py |
| Day indicator | ✅ Complete | Shows today/tomorrow/yesterday |
| Color-coded suitability | ✅ Complete | Green/yellow/red based on local hour |
| HTMX instant updates | ✅ Complete | Triggers on input change |
| Responsive grid layout | ✅ Complete | CSS grid with auto-fill |

### Success Criteria Status

| Criterion | Status |
|-----------|--------|
| 1. Time entry + timezone selection | ✅ Met |
| 2. Accurate timezone conversions | ✅ Met |
| 3. Correct day indicators | ✅ Met |
| 4. Visible color coding | ✅ Met |
| 5. Instant HTMX updates | ✅ Met |
| 6. 10+ timezones displayed | ✅ Met (12 cities) |

### Known Limitations

- Time input uses browser-native HTML5 time picker, which displays in 24-hour format on some browsers/platforms
- Mobile layout relies on CSS grid auto-sizing (not explicitly tested on all devices)

### Files

| File | Purpose |
|------|---------|
| `main.py` | All application logic — routes, timezone conversion, rendering |
| `pyproject.toml` | Dependencies (air framework) |
| `hello.py` | Sanity check / hello world |
