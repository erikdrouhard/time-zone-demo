import air
from datetime import datetime
from zoneinfo import ZoneInfo

app = air.Air()

# Timezone data: (display_name, IANA timezone)
TIMEZONES = [
    ("San Francisco", "America/Los_Angeles"),
    ("Chicago", "America/Chicago"),
    ("Washington DC", "America/New_York"),
    ("São Paulo", "America/Sao_Paulo"),
    ("London", "Europe/London"),
    ("Paris", "Europe/Paris"),
    ("Dubai", "Asia/Dubai"),
    ("Mumbai", "Asia/Kolkata"),
    ("Singapore", "Asia/Singapore"),
    ("Manila", "Asia/Manila"),
    ("Tokyo", "Asia/Tokyo"),
    ("Sydney", "Australia/Sydney"),
]


def get_current_time_in_tz(tz_name: str) -> tuple[int, int]:
    """Get current hour and minute in a timezone."""
    now = datetime.now(ZoneInfo(tz_name))
    return now.hour, now.minute


def get_color_for_hour(hour: int) -> str:
    """Return background color based on local hour."""
    if 9 <= hour < 16:  # 9 AM - 4 PM (before 4pm)
        return "#d4edda"  # subtle green
    elif (6 <= hour < 9) or (16 <= hour < 22):  # 6-9 AM or 4-10 PM
        return "#fff3cd"  # subtle yellow
    else:  # 10 PM - 6 AM
        return "#f8d7da"  # subtle red


def format_time_12h(hour: int, minute: int) -> str:
    """Format time in 12-hour AM/PM format."""
    am_pm = "AM" if hour < 12 else "PM"
    display_hour = hour % 12
    if display_hour == 0:
        display_hour = 12
    return f"{display_hour}:{minute:02d} {am_pm}"


def convert_time(ref_tz: str, hour: int, minute: int, target_tz: str) -> tuple[int, int, str]:
    """Convert time from reference timezone to target timezone.
    Returns (hour, minute, day_indicator).
    """
    # Create a datetime in the reference timezone for today
    ref_zone = ZoneInfo(ref_tz)
    target_zone = ZoneInfo(target_tz)

    today = datetime.now(ref_zone).date()
    ref_dt = datetime(today.year, today.month, today.day, hour, minute, tzinfo=ref_zone)

    # Convert to target timezone
    target_dt = ref_dt.astimezone(target_zone)

    # Determine day indicator
    target_date = target_dt.date()
    if target_date == today:
        day_indicator = "today"
    elif target_date > today:
        day_indicator = "tomorrow"
    else:
        day_indicator = "yesterday"

    return target_dt.hour, target_dt.minute, day_indicator


@app.get("/")
async def index():
    # Default to Washington DC, current time, today's date
    default_tz = "America/New_York"
    hour, minute = get_current_time_in_tz(default_tz)
    today_str = datetime.now(ZoneInfo(default_tz)).strftime("%Y-%m-%d")

    # Convert to 12-hour format
    am_pm = "AM" if hour < 12 else "PM"
    display_hour = hour % 12
    if display_hour == 0:
        display_hour = 12

    return air.layouts.picocss(
        air.Div(
            air.H1("Time Zone Meeting Planner"),
            air.P("Enter a time to see it across major time zones"),

            # Input form
            air.Form(
                air.Fieldset(
                    air.Label("Your timezone", _for="ref_tz"),
                    air.Select(
                        *[air.Option(name, value=tz, selected=(tz == default_tz))
                          for name, tz in TIMEZONES],
                        name="ref_tz",
                        id="ref_tz",
                    ),
                    air.Label("Time", _for="time_input"),
                    air.Input(
                        type="time",
                        name="time_input",
                        id="time_input",
                        value=f"{hour:02d}:{minute:02d}",
                    ),
                    air.Label("Date", _for="date_input"),
                    air.Input(
                        type="date",
                        name="date_input",
                        id="date_input",
                        value=today_str,
                    ),
                ),
                hx_get="/convert",
                hx_trigger="load, change",
                hx_target="#results",
            ),

            # Results container
            air.Div(id="results"),

            style="max-width: 1200px; margin: 0 auto; padding: 2rem;",
        ),
        title="Time Zone Planner",
    )


@app.get("/convert")
async def convert(ref_tz: str = "America/New_York", time_input: str = "12:00", date_input: str = ""):
    """Convert time to all timezones and return cards."""
    # Parse the date input (YYYY-MM-DD format from HTML date input)
    if date_input:
        try:
            selected_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            selected_date = datetime.now(ZoneInfo(ref_tz)).date()
    else:
        selected_date = datetime.now(ZoneInfo(ref_tz)).date()
    # Parse the time input (HH:MM format from HTML time input)
    try:
        hour, minute = map(int, time_input.split(":"))
    except ValueError:
        hour, minute = 12, 0

    cards = []
    for name, tz in TIMEZONES:
        target_hour, target_minute, day_ind = convert_time(ref_tz, hour, minute, tz)
        color = get_color_for_hour(target_hour)
        time_str = format_time_12h(target_hour, target_minute)

        cards.append(
            air.Article(
                air.Header(air.Strong(name)),
                air.P(time_str, style="font-size: 1.5rem; margin: 0;"),
                air.Small(day_ind),
                style=f"background-color: {color}; text-align: center; padding: 1rem;",
            )
        )

    return air.Div(
        *cards,
        style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;",
    )