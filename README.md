# 🧬 BC-GEPredict

**AI-Powered Breast Cancer Subtype Classification Using Gene Expression Data**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow.svg)
![AI](https://img.shields.io/badge/AI-Enabled-green.svg)

---

## 📌 Project Overview

**BC-GEPredict** is a machine learning pipeline that leverages RNA-Seq gene expression data to classify breast cancer subtypes. Using data from [GSE96058](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE96058), the model identifies distinct patterns in gene activity to distinguish between different types of breast cancer, helping researchers and clinicians gain deeper biological insight.

---

## 🎯 Objectives

* Predict breast cancer subtypes from RNA-Seq data using AI.
* Visualize gene expression patterns and class separability.
* Explore feature importance and biological interpretation.
* Provide a reproducible workflow for biomedical ML research.

---

## 🧪 Dataset: GSE96058

* 📊 **Samples**: 3,273 breast cancer tissue samples
* 🔬 **Data Type**: RNA-Seq gene and transcript expression
* 🧾 **Labels**: Clinical metadata including cancer subtype, survival, treatment response
* 📁 **Files Used**:

  * `GSE96058_gene_expression_3273_samples_and_136_replicates_transformed.csv.gz`
  * (Optional) `GSE96058_transcript_expression_3273_samples_and_136_replicates.csv.gz`
  * Clinical annotation from series matrix file or supplementary metadata

🔗 Dataset Link: [GSE96058 on GEO](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE96058)

---

## 🧰 Tech Stack

* **Python 3.8+**
* `pandas`, `numpy`, `scikit-learn`
* `matplotlib`, `seaborn`, `plotly`
* Optional: `xgboost`, `lightgbm`, `tensorflow/keras`


---

## 🚀 Getting Started

1. **Clone the Repo**

   ```bash
   git clone https://github.com/codynego/BC-GEPredict.git
   cd BC-GEPredict
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Notebooks**
   Use Jupyter or VSCode to run the analysis notebooks in order.

---

## 📊 Visualizations

* 📌 **PCA plots** to show clustering of subtypes
* 🎯 **Volcano plots** for gene differential expression
* 🔥 **Heatmaps** of high-impact genes
* 🧠 **Feature importance** from ML models

---

## ✅ Tasks

* [x] Load and preprocess gene expression data
* [x] Merge with clinical metadata
* [x] Build classification models (e.g., RandomForest, XGBoost)
* [x] Evaluate with accuracy, F1, confusion matrix
* [ ] Deploy as a web demo (Streamlit/Gradio)

---

## 📈 Results

*You can fill this section later with classification metrics, confusion matrix, and sample predictions.*

---

## 🧠 Future Work

* Integrate transcript-level expression
* Include methylation or mutation data (multi-omics)
* Deploy via API or web app for interactive use

---

## 🤝 Contributing

Contributions welcome! Please fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

Would you like me to generate a `requirements.txt` or help you write any of the notebook files?
