# POKEMON Protocol - Product Campaign Demo
# Author: Queen Osuji, VXP
# IMPORTANT: This is a conceptual simulation. No real API calls are made.

import time

# --- Simulated External API Functions ---

def call_text_generation_api(prompt, api_key="YOUR_FREE_API_KEY_HERE"):
    print(f"[TEXT_GEN_API] Called with prompt: '{prompt}'")
    time.sleep(1)
    if "brainstorm ideas for a new eco-friendly water bottle" in prompt:
        return "Simulated Ideas: 1. Self-filtering straw. 2. Made from ocean plastic. 3. Collapsible design."
    elif "write a short ad copy" in prompt:
        return f"Simulated Ad Copy: Discover the innovative AquaPure bottle! {prompt.split(':')[-1].strip()}"
    return "Simulated text generation response."

def call_image_search_api(query, api_key="YOUR_FREE_API_KEY_HERE"):
    print(f"[IMAGE_SEARCH_API] Called with query: '{query}'")
    time.sleep(1)
    return f"Simulated image URL for '{query}': http://example.com/{query.replace(' ', '_')}.jpg"

# --- Demo Starts Here ---

print("\n CogniMon Protocol Demo: Eco-Friendly Product Campaign")
print("-" * 50)

#  User Goal:
print(" Goal: Develop a campaign for a new eco-friendly water bottle.\n")

# 1. BrainstormingCogniMon (Idea Generation)
prompt1 = "System: You are BrainstormingCogniMon. Task: brainstorm ideas for a new eco-friendly water bottle."
ideas = call_text_generation_api(prompt1)
print(f" BrainstormingCogniMon Output:\n{ideas}\n" + "-" * 50)

# 2. CopywritingCogniMon (Ad Copy Generation)
chosen_idea_detail = ideas.split('. ')[1]  # e.g., "Made from ocean plastic"
prompt2 = f"System: You are CopywritingCogniMon. Task: write a short ad copy for an eco-friendly water bottle. Feature to highlight: {chosen_idea_detail}"
ad_copy = call_text_generation_api(prompt2)
print(f" CopywritingCogniMon Output:\n{ad_copy}\n" + "-" * 50)

# 3. VisualConceptCogniMon (Visual Asset Concept)
image_query = f"eco-friendly water bottle {chosen_idea_detail}"
image_url = call_image_search_api(image_query)
print(f" VisualConceptCogniMon Output:\nSuggested image for '{image_query}' - {image_url}\n" + "-" * 50)

#  Campaign Assembled
print(" Campaign elements assembled successfully!")
print("-" * 50)
print(" What You Now Have:")
print(f"1. Idea: {chosen_idea_detail}")
print(f"2. Ad Copy: {ad_copy}")
print(f"3. Visual Concept: {image_url}")
print("-" * 50)
