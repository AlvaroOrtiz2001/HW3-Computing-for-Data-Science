import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)


from sklearn.model_selection import train_test_split

def split_data(data, test_size=0.2, random_state=42):
    X_train, X_test = train_test_split(data, test_size=test_size, random_state=random_state)
    return X_train, X_test

def preprocess_data(data):
    # Remove rows with NaN values in specific columns
    data = data.dropna(subset=['age', 'gender', 'ethnicity'])
    
    # Fill NaN with mean values in specific columns
    data['height'] = data['height'].fillna(data['height'].mean())
    data['weight'] = data['weight'].fillna(data['weight'].mean())

    
    # Generate dummies for ethnicity
    data = pd.get_dummies(data, columns=['ethnicity'], prefix='ethnicity')
    
    # Create a binary variable for gender
    data['gender'] = data['gender'].apply(lambda x: 1 if x == 'M' else 0)
    
    return data



