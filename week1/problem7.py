# Question 7:
import pandas as pd
import numpy as np

def solution(df):
    # Part 1: Select all the "Lotus" cars from the dataset.
    lotus_df = df[df['Make'] == 'Lotus']

    # Part 2: Select only columns "Engine HP" and "Engine Cylinders"
    lotus_df = lotus_df[['Engine HP', 'Engine Cylinders']]

    # Part 3: Now drop all duplicated rows using 'drop_duplicates' method (you should get a df with 9 rows).
    lotus_df = lotus_df.drop_duplicates()

    # Part 4: Get the underlying NumPy array. Let's call it "X"
    X = lotus_df.to_numpy()

<<<<<<< HEAD
    # Part 5: Compute matrix-matrix multiplication between the transpose of X and X. 
    # To get the transpose, use X.T. Let's call the result XTX.
    XTX = X.T @ X

    # Part 6: Compute the inverse of XTX
    XTX_inv = np.linalg.inv(XTX)

    # Part 7: Create an array y with values [1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800].
    y = np.array([1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800])

    # Part 8: Multiply the inverse of XTX with the transpose of X, and then multiply the result by y. Call the result w.
    w = (XTX_inv @ X.T) @ y
    return w[0].round(3)
    # 4.594
=======
    #Question 5: Compute matrix-matrix multiplication between the transpose of X and X. 
    # To get the transpose, use X.T. Let's call the result XTX.
    XTX = X.T @ X

    # Question 6: Compute the inverse of XTX
    XTX_inv = np.linalg.inv(XTX)

    # Question 7: Create an array y with values [1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800].
    y = np.array([1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800])

    # Question 8: Multiply the inverse of XTX with the transpose of X, and then multiply the result by y. Call the result w.
    w = (XTX_inv @ X.T) @ y
    return w[0].round(3)
>>>>>>> main
