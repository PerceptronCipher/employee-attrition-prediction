# Deployment - Taking the Model to Production

This folder contains everything needed to deploy the employee attrition prediction model as a web application. The goal was to move beyond notebooks and create something HR teams could actually use in their daily workflow.

## What's Inside

### app.py - The Streamlit Application
A user-friendly web interface that allows HR professionals to input employee data and get instant attrition risk assessments. No data science knowledge required.

**Key Features:**
- Simple form-based input for all employee attributes
- Real-time prediction with probability scores
- Risk level classification (High/Medium/Low)
- Actionable recommendations based on risk level

**Design Philosophy:**
The interface was intentionally kept simple. HR teams don't need to understand logistic regression or feature engineering - they need quick, reliable predictions to guide retention conversations. Every input field uses plain language, and results are presented in business terms rather than technical jargon.

### model.pkl - The Trained Model
This is the serialized Logistic Regression model with balanced class weights. It's the final product of all the experimentation in the notebooks folder.

**Model Specifications:**
- Algorithm: Logistic Regression with class_weight='balanced'
- Training data: 1,176 employee records (after 80/20 split)
- Features: 19 carefully selected variables
- Performance: 73% recall, 74% accuracy

**Why This Model?**
After testing multiple algorithms and techniques, this model struck the best balance between catching employees who might leave (recall) and maintaining reasonable accuracy. It's not perfect, but it's practical for real-world deployment where missing an at-risk employee is more costly than a false alarm.

### requirements.txt - Dependencies
Lists all Python packages needed to run the application. Keeping this updated ensures anyone can replicate the deployment environment.

## Running the Application Locally

**Installation:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

The application will launch in your default browser at `http://localhost:8501`

**What You'll See:**
A clean interface divided into sections for personal information, job details, and satisfaction metrics. Fill in the employee's information, click "Predict Attrition Risk," and get an immediate assessment.

## How to Use the Predictions

The model outputs three key pieces of information:

1. **Binary Prediction:** Will the employee leave or stay?
2. **Probability Score:** How confident is the model? (0-100%)
3. **Risk Level:** High (>70%), Medium (40-70%), or Low (<40%)

**Interpreting Results:**

**High Risk (>70% probability):**
This employee needs immediate attention. Schedule a one-on-one conversation, understand their concerns, and explore retention options. The model is flagging clear warning signs.

**Medium Risk (40-70%):**
Proactive engagement is warranted. This employee might not be actively planning to leave, but conditions are ripe for attrition. Regular check-ins and career development discussions could make a difference.

**Low Risk (<40%):**
Continue standard engagement. While no employee is ever completely risk-free, this person shows characteristics of someone likely to stay.

## Limitations and Honest Disclaimers

Let's be clear about what this model can and cannot do:

**What it does well:**
- Identifies about 73% of employees who will actually leave
- Processes predictions instantly
- Considers multiple factors simultaneously
- Provides consistent, unbiased risk assessments

**What it doesn't do:**
- Predict individual decisions with certainty (people aren't algorithms)
- Account for sudden external factors (family emergencies, unexpected job offers)
- Replace human judgment and relationship-building
- Catch the remaining 27% of departing employees

**The precision trade-off:**
The model flags roughly 3 employees for every 1 who actually leaves (32% precision). This means some flagged employees will stay anyway. That's intentional - we optimized for catching departures rather than minimizing false positives. A conversation with someone who's staying is far less costly than missing someone who's leaving.

## Deployment Considerations

If you're thinking about deploying this in a real organization:

**Data Privacy:**
Employee data is sensitive. Ensure compliance with privacy regulations, implement proper access controls, and never store predictions without consent. The current app doesn't persist any data, but production deployments might need audit trails.

**Model Refresh:**
This model was trained on a specific snapshot of employee data. As organizational dynamics change, the model should be retrained periodically with fresh data to maintain accuracy.

**Integration Opportunities:**
The model could be integrated with HRIS systems for automated risk scoring, but manual input was chosen for this demo to maintain transparency and encourage thoughtful use.

## Technical Notes

**Why Streamlit?**
Streamlit was chosen for rapid prototyping and ease of use. It's not the most scalable solution for enterprise deployment, but it's perfect for demonstrating the model's capabilities and getting feedback from stakeholders.

**Model Loading:**
The `@st.cache_resource` decorator ensures the model loads only once, improving performance for multiple predictions.

**Feature Order:**
The input DataFrame must match the exact feature order the model was trained on. Any mismatch will cause errors. The current implementation hardcodes this order to prevent mistakes.

## Future Enhancements

Ideas for improving this deployment:

- Batch prediction capability for analyzing entire departments
- Historical tracking to validate predictions over time
- Feature importance visualization to explain individual predictions
- API endpoint for integration with other HR systems
- Confidence intervals on probability estimates

## Questions or Issues?

If the application doesn't run or predictions seem off, check:
1. All dependencies installed correctly (`pip install -r requirements.txt`)
2. `model.pkl` file is in the same directory as `app.py`
3. Python version compatibility (tested on Python 3.8+)

The model and application represent real work with real limitations. Use the predictions as one input among many when making retention decisions. Human judgment, relationship context, and individual circumstances should always play a role.