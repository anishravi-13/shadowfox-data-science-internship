# Task 2: Sentiment Analysis of X (Twitter) Data Using VADER

**ShadowFox Data Science Internship — Intermediate Level Task**  
*Track: Natural Language Processing & Social Media Intelligence*

---

## 1. Project Overview

Social media platforms like X (formerly Twitter) serve as modern public squares where users express real-time opinions, reactions, and critiques. For brands, policymakers, and platform moderators, tracking sentiment dynamics is crucial for detecting brand perception shifts, managing PR crises, and understanding public response to major announcements.

This project delivers an end-to-end sentiment analytics pipeline leveraging the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** NLP engine to categorize discourse into **Positive**, **Neutral**, and **Negative** sentiment classes, while exploring topic-level variations, temporal shifts, and engagement dynamics.

---

## 2. Research Questions (RQs)

1. **RQ1 (Macro Sentiment Distribution)**: What proportion of discourse is positive, negative, or neutral?
2. **RQ2 (Domain Variation)**: How does sentiment skew across critical discussion domains (*Tech & AI, Economy & Markets, Gaming, Entertainment, Climate & Energy*)?
3. **RQ3 (Temporal Dynamics)**: How does sentiment compound score fluctuate over daily cycles and moving averages?
4. **RQ4 (Engagement & Negativity Bias)**: Do negative or polarizing posts generate disproportionately higher engagement (retweets, replies, likes)?
5. **RQ5 (Linguistic Patterns)**: What dominant keywords and linguistic tokens distinguish positive vs. negative sentiment clusters?

---

## 3. Dataset Description & Preprocessing

The dataset (`data/x_tweets_sentiment_dataset.csv`) contains 1,200 timestamped conversational records spanning 5 key topics.

### Dataset Features:
| Column | Type | Description |
| :--- | :--- | :--- |
| `tweet_id` | String | Unique record identifier (`TWT_100000+`) |
| `timestamp` | Datetime | Date and time the post was published |
| `topic` | String | Discussion vertical (*Tech & AI, Economy, Gaming, etc.*) |
| `user_handle` | String | Anonymized user account handle |
| `raw_tweet` | String | Original post text containing hashtags and emojis |
| `retweets` | Integer | Number of retweets received |
| `likes` | Integer | Number of likes received |
| `replies` | Integer | Number of direct replies received |

### Preprocessing Strategy:
- Extracted URLs and hyperlinks using regular expressions.
- Removed user mentions (`@handle`) to protect privacy and eliminate entity bias.
- Unhashed hashtag tokens (retaining the semantic word while stripping `#`).
- Cleaned redundant whitespace and decoded HTML entities.

---

## 4. Methodology: VADER Sentiment Analyzer

VADER is a rule-based sentiment analysis model specifically tuned for social media contexts:
- Recognizes sentiment valence of emoticons (`:)`, `:(`), acronyms (`OMG`, `FTW`), and internet slang.
- Accounts for punctuation intensity (e.g. `Great!` vs `Great!!!`) and capitalization contrast.
- Evaluates grammatical modifiers (negation: `not terrible`, intensifiers: `exceptionally smooth`).

### Categorization Thresholds:
$$\text{Sentiment Class} = 
\begin{cases} 
\text{Positive}, & \text{Compound Score} \ge 0.05 \\
\text{Negative}, & \text{Compound Score} \le -0.05 \\
\text{Neutral}, & -0.05 < \text{Compound Score} < 0.05
\end{cases}$$

---

## 5. Key Findings & Strategic Insights

1. **Bimodal Sentiment Pattern**: Platform sentiment is strongly polarized, with ~44% positive, ~35% negative, and only ~21% neutral posts. Conversational social media naturally encourages expressive reactions rather than neutral updates.
2. **Topic Vulnerabilities**:
   - *Economy & Markets* and *Gaming* harbor the highest negative sentiment ratios (~42% and ~40% respectively), driven by inflation concerns and gaming server downtime/monetization complaints.
   - *Tech & AI* and *Climate & Energy* exhibit the highest optimism (>50% positive), driven by breakthroughs in generative AI and renewable energy.
3. **Engagement Dynamics**: Polarized posts (both strongly positive and strongly negative) generate on average **2.5x more retweets and 3x more replies** than neutral posts, confirming social media's algorithm-driven virality for emotional content.
4. **Actionable Recommendations**:
   - Automated alerts should trigger when a topic's 5-day rolling sentiment drops below $-0.15$.
   - Content moderation systems should prioritize posts combining high reply counts with strong negative compound scores to triage escalating conflicts.

---

## 6. How to Run

### Run the Python Pipeline:
```bash
# Generate the dataset and execute the modular pipeline
python src/nlp_pipeline.py
```

### Open and Explore the Jupyter Notebook:
```bash
jupyter notebook sentiment_analysis_x.ipynb
```
