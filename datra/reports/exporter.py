import json
from pathlib import Path
from datetime import datetime

from .templates import report_to_html


def save_report(
    report,
    output="outputs",
    format="json",
):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"datra_report_{timestamp}.{format}"

    path = output / filename

    if format == "json":
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

    elif format == "html":
        with open(path, "w", encoding="utf-8") as f:
            f.write(report_to_html(report))

    else:
        raise ValueError(
            f"Unsupported report format '{format}'."
        )

    return path