Here's the content rewritten in Markdown format:

```markdown
# Installing Python and boto3 for AWS Automation

### Step 1: Update the package list
```bash
sudo apt update
```

### Step 2: Install software-properties-common
```bash
sudo apt install software-properties-common
```

### Step 3: Add the deadsnakes PPA repository for Python versions
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
```

### Step 4: Update the package list again
```bash
sudo apt update
```

### Step 5: Install Python 3.10
```bash
sudo apt install python3.10
```

### Step 6: Install pip (Python package installer)
```bash
sudo apt install python3-pip
```

### Step 7: Verify the Python installation
```bash
python3.10 --version
```

### Step 8: Verify the pip installation
```bash
pip3 --version
```

### Step 9: Install boto3 using pip
```bash
pip3 install boto3
```

### Step 10: Verify the boto3 installation
```bash
python3.10 -m pip show boto3
```

## Create and Run a Python Script to Create an S3 Bucket

### Step 11: Create a Python script (e.g., `create_s3_bucket.py`)

```python
import boto3

s3 = boto3.client('s3')   # Create an S3 client

bucket_name = 'my-new-bucket'    # Create a bucket
s3.create_bucket(Bucket=bucket_name)

print(f"Bucket {bucket_name} created successfully.")
```

### Step 12: Run the script
```bash
python3.10 create_s3_bucket.py
```
```
