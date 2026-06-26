import json


def report_to_html(report: dict):
    return f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Datra Report</title>
            </head>

            <body>
                <h1>Datra Audit Report</h1>

                <h2>Summary</h2>
                <pre>{json.dumps(report["summary"], indent=4)}</pre>

                <h2>Score</h2>
                <pre>{json.dumps(report["score"], indent=4)}</pre>

                <h2>Checks</h2>
                <pre>{json.dumps(report["checks"], indent=4)}</pre>
            </body>
        </html>
        """