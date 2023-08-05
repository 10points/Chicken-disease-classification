from cnnClassifier import logger
from cnnClassifier.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.state_02_prepare_base_model import PrepareBaseModelTrainingPipeline


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