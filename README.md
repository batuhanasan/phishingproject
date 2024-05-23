PROBLEM STATEMENT
Phishing attacks pose a major threat to online users, jeopardizing their privacy, financial security, and confidence in online interactions. Detecting and preventing phishing sites is challenging due to the ever-evolving tactics of cybercriminals and requires effective techniques to accurately distinguish between legitimate and malicious websites.

Current phishing detection methods are inadequate in the face of the changing strategies of cybercriminals, and therefore an improved approach is needed to detect phishing sites.

Therefore, there is a critical need to develop an advanced system that can detect phishing sites accurately and efficiently using a combination of advanced machine learning techniques, feature engineering, and behavioral analysis. By overcoming these challenges, the proposed methodology aims to improve the security of online users, protect their sensitive information, and create a safer digital environment.

INTRODUCTION
The aim is to contribute to the development of a safer digital environment by providing an advanced approach to detecting phishing sites. By accurately detecting and preventing phishing threats, the proposed model will increase the security and reliability of online interactions, preventing users from becoming victims of phishing attacks.

In the following sections, we discuss the relevant literature, present the methodology, describe the experiments and results, and evaluate the implications and future directions of the research. The aim of this study is to ensure the security of online users and to create a more robust security infrastructure in the digital world.

APPROACH
⦁	Datasets containing phishing and legitimate websites is collected from open-source platform PhishTank.
⦁	Write a code to extract the required features from the URL database.
⦁	Analyze and preprocess the dataset by using EDA techniques.
⦁	Divide the dataset into training and testing sets.
⦁	Run selected machine learning and deep neural network algorithms on the dataset like Decision Tree, Random Forest, Multilayer Perceptrons, XGBoost and Support Vector Machines on the dataset.
⦁	Write a code for displaying the evaluation result considering accuracy metrics.
⦁	Compare the obtained results for trained models and specify which is better.


PROCEDURE
⦁	All libraries required for the Project:
⦁	TensorFlow
⦁	NumPy
⦁	Pandas
⦁	SciKit-Learn

⦁	Understanding the content of datasets:
⦁	Datasets containing phishing and legitimate websites are collected from the open-source platform PhishTank.
⦁	This service provides a set of phishing URLs in multiple formats, like CSV, JSON etc. , that gets updated hourly. From this dataset, 5000 random phishing URLs are collected to train the machine learning models.
⦁	The legitimate URLs are extracted from the open datasets of the University of New Brunswick. This dataset has a collection of benign, spam, phishing, malware, & defacement URLs. Out of all these types, the benign URL dataset is considered for this project. From this dataset, 5000 random legitimate URLs are collected to train the ML models.
 
 

⦁	Feature Extraction: 
The below-mentioned category of features are extracted from the URL data: ​
⦁	Addressed Bar-based features​
⦁	In this category, 9 features are extracted.​
⦁	Domain-based Features​
⦁	In this category, 4 features are extracted.​
⦁	 HTML & Javascript-based Features​
⦁	In this category, 4 features are extracted. 


Decision Tree and Feature Selection:
 
Random Forest and Feature Selection:
 





⦁	Build and train the model:
Before starting the ML model training, the data is split into 80-20, i.e., 8000 training samples & 2000 testing samples. From the dataset, it is clear that this is a supervised machine-learning task. This data set comes under a classification problem, as the input URL is classified as phishing (1) or legitimate (0). ​
The supervised machine learning models (classification) considered to train the dataset in this project are:
⦁	Decision Tree
⦁	Random Forest
⦁	Multilayer Perceptrons
⦁	XGBoost
⦁	Support Vector Machines


Accuracy Rates of Models before 50 Epoch
 
Accuracy Rates of Models after 50 Epoch
 





Accuracy Rates of Models after 5-Flod Cross Validation
 
Accuracy Rates of Models after Chi-square Feature Selection
 

⦁	Save the model:
⦁	Save the model and calculate the training and testing accuracy.
 

Introduction to the Project Report
This project aims to develop a model using various machine learning algorithms to detect phishing attacks. Phishing is a type of malicious attack that tricks users into revealing sensitive information. In this study, five different algorithms were used to detect phishing URLs: Support Vector Machine (SVM), Multi-Layer Perceptron (MLP), XGBoost, Random Forest, and Decision Tree. Additionally, model performance was evaluated using 5-fold cross-validation and feature selection methods.

Dataset
The dataset used consists of URLs with various features. These features are:
⦁	URL length
⦁	Domain information
⦁	IP address usage
⦁	Using HTTPS
⦁	symbols in URL
⦁	Email content
⦁	IFrame redirects
⦁	Google indexing status
⦁	Page rank
⦁	DNS information
 
 


Data Preprocessing
In the data preprocessing stage, missing data were completed, categorical data were converted to numerical values ​​and the data were normalized. These steps are necessary for machine learning algorithms to work efficiently.

Model Training and Evaluation
Models were trained and evaluated using five different machine learning algorithms. Model performances were evaluated using the 5-fold cross-validation method and the results were presented in tables.

Results and Evaluation
In evaluations made using five different algorithms, the highest accuracy rates were obtained with XGBoost and Random Forest. Feature selection increased model performance and made the model run faster. The results obtained in this project demonstrate the effectiveness of machine learning algorithms in detecting phishing attacks.

       

How does the website work?
- By changing the path of the dataset, the Jupyter Notebook file on which the model is trained will be run step by step from the beginning.
- Then, the libraries and models required in the "application" file and in the Jupyter Notebook content will be installed via the console with the "pip install" command.
- After all the requirements of the code content are prepared, open the command line and type "streamlit run yekta-application.py" and the website will be opened on the local host.

NOTE: If you encounter an error, check the libraries, models and file paths!
