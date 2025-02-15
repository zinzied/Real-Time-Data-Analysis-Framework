import pandas
import numpy as np
from typing import Tuple, Dict


def load_data():
    FILE_PATH = "data/data.csv"
    df = pandas.read_csv(FILE_PATH)
    return df


def get_public_orgs():
    df = load_data()
    public_df = df[df["Public?"] == 1]
    num = len(public_df)
    print("There are ", num, "public organizations.")

    return num


def revenue_per_industry():
    df = load_data()
    revenue_by_industry = df.groupby("Industry")["Revenue"].sum()
    count_by_industry = df["Industry"].value_counts()

    rev_ratio = revenue_by_industry / count_by_industry

    return rev_ratio


def highest_revenue_industry():
    df = load_data()
    revenue_by_industry = df.groupby("Industry")["Revenue"].sum()
    top_revenue_industry = revenue_by_industry.idxmax()

    return top_revenue_industry


def get_industry_statistics() -> Dict[str, float]:
    """Calculate key statistics per industry"""
    df = load_data()
    stats = {
        'mean_revenue': df.groupby('Industry')['Revenue'].mean(),
        'median_revenue': df.groupby('Industry')['Revenue'].median(),
        'std_revenue': df.groupby('Industry')['Revenue'].std(),
        'growth_rate': df.groupby('Industry')['GrowthRate'].mean() if 'GrowthRate' in df.columns else None
    }
    return stats


def get_top_performing_companies(n: int = 5) -> pandas.DataFrame:
    """Get top n companies by revenue"""
    df = load_data()
    return df.nlargest(n, 'Revenue')[['CompanyName', 'Industry', 'Revenue']]


def calculate_year_over_year_growth() -> pandas.Series:
    """Calculate YoY growth rate per industry"""
    df = load_data()
    current_year = df.groupby('Industry')['Revenue'].sum()
    prev_year = df.groupby('Industry')['PrevYearRevenue'].sum() if 'PrevYearRevenue' in df.columns else None
    
    if prev_year is not None:
        growth = ((current_year - prev_year) / prev_year) * 100
        return growth
    return pandas.Series()


def get_revenue_quartiles() -> Dict[str, pandas.DataFrame]:
    """Calculate revenue quartiles by industry"""
    df = load_data()
    quartiles = df.groupby('Industry')['Revenue'].describe()
    return quartiles


def calculate_market_share() -> pandas.Series:
    """Calculate market share percentage for each industry"""
    df = load_data()
    total_revenue = df['Revenue'].sum()
    market_share = (df.groupby('Industry')['Revenue'].sum() / total_revenue) * 100
    return market_share


def main():
    num_public_orgs = get_public_orgs()
    rev_per_industry = revenue_per_industry()
    highest_rev_industry = highest_revenue_industry()

    print("Number of public organizations:", num_public_orgs)
    print("Revenue per industry:")
    print(rev_per_industry)
    print("Industry with the highest revenue:", highest_rev_industry)

    print("\nIndustry Statistics:")
    stats = get_industry_statistics()
    for metric, values in stats.items():
        print(f"\n{metric}:")
        print(values)
    
    print("\nTop 5 Performing Companies:")
    print(get_top_performing_companies())
    
    print("\nMarket Share by Industry:")
    print(calculate_market_share())
    
    print("\nRevenue Quartiles by Industry:")
    print(get_revenue_quartiles())


if __name__ == "__main__":
    main()
