from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def make_ridge_model(alpha=1.0):
    """
    Create the Ridge Regression pipeline used in the project.
    """
    return Pipeline([
        ("scaler", StandardScaler()),
        ("ridge", Ridge(alpha=alpha))
    ])


def evaluate_regression(y_true, y_pred):
    """
    Calculate the main regression metrics used in the project.
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(
        y_true,
        y_pred
    ) ** 0.5
    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }