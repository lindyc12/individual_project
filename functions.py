from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split

# split data and explore on train
def split(df, stratify_by='Casualty_class'):
    # split df into train_validate 
    train_validate, test = train_test_split(df, test_size=.20, random_state=13)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=13)

    X_train = train.drop(columns=['Casualty_class'])
    y_train = train[['Casualty_class']]

    X_validate = validate.drop(columns=['Casualty_class'])
    y_validate = validate[['Casualty_class']]

    X_test = test.drop(columns=['Casualty_class'])
    y_test = test[['Casualty_class']]

    return train, X_train, X_validate, X_test, y_train, y_validate, y_test




# Chi-square feature selection
def feature_chi2(X_train, X_validate, X_test, y_train, k = 25):
     
    # Feature selection
    fs = SelectKBest(score_func = chi2, k = k)
    fs.fit(X_train, y_train)
    
    # Selected columns
    cols = fs.get_support(indices = True)
    
    # Output data
    X_train_fs = X_train.iloc[:, cols]
    X_validate_fs = X_validate.iloc[:, cols]
    X_test_fs = X_test.iloc[:, cols]
    
    return X_train_fs, X_validate_fs, X_test_fs


