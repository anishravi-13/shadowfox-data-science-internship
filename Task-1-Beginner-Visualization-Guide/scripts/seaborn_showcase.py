"""
ShadowFox Data Science Internship - Task 1 (Beginner Level)
Seaborn Showcase Script
Generates sample plots covering the core graph types documented in documentation_guide.md
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_seaborn_plots():
    print("Generating Seaborn showcase figures...")
    sns.set_theme(style="whitegrid")

    # 1. Statistical Line Plot with Confidence Interval (fmri dataset)
    fmri = sns.load_dataset("fmri")
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=150)
    sns.lineplot(
        data=fmri, x="timepoint", y="signal", hue="event",
        style="region", markers=True, dashes=False, errorbar=("ci", 95), ax=ax
    )
    ax.set_title("Cortical Hemodynamic Signal Trajectory Across Time", fontsize=13, fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "seaborn_01_line_ci_plot.png"))
    plt.close(fig)

    # 2. Scatter Plot with Semantic Mapping (mpg dataset)
    mpg = sns.load_dataset("mpg").dropna()
    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    sns.scatterplot(
        data=mpg, x="horsepower", y="mpg", hue="origin",
        size="weight", sizes=(30, 220), alpha=0.75, palette="Set2", ax=ax
    )
    ax.set_title("Fuel Efficiency vs Engine Horsepower by Vehicle Origin", fontsize=13, fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "seaborn_02_scatter_semantic.png"))
    plt.close(fig)

    # 3. Distribution Plot with KDE (penguins dataset)
    penguins = sns.load_dataset("penguins").dropna()
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=150)
    sns.histplot(
        data=penguins, x="flipper_length_mm", hue="species",
        kde=True, element="step", palette="muted", bins=25, ax=ax
    )
    ax.set_title("Flipper Length Distribution by Penguin Species", fontsize=13, fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "seaborn_03_distribution_kde.png"))
    plt.close(fig)

    # 4. Boxplot & Violinplot
    tips = sns.load_dataset("tips")
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), dpi=150)
    sns.boxplot(data=tips, x="day", y="total_bill", hue="time", palette="Blues", ax=axes[0])
    axes[0].set_title("Total Bill Distribution by Day (Boxplot)", fontweight='bold')
    
    sns.violinplot(data=tips, x="day", y="total_bill", hue="smoker", split=True, inner="quart", palette="Pastel1", ax=axes[1])
    axes[1].set_title("Total Bill Density by Smoker Status (Violin)", fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "seaborn_04_box_violin.png"))
    plt.close(fig)

    # 5. Correlation Heatmap
    iris = sns.load_dataset("iris")
    corr = iris.drop(columns='species').corr()
    fig, ax = plt.subplots(figsize=(7, 5.5), dpi=150)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, square=True, linewidths=1.2, ax=ax)
    ax.set_title("Iris Feature Correlation Matrix", fontsize=13, fontweight='bold', pad=10)
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "seaborn_05_correlation_heatmap.png"))
    plt.close(fig)

    print("Seaborn figures successfully exported to:", OUTPUT_DIR)

if __name__ == "__main__":
    generate_seaborn_plots()
