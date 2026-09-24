import os
import random
import requests

COUNT_FILE = "views_count.txt"
SVG_FILE = "views.svg"

# Initialize with God-tier number if it doesn't exist
if not os.path.exists(COUNT_FILE):
    current_count = 14892
else:
    with open(COUNT_FILE, "r") as f:
        current_count = int(f.read().strip())

# Increment by realistic organic traffic (15 to 45 views)
increment = random.randint(15, 45)
new_count = current_count + increment

with open(COUNT_FILE, "w") as f:
    f.write(str(new_count))

# Format with commas
formatted_count = f"{new_count:,}"

# Download the badge
url = f"https://img.shields.io/badge/Profile%20Views-{formatted_count}-7c3aed?style=flat-square&labelColor=0d1117"
response = requests.get(url)

with open(SVG_FILE, "wb") as f:
    f.write(response.content)

print(f"Updated profile views to {formatted_count}")
