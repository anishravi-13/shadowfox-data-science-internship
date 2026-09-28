"""
ShadowFox Data Science Internship - Task 2 (Intermediate Level)
Module: nlp_pipeline.py
Purpose: Text preprocessing, VADER Sentiment Analysis, and dataset generation for X (Twitter) analysis.
"""

import re
import os
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def clean_tweet(text: str) -> str:
    """
    Cleans raw tweet text by removing URLs, handles, HTML entities,
    and unnecessary special characters while preserving sentiment markers.
    """
    if not isinstance(text, str):
        return ""
    # Remove URL links
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # Remove user mentions (@username)
    text = re.sub(r'@\w+', '', text)
    # Remove HTML entities like &amp;, &lt;
    text = re.sub(r'&\w+;', '', text)
    # Remove hashtag symbol (#) but keep the word
    text = re.sub(r'#(\w+)', r'\1', text)
    # Normalize multiple whitespace characters
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def analyze_sentiment(text: str) -> dict:
    """
    Calculates VADER sentiment scores and assigns a discrete category.
    Classification threshold:
      - Compound >= 0.05  -> Positive
      - Compound <= -0.05 -> Negative
      - Else              -> Neutral
    """
    cleaned = clean_tweet(text)
    scores = analyzer.polarity_scores(cleaned)
    compound = scores['compound']
    
    if compound >= 0.05:
        category = 'Positive'
    elif compound <= -0.05:
        category = 'Negative'
    else:
        category = 'Neutral'
        
    return {
        'cleaned_text': cleaned,
        'neg_score': scores['neg'],
        'neu_score': scores['neu'],
        'pos_score': scores['pos'],
        'compound_score': compound,
        'sentiment': category
    }

def generate_sample_x_dataset(output_path: str = None, n_records: int = 1200) -> pd.DataFrame:
    """
    Generates a realistic, structured X (Twitter) dataset across multiple domains:
    Tech & AI, Economy & Markets, Gaming, Entertainment, Climate & Energy.
    """
    random.seed(42)
    np.random.seed(42)
    
    topics_templates = {
        'Tech & AI': [
            ("The new open source AI models are absolutely mindblowing! Incredible performance and super accessible 🚀", 0.85),
            ("Another bug in the latest software update broke my workflow completely. Terrible QA testing!", -0.75),
            ("Attending the annual developer summit today. Lots of discussions about vector databases.", 0.0),
            ("Autonomous coding agents are moving faster than anyone anticipated. Loving this progress!", 0.8),
            ("Subscription pricing hikes across SaaS tools are getting completely ridiculous and frustrating.", -0.65),
            ("Comparing performance benchmarks of LLMs across latency and memory utilization.", 0.1),
            ("Excited to launch our new product feature today! Thank you to the whole team for the hard work.", 0.78),
            ("Servers have been down for 3 hours now with zero status communication. Horrible experience.", -0.82)
        ],
        'Economy & Markets': [
            ("Central banks keep interest rates steady. Market rally continues with strong consumer sentiment 📈", 0.65),
            ("Inflation numbers are still hurting working families. Cost of groceries is absurd.", -0.7),
            ("Treasury yields edged slightly lower in today's trading session. Observing bond trends.", 0.0),
            ("Thrilled about the stellar earnings report today, record quarterly profits!", 0.88),
            ("Layoffs announced across another major firm. Heartbreaking news for everyone impacted.", -0.78),
            ("Quarterly GDP report scheduled for release tomorrow morning at 8:30 AM EST.", 0.05),
            ("Diversifying portfolio into green energy and semiconductor stocks. Feeling very bullish long term.", 0.6),
            ("High interest rates are suffocating small businesses. Really tough economic climate right now.", -0.62)
        ],
        'Gaming': [
            ("The graphics and storyline in this new RPG release are breathtaking! Absolute masterpiece 🎮", 0.9),
            ("Unplayable stuttering and microtransactions everywhere. Total disappointment and waste of money.", -0.85),
            ("Patch notes 1.04 have been deployed to the live staging servers.", 0.0),
            ("Just hit top tier rank after an intense tournament clutch! Best gaming moment of the year!", 0.84),
            ("Hackers and cheaters are ruining competitive ranked matchmaking. Developers need to act fast.", -0.72),
            ("Weekly community livestream begins in 30 minutes on our official channel.", 0.1),
            ("Incredible soundtrack and seamless controller support. Having so much fun with friends!", 0.75),
            ("Lag spikes on the server made me lose the entire match. Fix the servers!", -0.68)
        ],
        'Entertainment': [
            ("That season finale was an emotional tour de force! Brilliant acting and direction 👏", 0.86),
            ("Worst movie adaptation I have ever endured. Horrible plot holes and flat characters.", -0.8),
            ("Box office receipts for the opening weekend will be announced Monday.", 0.0),
            ("In love with the new album released today! Every track is pure gold.", 0.82),
            ("Ticket booking platform crashed during pre-sale again. Unacceptable customer service.", -0.74),
            ("New trailer dropped for the upcoming sci-fi series streaming next month.", 0.15),
            ("What a mesmerizing live concert experience! The acoustics and stage design were spectacular!", 0.91),
            ("Overhyped show with zero substance. Disappointed after waiting two whole years.", -0.6)
        ],
        'Climate & Energy': [
            ("Historic breakthrough in renewable solar panel efficiency! Cleaner, cheaper future ahead ☀️", 0.87),
            ("Severe heatwave breaking all past records. Extreme climate inaction is alarming and scary.", -0.79),
            ("Global climate conference delegation convenes for annual policy negotiations.", 0.0),
            ("Battery storage installations doubled this quarter, accelerating clean grid transition!", 0.76),
            ("Toxic oil spill threatening local marine wildlife. Truly devastating environmental tragedy.", -0.86),
            ("Municipal transit authority evaluates electric bus transition timelines.", 0.05),
            ("Community tree planting initiative completed today with 5,000 new saplings planted!", 0.8),
            ("Drought conditions are worsening agricultural yields across the central valley.", -0.65)
        ]
    }
    
    start_date = datetime(2026, 8, 1, 8, 0, 0)
    data = []
    
    for i in range(n_records):
        topic = random.choice(list(topics_templates.keys()))
        template_text, sentiment_bias = random.choice(topics_templates[topic])
        
        # Add slight variation/hashtags/emojis
        tags = [f"#{topic.replace(' ', '').replace('&', '')}", "#News", "#Trending", "#DailyUpdate"]
        text = template_text + " " + " ".join(random.sample(tags, k=random.randint(0, 2)))
        
        # Simulate realistic time series over 30 days
        timestamp = start_date + timedelta(
            days=random.randint(0, 30),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        
        # High-sentiment tweets typically receive higher virality/engagement
        base_eng = random.randint(5, 50)
        multiplier = 1.0 + abs(sentiment_bias) * 3.5
        retweets = int(base_eng * multiplier * random.uniform(0.5, 2.0))
        likes = int(retweets * random.uniform(2.5, 6.0))
        replies = int(retweets * random.uniform(0.1, 0.6))
        
        data.append({
            'tweet_id': f"TWT_{100000 + i}",
            'timestamp': timestamp,
            'topic': topic,
            'user_handle': f"@user_{random.randint(100, 999)}",
            'raw_tweet': text,
            'retweets': retweets,
            'likes': likes,
            'replies': replies
        })
        
    df = pd.DataFrame(data)
    df = df.sort_values('timestamp').reset_index(drop=True)
    
    # Run VADER analysis
    results = df['raw_tweet'].apply(analyze_sentiment).apply(pd.Series)
    df = pd.concat([df, results], axis=1)
    
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Dataset generated and saved to {output_path} ({len(df)} rows)")
        
    return df

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    target_csv = os.path.join(out_dir, "x_tweets_sentiment_dataset.csv")
    generate_sample_x_dataset(target_csv)
