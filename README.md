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
A client has hired the services of ARCOL Data Solutions and has requested that a complete analysis be carried out on the tourism business market in the United States and to create an App that presents a recommendation model with the purpose that interested potential investors have valuable information that allows them to make decisions about investing or not, according to their needs.
To do this, it provides data from the Yelp and Google Maps platforms, through a folder in the Google Drive cloud that it shares with the company.

## Project Structure

| Folder/File              | Description                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| **/data**                | Folder that stores datasets and files used by the Analysis,  Dashboard and ML models.                              |
| **/Preliminary Work**    | Folder containing Jupyter notebooks used for Preliminary ETL and Preliminary EDA process |
| **/Images**              | Folder containing relevant and illustrative images for the analysis project. |
| **/Docs**              | Folder containing LaTex and PDF files (in English and Spanish) with the documentation carried out during each stage of the project, as well as a report with the final analysis and the project conclusions report.|
| **gitignore**            | File specifying folders and files to be ignored by version control (git).                      |
| **LICENSE**              | MIT LICENSE - File specifying the terms under which the source code is shared.                 |
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

## Technology FLow

<p align="center">
  <img src="Images/Tech_dlow.gif">
</p>

## Database Scheme
The Data Warehouse has a snowflake schema where the Business fact table is used as the center, the other tables provide more information to the analyst when making queries, but only if it is necessary. Thus, the database is as follows:

<p align="center">
  <img src="Images/DER.png">
</p>