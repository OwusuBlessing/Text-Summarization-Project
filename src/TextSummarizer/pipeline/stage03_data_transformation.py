from TextSummarizer.config.configuration import  ConfigurationManager
from TextSummarizer.components.data_transformation import DataTransformation
from TextSummarizer.entity import DataTransformationConfig
from TextSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()

