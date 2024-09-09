import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Define the bucket name and region
bucket_name = 'mannu003'
region = 'ap-south-1'  # Change to your desired region

try:
    # Create an S3 client with the specified region
    s3 = boto3.client('s3', region_name=region)

    # Create a bucket in the specified region
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )

    print(f"Bucket {bucket_name} created successfully in {region} region.")
except NoCredentialsError:
    print("Credentials not available. Please configure your AWS credentials.")
except PartialCredentialsError:
    print("Incomplete credentials provided. Please check your AWS credentials.")
except ClientError as e:
    # Handle specific AWS errors
    error_code = e.response['Error']['Code']
    if error_code == 'IllegalLocationConstraintException':
        print("The specified region is not correct. Please ensure the region is specified correctly.")
    else:
        print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
