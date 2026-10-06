# Student Academic Performance Prediction

Machine learning study predicting **Low / High academic performance** among Sri Lankan undergraduates using behavioural, workload, and employment features.

**Module:** IT41043 - Intelligent Systems, Horizon Campus  
**Author:** S.W.M.L.M. Samarakoon (ITBIN-2312-0005)

## Research Question
Does adding engineered behavioural and workload features (workload, assignments, self-study hours, part-time work hours) improve predictive performance over a baseline model using attendance alone?

## Dataset
- **Source:** Google Forms survey
- **Size:** 512 raw responses -> cleaned to ~500 usable rows
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
See `results/tables/model_comparison.csv`

## How to Reproduce
```bash
git clone https://github.com/Lishani-Samarakoon/student-academic-performance-prediction.git
cd student-academic-performance-prediction
pip install -r requirements.txt