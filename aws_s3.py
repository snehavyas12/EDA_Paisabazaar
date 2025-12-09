import boto3

s3 = boto3.client('s3')

# Delete file
# s3.delete_object(
#     Bucket='snehas-projects-bucket',
#     Key='cleaned_data/paisabazaar_cleaned.csv'
# )

# Upload file
s3.upload_file(
    Filename='paisabazaar_cleaned.csv',
    Bucket='snehas-projects-bucket',
    Key='cleaned_data/paisabazaar_cleaned.csv'
)

# Download file
# s3.download_file(
#     'snehas-projects-bucket', #bucket name
#     'cleaned_data/paisabazaar_cleaned.csv', #file path in s3
#     'paisabazaar_cleaned.csv' #local file name to save as
# )