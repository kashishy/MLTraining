import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import warnings

warnings.filterwarnings(action='ignore')


# Function to get data
def get_data(file_name):
    dataframe = pd.read_csv(file_name)
    print(dataframe)
    x_parameters = []
    y_parameters = []

    for single_square_feet, single_price_value in zip(dataframe['square_feet'], dataframe['price']):
        x_parameters.append([float(single_square_feet)])
        y_parameters.append(float(single_price_value))

    return x_parameters, y_parameters


# Function for Fitting data to Linear model
def linear_model_main(X_parameters, Y_parameters, quest_value):
    # Create linear regression object
    regr = LinearRegression()
    print("AREA : ", X_parameters)
    print("PRICE : ", Y_parameters)
    regr.fit(X_parameters, Y_parameters)
    predicated_ans = regr.predict([[quest_value]])
    predictions = {}
    predictions['coefficient'] = regr.coef_
    predictions['intercept'] = regr.intercept_
    predictions['predicted_ans'] = predicated_ans

    print("Output from Machine = ", predicated_ans)

    plt.scatter(X_parameters, Y_parameters, color='m', marker='o', s=30)
    all_predicted_Y = regr.predict(X_parameters)
    plt.scatter(X_parameters, all_predicted_Y, color='b')
    plt.plot(X_parameters, all_predicted_Y, color='r')
    plt.scatter(quest_value, predicated_ans, color='g')
    plt.show()
    return predictions


# Predicting house price for house of 700 square feet area
if __name__ == '__main__':
    x, y = get_data('LR_House_price.csv')
    question_value = 700  # This is the question
    result = linear_model_main(x, y, question_value)
    print("Intercept value(c) : ", result['intercept'])
    print("Coefficient(m) : ", result['coefficient'])
    print("Predicted House Value(y) : ", result['predicted_ans'])
