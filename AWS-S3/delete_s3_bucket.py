import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Define the bucket name and region
bucket_name = 'mannu003'
region = 'ap-south-1'  # Update with the region of your bucket

def delete_all_objects(s3_client, bucket):
    """Delete all objects in the bucket."""
    try:
        # List all objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket)
        if 'Contents' in response:
            objects = [{'Key': obj['Key']} for obj in response['Contents']]
            # Delete all objects
            s3_client.delete_objects(Bucket=bucket, Delete={'Objects': objects})
            print(f"Deleted {len(objects)} objects from bucket {bucket}.")
    except ClientError as e:
        print(f"An error occurred while deleting objects: {e}")

try:
    # Create an S3 client with the specified region
    s3 = boto3.client('s3', region_name=region)

    # Delete all objects in the bucket
    delete_all_objects(s3, bucket_name)

    # Delete the bucket
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} deleted successfully.")

except NoCredentialsError:
    print("Credentials not available. Please configure your AWS credentials.")
except PartialCredentialsError:
    print("Incomplete credentials provided. Please check your AWS credentials.")
except ClientError as e:
    # Handle specific AWS errors
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
