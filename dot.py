import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
plt.rcParams.update({
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.labelsize": 9,
    "axes.edgecolor": "#444444",
    "axes.grid": True,
    "grid.alpha": 0.25,
    "grid.linestyle": "--",
})

COLORS = ["#2E86AB", "#A23B72", "#F18F01", "#3B8C6E", "#6A4C93"]

fig, axs = plt.subplots(3, 3, figsize=(15, 13))
fig.suptitle("My First Chart", fontsize=22, fontweight="bold", color="#222222", y=0.995)

# 1. Scatter plot
x1 = np.random.rand(50) * 10
y1 = np.random.rand(50) * 10
axs[0, 0].scatter(x1, y1, color=COLORS[0], edgecolor="white", s=60, alpha=0.85)
axs[0, 0].set_title("Scatter Plot")
axs[0, 0].set_xlabel("X Axis")
axs[0, 0].set_ylabel("Y Axis")

# 2. Bubble scatter plot (colored, varying sizes)
x2 = np.random.rand(40) * 10
y2 = np.random.rand(40) * 10
sizes = np.random.rand(40) * 500 + 30
colors = np.random.rand(40)
sc = axs[0, 1].scatter(x2, y2, s=sizes, c=colors, cmap="RdYlGn", alpha=0.65, edgecolor="white")
axs[0, 1].set_title("Bubble Plot")
axs[0, 1].set_xlabel("X Axis")
axs[0, 1].set_ylabel("Y Axis")

# 3. Horizontal bar
categories = ["Category A", "Category B", "Category C"]
values = [8, 5, 3]
axs[0, 2].barh(categories, values, color=COLORS[:3], height=0.5)
axs[0, 2].set_title("Horizontal Bar")
axs[0, 2].set_xlabel("Value")
axs[0, 2].set_ylabel("Category")
axs[0, 2].invert_yaxis()

# 4. Simple increasing line
x4 = np.linspace(0, 10, 10)
y4 = x4
axs[1, 0].plot(x4, y4, color=COLORS[0], marker="o", markersize=5, linewidth=2)
axs[1, 0].set_title("Line Plot")
axs[1, 0].set_xlabel("X Axis")
axs[1, 0].set_ylabel("Y Axis")

# 5. Zigzag line
x5 = np.arange(6)
y5 = [0, 10, 2, 8, 1, 9]
axs[1, 1].plot(x5, y5, color=COLORS[1], marker="o", markersize=5, linewidth=2)
axs[1, 1].set_title("Zigzag Line")
axs[1, 1].set_xlabel("X Axis")
axs[1, 1].set_ylabel("Y Axis")

# 6. Line with markers
x6 = np.arange(5)
y6 = [2, 9, 1, 10, 3]
axs[1, 2].plot(x6, y6, color=COLORS[2], marker="o", markersize=6, linewidth=2)
axs[1, 2].set_title("Line with Markers")
axs[1, 2].set_xlabel("X Axis")
axs[1, 2].set_ylabel("Y Axis")

# 7. Histogram (triangle-shaped distribution)
data = np.random.triangular(0, 50, 100, 1000)
axs[2, 0].hist(data, bins=20, color=COLORS[3], edgecolor="white")
axs[2, 0].set_title("Histogram")
axs[2, 0].set_xlabel("Value")
axs[2, 0].set_ylabel("Frequency")

# 8. Pie chart 1
labels8 = ["A", "B", "C"]
sizes8 = [40, 35, 25]
axs[2, 1].pie(
    sizes8, labels=labels8, autopct="%1.0f%%", startangle=90,
    colors=COLORS[:3], explode=(0.06, 0, 0),
    textprops={"fontsize": 9, "color": "white", "fontweight": "bold"},
    wedgeprops={"edgecolor": "white", "linewidth": 1.5},
)
axs[2, 1].set_title("Pie Chart 1")

# 9. Pie chart 2 (legend placed outside, no overlap)
labels9 = ["Group X", "Group Y", "Group Z"]
sizes9 = [50, 30, 20]
wedges, _ = axs[2, 2].pie(
    sizes9, colors=COLORS[:3], startangle=90,
    wedgeprops={"edgecolor": "white", "linewidth": 1.5},
)
axs[2, 2].set_title("Pie Chart 2")
axs[2, 2].legend(
    wedges, labels9, loc="center left", bbox_to_anchor=(1.02, 0.5),
    fontsize=8, frameon=False,
)

plt.tight_layout(rect=[0, 0, 1, 0.96], h_pad=3.0, w_pad=3.5)
plt.savefig("my_first_chart.png", dpi=150, bbox_inches="tight")
plt.show()