# data-scripts
This repository contains scripts to process and to publish data

Scripts
zenodo-publisher.py
This script uploads and deposits resources in Zenodo. 

Usage: python zenodo-publisher.py <name_file_to_upload> <name_config_file>

The structure of the config file is the following:
{
   "access":{
     "token": <token>
    },
    "data": {
      "metadata": {
        "title": "",
        "upload_type": "dataset",
        "description": "",
        "creators": [{"name": "ACTION"}],
        "communities": [{"identifier":"actionprojecteu"},{"identifier":"ecfunded"}],
        "publication_date":"2020-01-01",
        "access_right":"open",
        "license":"CC-BY-4.0",
        "grants":[{"id":"864203"}],
        "prereserve_doi":"true"
      }
    }
}

where:

- **token** is the token generated in Zenodo to enable the API to be used fwon an application,
- **title** is the title of the resource,
- **upload_type** is the type of the resource (in our case dataset),
- **description** is the description of the dataset,
- **creators** is the list of the authors,
- **communities** is the list of the commnities subscribed to the resource (for example ecfounded for OpenAire and H2020 projects,
- **publication** date is the date of the publication,
- **access_right** is the level of access,
- **license** is the type of license used,
- **grants** is the list of funding sources (grant agreement number for h2020 projects),
- **prereserved_doi** is a boolean to indicate if you want to reserve a DOI or not

Note: When the script finishes its execution, the resource and the metadata are saved in Zenodo but they are not published. User has to do it manually, clicking the Publish button. 
