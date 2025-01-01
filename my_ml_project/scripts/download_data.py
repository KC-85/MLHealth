from kaggle.api.kaggle_api_extended import KaggleApi

# Step 1: Authenticate using the Kaggle API
api = KaggleApi()
api.authenticate()

# Step 2: Define the dataset
dataset = "dhivyeshrk/diseases-and-symptoms-dataset"  # Dataset ID from Kaggle

# Step 3: Download and unzip the dataset
api.dataset_download_files(dataset, path="./data", unzip=True)

print("Dataset downloaded and extracted to './data'")
