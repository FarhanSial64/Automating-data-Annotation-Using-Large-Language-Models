import os
import fitz  # PyMuPDF
import pandas as pd
import time
import ollama  # Local LLM
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define categories for classification
categories = [
    "Machine Learning",
    "Deep Learning",
    "Optimization",
    "Computer Vision",
    "Natural Language Processing (NLP)"
]

# Path to the folder containing PDFs
pdf_folder = r"E:\pdfs\2024"
output_csv = r"E:\AnnotatedPapers.csv"

print("Starting the annotation process...")

# Function to extract text from the first page of a PDF
def extract_text_from_pdf(pdf_path):
    try:
        print(f"Extracting text from: {pdf_path}")
        doc = fitz.open(pdf_path)
        text = doc[0].get_text("text")  # Extract text from the first page
        doc.close()
        return text
    except Exception as e:
        print(f"Error extracting {pdf_path}: {e}")
        return ""

# Function to classify a paper using Ollama with the Gemma model
def classify_paper(title, abstract):
    prompt = f"""
    Classify the following research paper into one of these categories:
    - Machine Learning
    - Deep Learning
    - Optimization
    - Computer Vision
    - Natural Language Processing (NLP)

    Title: {title}
    Abstract: {abstract}
    Provide only the category name as output.
    """

    try:
        print(f"Classifying paper: {title}")
        response = ollama.chat(model="gemma", messages=[{"role": "user", "content": prompt}])

        # Debug: Print the full response to check its structure
        print("Ollama Response:", response)

        # Extract response safely
        raw_category = response.get("message", {}).get("content", "").strip()

        # Ensure response is valid
        if not raw_category:
            print("Error: Empty response from model")
            return "Error"

        # Normalize response (remove extra text)
        predicted_category = next((cat for cat in categories if cat.lower() in raw_category.lower()), "Other")

        print(f"Category assigned: {predicted_category}")
        return predicted_category
    except Exception as e:
        print(f"Error during classification: {e}")
        return "Error"

# Function to process a single PDF (extract text, classify, and save)
def process_pdf(pdf_file):
    pdf_path = os.path.join(pdf_folder, pdf_file)
    text = extract_text_from_pdf(pdf_path)

    if text:
        lines = text.split("\n")
        title = lines[0] if len(lines) > 0 else "Unknown Title"
        abstract = " ".join(lines[1:6]) if len(lines) > 5 else "No Abstract Found"

        category = classify_paper(title, abstract)
        paper_data = [pdf_file, title, abstract, category]

        # Save after every classification (Append Mode)
        df = pd.DataFrame([paper_data], columns=["File Name", "Title", "Abstract", "Category"])
        df.to_csv(output_csv, mode='a', header=not os.path.exists(output_csv), index=False)
        print(f"Saved {pdf_file} to CSV.")

    return pdf_file  # Return processed file name for tracking

# Process all PDFs in parallel using threading
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

with ThreadPoolExecutor(max_workers=5) as executor:  # You can adjust max_workers based on your CPU
    future_to_pdf = {executor.submit(process_pdf, pdf): pdf for pdf in pdf_files}

    for future in as_completed(future_to_pdf):
        try:
            processed_pdf = future.result()
            print(f"Completed processing: {processed_pdf}")
        except Exception as e:
            print(f" Error processing a file: {e}")

print(f" Annotation complete. Data stored at: {output_csv}")
