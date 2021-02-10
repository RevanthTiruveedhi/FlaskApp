from flask_restful import Resource
import logging as logger

class sampleAPI(Resource):
    def get(self):
        logger.debug("debugging part of code")
        sampleData = {
            "Owner" : "Thomas",
            "Version" : "1.0.0",
            "Description" : "Sample web Api"
        }
        return sampleData, 200