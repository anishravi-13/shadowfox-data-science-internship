"""
ShadowFox Data Science Internship - Task 1 (Beginner Level)
Matplotlib Showcase Script
Generates sample plots covering the core graph types documented in documentation_guide.md
"""

import os
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_matplotlib_plots():
    print("Generating Matplotlib showcase figures...")
    
    # 1. Line Plot: Annual Revenue Trajectory
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    rev_2025 = [45, 52, 58, 63, 70, 78, 85, 91, 98, 105, 115, 130]
    rev_2026_target = [50, 60, 68, 75, 85, 95, 105, 118, 130, 142, 155, 170]

    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=150)
    ax.plot(months, rev_2025, marker='o', color='#1f77b4', linewidth=2.5, label='2025 Actual ($k)')
    ax.plot(months, rev_2026_target, marker='s', linestyle='--', color='#2ca02c', linewidth=2, label='2026 Target ($k)')
    ax.set_title("Annual Revenue Trajectory: Actual vs Target", fontsize=13, fontweight='bold', pad=10)
    ax.set_xlabel("Fiscal Month", fontsize=10)
    ax.set_ylabel("Revenue ($k USD)", fontsize=10)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(frameon=True, loc='upper left')
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "matplotlib_01_line_plot.png"))
    plt.close(fig)

    # 2. Scatter Plot: Ad Spend vs Acquisitions
    np.random.seed(42)
    ad_spend = np.random.uniform(500, 10000, 120)
    acquisitions = (ad_spend * 0.08) + np.random.normal(50, 40, 120)
    roi = acquisitions / (ad_spend / 1000)

    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=150)
    scatter = ax.scatter(ad_spend, acquisitions, c=roi, cmap='plasma', s=60, alpha=0.85)
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label('ROI Multiplier', rotation=270, labelpad=15)
    ax.set_title("Marketing Spend vs Customer Acquisitions", fontsize=13, fontweight='bold')
    ax.set_xlabel("Ad Spend ($ USD)", fontsize=10)
    ax.set_ylabel("Acquisitions", fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "matplotlib_02_scatter_plot.png"))
    plt.close(fig)

    # 3. Bar Chart: Regional Sales Performance
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East']
    hardware = [120, 95, 140, 60, 45]
    software = [180, 130, 160, 80, 70]
    x = np.arange(len(regions))
    bar_width = 0.35

    fig, ax = plt.subplots(figsize=(9.5, 4.5), dpi=150)
    rects1 = ax.bar(x - bar_width/2, hardware, bar_width, label='Hardware', color='#34495e')
    rects2 = ax.bar(x + bar_width/2, software, bar_width, label='Software', color='#3498db')
    ax.set_title("Regional Sales Performance by Business Unit ($M)", fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(regions)
    ax.set_ylabel("Sales ($M)", fontsize=10)
    ax.legend()
    ax.grid(axis='y', linestyle=':', alpha=0.7)
    ax.bar_label(rects1, padding=3, fmt='%dM')
    ax.bar_label(rects2, padding=3, fmt='%dM')
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "matplotlib_03_bar_chart.png"))
    plt.close(fig)

    # 4. Donut Chart: Budget Allocation
    categories = ['Engineering', 'Sales & Marketing', 'Operations', 'G&A', 'Customer Support']
    shares = [38, 27, 15, 12, 8]
    colors = ['#2b5c8f', '#4682b4', '#70a1d7', '#a1c4fd', '#c2e9fb']

    fig, ax = plt.subplots(figsize=(6, 6), dpi=150)
    wedges, texts, autotexts = ax.pie(
        shares, labels=categories, autopct='%1.1f%%', startangle=140,
        colors=colors, pctdistance=0.78,
        wedgeprops=dict(width=0.42, edgecolor='white', linewidth=2)
    )
    for autotext in autotexts:
        autotext.set_fontweight('bold')
    ax.set_title("Annual Operating Expenditure Allocation", fontsize=13, fontweight='bold')
    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "matplotlib_04_donut_chart.png"))
    plt.close(fig)

    print("Matplotlib figures successfully exported to:", OUTPUT_DIR)

if __name__ == "__main__":
    generate_matplotlib_plots()
