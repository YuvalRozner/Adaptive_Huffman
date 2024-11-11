# Adaptive Huffman Encoding [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YuvalRozner/Adaptive_Huffman/blob/main/Adaptive_Huffman.ipynb)

This repository contains a Python-based Jupyter notebook implementation of Adaptive Huffman Encoding. The notebook generates a large text file and processes it with Adaptive Huffman coding techniques to illustrate the efficiency of this encoding method.

## Features

- **Text Generation**: Creates a large, random block of text based on user-defined parameters (block size, total length).
- **Adaptive Huffman Encoding**: Demonstrates dynamic Huffman encoding to compress the generated text effectively.
- **Visualization**: Includes visual representations of the Huffman Tree using `graphviz` for a better understanding of the adaptive encoding process.
- **Colab Compatibility**: Can be run directly in Google Colab, with dependencies automatically installed.

![Tree Picture](/TreePic.png)

## Installation

The notebook requires the following Python packages:

- `tqdm`
- `graphviz`
- `moviepy`

To install these dependencies, run the following command:

```bash
!pip install tqdm graphviz moviepy
```

## Usage

1. **Generate Text**: The notebook generates a random block of text using the `create_text` function, which saves the output to `rozner_text2.txt`.
   - Adjust parameters like `total_length` and `blocks` to customize the generated text.
2. **Run Encoding**: After generating the text, Adaptive Huffman encoding is applied, showcasing compression statistics and visualization.

## Running on Google Colab

This notebook is optimized for use in Google Colab. To open it in Colab, click the badge below:
