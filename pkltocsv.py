import pickle
import csv


pickle_file_path = 'data\eeg\image\data.pkl'  
with open('data\eeg\image\data.pkl', 'rb') as pickle_file:
    data = pickle.load(pickle_file, encoding='latin1')


data_list = [{'key': key, 'value': value} for key, value in data.items()]


csv_file_path = 'output_data.csv'  


field_names = ['key', 'value']


with open(csv_file_path, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writerows(data_list)

print(f'Pickle data has been converted and saved to {csv_file_path}')
