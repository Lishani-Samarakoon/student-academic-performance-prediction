# Student Academic Performance Prediction

Machine learning study predicting **Low / High academic performance** among Sri Lankan undergraduates using behavioural, workload, and employment features.

**Module:** IT41043 - Intelligent Systems, Horizon Campus  
**Authors:** S.W.M.L.M. Samarakoon (ITBIN-2312-0005) & M.M.H. Thilakarathne (ITBNM-2211-0191)

## Research Question
Does adding engineered behavioural and workload features (workload, assignments, self-study hours, part-time work hours) improve predictive performance over a baseline model using attendance alone?

## Dataset
- **Source:** Google Forms survey
- **Size:** 512 raw responses -> cleaned to 502 usable rows (396 Low, 106 High - a 79/21 class split)
- **Features:** Attendance, Workload, Assignment Frequency, Self-study Hours, Part-time Work Hours
- **Target:** Label from Current GPA (>=3.0 = High, <3.0 = Low)

## Models Compared
| Model | Algorithm | Features |
|-------|-----------|----------|
| LR-Base | Logistic Regression | Attendance only |
| RF-Base | Random Forest | Attendance only |
| LR-Prop | Logistic Regression | All 5 features |
| RF-Prop | Random Forest | All 5 features |

## Results

| Model | Accuracy | F1-Score | ROC-AUC |
|-------|----------|----------|---------|
| LR-Base | 0.448 | 0.242 | 0.426 |
| RF-Base | 0.552 | 0.180 | 0.424 |
| LR-Prop | 0.532 | 0.312 | 0.536 |
| RF-Prop | **0.673** | **0.300** | **0.584** |

### Class Imbalance Investigation
Initial models suffered from class imbalance (79/21 split). We tested SMOTETomek inside each cross-validation fold. While accuracy improved to 0.731, F1 dropped to 0.203 and ROC-AUC dropped to 0.563 — meaning the synthetic sampling did not improve minority-class detection on this dataset.

Statistical test (RF-Prop vs LR-Base): paired t-test, p = 0.1751 (not significant at α = 0.05).

## Project Structure
```text
├── data/                  # Raw and processed datasets
├── models/                # Saved .pkl model files
├── results/               # Evaluation metrics, tables, and figures
├── paper/figures/         # System architecture diagram
├── docs/                  # Ethics statement and methodology notes
├── src/                   # Python scripts for training and evaluation
└── Research_Pipeline.ipynb # Main Jupyter notebook with full pipeline
