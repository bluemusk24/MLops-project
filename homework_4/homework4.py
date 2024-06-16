#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import sys


categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


# Load the model
with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


# Apply dictvectorizer and predict
def predict(df):

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    
    y_pred = model.predict(X_val)
    return y_pred
    

def apply_model(input_data):
    print(f'reading the data from {input_data}..')
    df = read_data(input_data)

    print('applying the dictvectorizer and model to  get predictions...')
    y_pred = predict(df)
    
    print('get the mean predicted duration..')
    print(y_pred.mean())
    

def run():
    year = int(sys.argv[1])        #2023
    month = int(sys.argv[2])     # month 4
    
    input_data = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
    
    apply_model(input_data=input_data)


if __name__ == '__main__':
    run()