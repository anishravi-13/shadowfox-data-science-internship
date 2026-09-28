"""
ShadowFox Data Science Internship - Task 3 (Advanced Level)
Module: financial_metrics.py
Purpose: Financial metrics calculations and synthetic enterprise transactional dataset generation.
"""

import os
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def compute_financial_ratios(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes key financial performance indicators (KPIs):
      - Gross Profit = Net Sales - COGS
      - Operating Income = Gross Profit - Operating Expenses - Freight Costs
      - Gross Margin % = (Gross Profit / Net Sales) * 100
      - Net Margin % = (Operating Income / Net Sales) * 100
      - Freight-to-Sales Ratio % = (Freight Costs / Net Sales) * 100
      - Discount Rate % = (Discounts / Gross Sales) * 100
    """
    df = df.copy()
    df['Gross_Profit'] = df['Net_Sales'] - df['COGS']
    df['Net_Profit'] = df['Gross_Profit'] - df['Freight_Costs'] - df['Operating_Expenses']
    
    # Safe division
    df['Gross_Margin_Pct'] = np.where(df['Net_Sales'] > 0, (df['Gross_Profit'] / df['Net_Sales']) * 100, 0.0)
    df['Net_Margin_Pct'] = np.where(df['Net_Sales'] > 0, (df['Net_Profit'] / df['Net_Sales']) * 100, 0.0)
    df['Freight_to_Sales_Pct'] = np.where(df['Net_Sales'] > 0, (df['Freight_Costs'] / df['Net_Sales']) * 100, 0.0)
    df['Discount_Rate_Pct'] = np.where(df['Gross_Sales'] > 0, (df['Discounts'] / df['Gross_Sales']) * 100, 0.0)
    
    return df

def generate_enterprise_sales_data(output_path: str = None, n_records: int = 2500) -> pd.DataFrame:
    """
    Generates realistic multi-year transactional sales and cost accounting data
    spanning 2 Fiscal Years (FY2024: Oct 2023 - Sep 2024, FY2025: Oct 2024 - Sep 2025).
    """
    np.random.seed(42)
    random.seed(42)
    
    categories = {
        'Cloud Solutions': {'price_range': (2000, 15000), 'mfg_ratio': 0.22, 'freight_ratio': 0.02, 'op_ratio': 0.25},
        'Enterprise Hardware': {'price_range': (5000, 35000), 'mfg_ratio': 0.45, 'freight_ratio': 0.08, 'op_ratio': 0.15},
        'Consumer Electronics': {'price_range': (300, 2500), 'mfg_ratio': 0.52, 'freight_ratio': 0.12, 'op_ratio': 0.18},
        'Accessories & Peripherals': {'price_range': (50, 450), 'mfg_ratio': 0.38, 'freight_ratio': 0.15, 'op_ratio': 0.14}
    }
    
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America']
    channels = ['Direct Enterprise', 'Wholesale Distributor', 'Digital/Online']
    
    start_date = datetime(2023, 10, 1) # Start of FY2024
    end_date = datetime(2025, 9, 30)   # End of FY2025
    total_days = (end_date - start_date).days
    
    records = []
    
    for i in range(n_records):
        tx_id = f"TXN-202{random.randint(4, 5)}-{10000 + i}"
        
        # Transaction Date
        day_offset = random.randint(0, total_days)
        tx_date = start_date + timedelta(days=day_offset)
        
        # Determine Fiscal Year and Quarter (Fiscal year starts Oct 1)
        # Month 10, 11, 12 -> Q1 of FY (Calendar Year + 1)
        # Month 1, 2, 3 -> Q2 of FY
        # Month 4, 5, 6 -> Q3 of FY
        # Month 7, 8, 9 -> Q4 of FY
        m = tx_date.month
        y = tx_date.year
        if m in [10, 11, 12]:
            fy = f"FY{y + 1}"
            fq = "Q1 (Holiday Surge)"
        elif m in [1, 2, 3]:
            fy = f"FY{y}"
            fq = "Q2 (Post-Holiday)"
        elif m in [4, 5, 6]:
            fy = f"FY{y}"
            fq = "Q3 (Mid-Year Build)"
        else:
            fy = f"FY{y}"
            fq = "Q4 (Fiscal Closeout)"
            
        category = random.choices(
            list(categories.keys()), 
            weights=[0.30, 0.35, 0.20, 0.15]
        )[0]
        
        cat_meta = categories[category]
        region = random.choices(regions, weights=[0.40, 0.28, 0.22, 0.10])[0]
        channel = random.choices(channels, weights=[0.45, 0.35, 0.20])[0]
        
        # Quantities & Pricing
        if category in ['Enterprise Hardware', 'Cloud Solutions']:
            units = random.randint(1, 15)
        else:
            units = random.randint(10, 200)
            
        unit_price = round(random.uniform(*cat_meta['price_range']), 2)
        gross_sales = round(units * unit_price, 2)
        
        # Discount logic: wholesale and enterprise get higher volume discounts
        if channel == 'Wholesale Distributor':
            discount_pct = random.uniform(0.08, 0.22)
        elif channel == 'Direct Enterprise':
            discount_pct = random.uniform(0.05, 0.18)
        else:
            discount_pct = random.uniform(0.0, 0.10)
            
        discounts = round(gross_sales * discount_pct, 2)
        net_sales = round(gross_sales - discounts, 2)
        
        # Cost Structure Modeling
        # Manufacturing Cost with realistic variance
        mfg_factor = cat_meta['mfg_ratio'] * random.uniform(0.9, 1.15)
        mfg_costs = round(net_sales * mfg_factor, 2)
        
        # COGS = Manufacturing Costs + Direct packaging/warehousing overhead (10-15% of mfg)
        cogs = round(mfg_costs * random.uniform(1.10, 1.18), 2)
        
        # Freight Costs: higher for physical goods & remote regions (Latin America, APAC)
        freight_mult = 1.35 if region in ['Latin America', 'Asia Pacific'] else 1.0
        freight_factor = cat_meta['freight_ratio'] * freight_mult * random.uniform(0.85, 1.4)
        freight_costs = round(net_sales * freight_factor, 2)
        
        # Operating Expenses (Sales, Marketing, Admin)
        op_costs = round(net_sales * cat_meta['op_ratio'] * random.uniform(0.9, 1.1), 2)
        
        records.append({
            'Transaction_ID': tx_id,
            'Transaction_Date': tx_date.strftime('%Y-%m-%d'),
            'Fiscal_Year': fy,
            'Fiscal_Quarter': fq,
            'Calendar_Year': y,
            'Calendar_Month': m,
            'Region': region,
            'Product_Category': category,
            'Sales_Channel': channel,
            'Units_Sold': units,
            'Unit_Price': unit_price,
            'Gross_Sales': gross_sales,
            'Discounts': discounts,
            'Net_Sales': net_sales,
            'Manufacturing_Costs': mfg_costs,
            'COGS': cogs,
            'Freight_Costs': freight_costs,
            'Operating_Expenses': op_costs
        })
        
    df = pd.DataFrame(records)
    df = df.sort_values('Transaction_Date').reset_index(drop=True)
    df = compute_financial_ratios(df)
    
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Enterprise sales dataset generated at {output_path} ({len(df)} rows)")
        
    return df

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    target_csv = os.path.join(out_dir, "enterprise_sales_financials.csv")
    generate_enterprise_sales_data(target_csv)
