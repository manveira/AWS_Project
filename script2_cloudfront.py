import boto3
import json

cf_client = boto3.client('cloudformation')

stack_name = 'resources'

def get_stack_outputs(stack_name):
    response = cf_client.describe_stacks(StackName=stack_name)
    outputs = response['Stacks'][0]['Outputs']
    output_dict = {output['OutputKey']: output['OutputValue'] for output in outputs}
    return output_dict

def get_distribution_config(distribution_id):
    client = boto3.client('cloudfront')
    response = client.get_distribution_config(Id=distribution_id)
    return response['DistributionConfig'], response['ETag']

def update_distribution(distribution_id, distribution_config, etag):
    client = boto3.client('cloudfront')
    response = client.update_distribution(
        DistributionConfig=distribution_config,
        Id=distribution_id,
        IfMatch=etag
    )
    return response

def main():
    outputs = get_stack_outputs(stack_name)
    distribution_id = outputs['DistributionIdCloudFront']
    origin_access_control_id = outputs['OriginAccessControlIdCloudFront']
    
    distribution_config, etag = get_distribution_config(distribution_id)
    
    for origin in distribution_config['Origins']['Items']:
        origin['OriginAccessControlId'] = origin_access_control_id

    with open('updated_config.json', 'w') as f:
        json.dump(distribution_config, f, indent=4)
    
    response = update_distribution(distribution_id, distribution_config, etag)
    print('Distribution updated:', response)

if __name__ == '__main__':
    main()