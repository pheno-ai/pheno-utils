import os 
import json
import argparse

base_json = {
"DATASETS_PATH": "",
"BULK_DATA_PATH": {
    "\\./": ""
},
"EVENTS_DATASET": "events",
"COHORT": "None",
"ERROR_ACTION": "warn"
}

bulk_data_mapping = {
"s3://.*/fundus/10k/": "{bulk_data_path}/fundus_bulk/", 
"s3://.*/human_genetics/10k/": "{bulk_data_path}/human_genetics_bulk/", 
"s3://.*/gut_microbiome/10k/": "{bulk_data_path}/gut_microbiome_bulk/"
}

def handle_arguments():
    argparser = argparse.ArgumentParser(description='Create config.json file for pheno')
    argparser.add_argument('-d', '--datasets_bucket', type=str, help='datasets bucket name', required=True)
    argparser.add_argument('-events', '--events_dataset', default="events", type=str, help='events dataset name')
    argparser.add_argument('-cohort', '--cohort', default="None", type=str, help='cohort name')
    argparser.add_argument('-error', '--error_action', default="warn", type=str, help='error action')
    argparser.add_argument('-b', '--bulk_data_path', type=str, default=None, help='bulk data path')
    
    return argparser.parse_args()

def main():
    args = handle_arguments()
    base_json["DATASETS_PATH"] = args.datasets_bucket
    base_json["EVENTS_DATASET"] = args.events_dataset
    base_json["COHORT"] = args.cohort
    base_json["ERROR_ACTION"] = args.error_action
    base_json["BULK_DATA_PATH"]["\\./"] = args.datasets_bucket + "/{dataset}/"
    
    if args.bulk_data_path:
        for k, v in bulk_data_mapping.items():
            base_json["BULK_DATA_PATH"][k] = v.format(bulk_data_path=args.bulk_data_path)
    
    
    if not os.path.exists(os.path.expanduser('~/.pheno')):
        os.makedirs(os.path.expanduser('~/.pheno'))
    
    with open(os.path.expanduser('~/.pheno/config.json'), 'w') as outfile:
        json.dump(base_json, outfile, indent=4)
    
    


# run main 
if __name__ == '__main__':
    main()