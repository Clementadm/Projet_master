import numpy as np
import pandas as pd


def calculate_slope(series: pd.Series) -> float:
    """
    Calculates the slope of a numerical data series using linear regression.

    This function is designed to be applied over rolling windows of a Pandas Series,
    typically to determine the direction of a moving average or another time series.
    It fits a straight line (a polynomial of degree 1) to the data points in the series
    and returns the slope of this line.

    Args:
        series (pd.Series): series of price

    Returns:
        float: The slope of the linear regression line or NaN if less than 2 points
    """

    x = np.arange(len(series))
    if len(x) < 2:
        return np.nan

    slope, _ = np.polyfit(x, series, 1)

    return slope


def check_trend_of_price(df_name, ema_period=5, slope_window=5):
    """
    Calculates the Exponential Moving Average (EMA) and its directional slope
    This function adds three new columns to the input DataFrame:
    'EMA', 'EMA_Slope', and 'EMA_Direction_Slope'.

    Args:
        df_name: Input DataFrame, expected to have a 'Close' column representing closing prices.
        ema_period (int, optional): The period for calculating the EMA. Defaults to 5.
        slope_window (int, optional): The window size for calculating the EMA slope.
                                      Defaults to 5.

    Notes:
        - The 'EMA_Slope' is calculated using a rolling linear regression
          over the 'slope_window' period of the EMA.
        - 'EMA_Direction_Slope' categorizes the slope as 'Up', 'Down', or 'Flat'
          based on predefined thresholds (currently >0.001 for 'Up', <-0.001 for 'Down').
    """
    # Calculate Exponential Moving Average (EMA)
    df_name["EMA"] = df_name["Close"].ewm(span=ema_period, adjust=False).mean()

    # Apply the slope calculation function over a rolling window of the EMA
    df_name["EMA_Slope"] = (
        df_name["EMA"]
        .rolling(window=slope_window, min_periods=2)
        .apply(calculate_slope, raw=False)
    )

    # Determine the direction based on the slope
    df_name["EMA_Direction_Slope"] = np.select(
        [df_name["EMA_Slope"] > 0.001, df_name["EMA_Slope"] < -0.001],  # Create thresholds
        ["Up", "Down"],
        default="Flat",  # Considered flat if slope is very close to zero
    )
    # # --- Visualisation de la pente ---
    # plt.figure(figsize=(14, 10))
    # ax2 = plt.subplot(2, 1, 2) # Partage l'axe X pour le zoom synchronisé
    # ax2.plot(df_name['EMA_Slope'], label='Pente de l\'EMA', color='blue')
    # ax2.axhline(0, color='grey', linestyle='--', linewidth=0.8) # Ligne zéro pour référence
    # ax2.set_title('Pente de l\'EMA')
    # ax2.legend()
    # ax2.grid(True)

    # # Ajouter des zones colorées pour la direction
    # ax2.fill_between(df_name.index, 0, df_name['EMA_Slope'], where=df_name['EMA_Slope'] > 0.001, color='lightgreen', alpha=0.5, label='Up Trend')
    # ax2.fill_between(df_name.index, 0, df_name['EMA_Slope'], where=df_name['EMA_Slope'] < -0.001, color='lightcoral', alpha=0.5, label='Down Trend')

    # plt.tight_layout()
    # plt.show()
