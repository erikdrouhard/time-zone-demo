# Time Zone Meeting Planner — PRD

## Overview
A single-page web app for comparing meeting times across global time zones. Users enter a time in their local timezone and instantly see the equivalent time in 10-12 major world cities, color-coded by meeting suitability.

## Tech Stack
- **Backend:** AIR framework (FastAPI-based)
- **Frontend:** HTMX for interactivity
- **No database** — stateless, no persistence required
- **UI**: Pico CSS

## Core Features

### 1. Time Input
- User selects their **reference timezone** from a dropdown (default: Washington DC / America/New_York)
- User enters a **time in AM/PM format** (e.g., "7:00 PM")
- On page load, pre-fill with current time in selected reference timezone

### 2. Time Zone Display
Show converted times for ~10-12 zones covering major regions:

| Region | Cities |
|--------|--------|
| Americas | San Francisco, Chicago, Washington DC, São Paulo |
| Europe | London, Paris |
| Middle East/Asia | Dubai, Mumbai, Singapore, Manila, Tokyo |
| Oceania | Sydney |

Each timezone card displays:
- **City name**
- **Converted time** in AM/PM format
- **Day indicator:** "today", "tomorrow", or "yesterday"

### 3. Color Coding (based on destination's local time)
| Color | Time Range | Meaning |
|-------|-----------|---------|
| Green (subtle) | 9 AM – 4 PM | Ideal business hours |
| Yellow | 6 AM – 9 AM, 4 PM – 10 PM | Inconvenient but possible |
| Red | 10 PM – 6 AM | Unacceptable |

## UI Requirements
- **Desktop:** Grid of timezone cards
- **Mobile:** Stacked cards, one per row
- Clean, minimal design — the color coding should be the primary visual guide
- Instant updates via HTMX when time or reference timezone changes

## Success Criteria
The MVP is complete when:

1. **Time entry works** — User can enter a time (e.g., "7:00 PM") and select a reference timezone from a dropdown
2. **Conversions are accurate** — All displayed times correctly reflect the timezone offset from the reference
3. **Day indicators are correct** — Each timezone shows "today", "tomorrow", or "yesterday" based on whether the converted time crosses midnight
4. **Color coding is visible at a glance** — User can quickly scan and identify suitable meeting times without reading each entry
5. **Updates are instant** — Changing time or reference timezone updates all cards without full page reload (HTMX)
6. **Global coverage** — At least 10 timezones spanning Americas, Europe, Asia, and Oceania are displayed

## Out of Scope (MVP)
- User accounts / authentication
- Date selection (always assumes "today")
- Session persistence
- Custom timezone lists
- Calendar integration
