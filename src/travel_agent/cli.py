"""Command-line interface for travel_agent."""

import typer

from travel_agent import __version__

app = typer.Typer(
    name="travel_agent",
    help="AI powered travel agent",
    add_completion=False,
)


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        typer.echo(f"travel_agent version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool | None = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """AI powered travel agent."""


@app.command()
def hello(
    name: str = typer.Argument("World", help="Name to greet"),
) -> None:
    """Say hello to someone."""
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()
