import os
from mlProject import logger
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_schema(self) -> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            schema = self.config.all_schema

            for column, expected_dtype in schema.items():
                if column not in data.columns:
                    validation_status = False
                    break

                actual_dtype = str(data[column].dtype)

                if actual_dtype != expected_dtype:
                    validation_status = False
                    break

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
