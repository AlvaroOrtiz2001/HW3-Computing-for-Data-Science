from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression

def train_model(train_data):
    features = ['height','weight','age', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
    target = 'diabetes_mellitus'
    
    X_train = train_data[features]
    y_train = train_data[target]
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    return model

def predict_and_evaluate(model, train_data, test_data):
    X_train = train_data[['height','weight', 'age', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']]
    X_test = test_data[['height','weight', 'age', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']]
    
    train_preds = model.predict_proba(X_train)[:, 1]
    test_preds = model.predict_proba(X_test)[:, 1]
    
    train_roc_auc = roc_auc_score(train_data['diabetes_mellitus'], train_preds)
    test_roc_auc = roc_auc_score(test_data['diabetes_mellitus'], test_preds)
    
    train_data['predictions'] = train_preds
    test_data['predictions'] = test_preds
    
    return train_data, test_data, train_roc_auc, test_roc_auc

