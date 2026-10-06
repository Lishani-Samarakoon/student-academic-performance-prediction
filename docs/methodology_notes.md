# Methodology Notes

## Preprocessing
- Removed non-consenting responses
- Dropped rows missing critical fields
- Encoded ordinal features using midpoint mapping
- Set work hours = 0 where no part-time job
- Binary label from GPA threshold (3.0)

## Validation
- Stratified 5-Fold Cross-Validation
- Class imbalance handled via class_weight='balanced'
- Metrics: Accuracy, Precision, Recall, F1, ROC-AUC

## Statistical Testing
- Shapiro-Wilk for normality
- Paired t-test or Wilcoxon signed-rank (alpha = 0.05)

## Limitations
- Convenience sampling; ~35% Horizon Campus
- Self-reported GPA ranges (not exact values)
- Only ~500 responses collected
- Cross-sectional (no temporal prediction)
