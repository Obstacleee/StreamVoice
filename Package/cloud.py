import boto3

s3 = boto3.resource(
    service_name='s3',
    region_name='eu-west-3',
    aws_access_key_id='AKIA6GBMEVG3AT3DQU4T',
    aws_secret_access_key='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'
)

def download(key , output):
    s3.meta.client.download_file('rssmp3',key, output)
# Print out bucket names
def upload(filepath , key):
    s3.Bucket('rssmp3').upload_file(Filename=filepath, Key=key)

    
# cheez-willikers
# Upload files to S3 bucket
#s3.Bucket('rssmp3').upload_file(Filename='C:/Users/lucas/Desktop/projet rss/Projet-RSS/Package/save.mp3', Key='save.mp3')
# Load csv file directly into python


