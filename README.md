Introduction
This is interactive dashboard that simulates near real time updates without needing distributed system. Emphasis is placed on designing for responsiveness and clarity within local hardware limits.
Objectives
1.	Implement simple streaming or scheduled updates.
2.	Construct multi-element dashboards using Python libraries.
3.	Balance performance and responsiveness for moderate data volumes on a single machine.
4.	Develop a dashboard that is intuitive, with clear navigation and instructions.
5.	Incorporate user experience principles, including layout, color choices, tooltips, and labeling.
Requirement.txt
The following libraries are needed so far:
•	Pandas
•	Streamlit
•	Numpy
•	Matplotlib
•	Seaborn
•	Plotly
Accessibility
The dashboard can be accessed via link https://7yzqxjbsacsici8tvkjq96.streamlit.app/
Documentation of Generated Data
Features:
1.	Size: The dataset contains 750,000 rows, intentionally chosen to be within the 500k-1M range. 
2.	Time-Series Component (timestamp): The timestamp column provides a sequential date and time, allowing for time-based filtering, aggregation, and visualization of trends over time. 
3.	Categorical Grouping (category): The category column introduces a discrete variable, enabling breakdowns and comparisons across different segments.
4.	Numerical Metric (value): The value column provides a continuous numerical metric that can be aggregated and used for various types of quantitative analysis.
5.	Unique Identifier (id): A simple id column ensures each record is unique.
Why it was created for the project:
This synthetic dataset was created to meet the project's requirements for a large, dynamic dataset. Its structure facilitates:
•	Demonstrating Performance: The size will need techniques that handle substantial amounts of data, thereby emphasizing importance of optimization strategies.
•	Simulating Real-World Scenarios: The inclusion of timestamp allows simulating periodic data updates.
•	Enabling Interactive Explorations: The combination of timestamp, category, and value provides ample dimensions for users to interactively filter, group, and analyze the data, fulfilling the requirement for dynamic and user-driven visualizations.




