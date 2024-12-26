# generate_html_page.py Version 0.01 by chatGPT-4o

"""
This script generates an HTML file to display analysis results from the 'output' folder.

Instructions:
1. Ensure Output Files Exist:
   - Run `analysis.py` to generate the necessary files in the `output` folder.

2. Run the HTML Generator Script:
   - Save this script in your project directory.
   - Execute the script:
     ```bash
     python generate_html_page.py
     ```

3. Check the Generated File:
   - The script will create `index.html` in the `output` folder.
   - Open this file in a web browser to view the results.

4. Publish Using GitHub Pages:
   - Push the `output` folder (including `index.html` and analysis outputs) to your GitHub repository.
   - Follow GitHub Pages setup instructions to publish the page.
"""

import os

def generate_html(output_folder):
    """Generate an HTML page to display the analysis results."""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Data Analysis Results</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                line-height: 1.6;
            }}
            img {{
                max-width: 100%;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <h1>Descriptive Statistics and Keyword Analysis</h1>

        <h2>Pie Charts</h2>
        <p>Program Distribution by Main Categories:</p>
        <img src="output/main_categories_pie_chart.png" alt="Main Categories Pie Chart">

        <p>Program Distribution by AI Levels:</p>
        <img src="output/ai_levels_pie_chart.png" alt="AI Levels Pie Chart">

        <h2>Bar Charts</h2>
        <p>Program Fee Distribution:</p>
        <img src="output/program_fee_distribution.png" alt="Program Fee Distribution">

        <p>Program Duration Distribution:</p>
        <img src="output/program_duration_distribution.png" alt="Program Duration Distribution">

        <h2>Keyword Analysis</h2>
        <p>Download Keyword Distribution Table:</p>
        <a href="output/keyword_distribution.csv" download>Download Keyword Distribution</a>

        <h2>Summary Statistics</h2>
        <p>Download the summary statistics:</p>
        <a href="output/summary_statistics.txt" download>Download Summary Statistics</a>
    </body>
    </html>
    """

    # Save the HTML content to a file
    html_file_path = os.path.join(output_folder, "index.html")
    with open(html_file_path, "w") as file:
        file.write(html_content)

    print(f"HTML page generated successfully: {html_file_path}")

if __name__ == "__main__":
    # Assuming 'output' folder exists in the current directory
    output_directory = "output"

    if not os.path.exists(output_directory):
        print("Error: Output folder does not exist. Please run the analysis script first.")
    else:
        generate_html(output_directory)
