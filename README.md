# Grade Gurus: Linear Regression Model for Grades Prediction
Welcome to Grade Gurus, a predictive model aimed at understanding and forecasting student grades with the help of Linear Regression. Built with simplicity and efficiency in mind, our model provides insights into how various factors might influence academic outcomes. Hosted as a Streamlit application, Grade Gurus offers an interactive and user-friendly interface for real-time grade predictions.

## Features

1. __Grade Prediction__: Utilizes a Linear Regression model to estimate student grades based on provided input features.
2. __Interactive Application__: Powered by Streamlit, the application offers a dynamic and engaging user experience.
3. __Pre-Trained Model__: Comes with a pre-trained Linear Regression model, encapsulated within a Joblib file for immediate use.
## Getting Started

These instructions will guide you through the setup process and help you get the application running on your local machine.

### Prerequisites
Ensure you have Python installed on your system. The project has the following primary dependencies:
1. Streamlit
2. Scikit-learn
3. Pandas
4. Numpy
A comprehensive list of requirements can be found in the requirements.txt file provided with the project.
### Installation
#### Clone the Repository
Begin by cloning the repository to your local machine:
`git clone https://github.com/Nathan-Omenge/grade-gurus.git`
#### Set Up Your Environment
Navigate to the project directory and install the necessary Python packages:
```
cd grade-gurus
pip install -r requirements.txt
```
#### Running the Application
With the environment set up, launch the Streamlit application using:
```bash
streamlit run Grade_Gurus_streamlitscript.py
```
After the command executes, Streamlit will provide a local URL. Open this URL in your web browser to interact with the Grade Gurus application.
## The Model

The heart of Grade Gurus is a Linear Regression model trained on a dataset of student grades and various features that could influence academic performance. This model is serialized and saved as Grade_Gurus.joblib, which the Streamlit application loads to make predictions.

## Contributing

Your contributions make the open-source community a fantastic place to learn, inspire, and create. Any contributions you make to the Grade Gurus project are greatly appreciated;

1. __Fork the Project__
2. __Create your Feature Branch__ (git checkout -b feature/AmazingFeature)
3. __Commit your Changes__ (git commit -m 'Add some AmazingFeature')
4. __Push to the Branch__ (git push origin feature/AmazingFeature)
5. __Open a Pull Request__
## License

This project is not licensed and all rights are reserved by the author. Please contact the author for any requests to use, modify, or distribute this work.
