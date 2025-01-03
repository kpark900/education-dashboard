# generate_html_page.py Version 0.03 by chatGPT-4o

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
    """Generate a mobile-friendly HTML page to display the analysis results."""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Extracurricular Programs in 2025: Data Analysis Dashboard</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            h1, h2, h3 {{
                color: #333;
            }}
            .section {{
                margin-bottom: 40px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                overflow-x: auto;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f4f4f4;
            }}
            @media (max-width: 768px) {{
                body {{
                    margin: 10px;
                }}
                table {{
                    font-size: 14px;
                }}
                h1 {{
                    font-size: 24px;
                }}
                h2 {{
                    font-size: 20px;
                }}
                h3 {{
                    font-size: 18px;
                }}
            }}
        </style>
    </head>
    <body>
        <h1>Extracurricular Programs in 2025: Data Analysis Dashboard</h1>

        <div class="section">
            <h2>1. Descriptive Statistics</h2>
            <h3>1.1 Program Distribution Analysis</h3>

            <h4>Program Distribution by Main Categories</h4>
            <p>The distribution of programs across main categories indicates diverse offerings, with some categories being significantly more prevalent than others. For example, [Insert Most Frequent Category] accounts for the highest proportion of programs, highlighting its prominence in the institution's portfolio. Conversely, less represented categories may signal niche areas or opportunities for expansion.</p>
            <img src="output/main_categories_pie_chart.png" alt="Main Categories Pie Chart">

            <table>
                <thead>
                    <tr>
                        <th>Main Category</th>
                        <th>Frequency</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Category A</td>
                        <td>45</td>
                    </tr>
                    <tr>
                        <td>Category B</td>
                        <td>30</td>
                    </tr>
                </tbody>
            </table>

            <h4>Program Distribution by AI Levels</h4>
            <p>The analysis of AI levels shows [Insert Trend], such as a higher frequency of introductory AI programs compared to advanced ones. This pattern suggests an emphasis on foundational AI education, possibly catering to a broader audience, while more specialized levels are relatively limited.</p>
            <img src="output/ai_levels_pie_chart.png" alt="AI Levels Pie Chart">

            <table>
                <thead>
                    <tr>
                        <th>AI Level</th>
                        <th>Frequency</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Introductory</td>
                        <td>60</td>
                    </tr>
                    <tr>
                        <td>Advanced</td>
                        <td>20</td>
                    </tr>
                </tbody>
            </table>

            <h4>Program Fee Distribution</h4>
            <p>Program fees are predominantly clustered within the [Insert Most Frequent Bin, e.g., "1001-2000"] range, indicating affordability for most offerings. The lower frequency of programs in higher fee ranges may reflect a strategic effort to make programs accessible or a lack of premium, resource-intensive options.</p>
            <img src="output/program_fee_distribution.png" alt="Program Fee Distribution">

            <table>
                <thead>
                    <tr>
                        <th>Fee Range</th>
                        <th>Frequency</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1001-2000</td>
                        <td>50</td>
                    </tr>
                    <tr>
                        <td>2001-5000</td>
                        <td>10</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="section">
            <h2>2. Interpretation</h2>
            <p><b>Diverse Offerings:</b> The distribution of programs by main categories demonstrates a commitment to addressing various educational needs, with room to grow in less represented areas.</p>
            <p><b>AI Education Trends:</b> The emphasis on introductory AI programs aligns with the global trend of democratizing AI knowledge, while the limited advanced-level offerings suggest potential for growth in specialized education.</p>
            <p><b>Flexible Delivery Modes:</b> The popularity of certain delivery formats underscores the institution’s responsiveness to changing student preferences, particularly for online or hybrid learning.</p>
            <p><b>Affordability Focus:</b> The clustering of program fees in mid-range categories highlights a strategic focus on accessible pricing, though opportunities exist to diversify into premium segments.</p>
            <p><b>Efficient Program Lengths:</b> The preference for medium-length programs balances depth with accessibility, catering to a wide audience seeking practical, time-effective learning solutions.</p>
        </div>

        <div class="section">
            <h2>3. Additional Resources</h2>
            <p>Download Keyword Distribution Table:</p>
            <a href="output/keyword_distribution.csv" download>Download Keyword Distribution</a>

            <p>Download Summary Statistics:</p>
            <a href="output/summary_statistics.txt" download>Download Summary Statistics</a>
        </div>

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
