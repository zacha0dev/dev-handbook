
# Practical Tech Projects You Can Build

These three ideas blend design, automation, and everyday usefulness. They’re realistic to start small, yet expandable into full home-integration systems.

---

### 1. Personal Homepage / Dashboard
**Goal:** Create a private homepage that opens every time you start your browser.  
**Purpose:** Centralize everything that matters - quick links, tasks, notes, weather, and a motivational message.

**Core build:**
- HTML + CSS + JS (or React for structure)
- Store preferences and theme locally in browser storage or a small SQLite DB
- Add widgets: time/date, to-do list, bookmarks, weather, quote of the day
- Optional integrations: Google Calendar, Spotify, or local files

**Stretch goals:**
- Dark/light themes that auto-switch
- Keyboard shortcuts (`Ctrl + Space` to open quick-launch)
- Personal analytics (track most-used links or tasks)

---

### 2. Custom Google Home Dashboard
**Goal:** Replace the cluttered mobile app with a clean web or desktop control hub.  
**Purpose:** One page to manage Google Home scenes, devices, and automations.

**Core build:**
- React or simple HTML dashboard + Python/FastAPI backend
- Use the Google Home Graph API (read devices, execute commands)
- Create grouped “Scenes” like *Morning*, *Work Mode*, *Movie Night*
- Add on/off toggles, brightness sliders, and sensor readouts

**Stretch goals:**
- Save custom automation scripts (turn off lights + lock doors + send reminder)
- Local dashboard hosting on Raspberry Pi
- Sync settings to a cloud DB (Supabase, Firebase) for remote access

---

### 3. Home Info Display (Companion Screen)
**Goal:** A small always-on display that shows key info: time, weather, current mode, and alerts.  
**Purpose:** Give your space a subtle live dashboard that syncs with your other tools.

**Core build:**
- Raspberry Pi + small HDMI or e-ink display
- Lightweight web UI served from Pi (Flask or Node)
- Displays pulled data: weather API, Google Calendar, device states
- Refreshes automatically every few minutes

**Stretch goals:**
- Add voice or motion activation
- Display notifications from your main dashboard (new tasks, timers, etc.)
- Integrate with Home Assistant or MQTT for real-time device updates

---

### Combined Vision
Together, these projects can evolve into your own **personal environment network**:  
- The **homepage** lives in your browser.  
- The **Google Home dashboard** manages devices.  
- The **info display** reflects status and feedback in your physical space.  

Start with one - probably the homepage - and let it naturally grow into the next. Each layer adds a new skill: front-end design → API integration → hardware deployment.
