import os
import json

for split_index in range(10):
    
    org_data_path = "./data/thumos/annotations_split/thumos14_train_split_" + str(split_index) + ".json"
    save_path = "./data/thumos/rpn_annotations_split/thumos14_train_split_" + str(split_index) + ".json"

    with open(org_data_path, 'r') as json_f:
        json_data = json.load(json_f)

    database = json_data['database']

    for per_key, per_value in database.items():
        data_anno = per_value['annotations']
        for per_anno in data_anno:
            per_anno['label_id'] = 0
            per_anno['label'] = 'Action'

    json_data['database'] = database
    with open(save_path, 'w') as save_f:
        json.dump(json_data, save_f)
    # import ipdb; ipdb.set_trace()
    print(">>> Change label file finished! ")