
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.model_trainer import ModelTrainer
class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        trainer_config = config.model_trainer_config()
        model_trainer = ModelTrainer(trainer_config)
        model_trainer.train()