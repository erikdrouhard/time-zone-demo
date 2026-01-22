# Time Zone Meeting Planner

A single-page web app for comparing meeting times across global time zones. Enter a time in your local timezone and instantly see the equivalent time in 12 major world cities, color-coded by meeting suitability.

## Features

- Select your reference timezone from 12 major cities
- Enter a meeting time and see it converted across all zones
- Color-coded cards indicate meeting suitability:
  - **Green** — Ideal business hours (9 AM – 4 PM)
  - **Yellow** — Inconvenient but possible (6–9 AM, 4–10 PM)
  - **Red** — Unacceptable (10 PM – 6 AM)
- Day indicators show "today", "tomorrow", or "yesterday" for times crossing midnight
- Instant updates via HTMX — no page reload required

## Cities Covered

| Region | Cities |
|--------|--------|
| Americas | San Francisco, Chicago, Washington DC, São Paulo |
| Europe | London, Paris |
| Middle East/Asia | Dubai, Mumbai, Singapore, Manila, Tokyo |
| Oceania | Sydney |

## Requirements

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Quick Start

```bash
# Clone and enter the project
cd zero-plan

# Install dependencies
uv sync

# Run the app
uv run air main.py
```

Then open your browser to the URL shown (typically http://localhost:8000).

## Tech Stack

- **Backend:** [AIR framework](https://github.com/anthropics/anthropic-quickstarts/tree/main/air) (FastAPI-based)
- **Frontend:** HTMX for interactivity
- **Styling:** Pico CSS
- **No database** — fully stateless
