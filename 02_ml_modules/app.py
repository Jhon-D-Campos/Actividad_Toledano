import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from src.io import Dataset
    from src.models import build_pipeline
    from src.evaluation import ModelEvaluation

    return Dataset, ModelEvaluation, build_pipeline, mo


@app.cell
def _(Dataset, mo):
    data = Dataset(seed=43)
    X_train, y_train = data.load_xy()
    mo.md("### Datos cargados correctamente")
    return X_train, y_train


@app.cell
def _(mo):
    model_select = mo.ui.dropdown(
        options=["random_forest", "linear_regression", "decision_tree"],
        value="random_forest",
        label="Selecciona un modelo:"
    )
    model_select
    return (model_select,)


@app.cell
def _(ModelEvaluation, X_train, build_pipeline, model_select, y_train):
    pipeline = build_pipeline(model_name=model_select.value)
    ev = ModelEvaluation(X=X_train, y=y_train)
    metrics = ev.evaluate_model(pipeline)
    return


if __name__ == "__main__":
    app.run()
