import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

TOTAL_CALORIES_IN_KG = 7700
USER_GENDER = 0  # 0 - woman, 1 - man
USER_HEIGHT = 167
USER_AGE = 24
USER_SCORE = 2
NUM_OF_DAYS = 7
USER_WEIGHTS = [74.5, 73.7, 73.3, 73, 72.2, 72.4, 72.5, 70.1]
USER_DEFICITS = [0.0, 6160.0, 9240.0, 11550.0, 17710.0, 16170.0, 15400.0, 33880.0]
DAILY_CALORIES = 1500


# Metabolic Rate Calculator
def bmr_calc(gender, weight, height, age, score):
    # woman
    if gender == 0:
        bmr = 655 + weight * 9.6 + height * 1.8 - age * 4.7
    # man
    elif gender == 1:
        bmr = 66 + weight * 13.8 + height * 5 - age * 6.8

    # Easy active
    if score == 1:
        return 1.2 * bmr
    # Moderately active
    elif score == 2:
        return 1.375 * bmr
    # Very active
    elif score == 3:
        return 1.725 * bmr
    # An extraordinary activist
    elif score == 4:
        return 1.9 * bmr


def main():
    # dict of weights and caloric deficit for the client
    df1 = pd.DataFrame({'Weight': [], 'CaloricDeficit': []})
    df1 = df1.assign(Weight=USER_WEIGHTS, CaloricDeficit=USER_DEFICITS)

    # ml algorithm
    reg = linear_model.LinearRegression()
    y = np.asanyarray(df1['Weight'])
    x = np.asanyarray(df1['CaloricDeficit'])
    reg.fit(x.reshape(-1, 1), y)

    # prv info
    last_data = df1.tail(1).iloc[0]
    prv_weight = last_data['Weight']
    caloric_deficit_sum = last_data['CaloricDeficit']

    # find the predicted deficit based on the BMR calculator
    bme_result = (bmr_calc(gender=USER_GENDER, weight=prv_weight, height=USER_HEIGHT, age=USER_AGE,
                           score=USER_SCORE) - DAILY_CALORIES)
    bmr_deficit = round(bme_result * NUM_OF_DAYS, 2)
    total_deficit = bmr_deficit + caloric_deficit_sum

    # predict the weight based on the deficit by the linear regression model
    prediction = reg.predict([[total_deficit]])[0]
    prediction = round(prediction, 2)
    print("Your predicted weight according to your deficit: {}".format(prediction))

    # get the real weight
    print("Please enter you weight in scale: ")
    real_weight = float(input())

    # check the accuracy
    accuracy = (1 - (abs(prediction - real_weight) / real_weight)) * 100
    accuracy = round(accuracy, 2)
    print("Your models accuracy is % {}".format(accuracy))

    # update the data based on the *real* new info
    new_deficit = round((prv_weight - real_weight) * TOTAL_CALORIES_IN_KG, 2) + caloric_deficit_sum
    df1.append({'Weight': real_weight, 'CaloricDeficit': new_deficit}, ignore_index=True)


if __name__ == "__main__":
    main()


# find the calories predictions
# for w in USER_WEIGHTS:
#     try:
#         caloric_deficit_sum = df1.tail(1).iloc[0]['CaloricDeficit']
#         prv_weight = df1.tail(1).iloc[0]['Weight']
#         new_deficit = round((prv_weight - w) * TOTAL_CALORIES_IN_KG, 2) + caloric_deficit_sum
#         df1 = df1.append({'Weight': w, 'CaloricDeficit': new_deficit}, ignore_index=True)
#     except Exception as e:
#         new_row = {'Weight': w, 'CaloricDeficit': 0}
#         df1 = df1.append(new_row, ignore_index=True)


# plt.scatter(df1['CaloricDeficit'], df1['Weight'],  color='blue')
# plt.title("Weight Prediction Model")
# plt.ylabel('Weight')
# plt.xlabel('CaloricDeficit')
# plt.show()
