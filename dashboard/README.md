# HR Analytics Dashboard

An interactive Tableau dashboard providing comprehensive insights into employee attrition patterns across the organization.

## Dashboard Overview

**Live Metrics:**
- Total Employee Count: 1,470
- Attrition Count: 237 employees
- Attrition Rate: 16.12%
- Active Employees: 1,233
- Average Age: 37 years

## Key Visualizations

### 1. Department-wise Attrition
Pie chart showing attrition distribution across departments:
- **R&D**: 56.12% (133 employees) - Highest attrition
- **Sales**: 38.82% (92 employees)
- **HR**: 5.06% (12 employees) - Lowest attrition

### 2. Employee Distribution by Age Group
Bar chart revealing age demographics with concentration in the 25-44 range, highlighting where attrition risks are highest.

### 3. Job Satisfaction Ratings
Heat map showing satisfaction scores (1-4) across all job roles, with Laboratory Technicians and Sales Executives showing notably large populations at various satisfaction levels.

### 4. Education Field-wise Attrition
Life Sciences (89) and Medical (63) fields show highest attrition counts, suggesting potential targeting for retention efforts.

### 5. Attrition by Gender
Gender breakdown showing male employees (150) experiencing higher attrition than female employees (87).

### 6. Attrition Rate by Age Group and Gender
Donut charts revealing:
- Under 25: Highest attrition rate across both genders
- Attrition decreases with age
- Gender patterns vary by age group

## Business Insights

**High-Risk Segments:**
- R&D department employees
- Younger workforce (Under 25 and 25-34 age groups)
- Life Sciences and Medical education backgrounds
- Employees with lower job satisfaction ratings

**Retention Focus Areas:**
- Early-career employees need stronger engagement
- R&D department requires targeted retention strategies
- Job satisfaction improvements could reduce attrition

## Using the Dashboard

**Interactive Filters:**
- Education level dropdown for demographic analysis
- Click any visualization element to cross-filter related charts
- Hover over data points for detailed tooltips

**Use Cases:**
- Identify departments needing intervention
- Spot demographic trends in turnover
- Monitor satisfaction levels across roles
- Track attrition patterns over time

## Technical Details

**Data Source:** Processed attrition dataset (1,470 employee records)
**Tool:** Tableau Desktop
**File Format:** .twbx (Tableau Packaged Workbook)
**Last Updated:** [Current Date]

## Accessing the Dashboard

Open `Employee_Attrition_Dashboard.twbx` in Tableau Desktop or publish to Tableau Public/Server for web access.

**Requirements:**
- Tableau Desktop 2020.1 or later
- OR Tableau Reader (free) for view-only access

## Integration with ML Model

This dashboard complements the predictive model by:
- Providing historical context for attrition patterns
- Validating model predictions against actual trends
- Identifying segments for targeted intervention
- Monitoring post-intervention effectiveness

The visual insights inform which employee segments the ML model should prioritize for proactive outreach.