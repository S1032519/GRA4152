import argparse

def  my_logistic_regression(penalty , fit_intercept , max_iter , tol):
    from sklearn.linear_model import LogisticRegression

    # define a logistic regression object with your input params

    clf = LogisticRegression(penalty=penalty, fit_intercept=fit_intercept, max_iter=max_iter, tol=tol)
    
    return clf

parser = argparse.ArgumentParser(description= """
                                 This code runs a logistic regression and it has 4 arguments that must be specified:

                                 - Penalty: The penalty argument specifies the type of regularization, "l1" = Lasso, "l2" = Ridge, "elasticnet" = elastic net (combination of Ridge and Lasso) or you can have no regularisation "none".
                                 - fit_intercept: adds an intercept to the regression.
                                 - max_iter: Specify how many iterations you want to run. Default = 100.
                                 - tol: Is a stopping parameter and the solver will stop if it does not improve by at least this amount. Default = 0.0001.
                                """,
                                 epilog = "Find the originan function here: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html")
parser.add_argument("--Penalty", type = str, required = True, choices= ["l1", "l2", "elasticnet", "none"],
                    help = "Type of regularization, with the choices l1, l2, elasticnet and none")
parser.add_argument("--fit_intercept", action = "store_true", required = True,
                    help = "If this parameter is specified a constant term (intercept) is added to the regression.")
parser.add_argument("--max_iter", type = int, default = 100,required = True,
                    help = "Choose the number of iterations, the default value is 100")
parser.add_argument("--tol", type = float, default = 0.0001 ,required = True,
                    help = "Choose tolerance (often a very low number) for stopping criteria. The default value is 0.0001")

args = parser.parse_args()
print(args)