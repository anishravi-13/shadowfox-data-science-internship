# ShadowFox Data Science Internship Portfolio

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?logo=jupyter)
![Pandas](https://img.shields.io/badge/Data%20Analysis-Pandas%20%7C%20NumPy-150458?logo=pandas)
![Visualization](https://img.shields.io/badge/Visualization-Matplotlib%20%7C%20Seaborn-success)
![NLP](https://img.shields.io/badge/NLP-VADER%20Sentiment-9cf)
![Status](https://img.shields.io/badge/Internship-ShadowFox-blueviolet)

This repository contains the complete, production-grade project deliverables for the **ShadowFox Data Science Internship**, spanning Beginner, Intermediate, and Advanced tiers.

---

## 📂 Repository Structure

```text
shadowfox-data-science/
├── README.md                                # Root repository showcase & navigation
├── requirements.txt                         # Python dependencies
│
├── Task-1-Beginner-Visualization-Guide/     # TASK 1: Data Visualization Documentation
│   ├── documentation_guide.md               # In-depth guide (Matplotlib & Seaborn)
│   ├── scripts/
│   │   ├── matplotlib_showcase.py           # Runnable code recipes (4 core plot types)
│   │   └── seaborn_showcase.py              # Runnable code recipes (5 statistical plot types)
│   └── images/                              # High-resolution generated plot figures
│
├── Task-2-Intermediate-Sentiment-Analysis/  # TASK 2: Social Media NLP Sentiment Intelligence
│   ├── README.md                            # Project report & research conclusions
│   ├── sentiment_analysis_x.ipynb           # Fully executed Jupyter Notebook with outputs
│   ├── data/
│   │   └── x_tweets_sentiment_dataset.csv   # 1,200 curated conversational records
│   └── src/
│       └── nlp_pipeline.py                  # Text cleaner & VADER classification engine
│
├── Task-3-Advanced-Sales-Analytics/         # TASK 3: Enterprise Sales & Financial Analytics
│   ├── README.md                            # Executive FP&A report & business recommendations
│   ├── sales_financial_eda.ipynb            # Fully executed Jupyter Notebook with outputs
│   ├── data/
│   │   └── enterprise_sales_financials.csv  # 2,500 multi-fiscal-year transactional records
│   └── src/
│       └── financial_metrics.py             # Financial KPI calculation engine
│
└── Video-Submission-Guide/                  # Mandatory Submission Video Materials
    └── presentation_script.md               # 3–5 min word-for-word presentation script & slide guide
```

---

## 🚀 Project Overviews & Key Deliverables

### 📘 Task 1 (Beginner): Visualization Library Documentation Guide
- **Focus**: Exhaustive technical documentation comparing **Matplotlib** and **Seaborn**.
- **Content**:
  - Architectural breakdown: Low-level Object-Oriented hierarchy (`Figure`/`Axes`) vs. High-level statistical interface.
  - Comprehensive graph catalog with descriptions, real-world use cases, and self-contained code recipes:
    - *Matplotlib*: Line plots, scatter plots, grouped bar charts, histograms, donut charts, and subplots.
    - *Seaborn*: Statistical line plots with 95% bootstrapped confidence intervals, multi-variable semantic scatter plots (`hue`, `style`, `size`), KDE distribution plots, box/violin plots, and correlation heatmaps.
  - Comparative evaluation matrix across ease of use, customization ceiling, aesthetic defaults, and large-scale rendering performance.
- 📄 [View Documentation Guide](Task-1-Beginner-Visualization-Guide/documentation_guide.md)

---

### 💬 Task 2 (Intermediate): Sentiment Analysis of X (Twitter) Conversations
- **Focus**: Natural Language Processing (NLP) pipeline analyzing public sentiment dynamics using the **VADER** sentiment analyzer.
- **Key Research Findings**:
  - **Bimodal Polarity**: Platform discourse exhibits strong emotional concentration (44% positive, 35% negative, and 21% neutral).
  - **Topic Divergence**: *Economy & Markets* and *Gaming* show the highest negative spikes (inflation anxiety, infrastructure latency), whereas *Tech & AI* exhibits the highest optimism (>50% positive) fueled by generative AI innovation.
  - **Engagement Bias**: Strongly polarized posts generate **2.5x more retweets and 3x more replies** than neutral updates, confirming social media's algorithm-driven virality for emotional content.
- 📓 [View Executed Sentiment Analysis Notebook](Task-2-Intermediate-Sentiment-Analysis/sentiment_analysis_x.ipynb)
- 📄 [View Task 2 Executive Report](Task-2-Intermediate-Sentiment-Analysis/README.md)

---

### 📊 Task 3 (Advanced): Enterprise Sales & Financial Analytics
- **Focus**: Multi-year corporate sales and cost accounting analysis navigating COGS, freight logistics, and fiscal calendar seasonality across FY2024 and FY2025.
- **Key Analytical Findings**:
  - **The Profit Waterfall**: Deconstructs Gross Sales down to Net Profit, mapping the cumulative erosion caused by volume discounts, manufacturing costs, COGS, and freight surcharges.
  - **Product Line Margin Disparity**: **Cloud Solutions** achieved superior **45% net profit margins** due to near-zero fulfillment costs, whereas **Consumer Electronics** suffered from margin compression (**~12% net margin**) where COGS and freight absorbed over 70% of revenue.
  - **Geographical Freight Friction**: International logistics across Latin America and APAC imposed an 8–10% freight burden on net sales, reducing regional operating profitability by nearly 6 percentage points compared to North America.
  - **Fiscal Seasonality**: Analyzed performance aligned with corporate fiscal years (Q1 October holiday surge vs. Q4 fiscal closeouts), diagnosing late-year discount cannibalization.
- 📓 [View Executed Sales Analytics Notebook](Task-3-Advanced-Sales-Analytics/sales_financial_eda.ipynb)
- 📄 [View Task 3 Executive Report](Task-3-Advanced-Sales-Analytics/README.md)

---

### 🎥 Mandatory Submission Video Guide
ShadowFox requires submitting a **3 to 5-minute self-recorded video walkthrough** explaining your work via a public Google Drive link.
- A complete, timed, word-for-word presentation script and slide walkthrough has been prepared.
- 🎬 [View Video Presentation Script](Video-Submission-Guide/presentation_script.md)

---

## 🛠️ Quickstart & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/shadowfox-data-science.git
cd shadowfox-data-science
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

### 3. Run Pipeline Scripts
```bash
# Generate Task 1 visual assets
python Task-1-Beginner-Visualization-Guide/scripts/matplotlib_showcase.py
python Task-1-Beginner-Visualization-Guide/scripts/seaborn_showcase.py

# Run Task 2 NLP pipeline
python Task-2-Intermediate-Sentiment-Analysis/src/nlp_pipeline.py

# Run Task 3 Financial calculation engine
python Task-3-Advanced-Sales-Analytics/src/financial_metrics.py
```

### 4. Launch Jupyter Notebooks
```bash
jupyter notebook
```
Navigate to:
- `Task-2-Intermediate-Sentiment-Analysis/sentiment_analysis_x.ipynb`
- `Task-3-Advanced-Sales-Analytics/sales_financial_eda.ipynb`

---

## 👨‍💻 Author & Acknowledgments

- **Intern**: Data Science Intern
- **Program**: ShadowFox Data Science Internship Program
- **Guidance & Queries**: `g2doubts@shadowfox.in`
