import pandas as pd
import os
import json


class CommonUtils:
    def __init__(self):
        pass

    @staticmethod
    def create_df(data_dict, columns):
        return pd.DataFrame(data_dict, columns=columns)

    @staticmethod
    def create_dict(key_list, values_list):
        new_dict = {}

        for i in range(len(key_list)):
            new_dict[key_list[i]] = values_list[i]

        return new_dict

    @staticmethod
    def load_json(file_path):
        if os.path.exists(file_path):
            try:
                with open(file_path) as json_file:
                    data = json.load(json_file)

            except Exception as exc:
                print("! Failed to load Json File !\n", exc)

            else:
                print("> Successfully loaded json file")
                return data

        else:
            raise FileNotFoundError(f"JSON file not found: {file_path}")

    @staticmethod
    def save_json(file_path, data_dict):
        try:
            with open(file_path, 'w') as file:
                json.dump(data_dict, file)

        except Exception as exc:
            print(f"! Failed to save data. !\n", exc)

        else:
            print("> Json storage is successful.")

    @staticmethod
    def save_df(df, path, ext):
        if path:
            try:
                if ext == '.csv':
                    df.to_csv(path+ext, sep=',')

                elif ext == '.xlsx':
                    df.to_excel(path+ext)

            except Exception as exc:
                print(f"! Failed to save data. !\n", exc)

            else:
                print("> Dataframe storage is successful.")


if __name__ == "__main__":
    main = CommonUtils()
