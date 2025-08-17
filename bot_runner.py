#!/usr/bin/env python3
from datetime import datetime
from personal_assistant import PersonalAssistant
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

assistant = PersonalAssistant(BOT_TOKEN, CHAT_ID)

now = datetime.now()
hour = now.hour
weekday = now.weekday()  # Monday=0

# Morning routine 7:00
if hour == 7:
    assistant.morning_routine()

# Habit tracker 18:00
if hour == 18:
    assistant.habit_tracker_reminder()

# Evening reflection 21:00
if hour == 21:
    assistant.evening_reflection()

# Weekly planning Monday 9:00
if weekday == 0 and hour == 9:
    assistant.weekly_planning()

# Weekend planning Saturday 10:00
if weekday == 5 and hour == 10:
    assistant.weekend_planning()

# Motivation & productivity every run
assistant.motivational_boost()
assistant.productivity_tips()
