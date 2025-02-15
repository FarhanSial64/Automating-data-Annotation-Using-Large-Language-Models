# Automating-data-Annotation-Using-Large-Language-Models.

## **Overview**  
This project automates the annotation of research papers by extracting text from PDFs and classifying them into predefined categories using **Large Language Models (LLMs)**. By leveraging **Ollama with the Gemma model**, the system categorizes research papers efficiently, reducing manual effort and improving organization.  

## **Features**  
✅ **Automatic PDF text extraction** (Title & Abstract)  
✅ **LLM-based classification** using locally hosted models  
✅ **Multi-threading support** for faster processing  
✅ **Incremental CSV storage** to prevent data loss  
✅ **Error handling & retries** for stable execution  

## **Project Structure**  

```
📂 Automating-Data-Annotation
│── 📂 data  
│   ├── 2024/ (Folder containing PDFs to process)  
│── 📂 results  
│   ├── AnnotatedPapers.csv (Final output file)  
│── 📜 main.py (Core script for annotation)  
│── 📜 requirements.txt (Dependencies)  
│── 📜 README.md (Project documentation)  
```

## **Installation**  

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/yourusername/Automating-Data-Annotation.git
   cd Automating-Data-Annotation
   ```

2. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Download and set up Ollama (for local LLM processing)**  
   - Install Ollama from [ollama.ai](https://ollama.ai/)  
   - Download the **Gemma** model:  
     ```sh
     ollama pull gemma
     ```

## **Usage**  

1. **Place research papers (PDFs) inside the `/data/2024/` folder.**  
2. **Run the script:**  
   ```sh
   python main.py
   ```  
3. **Annotated results will be saved in `/results/AnnotatedPapers.csv`.**  

## **How It Works**  

1. **Extracts the first page text from each PDF** (title & abstract).  
2. **Sends extracted text to the Gemma LLM model** for classification.  
3. **Assigns a category** based on the model’s response.  
4. **Saves results** (file name, title, abstract, category) in a CSV file.  

## **Categories Used for Classification**  

- Machine Learning  
- Deep Learning  
- Optimization  
- Computer Vision  
- Natural Language Processing (NLP)  

## **Performance Optimization**  

- Implemented **multi-threading** to process multiple PDFs concurrently.  
- Reduced **API dependencies** by using a **local LLM model** (Ollama).  
- Used **incremental file saving** to avoid data loss in case of failure.  

## **Challenges Faced & Solutions**  

🔹 **Slow processing time** → Used multi-threading to speed up execution.  
🔹 **Unexpected model responses** → Implemented text filtering for valid category extraction.  
🔹 **API rate limits** → Switched from cloud-based models to a local LLM.  
🔹 **Handling large datasets** → Optimized memory usage and error handling.  

## **Links**  

📌 **Blog Post:** [Insert Link]  
📌 **LinkedIn Post:** [Insert Link]  

---

This repository provides a **ready-to-use solution for automating research paper annotation** using LLMs. Contributions and improvements are welcome! 🚀  
