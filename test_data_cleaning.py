import pandas as pd
import pytest

@pytest.fixture(scope="module")
def cleaned_df():
    """Load the cleaned crime dataset once for all tests."""
    df = pd.read_excel("Crime_2024_with_Weather_Unemp_Monthly.xlsx")
    return df

def test_no_missing_victim_age_sex(cleaned_df):
    """Test that victim_age and victim_sex_new are properly cleaned."""
    # victim_age: after cleaning, should be non-negative if not missing
    assert (cleaned_df['victim_age'] >= 0).all(), "There are invalid victim ages (e.g., negative numbers)."
    # victim_sex_new: should only be 0, 1, 2, or None
    assert cleaned_df['victim_sex_new'].dropna().isin([0, 1, 2]).all(), "Victim sex encoding contains invalid values."

# Test if within 0-12
def test_no_invalid_victim_descent(cleaned_df):
    """Test that victim_descent_code_new has only allowed codes."""
    allowed_codes = list(range(13))
    assert cleaned_df['victim_descent_code_new'].dropna().isin(allowed_codes).all(), "Victim descent encoding contains invalid codes."

def test_no_unexpected_crime_codes(cleaned_df):
    """Test that crime_code_description is clean: all strings, no empty."""
    assert cleaned_df['crime_code_description'].apply(lambda x: isinstance(x, str) and x.strip() != "").all(), "Found invalid crime code descriptions (not string or empty)."

def test_lat_lon_within_bounds(cleaned_df):
    """Test that latitude and longitude are within Los Angeles reasonable range."""
    assert cleaned_df['latitude'].between(33.5, 34.5).all(), "Latitude values are out of expected bounds."
    assert cleaned_df['longitude'].between(-119.0, -117.5).all(), "Longitude values are out of expected bounds."

def test_no_missing_critical_columns(cleaned_df):
    """Optional: Test that critical columns are not missing too much data."""
    critical_columns = ['date_of_occurrence', 'area_name', 'crime_code_description']
    for col in critical_columns:
        missing_rate = cleaned_df[col].isnull().mean()
        assert missing_rate < 0.05, f"Column {col} has too much missing data: {missing_rate:.2%}"

def test_victim_sex_only_0_or_1(cleaned_df):
    """Test that victim_sex_new is either 0 or 1 (excluding None/NaN)."""
    non_null_sex = cleaned_df['victim_sex_new'].dropna()
    assert non_null_sex.isin([0, 1]).all(), "Found victim_sex_new values not equal to 0 or 1."

def test_unemployment_rate_bounds(cleaned_df):
    """Test that unemployment rate is within reasonable range [0%, 100%]."""
    non_null_unemp = cleaned_df['unemployment_rate_pct']
    assert non_null_unemp.between(0, 100).all(), "Unemployment rate out of [0,100]% range."

def test_weather_temperature_bounds(cleaned_df):
    """Test that daily_avg_temperature_celsius is within a reasonable range [-30C, 60C]."""
    if 'daily_avg_temperature_celsius' in cleaned_df.columns:
        non_null_temp = cleaned_df['daily_avg_temperature_celsius'].dropna()
        assert non_null_temp.between(-30, 60).all(), "Temperature values are outside of [-30C, 60C] range."

def test_weather_precipitation_bounds(cleaned_df):
    """Test that daily_precipitation_mm is non-negative and within reasonable range [0, 500mm]."""
    if 'daily_precipitation_mm' in cleaned_df.columns:
        non_null_precip = cleaned_df['daily_precipitation_mm'].dropna()
        assert non_null_precip.between(0, 500).all(), "Precipitation values are outside of [0mm, 500mm] range."


### ALL TESTS PASSED ###