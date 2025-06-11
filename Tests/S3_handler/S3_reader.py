import boto3
import xml.etree.ElementTree as ET
from io import BytesIO

def read_xml_from_s3(bucket_name, file_key):
    """
    Reads an XML file from S3 and returns the parsed XML root.
    
    :param bucket_name: Name of the S3 bucket
    :param file_key: Path to the XML file in S3
    :return: XML root element
    """
    s3 = boto3.client('s3')  # Initialize S3 client
    
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        xml_content = response['Body'].read()
        
        tree = ET.parse(BytesIO(xml_content))  # Parse XML
        return tree.getroot()  # Return the root element
    except Exception as e:
        print(f"Error fetching XML from S3: {e}")
        return None