def create_prompt(destination, days, budget, travel_style, interests):

    prompt = f"""
You are an expert travel planner.

Create a personalized travel itinerary.

Destination: {destination}

Duration: {days} days

Budget: ₹{budget}

Travel Style: {travel_style}

Interests: {", ".join(interests)}

Generate the itinerary using proper Markdown.

Use EXACTLY this format:

# 🌍 Trip Overview

Write a short introduction.

---

# 📅 Day 1

## 🌅 Morning

- Mention places to visit
- Mention breakfast
- Mention transport

## ☀️ Afternoon

- Mention attractions
- Suggest lunch
- Mention shopping if available

## 🌙 Evening

- Mention sunset point
- Suggest dinner
- Mention nightlife if applicable

## 💰 Estimated Cost

- Accommodation:
- Food:
- Transport:
- Activities:
- Total:

---

# 📅 Day 2

Follow the same format as Day 1.

---

# 📅 Day 3

Follow the same format as Day 1.

Continue similarly until Day {days}.

---

# 🍽️ Food Recommendations

- Mention famous local dishes.
- Mention the best restaurants.

---

# 🛍️ Shopping Guide

- Best markets
- Best souvenirs
- Approximate prices

---

# 💰 Budget Summary

Create a Markdown table.

| Category | Cost |
|----------|------|
| Accommodation | ₹ |
| Food | ₹ |
| Transport | ₹ |
| Activities | ₹ |
| Shopping | ₹ |
| Total | ₹ |

---

# ✈️ Travel Tips

Give at least 5 useful travel tips.

Use Markdown headings (# and ##), bullet points, and make important place names and restaurant names **bold**.
"""

    return prompt