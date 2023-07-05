from shoes_brand_classification import logger
from shoes_brand_classification.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from shoes_brand_classification.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from shoes_brand_classification.pipeline.stage03_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx=======x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Prepare base model"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx=======x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Training"

try:
    logger.info(f"************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===========x")
except Exception as e:
        logger.exception(e)
        raise e