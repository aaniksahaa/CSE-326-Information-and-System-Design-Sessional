import json

# Sample JSON structure (replace this with your actual JSON file loading)
data = [
    {
        "usecase": {
            "name": "Rich Text Formatting",
            "scenario": "Users format their text with rich options adding links.",
            "actors": "User",
            "preconditions": "The text block exists in the document.",
            "steps": [
                "User selects the text block.",
                "User applies the formatting options",
                "User checks the formatted result."
            ]
        },
        "testcases": [
            {
                "name": "Valid Text Hyperlinking",
                "description": "Verify that a user can add a hyperlink to selected text.",
                "input": {
                    "text": "Click here",
                    "link": "http://example.com"
                },
                "expected": {
                    "outcome": "Hyperlink added to text.",
                    "status": "Link Working"
                }
            },
            {
                "name": "Valid Markdown Syntax",
                "description": "Verify that correct markdown content is rendered successfully.",
                "input": {
                    "markdown": "**Hello World**"
                },
                "expected": {
                    "outcome": "Formatting successfully applied.",
                    "status": "Success"
                }
            }
        ]
    }
]

# Function to convert JSON data to LaTeX format
def generate_latex(json_data):
    latex_content = r"""
    \documentclass{article}
    \usepackage{hyperref}
    \usepackage{longtable}
    \begin{document}
    """

    for entry in json_data:
        # Extract Use Case
        usecase = entry.get('usecase', {})
        latex_content += f"\\section*{{Use Case: {usecase.get('name', '')}}}\n"
        latex_content += f"\\textbf{{Scenario:}} {usecase.get('scenario', '')}\\\\\n"
        latex_content += f"\\textbf{{Actors:}} {usecase.get('actors', '')}\\\\\n"
        latex_content += f"\\textbf{{Preconditions:}} {usecase.get('preconditions', '')}\\\\\n"
        latex_content += "\\textbf{Steps:}\n\\begin{enumerate}\n"
        for step in usecase.get('steps', []):
            latex_content += f"\\item {step}\n"
        latex_content += "\\end{enumerate}\n"

        # Extract Test Cases
        latex_content += "\\subsection*{Test Cases}\n"
        latex_content += "\\begin{longtable}{|p{5cm}|p{8cm}|}\n"
        latex_content += "\\hline\n"
        latex_content += "\\textbf{Test Case Name} & \\textbf{Description} \\\\\n\\hline\n"
        for testcase in entry.get('testcases', []):
            latex_content += f"{testcase.get('name', '')} & {testcase.get('description', '')} \\\\\n"
            latex_content += "\\hline\n"
            latex_content += "\\textbf{Input:} & \\\\\n"
            for key, value in testcase.get('input', {}).items():
                latex_content += f"{key}: {value} \\\\\n"
            latex_content += "\\hline\n"
            latex_content += "\\textbf{Expected Outcome:} & \\\\\n"
            latex_content += f"Outcome: {testcase.get('expected', {}).get('outcome', '')} \\\\\n"
            latex_content += f"Status: {testcase.get('expected', {}).get('status', '')} \\\\\n"
            latex_content += "\\hline\n"
        latex_content += "\\end{longtable}\n"

    latex_content += "\\end{document}"
    return latex_content

# Write LaTeX content to a file
latex_output = generate_latex(data)
with open("output.tex", "w") as latex_file:
    latex_file.write(latex_output)

print("LaTeX document generated: output.tex")
