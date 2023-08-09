from cnnClassifier import logger
from cnnClassifier.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.state_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(">>>> stage {STAGE_NAME} complete <<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare base model"

try:
    logger.info(f"**********************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Training"
try:
    logger.info(f"**********************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"**********************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e