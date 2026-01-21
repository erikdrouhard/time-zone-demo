I'm looking to build an app. I'm in a directory which has a quick start guide for AIR, which is a web development framework built on top of FastAPI. I would like to use AIR to create this application and have the interactivity use HTMX. 

I would like this to be an app that the user can go in and put in their time in in AM/PM format, select a time they might like to meet, where they can compare it to a lot of other major time zones. that start with maybe San Francisco, Chicago, Washington DC, a few European time zones, Manila time, Australia, maybe Sydney, whatever some of the standard ones are, like the big ones. Make sure it's kind of worldwide. We don't need every single one. Just pick a decent number that covers the big regions. 

When I select a time, I would like to show what those times are in those time zones. For example, I'm in Washington, DC. if I say Washington, DC at 7:00 PM. That's my time. They wanted to give me the time in all the others. Washington DC will just show 7:00 PM. We don't need any fancy conversation, conversation, rather conversion there. other zones should show different information. For example, the European time zones, London is five hours ahead. So it should show that. for Manila, I believe that's a 12 hour gap. So if I say 7:00 PM Washington DC, it should show 7:00 AM Manila tomorrow, tomorrow or 4:00 PM San Francisco today and so on. I'm not putting in any data selectors, but it should indicate whether that particular time is today, yesterday, or tomorrow depending on the time zone entered. 


I also just want it to really be easy. I don't want to read them all to find good times. So when I enter a time, make things a very light, subtle green. if they're a good, convenient business time, something like say 9am or 4pm local time if it's something like 6am to 9am or 4pm to 10pm and make it yellow as inconvenient. it. And if it's outside outside of that like 10 p.m. to 6 a.m. it should read as red as an unacceptable time to meet. 

This is an MVP. I want to keep it simple. I do not need multi-user or authentication. You can put everything in a local session. I just want to get a simple proof of concept first.

---

## Clarifications (with defaults)

1. **Reference timezone selection** — Should users select their own timezone from a dropdown, or fixed default?
   - *Default: Dropdown to select reference timezone, defaulting to Washington DC (America/New_York)*

2. **Color coding basis** — Green/yellow/red based on the destination timezone's local time?
   - *Default: Yes, color each timezone based on its own local time (e.g., 7 AM Manila gets colored based on whether 7 AM is acceptable there)*

3. **Initial state** — What to display before user enters a time?
   - *Default: Pre-fill with current time in the selected reference timezone*

4. **Number of timezones** — How many to display?
   - *Default: ~10-12 covering major regions (US West/Central/East, London, Paris, Dubai, Mumbai, Singapore, Manila, Tokyo, Sydney)*

5. **Output time format** — AM/PM or 24-hour?
   - *Default: AM/PM to match input format*

6. **Session persistence** — Persist last entered time on refresh?
   - *Default: No persistence, start fresh each visit (simpler for MVP)*

7. **Mobile layout** — Display preference on mobile?
   - *Default: Stacked cards, one timezone per row*