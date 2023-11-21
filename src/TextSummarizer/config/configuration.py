from TextSummarizer.constants import *
from TextSummarizer.utils.common import read_yaml,create_directory
from TextSummarizer.entity import DataIngestionConfig,DataValidationConfig
class ConfigurationManager:
    def __init__(self,
                 condfi_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(condfi_filepath)
        self.params = read_yaml(params_filepath)
        create_directory([self.config.artifact_root])

    def data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directory([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )
        return data_validation_config