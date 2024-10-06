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
                "description": "Verify that a user can add a hyperlink to selected text."
            },
            {
                "name": "Valid Markdown Syntax",
                "description": "Verify that correct markdown content is rendered successfully."
            }
        ]
    }
]

# Function to convert JSON data to LaTeX format
def generate_latex(json_data):
    latex_content = r"""
    \documentclass{article}
    \usepackage{hyperref}
    \begin{document}
    """

    for entry in json_data:
        # Extract Use Case
        usecase = entry.get('usecase', {})
        latex_content += f"\\section{{\\textbf{{Use Case: {usecase.get('name', '')}}}}}\n"
        latex_content += f"\\textbf{{Scenario:}} {usecase.get('scenario', '')}\\\\\n"
        latex_content += f"\\textbf{{Actors:}} {usecase.get('actors', '')}\\\\\n"
        latex_content += "\\textbf{Steps:}\n\\begin{enumerate}\n"
        for step in usecase.get('steps', []):
            latex_content += f"\\item {step}\n"
        latex_content += "\\end{enumerate}\n"

        # Extract Test Cases
        latex_content += "\\subsection{Test Cases}\n"
        for testcase in entry.get('testcases', []):
            latex_content += f"\\subsubsection{{{testcase.get('name', '')}}}"
            latex_content += f"{testcase.get('description', '')}"

    latex_content += "\\end{document}"
    return latex_content

# Write LaTeX content to a file
latex_output = generate_latex(data)
with open("output.tex", "w") as latex_file:
    latex_file.write(latex_output)

print("LaTeX document generated: output.tex")
