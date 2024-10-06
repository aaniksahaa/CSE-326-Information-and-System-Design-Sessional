import json

# Example filenames (you will replace these with actual file names)
# filenames = ["file1.json", "file2.json", "file3.json", "file4.json", "file5.json", "file6.json"]

filenames = [
    "Workspace Management.json",
    "Content Management.json",
    "Database Creation and Management.json",
    "Sharing and Collaboration.json",
    "Plans and Payment.json",
    "Third Party Integration.json"
]

total_data = []

prefix = r"""

\documentclass{article}
\usepackage[a4paper, margin=2cm]{geometry}
\usepackage{hyperref}
\usepackage{longtable}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage[label=corner]{karnaugh-map}
\usepackage{tabularray}
\usepackage{multicol}
\usepackage{multirow}
\usepackage{array}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    }
\usepackage{float}
\usepackage{caption}
\usepackage{subcaption}
\usepackage[siunitx, RPvoltages]{circuitikz}
\usetikzlibrary{calc}
\usepackage{tikz, pgfplots}
\usetikzlibrary{positioning}
\usepackage{enumitem}
\usepackage{biblatex}
\usepackage{rotating}
\usepackage{ragged2e}
\usepackage[outputdir=../../]{minted}


\title{CSE 306 \\
Computer Architecture Sessional \\

\vspace{5mm}

\begin{figure}[h]
    \centering
    \includegraphics[width=0.3\textwidth]{images/buet.png}
    \label{fig:enter-label}
\end{figure}

\vspace{5mm}
Assignment-3\\
4-bit MIPS Implementation \\
\vspace{10mm}
Section - A1 \\
Group - 01 \\
\vspace{15mm}
\RaggedRight
Group Members: \\
\normalsize	{
\centering
\begin{enumerate}[]
    \item 2005001 - Anik Saha
    \item 2005012 - Abrar Jahin Sarker
    \item 2005013 - Al Muhit Muhtadi
    \item 2005017 - Abdullah Muhammed Amimul Ehsan
    \item 2005023 - Jaber Ahmed Deeder
\end{enumerate}
}
}
\author{}
\date{}
    
    \begin{document}

\maketitle

\newpage

"""

# Function to convert JSON data to LaTeX format for multiple files
def generate_latex(filenames):
    latex_content = prefix

    # Loop through each file and process its content
    for filename in filenames:
        # Open the JSON file and load the data
        with open(filename, "r") as file:
            data = json.load(file)

        total_data.extend(data)
        
        # Add a section for the filename
        latex_content += f"\\section{{\\textbf{{{filename.split('.')[0]}}}}}\n"
        
        # Process each use case and test case inside the JSON file
        for entry in data:
            # Extract Use Case
            usecase = entry.get('usecase', {})
            latex_content += f"\\subsection{{\\textbf{{Use Case: {usecase.get('name', '')}}}}}\n"
            latex_content += f"\\textbf{{Scenario:}} {usecase.get('scenario', '')}\\\\\n"
            latex_content += f"\\textbf{{Actors:}} {usecase.get('actors', '')}\\\\\n"
            latex_content += "\\textbf{Steps:}\n\\begin{enumerate}\n"
            for step in usecase.get('steps', []):
                latex_content += f"\\item {step}\n"
            latex_content += "\\end{enumerate}\n"

            # Extract Test Cases - use a table format
            latex_content += "\\textbf{Test Cases}\n"
            latex_content += r"""
            \begin{longtable}{|p{0.3\textwidth}|p{0.6\textwidth}|}
            \hline
            \textbf{Name} & \textbf{Description} \\
            \hline
            """
            for testcase in entry.get('testcases', []):
                latex_content += f"{testcase.get('name', '')} & {testcase.get('description', '')} \\\\\n\\hline\n"
            
            latex_content += r"\end{longtable}"

    latex_content += "\\end{document}"
    return latex_content

# Specify filenames here or dynamically based on user input
latex_output = generate_latex(filenames)

# Write LaTeX content to a file
with open("output.tex", "w") as latex_file:
    latex_file.write(latex_output)

print("LaTeX document generated: output.tex")


with open("merged.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(total_data, indent=4))