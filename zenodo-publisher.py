import requests
import json
import sys

#URL for depositing files
url = "https://zenodo.org/api/deposit/depositions"

config_file = {}


#Function to create an empty container
def create_empty_upload(api_token):
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, params = {'access_token': api_token}, json = {}, headers = headers)

    return r.json()['id'],r.json()['links']['bucket'], r.status_code

#Function to upload a file
def upload_file(deposition_id, api_token, bucket_url, file):
    with open(file, 'rb') as fp:
        r = requests.put(
            bucket_url + '/' + file,
            data=fp,
            # No headers included in the request, since it's a raw byte request
            params={'access_token': api_token},
        )

    return r.status_code

#Function to add the metadata
def add_metadata(deposition_id,api_token,data):
    headers = {"Content-Type": "application/json"}
    r = requests.put('https://zenodo.org/api/deposit/depositions/%s' % deposition_id,
        params = {'access_token': api_token}, data = json.dumps(data),
        headers = headers)
    return r.status_code


def main():
    #Load config file
    with open(sys.argv[2]) as f:
        config_file = json.load(f)

    #Create an empty container
    id,url,status = create_empty_upload(config_file["access"]["token"])

    if status!= 200 and status!=201:
        print "Error to create an empty container"
        sys.exit(-1)  # Exit

    print "Create container with id:"+str(id)



    #Upload the file
    print "Uploading file"

    status = upload_file(id,config_file["access"]["token"],url,sys.argv[1])
    if status!= 200 and status!=201:
        print "Error to create an empty container"
        sys.exit(-2)  # Exit

    #These are the metadata used by this resource. This information is taken from the metadata config file
    print "Adding metadata"

    result = add_metadata(id,config_file["access"]["token"],config_file["data"])
    if result == 200:
        print "Resource created and deposited"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Number of arguments invalided."
        print "Usage: zenodo-publisher.sh <name_file_deposit> <name_configuration_file>"
        exit (-1)
    main()