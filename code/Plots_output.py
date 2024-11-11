import pandas as pd
import matplotlib.pyplot as plt

def plot_encoded_text_len_with_zoom(file_path):
    # Read the file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Find the minimum value and its index
    min_value = df['EncodedTextLen'].min()
    min_index = df['EncodedTextLen'].idxmin()
    min_iteration = df['Iteration'][min_index]

    # Define a window around the minimum value for zooming
    window_size = 10  # Number of iterations to include on each side of the min value
    start_index = max(min_index - window_size, 0)
    end_index = min(min_index + window_size, len(df) - 1)

    # Apply a custom style
    plt.style.use('seaborn-darkgrid')

    # Main Plot
    plt.figure(figsize=(12, 7))
    plt.plot(df['Iteration'], df['EncodedTextLen'], marker='o', linestyle='-', color='blue', label='Encoded Text Length')
    plt.title('Encoded Text Length Over Iterations', fontsize=16, fontweight='bold')
    plt.xlabel('Iteration', fontsize=14)
    plt.ylabel('Encoded Text Length', fontsize=14)
    plt.grid(True)

    # Annotate the minimum value
    plt.annotate(f'Min: {min_value}', xy=(min_iteration, min_value), xytext=(min_iteration, min_value + 100),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, fontweight='bold')

    # Highlight the zoomed-in area
    plt.axvspan(df['Iteration'][start_index], df['Iteration'][end_index], color='gray', alpha=0.2, label='Zoomed Area')

    plt.legend()
    plt.savefig('encoded_text_length_over_iterations1.png', format='png')
    plt.show()

    # Zoomed-in Plot
    plt.figure(figsize=(12, 7))
    plt.plot(df['Iteration'][start_index:end_index + 1], df['EncodedTextLen'][start_index:end_index + 1], marker='o', linestyle='-', color='green')
    plt.title(f'Zoomed In: Encoded Text Length Around Minimum Value (Iteration {min_iteration})', fontsize=16, fontweight='bold')
    plt.xlabel('Iteration', fontsize=14)
    plt.ylabel('Encoded Text Length', fontsize=14)
    plt.grid(True)

     # Highlight the zoomed-in area
    window_size = 10  # Number of iterations to include on each side of the min value
    start_index = max(min_index - window_size, 0)
    end_index = min(min_index + window_size, len(df) - 1)
    plt.axvspan(df['Iteration'][start_index], df['Iteration'][end_index], color='gray', alpha=0.2, label='Zoomed Area')

    plt.legend()
    plt.savefig('encoded_text_length_over_iterations3.png', format='png')
    plt.show()

# Path to the uploaded file
file_path = '/content/rozner_text_log1.txt'

plot_encoded_text_len_with_zoom(file_path)