![Python](https://img.shields.io/badge/Python-333333?style=flat&logo=python)
![Apache Spark](https://img.shields.io/badge/-Apache%20Spark-333333?style=flat&logo=apache-spark)
![PySpark](https://img.shields.io/badge/-PySpark-333333?style=flat&logo=apache-spark)
![Jupyter](https://img.shields.io/badge/-Jupyter_Notebook-333333?style=flat&logo=jupyter)
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![MySQL](https://img.shields.io/badge/-MySQL-333333?style=flat&logo=mysql)
![Azure](https://img.shields.io/badge/-Microsoft%20Azure-333333?style=flat&logo=microsoft-azure)
![Powerbi](https://img.shields.io/badge/-PowerBI-333333?style=flat&logo=powerbi)
![VSC](https://img.shields.io/badge/Visual_Studio_Code-333333?style=flat&logo=visual%20studio%20code&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-333333?style=flat-square&logo=LaTeX&logoColor=white)

# Invesment_Recomendation_Project
<p align="center">
  <img src="Images/ARCOL.gif" alt="Logo" width="300" height="300">
</p>

## Project Description
A costumer has hired the services of ARCOL Data Solutions and has requested that a complete analysis be carried out on the tourism business market in the United States and to create an App that presents a recommendation model with the purpose that interested potential investors have valuable information that allows them to make decisions about investing or not, according to their needs.
To do this, it provides data from the Yelp and Google Maps platforms, through a folder in the Google Drive cloud that it shares with the company.

## Project Structure

| Folder/File              | Description                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| **/data**                | Folder that stores datasets and files used by the Analysis,  Dashboard and ML models.                              |
| **/Notebooks**           | Folder containing Jupyter notebooks used for ETL, EDA and feature engineering processes |
| **/Images**              | Folder containing relevant and illustrative images for the analysis project. |
| **/Docs**              | Folder containing LaTex and PDF files (in English and Spanish) with the documentation carried out during each stage of the project, as well as a report with the final analysis and the project conclusions report.|
| **requirements.txt**     | File listing dependencies and libraries required to run the project.                           |
| **gitignore**            | File specifying folders and files to be ignored by version control (git).                      |
| **LICENSE**              | MIT LICENSE - File specifying the terms under which the source code is shared.                 |
| **main.py**              | Main Python file serving as an entry point for the application, defining Model configuration and execution|
| **README.md**            | Main project documentation in English.                                                         |
| **README_ESP.md**        | Main project documentation in Spanish.                                                         |


## Authors

<p align="center">
  <img src="Images/Team.png">
</p>


| Name                     | Rol                                       | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)|![LinkedIn](https://img.shields.io/badge/linkedin-%231DA1F2.svg?style=for-the-badge&logo=linkedin&logoColor=white)                |
| ------------------------ | ----------------------------------------- | -------------------------------- |--------------------------------|
| **Leonardo Cortés**      | Project Manager (PM) and Data Scientist   |[leocortes85](https://github.com/leocortes85/)  |[Leonardo Cortés Zambrano](https://www.linkedin.com/in/leonardo-cort%C3%A9s-zambrano/)
| **Marcelo Atencio**      | Task Manager and Data Engineer            |[MarceloAtencio](https://github.com/MarceloAtencio/) |[Marcelo Atencio](https://www.linkedin.com/in/marcelo-atencio/)
| **Federico López**       | Data Analyst and Data Story Teller.       |[alopezfederico](https://github.com/alopezfederico/) |[Federico Antonio López](https://www.linkedin.com/in/federico-a-lopez/)  |
| **Andrés Ruiz**         | Data Engineer and ML Engineer             |[a1ternocles](https://github.com/alopezfederico/) |[Andrés Ruiz](https://www.linkedin.com/in/andresruiz94/) |

## Preliminay Work

As preliminary work, business data that exists on Google Maps and Yelp is loaded.
In order to optimize the size of the files and the use of resources when working with the data, a change to parquet format is made, optimizing the use of resources by 69%.
Additionally, a preliminary analysis of the quality of the data contained in the files is carried out.


## Technology Stack

<p align="center">
  <img src="Images/Tech_Stack.png">
</p>

## Technology FLow

<p align="center">
  <img src="Images/Tech_flow.gif">
</p>

## Database Scheme
The Data Warehouse has a snowflake schema where the Business fact table is used as the center, the other tables provide more information to the analyst when making queries, but only if it is necessary. Thus, the database is as follows:

<p align="center">
  <img src="Images/DER.png">
</p>


## Transformations

- Extract, transform and load (ETL) were performed using the Pandas library automating a data loading scheme from the client-provided folder.
- Strategies were applied to handle nested data and irrelevant or highly null columns were eliminated.
- An incremental load of information required to complement the tables was carried out, based on extraction models with external APIs, web-scrapping and function formulation

## Exploratory Data Analysis (EDA)

- EDA was conducted on transformed datasets using Pandas, Matplotlib, and Seaborn.
- Relevant variables for creating the recommendation and relational models were identified.

## Dimensional Tables and Relational Model

- With the variables selected during the analysis, a relational model was created with auxiliary dimensional tables, tow facts tables and a main table, in order to organize the information and easily access it.
- The relational model was automatized to work with in Data Warehouse

## Pipeline
An autimatized pipline of data was created and executed to run the projecto from data base provided by costumer to Data Warehouse

<p align="center">
  <video width="640" height="360" controls>
    <source src="Images/Pipeline.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</p>

## Data Analysis Process

From the Data Warehouse, we extract clean and structured data to perform data analysis and data science processes.

For the Data Analysis process, we take the dimensional tables and create a semantic model that relates the tables to each other to perform specific analysis in an interactive Dashboard.

<p align="center">
  <img src="Images/Analysis.png">
</p>

<p align="center">
  <img src="Images/KPI.png">
</p>


## Machine Learning Process

Likewise, we use structured data to perform the Machine Learning process, where three functions are proposed to obtain the desired results. These functions take one or two arguments provided by the user according to their interest (State, Category) to choose from a series of recommended businesses with their respective information.

<p align="center">
  <img src="Images/ML.png">
</p>

## Deployment and Final Product

Finally, the necessary process was carried out to deliver a final product installed on a website with Streamlit tool, where the user can find all the corresponding information about ARCOL Data Solutions and, of course, the interactive dashboard and the model that will recommend businesses tailored to their interests.

The final product can be viewed [HERE](https://arcolsolutions.streamlit.app/)

## Improvement opportunities

Some improvement opportunities identified in this project, which are planned as future work, are:

- Create a loop through a link to the recommendations given by the ML model created, so that the user can also obtain information about each of the recommended businesses, beyond the one chosen by them.
- Carry out a greater analysis with each KPI, showing not only the measurement result but also the information relevant to each KPI.
- Add more relevant information about the business (photographs, sales, etc.) to give a better decision tool to an investor

## Dislcaimer

This README provides an overview of the Invesment Recomendation project, highlighting key processes and outcomes. For detailed information on implementation, refer to the documentation and source code on the GitHub repository. You can also access the API and explore the documentation at the Product model link.
