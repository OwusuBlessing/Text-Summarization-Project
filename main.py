from TextSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage01_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage04_model_training import ModelTrainerTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e







