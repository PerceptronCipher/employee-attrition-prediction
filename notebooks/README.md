# Notebooks - The Heart of the Analysis

Welcome to the notebooks folder. This is where the real work happened - the exploration, experimentation, and model building that transformed raw employee data into a production-ready attrition prediction system.

## What You'll Find Here

### eda.ipynb - Exploratory Data Analysis
This is where I got to know the data intimately. Before making any modeling decisions, I needed to understand what I was working with.

**What's inside:**
- Initial data exploration and quality assessment
- Distribution analysis of attrition across different employee segments
- Correlation patterns between features
- Visual storytelling through charts and plots

**Key discoveries from EDA:**
The data revealed some interesting patterns. Attrition wasn't evenly distributed across the organization - certain departments, job roles, and age groups showed notably higher turnover rates. These insights directly influenced my preprocessing and feature engineering decisions. You'll see how satisfaction metrics, overtime work, and compensation factors emerged as potential signals worth investigating further.

The visualizations saved to `reports/figures/` tell the story more clearly than any summary could. Take a look at the attrition by department chart - it's quite revealing.

### models.ipynb - Building the Prediction Engine
This notebook represents the iterative journey of model development. Spoiler alert: it wasn't a straight path.

**The progression:**
1. **Baseline models** - Started with Logistic Regression, Random Forest, and KNN
2. **The wake-up call** - All models achieved ~87% accuracy but only caught 15% of employees who actually left
3. **Root cause analysis** - Identified class imbalance as the culprit (83% vs 17% distribution)
4. **Solution implementation** - Applied class weighting and SMOTE techniques
5. **Breakthrough** - Improved recall from 15% to 73%

**Why this matters:**
In employee attrition prediction, missing someone who's about to leave is expensive. We needed a model that errs on the side of caution - better to have a conversation with someone who's actually staying than to miss someone who's walking out the door.

The final Logistic Regression model with balanced class weights became our production choice. Not because it had the highest accuracy, but because it aligned with the business objective: catch as many departing employees as possible while they can still be retained.

## The Story Behind the Analysis

If you're reviewing this project, you might wonder why I chose certain approaches. Let me walk you through the thinking.

**On feature selection:** The mutual information analysis in preprocessing wasn't just a statistical exercise. It was about understanding which employee characteristics actually predict attrition. Age and job level emerged as top predictors, but so did factors like job involvement and specific roles. This informed both the modeling strategy and potential business interventions.

**On class imbalance:** The initial models looked great on paper - 87% accuracy sounds impressive. But when you dig into the confusion matrix, you realize the models were just predicting "stays" for almost everyone. This is a common trap in imbalanced datasets. The real work was forcing the models to care about the minority class.

**On model selection:** I tested multiple algorithms not to show off technical skills, but because different algorithms make different assumptions. Logistic Regression's interpretability won out because stakeholders need to understand why someone is flagged as at-risk. Random Forest gave marginally better accuracy but couldn't explain individual predictions as clearly.

## Running These Notebooks

Both notebooks are designed to run sequentially:
1. Start with `eda.ipynb` to understand the data landscape
2. Move to `models.ipynb` to see the modeling journey

**Requirements:**
- Python 3.8+
- Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, imbalanced-learn
- The processed dataset from `data/processed/`

**Expected runtime:** 
- EDA: ~5 minutes
- Models: ~15 minutes (SMOTE resampling takes time with 1,470 samples)

## What I Learned

This project reinforced something important: high accuracy doesn't mean a good model. It means your model learned something, but not necessarily what you need it to learn. The class imbalance problem was a humbling reminder that evaluation metrics need to align with business objectives.

The 73% recall we achieved with the final model isn't perfect - we're still missing 27% of departures. But it's a massive improvement over baseline, and more importantly, it's actionable. HR can now proactively engage with three-quarters of at-risk employees instead of being blindsided by resignations.

## Questions or Feedback?

If you're reviewing this project and something isn't clear, that's on me. These notebooks represent real work, including the messy parts where things didn't work as expected. That's the honest story of data science - iteration, experimentation, and course correction.

Feel free to dig into the code, challenge the assumptions, or suggest improvements. Every model has limitations, and I'm always interested in perspectives I might have missed.