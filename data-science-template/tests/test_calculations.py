from calculations import get_public_orgs, revenue_per_industry
import pytest
import pandas as pd
import numpy as np

def test_get_public_orgs():
    expected_num_public_orgs = (
        54  # replace with the actual number of active drivers in your dataset
    )
    assert get_public_orgs() == expected_num_public_orgs

@pytest.mark.parametrize(
    "Industry, expected_revenue",
    [
        ("Wireless", 3560000.0),
        ("Textiles", 4285000.0),
        ("Accounting", 2930000.0),
    ],
    ids=["Wireless", "Textiles", "Accounting"],
)
def test_revenue_per_industry(Industry, expected_revenue):
    revenue_ratio = revenue_per_industry()
    assert (
        revenue_ratio[Industry] == expected_revenue
    ), f"expected: {expected_revenue}, got: {revenue_ratio[Industry]}"

# New test functions

def test_revenue_data_type():
    """Test if revenue_per_industry returns a pandas Series"""
    result = revenue_per_industry()
    assert isinstance(result, pd.Series), "Result should be a pandas Series"

def test_revenue_values_positive():
    """Test if all revenue values are positive"""
    result = revenue_per_industry()
    assert (result >= 0).all(), "All revenue values should be positive"

def test_revenue_not_empty():
    """Test if the revenue data is not empty"""
    result = revenue_per_industry()
    assert not result.empty, "Revenue data should not be empty"

@pytest.mark.parametrize(
    "invalid_industry",
    ["NonExistent", "Invalid", "NotReal"],
    ids=["test1", "test2", "test3"]
)
def test_invalid_industry(invalid_industry):
    """Test handling of invalid industry names"""
    revenue_ratio = revenue_per_industry()
    assert invalid_industry not in revenue_ratio.index, f"Invalid industry {invalid_industry} should not be present"

@pytest.fixture
def sample_revenue_data():
    """Fixture to provide sample revenue data for tests"""
    return pd.Series({
        "Wireless": 3560000.0,
        "Textiles": 4285000.0,
        "Accounting": 2930000.0
    })

def test_revenue_statistics(sample_revenue_data):
    """Test basic statistical properties of revenue data"""
    result = revenue_per_industry()
    assert result.mean() > 0, "Mean revenue should be positive"
    assert result.std() > 0, "Revenue standard deviation should be positive"
    assert len(result) > 0, "Should have at least one industry"

@pytest.mark.performance
def test_performance():
    """Test performance of revenue calculations"""
    import time
    start_time = time.time()
    revenue_per_industry()
    end_time = time.time()
    assert end_time - start_time < 1.0, "Revenue calculation should take less than 1 second"
