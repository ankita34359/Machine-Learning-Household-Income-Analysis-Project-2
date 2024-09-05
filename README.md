# Household Income Prediction Model

𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗢𝘃𝗲𝗿𝘃𝗶𝗲𝘄:

This project aims to predict annual household income based on various demographic, socioeconomic, and personal factors. 
The dataset includes multiple features such as age, education level, occupation, number of dependents, and more. The objective is to build a machine learning model that can accurately predict household income based on these factors.

𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲:

𝗛𝗼𝘂𝘀𝗲𝗵𝗼𝗹𝗱 I𝗻𝗰𝗼𝗺𝗲 M𝗼𝗱𝗲𝗹.𝗶𝗽𝘆𝗻𝗯: Jupyter notebook containing the full data exploration, preprocessing, model training, evaluation, and selection process.
𝗵𝗼𝘂𝘀𝗲𝗵𝗼𝗹𝗱𝗜𝗻𝗰𝗼𝗺𝗲.𝗽𝘆: Streamlit web application that allows users to input data and predict the household income based on the trained model.
𝗵𝗼𝘂𝘀𝗲𝗵𝗼𝗹𝗱_𝗶𝗻𝗰𝗼𝗺𝗲_𝗱𝗮𝘁𝗮.𝗰𝘀𝘃: The dataset used for training and evaluating the models.
𝗵𝗼𝘂𝘀𝗲𝗵𝗼𝗹𝗱_𝗶𝗻𝗰𝗼𝗺𝗲_𝗰𝗵𝘂𝗿𝗻_𝗺𝗼𝗱𝗲𝗹.𝗽𝗸𝗹: The saved machine learning model (using joblib) that is used for predictions in the Streamlit app.

𝗧𝗮𝘀𝗸𝘀 𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗲𝗱

𝟭) 𝗗𝗮𝘁𝗮 𝗘𝘅𝗽𝗹𝗼𝗿𝗮𝘁𝗶𝗼𝗻 𝗮𝗻𝗱 𝗦𝘁𝗮𝘁𝗶𝘀𝘁𝗶𝗰𝗮𝗹 𝗔𝗻𝗮𝗹𝘆𝘀𝗶𝘀

Performed exploratory data analysis (EDA) to understand the dataset.
Calculated summary statistics, identified outliers, and visualized distributions.
Handled missing values and corrected any inconsistencies in the data.

𝟮) 𝗔𝗹𝗴𝗼𝗿𝗶𝘁𝗵𝗺 𝗦𝗲𝗹𝗲𝗰𝘁𝗶𝗼𝗻

Considered and tested multiple machine learning algorithms suitable for regression tasks, including:
Linear Regression
Decision Tree Regressor
Random Forest Regressor
K-Nearest Neighbors (KNN)
Gradient Boosting Machine (GBM)
XGBoost Regressor

𝟯) 𝗗𝗮𝘁𝗮 𝗣𝗿𝗲𝗽𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴

Normalized continuous variables like age and work experience.
Applied encoding to categorical variables such as education level, occupation, and homeownership status.
Split the dataset into training and testing sets to evaluate model performance.

𝟰) 𝗠𝗼𝗱𝗲𝗹 𝗧𝗿𝗮𝗶𝗻𝗶𝗻𝗴

Trained several regression models using the processed data.
Used cross-validation to ensure models were generalized well.
Evaluated each model using performance metrics such as Mean Squared Error (MSE), R-squared (R²), and Root Mean Squared Error (RMSE).

𝟱) 𝗠𝗼𝗱𝗲𝗹 𝗘𝘃𝗮𝗹𝘂𝗮𝘁𝗶𝗼𝗻

Compared models based on their performance metrics and selected the best model.
Used feature importance methods to understand which features contributed most to predicting household income.

 𝟲) 𝗠𝗼𝗱𝗲𝗹 𝗦𝗮𝘃𝗶𝗻𝗴

Saved the best-performing model using joblib for future use in the application.

𝟳) 𝗦𝘁𝗿𝗲𝗮𝗺𝗹𝗶𝘁 𝗪𝗲𝗯 𝗔𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻

Developed a user-friendly web application using Streamlit that allows users to predict household income based on the input of demographic and socioeconomic features.
The app also provides visual feedback in the form of graphs for better understanding of income trends.

𝟴) 𝗗𝗲𝗽𝗹𝗼𝘆𝗺𝗲𝗻𝘁 𝗼𝗻 𝗚𝗶𝘁𝗛𝘂𝗯

Uploaded the Jupyter notebook, trained model, Streamlit app, and dataset to GitHub for public access.

𝗖𝗼𝗻𝗰𝗹𝘂𝘀𝗶𝗼𝗻

This project successfully demonstrates the ability to predict household income based on a variety of demographic and socioeconomic factors. The Streamlit application provides an easy-to-use interface for users to input relevant data and receive income predictions. 
