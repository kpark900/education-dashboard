# analysis.py Version 0.01 by chatGPT-4o

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

def load_data():
    """Load datasets into dataframes."""
    categories_file = 'revised-1-program-categories.csv'
    instances_file = 'revised-2-program-instances-100.csv'
    learning_outcomes_file = 'revised-3-learning-outcomes.csv'

    categories_df = pd.read_csv(categories_file)
    instances_df = pd.read_csv(instances_file)
    learning_outcomes_df = pd.read_csv(learning_outcomes_file)

    return categories_df, instances_df, learning_outcomes_df

def descriptive_statistics(categories_df):
    """Generate descriptive statistics and visualizations."""
    # Frequency of main categories
    main_categories_freq = categories_df['Main_Categories'].value_counts()

    # Frequency of AI levels
    ai_level_freq = categories_df['AI_Level'].value_counts()

    # Frequency of delivery modes
    delivery_mode_freq = categories_df['Delivery_Mode'].value_counts()

    # Frequency of program fees (binned)
    program_fee_bins = pd.cut(categories_df['Program_Fee'], bins=[0, 500, 1000, 2000, 5000, 10000], 
                              labels=['0-500', '501-1000', '1001-2000', '2001-5000', '5001-10000'])
    program_fee_freq = program_fee_bins.value_counts()

    # Frequency of durations (binned)
    duration_bins = pd.cut(categories_df['Duration_Weeks'], bins=[0, 4, 8, 12, 16, 52], 
                           labels=['0-4 weeks', '5-8 weeks', '9-12 weeks', '13-16 weeks', '17-52 weeks'])
    duration_freq = duration_bins.value_counts()

    # Visualize main categories
    plt.figure(figsize=(10, 6))
    main_categories_freq.plot.pie(autopct='%1.1f%%', title='Program Distribution by Main Categories', ylabel='')
    plt.savefig('output/main_categories_pie_chart.png')

    # Visualize AI levels
    plt.figure(figsize=(10, 6))
    ai_level_freq.plot.pie(autopct='%1.1f%%', title='Program Distribution by AI Levels', ylabel='')
    plt.savefig('output/ai_levels_pie_chart.png')

    # Visualize delivery modes
    plt.figure(figsize=(10, 6))
    delivery_mode_freq.plot.pie(autopct='%1.1f%%', title='Program Distribution by Delivery Modes', ylabel='')
    plt.savefig('output/delivery_modes_pie_chart.png')

    # Visualize program fee distribution
    plt.figure(figsize=(10, 6))
    program_fee_freq.plot.bar(title='Program Fee Distribution (Binned)', rot=45)
    plt.xlabel('Program Fee Ranges')
    plt.ylabel('Frequency')
    plt.savefig('output/program_fee_distribution.png')

    # Visualize program duration distribution
    plt.figure(figsize=(10, 6))
    duration_freq.plot.bar(title='Program Duration Distribution (Binned)', rot=45)
    plt.xlabel('Duration Ranges (Weeks)')
    plt.ylabel('Frequency')
    plt.savefig('output/program_duration_distribution.png')

    return {
        'Main Categories Frequency': main_categories_freq,
        'AI Level Frequency': ai_level_freq,
        'Delivery Mode Frequency': delivery_mode_freq,
        'Program Fee Frequency': program_fee_freq,
        'Program Duration Frequency': duration_freq
    }

def keyword_analysis(categories_df):
    """Analyze keywords that highlight program focus."""
    # Combine text from relevant columns for keyword analysis
    text_data = " ".join(categories_df['Program_Title'] + " " + categories_df['Main_Categories'])

    # Tokenize and clean text data
    keywords = re.findall(r'\b\w+\b', text_data.lower())

    # Exclude stop words
    stop_words = set(['and', 'of', 'in', 'the', 'to', 'for', 'with', 'on', 'by', 'a', 'an', 'as', 'at'])
    filtered_keywords = [word for word in keywords if word not in stop_words]

    # Count keyword frequencies
    keyword_counts = Counter(filtered_keywords)
    keyword_distribution = pd.DataFrame(keyword_counts.most_common(15), columns=['Keyword', 'Frequency'])

    # Visualize keyword distribution
    plt.figure(figsize=(12, 6))
    plt.bar(keyword_distribution['Keyword'], keyword_distribution['Frequency'])
    plt.title('Distribution of Keywords Highlighting Program Focus')
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.savefig('output/keyword_distribution.png')

    return keyword_distribution

def main():
    """Main function to execute the analysis."""
    # Load data
    categories_df, instances_df, learning_outcomes_df = load_data()

    # Generate descriptive statistics
    stats = descriptive_statistics(categories_df)
    print("Descriptive statistics saved.")

    # Perform keyword analysis
    keyword_dist = keyword_analysis(categories_df)
    print("Keyword distribution analysis saved.")

    # Save summary results
    with open('output/summary_statistics.txt', 'w') as f:
        f.write("Descriptive Statistics Summary:\n")
        for key, value in stats.items():
            f.write(f"{key}:\n{value}\n\n")

    keyword_dist.to_csv('output/keyword_distribution.csv', index=False)
    print("Results saved in the output directory.")

if __name__ == "__main__":
    main()
