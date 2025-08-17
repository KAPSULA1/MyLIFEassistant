#!/usr/bin/env python3
"""
Personal Life Assistant Bot
Fully automated Telegram life assistant
"""

import requests
import random
from datetime import datetime

class PersonalAssistant:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def send_telegram(self, message):
        """Send message via Telegram bot"""
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        try:
            response = requests.post(url, data=data, timeout=30)
            if response.status_code == 200:
                print("✅ Message sent successfully")
            else:
                print(f"❌ Failed to send message: {response.status_code}")
        except Exception as e:
            print(f"❌ Telegram error: {e}")

    def morning_routine(self):
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        current_time = datetime.now().strftime("%H:%M")
        motivational_starts = [
            "🌅 Rise and shine!", "☀️ Good morning, champion!",
            "🌟 Start your day with purpose!", "💪 Ready to conquer today?",
            "🚀 Let's make today amazing!"
        ]
        daily_tips = [
            "Start with your most challenging task while your mind is fresh",
            "Set 3 clear priorities for today and focus on them",
            "Take breaks every 90 minutes to maintain peak performance",
            "Stay hydrated - aim for a glass of water every hour",
            "Practice gratitude - name 3 things you're thankful for"
        ]
        message = f"""
{random.choice(motivational_starts)}

📅 <b>Today is {current_date}</b>
⏰ Current time: {current_time}

🎯 <b>Daily Focus Questions:</b>
• What are your top 3 priorities today?
• What would make today feel successful?
• How can you move closer to your long-term goals?

💡 <b>Today's Success Tip:</b>
{random.choice(daily_tips)}

🌈 Remember: Every small step counts toward your bigger dreams!

Have an amazing day! ✨
"""
        self.send_telegram(message)

    def habit_tracker_reminder(self):
        habit_categories = {
            "Health & Wellness": ["💧 Drink 8 glasses of water", "🏃‍♂️ 20+ min exercise", "🧘‍♀️ 5 min meditation"],
            "Personal Growth": ["📚 Read 15+ min", "📝 Journal", "🎧 Listen to educational content"],
            "Productivity": ["🎯 Complete #1 priority", "📱 Limit social media to 30 mins", "🛏️ Prepare tomorrow's tasks"]
        }
        message = "📋 <b>Daily Habit Check-in</b>\n\nTime to review your positive habits:\n\n"
        for category, habits in habit_categories.items():
            message += f"<b>{category}:</b>\n"
            for habit in habits:
                message += f"• {habit}\n"
            message += "\n"
        message += "✅ <b>How many did you complete today?</b>\n\n🏆 <b>Consistency beats perfection!</b>"
        self.send_telegram(message)

    def evening_reflection(self):
        reflection_prompts = [
            "What was the highlight of your day?",
            "What challenge did you overcome today?",
            "How did you grow or learn today?",
            "What moment made you smile today?",
            "What are you most proud of today?"
        ]
        message = f"""
🌙 <b>Evening Reflection Time</b>

Take a moment to reflect and appreciate your day:

📚 <b>Today's Learning:</b>
• {random.choice(reflection_prompts)}

🙏 <b>Gratitude Moment:</b>
• Name 3 things you're grateful for today

🎯 <b>Tomorrow's Focus:</b>
• What's your ONE priority for tomorrow?

😴 <b>Rest Well</b> – You've earned your rest!
"""
        self.send_telegram(message)

    def weekly_planning(self):
        week_start = datetime.now().strftime("%B %d")
        message = f"""
📅 <b>Weekly Planning Session</b>
Week of {week_start}

🔍 <b>Last Week Review:</b>
• Wins, challenges, lessons

🎯 <b>This Week's Priorities:</b>
• Top 5 goals
• Biggest impact goal

🏃‍♂️ <b>Habit Check:</b>
• Which habits served you well last week?
• Pick ONE new habit to focus on

💪 <b>Self-Care Plan:</b>
• Schedule downtime

🚀 <b>Success Mantra:</b> "Plan your week, win your week!"
"""
        self.send_telegram(message)

    def weekend_planning(self):
        message = """
🎉 <b>Weekend Vibes!</b>

🛋️ Recharge:
• Nature, hobbies, rest
📋 Gentle Productivity:
• Review wins, prep next week
🌱 Personal Growth:
• Read, learn, journal
⚡ Energy Boost:
• Move body, smile

🎯 Enjoy your weekend! 🌟
"""
        self.send_telegram(message)

    def motivational_boost(self):
        messages = [
            {"quote":"🚀 'Start doing, not just talking.'", "tip":"Take one small action now!"},
            {"quote":"💪 'Success is courage to continue.'", "tip":"Every setback = setup for comeback!"},
            {"quote":"🌟 'Only impossible journey is unstarted.'", "tip":"Start where you are!"}
        ]
        selected = random.choice(messages)
        message = f"""
💫 <b>Motivation Boost!</b>

{selected['quote']}

💡 <b>Action Tip:</b> {selected['tip']}
"""
        self.send_telegram(message)

    def productivity_tips(self):
        tips = [
            "🍅 Try Pomodoro: 25 min work / 5 min break",
            "📱 Put phone in another room to focus",
            "🎵 Use instrumental or white noise to focus",
            "🧹 Organize workspace before work"
        ]
        tip = random.choice(tips)
        message = f"🧠 <b>Productivity Tip:</b>\n{tip}"
        self.send_telegram(message)
