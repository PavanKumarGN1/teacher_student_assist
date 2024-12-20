# # ## store_mcqs.py

# # from pymongo import MongoClient
# # import json
# # import os

# # # MongoDB connection
# # MONGODB_URI = os.getenv("MONGODB_URI") or "mongodb://127.0.0.1:27017/"
# # COLLECTION_NAME = "mcqs"

# # client = MongoClient(MONGODB_URI)
# # db = client["mcq_database"]

# # def store_mcqs(mcqs):
# #     try:
# #         # Parse the MCQs string into a list
# #         mcq_data = json.loads(mcqs)
        
# #         # Prepare the MCQs for MongoDB, ensuring they are dictionaries
# #         formatted_mcqs = [{"mcq": mcq} for mcq in mcq_data]
        
# #         # Insert the formatted MCQs into MongoDB
# #         result = db[COLLECTION_NAME].insert_many(formatted_mcqs)
# #         print(f"Stored {len(result.inserted_ids)} MCQs in MongoDB.")
# #     except Exception as e:
# #         print(f"Error storing MCQs in MongoDB: {e}")




from pymongo import MongoClient
import os

# MongoDB connection
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://127.0.0.1:27017/")
client = MongoClient(MONGODB_URI)
db = client["mcq_database"]
COLLECTION_NAME = "mcqs"

def store_mcqs(mcqs):
    try:
        if not isinstance(mcqs, list):
            raise ValueError("MCQs should be a list of dictionaries.")

        for mcq in mcqs:
            if "question" in mcq and "options" in mcq and "correct_answer" in mcq:
                mcq_document = {
                    "question": mcq["question"],
                    "options": mcq["options"],
                    "correct_answer": mcq["correct_answer"]
                }
                db[COLLECTION_NAME].insert_one(mcq_document)
                print(f"Stored MCQ: {mcq['question']}")
            else:
                print(f"Skipping invalid MCQ format: {mcq}")

        print(f"Successfully stored {len(mcqs)} MCQs in MongoDB.")
    except Exception as e:
        print(f"Error storing MCQs in MongoDB: {e}")
