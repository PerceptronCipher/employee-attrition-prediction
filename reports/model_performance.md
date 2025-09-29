# Model Performance Analysis

## Executive Summary

This project developed a machine learning solution to predict employee attrition with 73% recall, enabling HR teams to proactively identify and engage with at-risk employees before they resign.

## Performance Metrics Comparison

| Model | Accuracy | Precision | Recall | F1-Score |

| Logistic Regression | 0.87 | 0.67 | 0.15 | 0.24 |
| Random Forest | 0.87 | 0.75 | 0.15 | 0.24 |
| KNN | 0.87 | 0.75 | 0.15 | 0.24 |
| Log Reg (Balanced) | **0.74** | **0.32** | **0.73** | **0.44** |
| RF (Balanced) | 0.87 | 0.75 | 0.15 | 0.24 |
| Log Reg (SMOTE) | 0.73 | 0.31 | 0.71 | 0.43 |
| RF (SMOTE) | 0.88 | 0.65 | 0.27 | 0.38 |
| KNN (SMOTE) | 0.69 | 0.26 | 0.63 | 0.37 |

## Key Findings

**The Class Imbalance Problem:**
Initial models achieved 87% accuracy but failed catastrophically at the actual business objective - they only identified 15% of employees who left. The models learned to predict "stays" for everyone, maximizing accuracy while providing zero business value.

**The Solution:**
Implementing class-balanced weights in Logistic Regression increased recall from 15% to 73%, a 387% improvement. This came at the cost of lower precision (32%) and accuracy (74%), but aligned the model with the business need.

**Selected Model: Logistic Regression (Balanced)**
- Catches 73% of departing employees (30 out of 41 in test set)
- Flags approximately 3 employees for every actual departure
- Maintains interpretability for stakeholder trust

## Business Impact

**Cost-Benefit Analysis:**
- Average cost of employee turnover: $15,000-$50,000 per employee
- Cost of retention conversation: ~$500 (manager time)
- False positive rate acceptable given cost differential

**Actionable Insights:**
The model correctly identified 30 of 41 employees who left in the test set. With proactive intervention, even a 30% success rate on these 30 employees would prevent 9 departures, potentially saving $135,000-$450,000 in turnover costs.

## Model Limitations

**What We're Missing:**
- 27% of departing employees still go undetected (11 of 41)
- 68% of flagged employees don't actually leave (false positives)
- Model can't predict sudden external factors (family moves, unexpected opportunities)

**Assumptions:**
- Historical patterns continue to predict future behavior
- Feature relationships remain stable over time
- Training data represents the current workforce

## Feature Importance

Top predictors of attrition:
1. Age - Younger employees show higher turnover
2. Job Level - Entry and mid-level positions at higher risk
3. Job Involvement - Disengaged employees more likely to leave
4. Monthly Income - Compensation matters
5. Overtime - Work-life balance impacts retention

## Recommendations

**Model Deployment:**
Deploy Logistic Regression (Balanced) as the production model for quarterly attrition risk assessments.

**Model Maintenance:**
- Retrain quarterly with fresh data
- Monitor prediction accuracy against actual departures
- Adjust probability thresholds based on organizational risk tolerance

**Intervention Strategy:**
- High risk (>70%): Immediate manager intervention
- Medium risk (40-70%): Regular check-ins and development planning
- Low risk (<40%): Standard engagement

## Technical Notes

**Test Set:** 294 employees (20% of dataset)
**Class Distribution:** 253 stayed, 41 left (14% attrition rate)
**Training Method:** Stratified split to maintain class balance
**Evaluation:** Focused on recall as primary metric given business context