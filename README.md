# 📊 Advanced Donut Chart Visualization

A clean and professional **donut-style pie chart** built using **Python** and **Matplotlib**, featuring modern styling, customization, and enhanced visual elements.

---

## 🚀 Features

* 🍩 Donut-style pie chart (custom inner radius)
* 🎨 Custom color palette
* 💥 Exploded slices for emphasis
* 📊 Percentage labels with styling
* 🏷️ Title and legend support
* 🌗 Shadow effects for depth
* 📐 Responsive layout with proper spacing
* ✨ Clean and beginner-friendly code

---

## 🛠️ Technologies Used

* **Python 3**
* **Matplotlib**

---

## 📂 Project Structure

```
donut-chart/
│── donut_chart.py
│── README.md
```

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/donut-chart.git
cd donut-chart
```

2. Install required library:

```bash
pip install matplotlib
```

---

## ▶️ Usage

Run the Python script:

```bash
python donut_chart.py
```

---

## 🧾 Code Example

```python
import matplotlib.pyplot as plt

sizes = [30, 20, 50]
labels = ['Category A', 'Category B', 'Category C']
colors = ['#4CAF50', '#FF9800', '#2196F3']

explode = (0.05, 0.05, 0.05)

fig, ax = plt.subplots(figsize=(7, 7))

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

centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

plt.title("Advanced Donut Chart", fontsize=16, fontweight='bold')

plt.legend(
    wedges,
    labels,
    title="Categories",
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

plt.axis('equal')
plt.tight_layout()
plt.show()
```

---

## 📸 Output Preview

<img width="842" height="642" alt="image" src="https://github.com/user-attachments/assets/40939881-ab2c-4e62-a179-ec4d96794f51" />

* Displays a **donut chart** with:

  * Colored segments
  * Percentage labels
  * Legend on the side
  * Smooth layout and styling

---

## 🔧 Customization

You can easily modify:

* `sizes` → Change data values
* `labels` → Rename categories
* `colors` → Apply your own color theme
* `explode` → Highlight specific slices
* `wedgeprops['width']` → Adjust donut thickness

---

## 📈 Future Improvements

* Add animation support
* Export chart as image (PNG, JPG)
* Integrate with real-time data (CSV/Excel)
* Convert to interactive web charts (Plotly / Chart.js)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Abdur Rahman**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
