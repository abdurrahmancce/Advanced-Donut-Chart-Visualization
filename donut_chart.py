import matplotlib.pyplot as plt

# Data
sizes = [30, 20, 50]
labels = ['Category A', 'Category B', 'Category C']
colors = ['#4CAF50', '#FF9800', '#2196F3']

# Explode effect (slightly separate slices)
explode = (0.05, 0.05, 0.05)

# Create figure
fig, ax = plt.subplots(figsize=(7, 7))

# Plot donut chart
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    explode=explode,
    pctdistance=0.8,
    wedgeprops={'width': 0.35, 'edgecolor': 'white'},
    shadow=True
)

# Center circle (to enhance donut look)
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

# Title
plt.title("📊 Advanced Donut Chart", fontsize=16, fontweight='bold')

# Legend
plt.legend(
    wedges,
    labels,
    title="Categories",
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

# Improve text style
for text in texts:
    text.set_fontsize(11)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Equal aspect ratio ensures circle shape
plt.axis('equal')

plt.tight_layout()
plt.show()